"""
Evaluation Router
==================
Exposes a single endpoint that runs offline evaluation for all methods
and returns metrics suitable for the frontend evaluation/comparison page.
"""
from fastapi import APIRouter

router = APIRouter(prefix="/evaluate", tags=["Evaluation"])


@router.get("/metrics")
def get_metrics():
    """
    Run offline evaluation for all CF, CB, and KB methods.

    CF methods use leave-one-out evaluation on 8 test users (one per persona).
    CB methods use category-overlap precision on the same test users.
    KB methods report catalog coverage and average score with no constraints.

    Results are cached after the first call (CB model loading takes ~30s).
    """
    from backend.services.evaluation import compute_all_metrics
    return compute_all_metrics()
