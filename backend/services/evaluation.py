"""
Offline Evaluation Service
===========================
Implements leave-one-out evaluation for CF methods and coverage/precision
metrics for CB and KB methods. Results are cached after first computation.

CF metrics (leave-one-out on 8 test users, K=10):
  Precision@K, Recall@K, NDCG@K, Hit Rate@K, F1@K, MRR@K, Coverage

CB metrics (full-profile, category-overlap precision):
  Category Precision@K, Coverage, Avg Score

KB metrics (no-constraint run):
  Coverage, Avg Score, Result Count
"""
import math
from typing import Dict, List

from backend.models.user_data import USER_RATINGS
from backend.models.product_datar import PRODUCT_BY_ID as ML_CATALOG

K = 10
REL_THRESHOLD = 4.0
TEST_USERS = ["U001", "U006", "U011", "U016", "U021", "U026", "U031", "U036"]
CATALOG_SIZE = len(ML_CATALOG)

# ── Similarity helpers ─────────────────────────────────────────────

def _cosine(a: dict, b: dict) -> float:
    common = set(a) & set(b)
    if not common:
        return 0.0
    dot = sum(a[k] * b[k] for k in common)
    ma = math.sqrt(sum(v ** 2 for v in a.values()))
    mb = math.sqrt(sum(v ** 2 for v in b.values()))
    return dot / (ma * mb) if ma and mb else 0.0


def _pearson(a: dict, b: dict) -> float:
    common = set(a) & set(b)
    if len(common) < 2:
        return 0.0
    ma = sum(a[k] for k in common) / len(common)
    mb = sum(b[k] for k in common) / len(common)
    num = sum((a[k] - ma) * (b[k] - mb) for k in common)
    da = math.sqrt(sum((a[k] - ma) ** 2 for k in common))
    db = math.sqrt(sum((b[k] - mb) ** 2 for k in common))
    return num / (da * db) if da and db else 0.0


def _jaccard(s1: set, s2: set) -> float:
    if not s1 and not s2:
        return 0.0
    return len(s1 & s2) / len(s1 | s2)


# ── Metric helpers ─────────────────────────────────────────────────

def _prec(ranked: List[str], rel: set, k: int) -> float:
    return len(set(ranked[:k]) & rel) / k


def _rec(ranked: List[str], rel: set, k: int) -> float:
    return len(set(ranked[:k]) & rel) / len(rel) if rel else 0.0


def _ndcg(ranked: List[str], rdict: dict, k: int) -> float:
    dcg = sum(rdict.get(p, 0.0) / math.log2(i + 2) for i, p in enumerate(ranked[:k]))
    idcg = sum(r / math.log2(i + 2) for i, r in enumerate(sorted(rdict.values(), reverse=True)[:k]))
    return dcg / idcg if idcg else 0.0


def _hit(ranked: List[str], rel: set, k: int) -> float:
    return 1.0 if set(ranked[:k]) & rel else 0.0


def _mrr(ranked: List[str], rel: set) -> float:
    for i, p in enumerate(ranked):
        if p in rel:
            return 1.0 / (i + 1)
    return 0.0


def _f1(p: float, r: float) -> float:
    return 2 * p * r / (p + r) if p + r else 0.0


def _avg(lst: list) -> float:
    return sum(lst) / len(lst) if lst else 0.0


# ── CF ranking functions (LOO-compatible) ─────────────────────────

def _user_cosine_rank(train_r: dict, train_p: set, others: dict) -> List[str]:
    sc: dict = {}
    wt: dict = {}
    for uid, or_ in others.items():
        s = _cosine(train_r, or_)
        if s <= 0:
            continue
        for pid, r in or_.items():
            if pid in train_p:
                continue
            sc[pid] = sc.get(pid, 0.0) + s * r
            wt[pid] = wt.get(pid, 0.0) + s
    pred = {p: sc[p] / wt[p] for p in sc if wt.get(p, 0) > 0}
    return sorted(pred, key=lambda p: pred[p], reverse=True)


def _user_pearson_rank(train_r: dict, train_p: set, others: dict) -> List[str]:
    sims = {uid: _pearson(train_r, or_) for uid, or_ in others.items()}
    top5 = sorted((u for u in sims if sims[u] > 0), key=lambda u: sims[u], reverse=True)[:5]
    sc: dict = {}
    wt: dict = {}
    for uid in top5:
        s = sims[uid]
        for pid, r in others[uid].items():
            if pid in train_p:
                continue
            sc[pid] = sc.get(pid, 0.0) + s * r
            wt[pid] = wt.get(pid, 0.0) + s
    pred = {p: sc[p] / wt[p] for p in sc if wt.get(p, 0) > 0}
    return sorted(pred, key=lambda p: pred[p], reverse=True)


def _item_cosine_rank(train_r: dict, train_p: set) -> List[str]:
    ivec: dict = {}
    for uid, ratings in USER_RATINGS.items():
        for pid, r in ratings.items():
            ivec.setdefault(pid, {})[uid] = r
    sc: dict = {}
    for tp, tr in train_r.items():
        tvec = ivec.get(tp, {})
        for cp, cvec in ivec.items():
            if cp in train_p:
                continue
            s = _cosine(tvec, cvec)
            if s > 0:
                sc[cp] = sc.get(cp, 0.0) + s * tr
    return sorted(sc, key=lambda p: sc[p], reverse=True)


def _item_jaccard_rank(train_r: dict, train_p: set) -> List[str]:
    iu: dict = {}
    for uid, ratings in USER_RATINGS.items():
        for pid, r in ratings.items():
            if r >= 3.5:
                iu.setdefault(pid, set()).add(uid)
    sc: dict = {}
    for tp in train_p:
        ts = iu.get(tp, set())
        for cp, cs in iu.items():
            if cp in train_p:
                continue
            s = _jaccard(ts, cs)
            if s > 0:
                sc[cp] = max(sc.get(cp, 0.0), s)
    return sorted(sc, key=lambda p: sc[p], reverse=True)


_CF_RANK_FNS = {
    "user_cosine": ("user", _user_cosine_rank),
    "user_pearson": ("user", _user_pearson_rank),
    "item_cosine": ("item", _item_cosine_rank),
    "item_jaccard": ("item", _item_jaccard_rank),
}


def _eval_cf(method_key: str) -> dict:
    """Leave-one-out evaluation for a CF method."""
    kind, fn = _CF_RANK_FNS[method_key]
    precs, recs, ndcgs, hits, mrrs = [], [], [], [], []
    all_rec: set = set()

    for uid in TEST_USERS:
        ratings = USER_RATINGS.get(uid, {})
        rel_pairs = [(p, r) for p, r in ratings.items() if r >= REL_THRESHOLD]
        if len(rel_pairs) < 2:
            continue

        test_pid, test_r = rel_pairs[0]
        train_r = {p: r for p, r in ratings.items() if p != test_pid}
        train_p = set(train_r.keys())

        if kind == "user":
            others = {u: USER_RATINGS[u] for u in USER_RATINGS if u != uid}
            ranked = fn(train_r, train_p, others)
        else:
            ranked = fn(train_r, train_p)

        all_rec.update(ranked[:K])
        rel = {test_pid}
        precs.append(_prec(ranked, rel, K))
        recs.append(_rec(ranked, rel, K))
        ndcgs.append(_ndcg(ranked, {test_pid: test_r}, K))
        hits.append(_hit(ranked, rel, K))
        mrrs.append(_mrr(ranked, rel))

    pa, ra = _avg(precs), _avg(recs)
    return {
        "precision": round(pa * 100, 1),
        "recall": round(ra * 100, 1),
        "ndcg": round(_avg(ndcgs) * 100, 1),
        "hit_rate": round(_avg(hits) * 100, 1),
        "f1": round(_f1(pa, ra) * 100, 1),
        "mrr": round(_avg(mrrs) * 100, 1),
        "coverage": round(len(all_rec) / CATALOG_SIZE * 100, 1) if CATALOG_SIZE else 0.0,
    }


# ── CB evaluation ──────────────────────────────────────────────────

def _get_cb_eval_engine():
    # Reuse the engine already loaded by the recommender router (avoids double load).
    from backend.routers.recommender import _get_cb_engine
    engine = _get_cb_engine()
    # Map recommender keys to evaluation keys
    return {
        "loader": engine["loader"],
        "recs": engine["recommenders"],
    }


def _eval_cb(method_key: str) -> dict:
    """
    Evaluate CB method using category-overlap precision.
    For each test user, measure what fraction of recommendations
    fall in the user's demonstrated interest categories.
    """
    engine = _get_cb_eval_engine()
    loader = engine["loader"]
    rec = engine["recs"][method_key]

    cat_precs: list = []
    scores: list = []
    all_rec: set = set()

    for uid in TEST_USERS:
        ratings = USER_RATINGS.get(uid, {})
        fav_cats: set = set()
        for pid, r in ratings.items():
            if r >= REL_THRESHOLD:
                prod = ML_CATALOG.get(pid, {})
                cat = prod.get("category_l2", "").lower()
                if cat:
                    fav_cats.add(cat)
        if not fav_cats:
            continue

        try:
            results = rec.recommend(uid, K)
        except Exception:
            continue

        rec_cats: list = []
        for result in results:
            try:
                info = loader.get_product_info(result.product_id)
                cat = info.get("category_l2_name", info.get("category_l2", "")).lower()
                rec_cats.append(cat)
                scores.append(result.score)
                all_rec.add(result.product_id)
            except Exception:
                pass

        hits = sum(1 for c in rec_cats if c in fav_cats)
        cat_precs.append(hits / len(rec_cats) if rec_cats else 0.0)

    p = _avg(cat_precs)
    avg_s = _avg(scores)
    coverage = len(all_rec) / CATALOG_SIZE * 100 if CATALOG_SIZE else 0.0

    return {
        "precision": round(p * 100, 1),
        "avg_score": round(avg_s, 3),
        "coverage": round(coverage, 1),
    }


# ── KB evaluation ──────────────────────────────────────────────────

def _eval_kb(method_key: str) -> dict:
    """Run KB method with no constraints and measure coverage and avg score."""
    from backend.services.knowledge_base import (
        recommend_rule_based,
        recommend_constraint_based,
        recommend_utility_based,
    )
    from backend.models.product_data import PRODUCTS

    fns = {
        "rule": lambda: recommend_rule_based(),
        "constraint": lambda: recommend_constraint_based(),
        "utility": lambda: recommend_utility_based(),
    }
    try:
        results = fns[method_key]()
    except Exception:
        results = []

    n = len(PRODUCTS)
    coverage = len(results) / n * 100 if n else 0.0
    avg_score = _avg([r.get("score", r.get("product", {}).get("rating", 0)) for r in results])

    return {
        "coverage": round(coverage, 1),
        "avg_score": round(avg_score, 3),
        "result_count": len(results),
    }


# ── Main entry point ───────────────────────────────────────────────

_CACHE: dict = {}


def compute_all_metrics() -> dict:
    """
    Compute metrics for all methods. Cached after first call.
    First call may take ~30s due to CB model loading.
    """
    if _CACHE:
        return _CACHE

    cf = {m: _eval_cf(m) for m in ["user_cosine", "user_pearson", "item_cosine", "item_jaccard"]}

    try:
        cb = {m: _eval_cb(m) for m in ["tfidf", "lsa", "word2vec", "feature"]}
        cb_available = True
    except Exception:
        cb = {m: {"precision": 0, "avg_score": 0, "coverage": 0} for m in ["tfidf", "lsa", "word2vec", "feature"]}
        cb_available = False

    kb: dict = {}
    for m in ["rule", "constraint", "utility"]:
        try:
            kb[m] = _eval_kb(m)
        except Exception:
            kb[m] = {"coverage": 0, "avg_score": 0, "result_count": 0}

    best_cf = max(cf, key=lambda k: cf[k]["ndcg"])
    best_cb = max(cb, key=lambda k: cb[k]["precision"]) if cb_available else "tfidf"

    _CACHE.update({
        "k": K,
        "test_users": TEST_USERS,
        "cf": cf,
        "cb": cb,
        "cb_available": cb_available,
        "kb": kb,
        "best_cf": best_cf,
        "best_cb": best_cb,
    })
    return _CACHE
