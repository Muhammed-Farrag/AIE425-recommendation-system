"""
backend/models/product_data.py

120 realistic electronics products in the exact schema required by Phase 2.

NOTE ON EXISTING FRONTEND DATA
--------------------------------
Your existing 80-item frontend list uses keys: id, name, category, rating,
features (list).  That list drives the product-card UI and is NOT imported
here.  This file uses the Phase 2 ML schema:
  product_id (str), title, brand, price, category_l1/l2/l3,
  avg_rating, rating_count, description, features (comma-separated str).
DataLoader is the only bridge between the two worlds.

Category distribution (120 total):
  Headphones & Audio          30
  Smartphones & Accessories   25
  Laptops & Computers         20
  Cameras & Photography       15
  Smart Home & IoT            15
  Gaming                      15
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# 120 products — realistic names, brands, prices, descriptions
# ---------------------------------------------------------------------------

PRODUCTS: list[dict] = [

    # =========================================================================
    # HEADPHONES & AUDIO  (30 products, P0001–P0030)
    # =========================================================================

    # --- Over-Ear Headphones (8) ---
    {
        "product_id":   "P0001",
        "title":        "Sony WH-1000XM5 Wireless Noise-Cancelling Headphones",
        "brand":        "Sony",
        "price":        349.99,
        "category_l1":  "Electronics",
        "category_l2":  "Headphones & Audio",
        "category_l3":  "Over-Ear Headphones",
        "avg_rating":   4.8,
        "rating_count": 12450,
        "description":  (
            "Industry-leading noise cancellation with eight microphones and two "
            "processors delivers unrivalled quiet. The 30-hour battery life and "
            "multipoint connection let you seamlessly switch between two Bluetooth "
            "devices. Foldable design and speak-to-chat auto-pause make commuting effortless."
        ),
        "features": (
            "30-hour battery, active noise cancellation, multipoint Bluetooth, "
            "LDAC hi-res audio, touch controls, speak-to-chat, USB-C charging, foldable"
        ),
        "image":    "https://images.unsplash.com/photo-1618366712010-f4ae9c647dcb?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0002",
        "title":        "Bose QuietComfort 45 Bluetooth Headphones",
        "brand":        "Bose",
        "price":        279.00,
        "category_l1":  "Electronics",
        "category_l2":  "Headphones & Audio",
        "category_l3":  "Over-Ear Headphones",
        "avg_rating":   4.7,
        "rating_count": 9820,
        "description":  (
            "Bose QuietComfort 45 combines legendary noise cancellation with a "
            "lightweight, comfortable design engineered for all-day wear. The "
            "Aware mode lets in the sounds around you when you need to stay "
            "connected to your environment without removing the headphones."
        ),
        "features": (
            "24-hour battery, Quiet and Aware modes, TriPort acoustic, "
            "multipoint connection, comfortable earcups, USB-C, built-in mic, foldable"
        ),
        "image":    "https://images.unsplash.com/photo-1546435770-a3e426bf472b?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0003",
        "title":        "Sennheiser HD 660S2 Open-Back Headphones",
        "brand":        "Sennheiser",
        "price":        399.95,
        "category_l1":  "Electronics",
        "category_l2":  "Headphones & Audio",
        "category_l3":  "Over-Ear Headphones",
        "avg_rating":   4.7,
        "rating_count": 3140,
        "description":  (
            "The HD 660S2 features newly developed 38 mm transducers with a lower "
            "impedance of 300 ohms for exceptional detail retrieval from high-res "
            "sources. Open-back design creates a wide, natural soundstage ideal "
            "for critical listening and studio reference work."
        ),
        "features": (
            "300 ohm impedance, open-back design, 38 mm transducers, "
            "replaceable cable, velour earpads, 6.35 mm adapter included, wired, studio-grade"
        ),
        "image":    "https://images.unsplash.com/photo-1599669454699-248893623440?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0004",
        "title":        "Apple AirPods Max Space Grey",
        "brand":        "Apple",
        "price":        549.00,
        "category_l1":  "Electronics",
        "category_l2":  "Headphones & Audio",
        "category_l3":  "Over-Ear Headphones",
        "avg_rating":   4.6,
        "rating_count": 8760,
        "description":  (
            "AirPods Max deliver a perfect balance of high-fidelity audio and "
            "industry-leading Active Noise Cancellation. The adaptive EQ "
            "automatically tunes music to the shape of your ear, while the "
            "breathable knit mesh canopy distributes weight for all-day comfort."
        ),
        "features": (
            "Active Noise Cancellation, Transparency mode, adaptive EQ, "
            "Spatial Audio, 20-hour battery, Apple H1 chip, Lightning charging, mesh canopy"
        ),
        "image":    "https://images.unsplash.com/photo-1625245488600-f03fef636a3c?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0005",
        "title":        "Sony MDR-7506 Professional Monitoring Headphones",
        "brand":        "Sony",
        "price":        79.99,
        "category_l1":  "Electronics",
        "category_l2":  "Headphones & Audio",
        "category_l3":  "Over-Ear Headphones",
        "avg_rating":   4.6,
        "rating_count": 15000,
        "description":  (
            "A studio standard since 1991, the MDR-7506 delivers accurate, "
            "detailed sound for professional monitoring and mixing. The closed-back "
            "design provides excellent isolation, and the neodymium magnets ensure "
            "powerful sound reproduction across the 10 Hz–20 kHz frequency range."
        ),
        "features": (
            "40 mm neodymium drivers, closed-back, foldable, 9.8 ft coiled cable, "
            "63 ohm impedance, wide frequency response, gold-plated plug, professional"
        ),
        "image":    "https://images.unsplash.com/photo-1583394838336-acd977736f90?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0006",
        "title":        "Sennheiser HD 560S Over-Ear Audiophile Headphones",
        "brand":        "Sennheiser",
        "price":        149.95,
        "category_l1":  "Electronics",
        "category_l2":  "Headphones & Audio",
        "category_l3":  "Over-Ear Headphones",
        "avg_rating":   4.5,
        "rating_count": 4200,
        "description":  (
            "Engineered for audiophiles on a budget, the HD 560S features an "
            "angled 38 mm transducer positioning that mimics the natural angle "
            "of the ears. Its open-back design and 120 ohm impedance make it "
            "compatible with a wide range of amplifiers and portable devices."
        ),
        "features": (
            "angled transducer, open-back, 120 ohm, replaceable cable, "
            "3.5 mm TRS, 6.35 mm adapter, velour pads, wide soundstage"
        ),
        "image":    "https://images.unsplash.com/photo-1484704849700-f032a568e944?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0007",
        "title":        "Bose 700 Noise Cancelling Headphones",
        "brand":        "Bose",
        "price":        319.00,
        "category_l1":  "Electronics",
        "category_l2":  "Headphones & Audio",
        "category_l3":  "Over-Ear Headphones",
        "avg_rating":   4.5,
        "rating_count": 7340,
        "description":  (
            "The Bose 700 offers 11 levels of adjustable noise cancellation, "
            "giving you precise control from total immersion to fully open. "
            "The stainless steel headband and refined industrial design set it "
            "apart visually, while six-mic voice pickup ensures crystal-clear calls."
        ),
        "features": (
            "11-level adjustable ANC, 20-hour battery, 6-mic system, "
            "Alexa and Google built-in, USB-C, stainless steel, touch controls, multipoint"
        ),
        "image":    "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0008",
        "title":        "Philips Fidelio X3 Wired Over-Ear Headphones",
        "brand":        "Philips",
        "price":        199.99,
        "category_l1":  "Electronics",
        "category_l2":  "Headphones & Audio",
        "category_l3":  "Over-Ear Headphones",
        "avg_rating":   4.4,
        "rating_count": 1850,
        "description":  (
            "The Fidelio X3 uses 50 mm neodymium drivers with an open acoustic "
            "chamber design to deliver a wide, airy soundstage. Memory foam ear "
            "cushions wrapped in breathable fabric provide extended listening "
            "comfort, and the double-layered headband eliminates pressure points."
        ),
        "features": (
            "50 mm open-back drivers, memory foam cushions, detachable cable, "
            "3-button remote, high-res audio certified, 32 ohm, fabric headband, wired"
        ),
        "image":    "https://images.unsplash.com/photo-1524678606370-a47ad25cb82a?w=500&h=500&fit=crop",
    },

    # --- In-Ear Headphones (6) ---
    {
        "product_id":   "P0009",
        "title":        "Sennheiser IE 300 In-Ear Audiophile Headphones",
        "brand":        "Sennheiser",
        "price":        299.95,
        "category_l1":  "Electronics",
        "category_l2":  "Headphones & Audio",
        "category_l3":  "In-Ear Headphones",
        "avg_rating":   4.6,
        "rating_count": 2100,
        "description":  (
            "Built around Sennheiser's extra-wide band transducer technology, "
            "the IE 300 achieves extraordinarily low harmonic distortion. "
            "The ear canal geometry is carefully tuned to deliver balanced, "
            "natural sound reproduction for demanding audiophile listening sessions."
        ),
        "features": (
            "X3R transducer, 16 ohm, replaceable cable with 2-pin connector, "
            "3.5 mm plug, multiple ear tip sizes, resonator chamber, high-res, wired"
        ),
        "image":    "https://images.unsplash.com/photo-1598331668826-20cecc596b86?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0010",
        "title":        "Sony IER-M9 In-Ear Monitor Headphones",
        "brand":        "Sony",
        "price":        399.99,
        "category_l1":  "Electronics",
        "category_l2":  "Headphones & Audio",
        "category_l3":  "In-Ear Headphones",
        "avg_rating":   4.7,
        "rating_count": 980,
        "description":  (
            "Professional in-ear monitors for stage and studio use, the IER-M9 "
            "employs five balanced armature drivers per side in a four-way "
            "crossover configuration. The magnesium housing minimises resonance "
            "while delivering extraordinary detail and channel separation."
        ),
        "features": (
            "5 balanced armature drivers, 4-way crossover, magnesium shell, "
            "MMCX connector, 16 ohm, professional monitor tuning, multiple tips, wired"
        ),
        "image":    "https://images.unsplash.com/photo-1606220588913-b3aacb4d2f46?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0011",
        "title":        "Anker Soundcore P20i True Wireless Earbuds",
        "brand":        "Anker",
        "price":        25.99,
        "category_l1":  "Electronics",
        "category_l2":  "Headphones & Audio",
        "category_l3":  "In-Ear Headphones",
        "avg_rating":   4.2,
        "rating_count": 8900,
        "description":  (
            "Soundcore P20i packs 10 mm drivers and Bluetooth 5.3 into an "
            "IPX5-waterproof body at a budget-friendly price. The compact "
            "charging case provides three additional charges, and custom EQ "
            "presets let you tailor the sound profile through the Soundcore app."
        ),
        "features": (
            "10 mm drivers, IPX5 waterproof, 10-hour playtime, USB-C case, "
            "Bluetooth 5.3, touch controls, Soundcore app EQ, deep bass preset"
        ),
        "image":    "https://images.unsplash.com/photo-1590658268037-6bf12f032f55?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0012",
        "title":        "JBL Tune 230NC True Wireless Noise Cancelling Earbuds",
        "brand":        "JBL",
        "price":        79.95,
        "category_l1":  "Electronics",
        "category_l2":  "Headphones & Audio",
        "category_l3":  "In-Ear Headphones",
        "avg_rating":   4.3,
        "rating_count": 5600,
        "description":  (
            "JBL's Active Noise Cancelling technology eliminates unwanted ambient "
            "sound while JBL Pure Bass delivers the signature deep, punchy bass "
            "response. Four-microphone call pickup and ambient-aware mode make "
            "the Tune 230NC practical for commuting and open-plan offices."
        ),
        "features": (
            "active noise cancelling, 40-hour total battery, JBL Pure Bass, "
            "4-mic call pickup, ambient aware, USB-C, IPX4, Bluetooth 5.2"
        ),
        "image":    "https://images.unsplash.com/photo-1631867675167-90a456a90863?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0013",
        "title":        "Bose QuietComfort Earbuds II",
        "brand":        "Bose",
        "price":        249.00,
        "category_l1":  "Electronics",
        "category_l2":  "Headphones & Audio",
        "category_l3":  "In-Ear Headphones",
        "avg_rating":   4.6,
        "rating_count": 7100,
        "description":  (
            "Bose CustomTune technology measures your unique ear geometry every "
            "time you put on the earbuds to deliver perfectly personalised sound "
            "and ANC. The result is the most effective noise cancellation Bose has "
            "ever created in a true-wireless earbud form factor."
        ),
        "features": (
            "CustomTune personalised ANC, 6-hour battery, wireless charging case, "
            "IPX4, Bose Aware mode, touch controls, USB-C, Bluetooth 5.3"
        ),
        "image":    "https://images.unsplash.com/photo-1649885756377-60b379044ea5?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0014",
        "title":        "Sony WF-1000XM5 Wireless Noise Cancelling Earbuds",
        "brand":        "Sony",
        "price":        279.99,
        "category_l1":  "Electronics",
        "category_l2":  "Headphones & Audio",
        "category_l3":  "In-Ear Headphones",
        "avg_rating":   4.7,
        "rating_count": 9300,
        "description":  (
            "The smallest, lightest noise-cancelling earbuds Sony has ever made, "
            "the WF-1000XM5 uses the QN2e processor and V2 integrated processor "
            "in tandem to deliver best-in-class ANC. LDAC support streams hi-res "
            "audio at up to 990 kbps for studio-quality wireless listening."
        ),
        "features": (
            "QN2e + V2 dual processor ANC, LDAC hi-res, 8-hour battery, "
            "Qi wireless charging, speak-to-chat, multipoint, IPX4, USB-C"
        ),
        "image":    "https://images.unsplash.com/photo-1645438835442-083f59bcce18?w=500&h=500&fit=crop",
    },

    # --- Wireless Earbuds (6) ---
    {
        "product_id":   "P0015",
        "title":        "Apple AirPods Pro (2nd Generation)",
        "brand":        "Apple",
        "price":        249.00,
        "category_l1":  "Electronics",
        "category_l2":  "Headphones & Audio",
        "category_l3":  "Wireless Earbuds",
        "avg_rating":   4.8,
        "rating_count": 14200,
        "description":  (
            "The second-generation AirPods Pro deliver up to 2× more Active Noise "
            "Cancellation than the previous generation, powered by the H2 chip. "
            "Adaptive Transparency intelligently reduces loud environmental sounds "
            "in real time, and Personalized Spatial Audio creates a theatre-like experience."
        ),
        "features": (
            "H2 chip, Adaptive ANC, Personalized Spatial Audio, 6-hour battery, "
            "MagSafe charging case, IPX4, touch controls, USB-C, precision finding"
        ),
        "image":    "https://images.unsplash.com/photo-1600294037681-c80b4cb5b434?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0016",
        "title":        "Samsung Galaxy Buds2 Pro",
        "brand":        "Samsung",
        "price":        189.99,
        "category_l1":  "Electronics",
        "category_l2":  "Headphones & Audio",
        "category_l3":  "Wireless Earbuds",
        "avg_rating":   4.4,
        "rating_count": 6700,
        "description":  (
            "Galaxy Buds2 Pro achieves 99% voice pickup isolation through a "
            "three-microphone system and wind-shield mesh, making calls clear "
            "even in breezy outdoor environments. 24-bit Hi-Fi audio and "
            "360-degree audio with head tracking deliver an immersive soundstage."
        ),
        "features": (
            "24-bit Hi-Fi audio, 3-mic ANC, 360 Audio, 8-hour battery, "
            "IPX7 water resistant, Galaxy ecosystem integration, USB-C, Bluetooth 5.3"
        ),
        "image":    "https://images.unsplash.com/photo-1628815113969-0487917e8b76?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0017",
        "title":        "JBL Live Pro 2 TWS Noise Cancelling Earbuds",
        "brand":        "JBL",
        "price":        149.95,
        "category_l1":  "Electronics",
        "category_l2":  "Headphones & Audio",
        "category_l3":  "Wireless Earbuds",
        "avg_rating":   4.3,
        "rating_count": 3800,
        "description":  (
            "JBL Live Pro 2 combines Adaptive Noise Cancelling with six microphones "
            "to put you in full control of your audio environment. Smart Ambient "
            "lets you stay aware of your surroundings safely, while the ergonomic "
            "twist-lock fit ensures the earbuds stay secure during workouts."
        ),
        "features": (
            "6-mic ANC, 40-hour total battery, Smart Ambient, Qi wireless charging, "
            "IPX5, JBL Pure Bass, Bluetooth 5.3, multipoint, USB-C"
        ),
        "image":    "https://images.unsplash.com/photo-1608156639585-b3a776571bef?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0018",
        "title":        "Anker Soundcore Liberty 4 NC Earbuds",
        "brand":        "Anker",
        "price":        79.99,
        "category_l1":  "Electronics",
        "category_l2":  "Headphones & Audio",
        "category_l3":  "Wireless Earbuds",
        "avg_rating":   4.4,
        "rating_count": 7200,
        "description":  (
            "Liberty 4 NC achieves 98.5% noise reduction through its adaptive ANC "
            "system and six-microphone array. The coaxial dual-driver setup pairs "
            "a 10.6 mm dynamic woofer with a separate tweeter for detailed, "
            "full-spectrum sound that punches well above its price point."
        ),
        "features": (
            "coaxial dual driver, 98.5% ANC, 50-hour total battery, Qi wireless charging, "
            "IPX4, LDAC, HearID EQ, Bluetooth 5.3, USB-C"
        ),
        "image":    "https://images.unsplash.com/photo-1606841837239-c5a1a4a07af7?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0019",
        "title":        "Google Pixel Buds Pro",
        "brand":        "Google",
        "price":        199.00,
        "category_l1":  "Electronics",
        "category_l2":  "Headphones & Audio",
        "category_l3":  "Wireless Earbuds",
        "avg_rating":   4.3,
        "rating_count": 4900,
        "description":  (
            "Pixel Buds Pro use a custom six-core audio chip to run Active Noise "
            "Cancellation and transparency mode simultaneously, continuously "
            "adapting to your ear canal pressure every 2 ms. Deep integration "
            "with Google Assistant enables real-time translation across 40 languages."
        ),
        "features": (
            "custom 6-core chip, continuous ANC + transparency, 7-hour battery, "
            "Qi charging, IPX4, real-time translation, multipoint, USB-C, Bluetooth 5.0"
        ),
        "image":    "https://images.unsplash.com/photo-1572569511254-d8f925fe2cbb?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0020",
        "title":        "Sennheiser Momentum True Wireless 3",
        "brand":        "Sennheiser",
        "price":        199.95,
        "category_l1":  "Electronics",
        "category_l2":  "Headphones & Audio",
        "category_l3":  "Wireless Earbuds",
        "avg_rating":   4.5,
        "rating_count": 3200,
        "description":  (
            "Momentum True Wireless 3 represents Sennheiser's reference-class "
            "earbuds, tuned for audiophile precision with 7 mm transducers "
            "developed entirely in-house. Sound Personalisation via the Smart "
            "Control app tailors the EQ to your individual hearing profile."
        ),
        "features": (
            "7 mm Sennheiser transducers, adaptive ANC, 28-hour total, "
            "Qi wireless charging, IPX4, aptX Adaptive, Sound Personalisation, USB-C"
        ),
        "image":    "https://images.unsplash.com/photo-1655212798482-44a8024947ff?w=500&h=500&fit=crop",
    },

    # --- Soundbars (5) ---
    {
        "product_id":   "P0021",
        "title":        "Sony HT-A7000 7.1.2ch Dolby Atmos Soundbar",
        "brand":        "Sony",
        "price":        1299.99,
        "category_l1":  "Electronics",
        "category_l2":  "Headphones & Audio",
        "category_l3":  "Soundbars",
        "avg_rating":   4.6,
        "rating_count": 2800,
        "description":  (
            "The HT-A7000 delivers a genuine 7.1.2 channel Dolby Atmos experience "
            "from a single soundbar using beamforming speakers and Sony's Vertical "
            "Surround Engine. 360 Spatial Sound Mapping creates virtual surround "
            "channels that expand the soundfield beyond the physical speaker positions."
        ),
        "features": (
            "7.1.2 ch Dolby Atmos, DTS:X, 500W, 360 Spatial Sound Mapping, "
            "HDMI eARC, Bluetooth, Wi-Fi, beamforming speakers, subwoofer out"
        ),
        "image":    "https://images.unsplash.com/photo-1545454675-3531b543be5d?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0022",
        "title":        "Samsung HW-Q990C 11.1.4ch Soundbar",
        "brand":        "Samsung",
        "price":        1497.99,
        "category_l1":  "Electronics",
        "category_l2":  "Headphones & Audio",
        "category_l3":  "Soundbars",
        "avg_rating":   4.5,
        "rating_count": 1900,
        "description":  (
            "Samsung's flagship 11.1.4 channel soundbar system includes a wireless "
            "subwoofer and rear speakers for a true surround configuration right "
            "out of the box. SpaceFit Sound Pro analyses room acoustics using built-in "
            "microphones and auto-calibrates EQ for the optimal listening position."
        ),
        "features": (
            "11.1.4 ch, wireless subwoofer + rear speakers, SpaceFit Sound Pro, "
            "Dolby Atmos, DTS:X, HDMI eARC, 656W, Q-Symphony with Samsung TV, Wi-Fi"
        ),
        "image":    "https://images.unsplash.com/photo-1558537348-c0f8e733989d?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0023",
        "title":        "Bose Smart Soundbar 600 with Dolby Atmos",
        "brand":        "Bose",
        "price":        499.00,
        "category_l1":  "Electronics",
        "category_l2":  "Headphones & Audio",
        "category_l3":  "Soundbars",
        "avg_rating":   4.4,
        "rating_count": 4100,
        "description":  (
            "Bose Soundbar 600 uses PhaseGuide speaker arrays and TrueSpace "
            "processing to project height channels from a slim soundbar without "
            "physical upward-firing drivers. Multiroom audio via Bose SimpleSync "
            "links it with other Bose speakers for whole-home listening."
        ),
        "features": (
            "Dolby Atmos, TrueSpace 3D, HDMI eARC, Wi-Fi, Bluetooth, "
            "Alexa + Google built-in, Bose SimpleSync, USB-A, ADAPTiQ calibration"
        ),
        "image":    "https://images.unsplash.com/photo-1507646227500-4d389e0fcb8d?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0024",
        "title":        "JBL Bar 1000 7.1.4ch Dolby Atmos Soundbar",
        "brand":        "JBL",
        "price":        799.95,
        "category_l1":  "Electronics",
        "category_l2":  "Headphones & Audio",
        "category_l3":  "Soundbars",
        "avg_rating":   4.4,
        "rating_count": 3300,
        "description":  (
            "JBL Bar 1000 is the first soundbar in the world to deliver detachable "
            "rear speaker satellites that charge wirelessly in the main unit. "
            "The MultiBeam technology creates a precise surround sound envelope "
            "optimised for room size using built-in acoustic sensors."
        ),
        "features": (
            "7.1.4 ch, detachable wireless rear satellites, MultiBeam, "
            "Dolby Atmos, DTS:X, 880W, HDMI eARC, Bluetooth, USB, wireless subwoofer"
        ),
        "image":    "https://images.unsplash.com/photo-1593784991095-a205069470b6?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0025",
        "title":        "Philips TAB7807 Soundbar with Wireless Subwoofer",
        "brand":        "Philips",
        "price":        299.99,
        "category_l1":  "Electronics",
        "category_l2":  "Headphones & Audio",
        "category_l3":  "Soundbars",
        "avg_rating":   4.1,
        "rating_count": 1200,
        "description":  (
            "A practical 3.1.2 channel soundbar with built-in upward-firing "
            "drivers and a wireless subwoofer, the TAB7807 brings Dolby Atmos "
            "height effects at a mid-range price. IMAX Enhanced certification "
            "confirms accurate rendering of IMAX-encoded home content."
        ),
        "features": (
            "3.1.2 ch, Dolby Atmos, IMAX Enhanced, wireless subwoofer, "
            "HDMI ARC, Bluetooth, 240W, DTS Play-Fi, Alexa compatible"
        ),
        "image":    "https://images.unsplash.com/photo-1524170342594-eaab6c6f15f0?w=500&h=500&fit=crop",
    },

    # --- Portable Speakers (5) ---
    {
        "product_id":   "P0026",
        "title":        "JBL Charge 5 Portable Waterproof Bluetooth Speaker",
        "brand":        "JBL",
        "price":        179.95,
        "category_l1":  "Electronics",
        "category_l2":  "Headphones & Audio",
        "category_l3":  "Portable Speakers",
        "avg_rating":   4.7,
        "rating_count": 11200,
        "description":  (
            "JBL Charge 5 is IP67 waterproof and dustproof, making it the "
            "go-to speaker for pool parties and camping trips. The built-in "
            "20,000 mAh power bank charges your devices while the speaker "
            "plays up to 20 hours of JBL Pure Bass sound."
        ),
        "features": (
            "IP67 waterproof, 20-hour battery, 20,000 mAh power bank, "
            "JBL PartyBoost, USB-C, JBL Pure Bass, passive radiator, Bluetooth 5.1"
        ),
        "image":    "https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0027",
        "title":        "Bose SoundLink Flex Portable Bluetooth Speaker",
        "brand":        "Bose",
        "price":        149.00,
        "category_l1":  "Electronics",
        "category_l2":  "Headphones & Audio",
        "category_l3":  "Portable Speakers",
        "avg_rating":   4.6,
        "rating_count": 8700,
        "description":  (
            "SoundLink Flex uses PositionIQ technology to automatically detect "
            "whether it is upright, on its side, or face-up on a surface and "
            "adjusts the EQ accordingly. IP67 rating and a tear-resistant silicone "
            "exterior make it purpose-built for outdoor adventures."
        ),
        "features": (
            "IP67, PositionIQ EQ, 12-hour battery, USB-C, voice assistant, "
            "rLoop transducer, Bose SimpleSync, Bluetooth 5.1, lanyard loop"
        ),
        "image":    "https://images.unsplash.com/photo-1589003077984-894e133dabab?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0028",
        "title":        "Sony SRS-XB43 Extra Bass Portable Bluetooth Speaker",
        "brand":        "Sony",
        "price":        149.99,
        "category_l1":  "Electronics",
        "category_l2":  "Headphones & Audio",
        "category_l3":  "Portable Speakers",
        "avg_rating":   4.4,
        "rating_count": 6500,
        "description":  (
            "SRS-XB43 delivers party-ready Extra Bass with dual passive radiators "
            "and a 24-hour battery that outlasts most outdoor events. The built-in "
            "speaker lighting system syncs colours to the music beat, and the "
            "IP67 rating means splashes and dust are no concern."
        ),
        "features": (
            "Extra Bass, dual passive radiators, 24-hour battery, IP67, "
            "LED lighting, Live Sound mode, Bluetooth 5.0, USB-C, Party Connect"
        ),
        "image":    "https://images.unsplash.com/photo-1518609878373-06d740f60d8b?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0029",
        "title":        "Anker Soundcore Motion X600 Portable HiFi Speaker",
        "brand":        "Anker",
        "price":        99.99,
        "category_l1":  "Electronics",
        "category_l2":  "Headphones & Audio",
        "category_l3":  "Portable Speakers",
        "avg_rating":   4.5,
        "rating_count": 5100,
        "description":  (
            "Motion X600 offers Spatial Audio through five drivers configured "
            "in a 3D arrangement — a 40 W tweeter fires upward to create true "
            "height effects alongside two side-firing passive radiators. "
            "Hi-Res Audio certification and aptX adaptive codec support "
            "preserve detail from high-quality streaming sources."
        ),
        "features": (
            "Spatial Audio, 5-driver system, 40W upward tweeter, aptX Adaptive, "
            "hi-res audio, IPX7, 12-hour battery, USB-C, Bluetooth 5.3"
        ),
        "image":    "https://images.unsplash.com/photo-1558089687-f282ffcbc126?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0030",
        "title":        "JBL Flip 6 Compact Waterproof Bluetooth Speaker",
        "brand":        "JBL",
        "price":        129.95,
        "category_l1":  "Electronics",
        "category_l2":  "Headphones & Audio",
        "category_l3":  "Portable Speakers",
        "avg_rating":   4.5,
        "rating_count": 9800,
        "description":  (
            "The JBL Flip 6 packs a two-way speaker system with a dedicated "
            "tweeter for clearer highs into a cylindrical, IP67-rated body. "
            "JBL PartyBoost wireless linking connects multiple compatible "
            "speakers for a bigger sound across larger spaces."
        ),
        "features": (
            "2-way speaker system, IP67, 12-hour battery, JBL PartyBoost, "
            "USB-C charging, JBL Pure Bass, racetrack woofer, Bluetooth 5.1"
        ),
        "image":    "https://images.unsplash.com/photo-1564424224827-cd24b8915874?w=500&h=500&fit=crop",
    },

    # =========================================================================
    # SMARTPHONES & ACCESSORIES  (25 products, P0031–P0055)
    # =========================================================================

    # --- Smartphones (8) ---
    {
        "product_id":   "P0031",
        "title":        "Apple iPhone 15 Pro Max 256GB Natural Titanium",
        "brand":        "Apple",
        "price":        1199.00,
        "category_l1":  "Electronics",
        "category_l2":  "Smartphones & Accessories",
        "category_l3":  "Smartphones",
        "avg_rating":   4.8,
        "rating_count": 13400,
        "description":  (
            "iPhone 15 Pro Max introduces a titanium frame for an unprecedented "
            "strength-to-weight ratio in a smartphone chassis. The A17 Pro chip "
            "enables hardware-accelerated ray tracing for console-quality gaming, "
            "and the 5× optical telephoto camera opens new creative possibilities."
        ),
        "features": (
            "A17 Pro chip, 5× optical telephoto, titanium frame, USB 3 speeds, "
            "Action Button, ProRAW capture, Always-On Display, satellite SOS, 4K ProRes"
        ),
        "image":    "https://images.unsplash.com/photo-1695048133142-1a20484d2569?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0032",
        "title":        "Samsung Galaxy S24 Ultra 256GB Titanium Black",
        "brand":        "Samsung",
        "price":        1299.99,
        "category_l1":  "Electronics",
        "category_l2":  "Smartphones & Accessories",
        "category_l3":  "Smartphones",
        "avg_rating":   4.7,
        "rating_count": 11800,
        "description":  (
            "Galaxy S24 Ultra integrates Galaxy AI for real-time call translation, "
            "Circle to Search, and generative edit photo tools directly on device. "
            "The built-in S Pen provides 2.8 ms latency for natural handwriting, "
            "and the 200 MP main sensor captures extraordinary detail in low light."
        ),
        "features": (
            "Snapdragon 8 Gen 3, 200 MP camera, 10× optical zoom, built-in S Pen, "
            "Galaxy AI, 5000 mAh battery, 45W charging, titanium frame, 6.8-inch QHD+"
        ),
        "image":    "https://images.unsplash.com/photo-1610945415295-d9bbf067e59c?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0033",
        "title":        "Google Pixel 8 Pro 128GB Obsidian",
        "brand":        "Google",
        "price":        999.00,
        "category_l1":  "Electronics",
        "category_l2":  "Smartphones & Accessories",
        "category_l3":  "Smartphones",
        "avg_rating":   4.6,
        "rating_count": 7200,
        "description":  (
            "Google Tensor G3 enables exclusive AI features including Audio Magic "
            "Eraser for removing background noise from videos and Best Take for "
            "selecting the best face from a burst of group photos. The 50 MP main "
            "camera with 5× telephoto delivers exceptional computational photography."
        ),
        "features": (
            "Google Tensor G3, 50 MP + 48 MP + 48 MP cameras, 5× optical zoom, "
            "temperature sensor, 7-year software updates, Titan M2 chip, 5050 mAh, 30W"
        ),
        "image":    "https://images.unsplash.com/photo-1598327105666-5b89351aff97?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0034",
        "title":        "Samsung Galaxy A54 5G 128GB Awesome Graphite",
        "brand":        "Samsung",
        "price":        349.99,
        "category_l1":  "Electronics",
        "category_l2":  "Smartphones & Accessories",
        "category_l3":  "Smartphones",
        "avg_rating":   4.4,
        "rating_count": 8900,
        "description":  (
            "The Galaxy A54 brings flagship-inspired design with an IP67 rating "
            "and Gorilla Glass 5 display to the mid-range segment. The 50 MP "
            "optical image-stabilised main camera and 5000 mAh battery deliver "
            "dependable performance across a full day of heavy use."
        ),
        "features": (
            "50 MP OIS camera, 5000 mAh battery, IP67, Gorilla Glass 5, "
            "5G, 25W fast charging, 6.4-inch AMOLED, 4 years OS updates, Exynos 1380"
        ),
        "image":    "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0035",
        "title":        "Apple iPhone 15 128GB Blue",
        "brand":        "Apple",
        "price":        799.00,
        "category_l1":  "Electronics",
        "category_l2":  "Smartphones & Accessories",
        "category_l3":  "Smartphones",
        "avg_rating":   4.7,
        "rating_count": 12100,
        "description":  (
            "iPhone 15 brings the Dynamic Island and USB-C connector to Apple's "
            "mainstream lineup for the first time. The A16 Bionic chip handles "
            "computational photography for the 48 MP main camera, enabling "
            "4× zoom using a high-resolution 12 MP crop without quality loss."
        ),
        "features": (
            "A16 Bionic, 48 MP main camera, Dynamic Island, USB-C, crash detection, "
            "satellite SOS, 6.1-inch Super Retina XDR, 5G, all-day battery"
        ),
        "image":    "https://images.unsplash.com/photo-1592750475338-74b7b21085ab?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0036",
        "title":        "Google Pixel 7a 128GB Sea",
        "brand":        "Google",
        "price":        499.00,
        "category_l1":  "Electronics",
        "category_l2":  "Smartphones & Accessories",
        "category_l3":  "Smartphones",
        "avg_rating":   4.5,
        "rating_count": 6300,
        "description":  (
            "Pixel 7a brings the Google Tensor G2 chip and a 64 MP camera with "
            "optical image stabilisation to a more affordable price than the "
            "flagship Pixel 7. The 90 Hz OLED display and wireless charging "
            "capability make it feel like a premium device for a mid-range investment."
        ),
        "features": (
            "Google Tensor G2, 64 MP OIS camera, 90 Hz OLED, wireless charging, "
            "5G, IP67, face unlock, 4385 mAh, 18W charging, 5 years security updates"
        ),
        "image":    "https://images.unsplash.com/photo-1565849904461-04a58ad377e0?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0037",
        "title":        "Samsung Galaxy Z Flip5 256GB Cream",
        "brand":        "Samsung",
        "price":        999.99,
        "category_l1":  "Electronics",
        "category_l2":  "Smartphones & Accessories",
        "category_l3":  "Smartphones",
        "avg_rating":   4.4,
        "rating_count": 4100,
        "description":  (
            "Galaxy Z Flip5's larger 3.4-inch cover screen lets you check "
            "notifications, reply to messages, and use apps without unfolding "
            "the phone. The Flex hinge enables Flex Mode shooting, using the "
            "bottom half of the phone as a built-in tripod for hands-free content."
        ),
        "features": (
            "3.4-inch cover screen, Flex Mode, 12 MP camera, Snapdragon 8 Gen 2, "
            "IPX8, 5G, 25W charging, wireless charging, 6.7-inch foldable main display"
        ),
        "image":    "https://images.unsplash.com/photo-1631452180519-c014fe946bc7?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0038",
        "title":        "Apple iPhone SE (3rd Gen) 64GB Midnight",
        "brand":        "Apple",
        "price":        429.00,
        "category_l1":  "Electronics",
        "category_l2":  "Smartphones & Accessories",
        "category_l3":  "Smartphones",
        "avg_rating":   4.3,
        "rating_count": 7800,
        "description":  (
            "The most affordable iPhone packs the A15 Bionic chip — the same "
            "processor used in iPhone 13 Pro — into a 4.7-inch form factor with "
            "Touch ID. 5G connectivity and Smart HDR 4 photography make this a "
            "compelling choice for those who prefer a one-handed phone experience."
        ),
        "features": (
            "A15 Bionic, Touch ID, 5G, 12 MP camera, Smart HDR 4, 4.7-inch Retina, "
            "IP67, fast charging, Bluetooth 5.0, Ceramic Shield front"
        ),
        "image":    "https://images.unsplash.com/photo-1591337676887-a217a6970a8a?w=500&h=500&fit=crop",
    },

    # --- Phone Cases (4) ---
    {
        "product_id":   "P0039",
        "title":        "Apple MagSafe Clear Case for iPhone 15 Pro",
        "brand":        "Apple",
        "price":        49.00,
        "category_l1":  "Electronics",
        "category_l2":  "Smartphones & Accessories",
        "category_l3":  "Phone Cases",
        "avg_rating":   4.1,
        "rating_count": 5400,
        "description":  (
            "The Apple MagSafe Clear Case is optically clear to show off the "
            "natural titanium finish of iPhone 15 Pro while providing MagSafe "
            "charging compatibility. The hard polycarbonate back and soft "
            "microfibre lining protect against bumps and scratches."
        ),
        "features": (
            "MagSafe compatible, polycarbonate back, microfibre lining, "
            "raised edges, optically clear, wireless charging compatible, precise cutouts"
        ),
        "image":    "https://images.unsplash.com/photo-1601593346740-925612772716?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0040",
        "title":        "Anker 360° Protective Case for Samsung Galaxy S24",
        "brand":        "Anker",
        "price":        19.99,
        "category_l1":  "Electronics",
        "category_l2":  "Smartphones & Accessories",
        "category_l3":  "Phone Cases",
        "avg_rating":   4.3,
        "rating_count": 3200,
        "description":  (
            "Anker's 360-degree protective case pairs a rigid polycarbonate shell "
            "with a flexible TPU bumper to achieve MIL-STD-810G drop protection. "
            "The raised camera lip prevents lens scratches on flat surfaces, and "
            "precise port cutouts maintain quick access to all buttons and speakers."
        ),
        "features": (
            "MIL-STD-810G, dual-layer construction, raised camera lip, "
            "wireless charging compatible, anti-scratch, precise cutouts, slim profile"
        ),
        "image":    "https://images.unsplash.com/photo-1585386959984-a4155224a1ad?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0041",
        "title":        "Belkin SheerForce Protective Case for iPhone 15",
        "brand":        "Belkin",
        "price":        34.99,
        "category_l1":  "Electronics",
        "category_l2":  "Smartphones & Accessories",
        "category_l3":  "Phone Cases",
        "avg_rating":   4.0,
        "rating_count": 2100,
        "description":  (
            "SheerForce is constructed with an aramid fibre-reinforced polycarbonate "
            "to be both ultra-thin and highly impact resistant. At only 0.35 mm "
            "slim, it adds virtually no bulk while protecting against drops tested "
            "to 10 feet on a steel surface."
        ),
        "features": (
            "aramid fibre reinforced, 0.35 mm slim, 10-foot drop tested, "
            "wireless charging compatible, raised bezel, lightweight, UV-resistant"
        ),
        "image":    "https://images.unsplash.com/photo-1541367777708-7905fe3296c0?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0042",
        "title":        "Samsung Galaxy S24 Ultra Standing Grip Case",
        "brand":        "Samsung",
        "price":        59.99,
        "category_l1":  "Electronics",
        "category_l2":  "Smartphones & Accessories",
        "category_l3":  "Phone Cases",
        "avg_rating":   4.2,
        "rating_count": 2800,
        "description":  (
            "Samsung's official Standing Grip Case features a built-in ring that "
            "doubles as a kickstand for hands-free video watching and a secure "
            "finger loop for a more confident one-handed hold. The S Pen slot "
            "is preserved with a precise cutout at the base of the case."
        ),
        "features": (
            "built-in ring kickstand, S Pen compatible cutout, textured grip, "
            "wireless charging compatible, raised lips, TPU + PC, official Samsung"
        ),
        "image":    "https://images.unsplash.com/photo-1609081219090-a6d81d3085bf?w=500&h=500&fit=crop",
    },

    # --- Chargers & Cables (5) ---
    {
        "product_id":   "P0043",
        "title":        "Anker 737 GaN Prime 120W Desktop Charger",
        "brand":        "Anker",
        "price":        85.99,
        "category_l1":  "Electronics",
        "category_l2":  "Smartphones & Accessories",
        "category_l3":  "Chargers & Cables",
        "avg_rating":   4.6,
        "rating_count": 6700,
        "description":  (
            "Anker 737 uses third-generation GaN technology to deliver 120W of "
            "total power from three ports simultaneously — two USB-C and one USB-A. "
            "Its AI-controlled power distribution automatically adjusts wattage "
            "allocation based on which devices are connected and their charge states."
        ),
        "features": (
            "120W total, 3-port (2C + 1A), GaN III, AI power distribution, "
            "PowerIQ 4.0, foldable plug, USB-C 100W single port, compact desktop design"
        ),
        "image":    "https://images.unsplash.com/photo-1583863788434-e58a36330cf0?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0044",
        "title":        "Apple 20W USB-C Power Adapter",
        "brand":        "Apple",
        "price":        19.00,
        "category_l1":  "Electronics",
        "category_l2":  "Smartphones & Accessories",
        "category_l3":  "Chargers & Cables",
        "avg_rating":   4.4,
        "rating_count": 12800,
        "description":  (
            "The Apple 20W USB-C Power Adapter supports fast charging for iPhone "
            "8 and later, delivering up to 50% charge in 30 minutes. The compact "
            "foldable plug design reduces bulk in your bag, and USB Power Delivery "
            "compatibility charges iPad Pro, MacBook, and compatible Android phones."
        ),
        "features": (
            "20W USB-C PD, fast charging for iPhone, foldable plug, "
            "USB-C, compact design, Apple certified, universal voltage 100-240V"
        ),
        "image":    "https://images.unsplash.com/photo-1628815114220-718cf5e8d2d5?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0045",
        "title":        "Anker 240W USB-C to USB-C Braided Cable 6ft",
        "brand":        "Anker",
        "price":        15.99,
        "category_l1":  "Electronics",
        "category_l2":  "Smartphones & Accessories",
        "category_l3":  "Chargers & Cables",
        "avg_rating":   4.5,
        "rating_count": 9100,
        "description":  (
            "Rated for 240W power delivery, this USB-C cable handles everything "
            "from phone fast-charging to MacBook Pro powering without breaking a "
            "sweat. The braided nylon exterior is rated for 35,000+ bends, and "
            "a built-in E-Marker chip enables USB 2.0 480 Mbps data transfer."
        ),
        "features": (
            "240W USB PD 3.1, 480 Mbps data, nylon braided, 6 ft, "
            "35,000 bend cycles, E-Marker chip, USB-C to USB-C, universal compatibility"
        ),
        "image":    "https://images.unsplash.com/photo-1601999109332-542b18dbbc21?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0046",
        "title":        "Belkin BoostCharge Pro 3-in-1 MagSafe Charger",
        "brand":        "Belkin",
        "price":        149.99,
        "category_l1":  "Electronics",
        "category_l2":  "Smartphones & Accessories",
        "category_l3":  "Chargers & Cables",
        "avg_rating":   4.3,
        "rating_count": 4200,
        "description":  (
            "This MFi-certified charging station simultaneously charges iPhone via "
            "15W MagSafe, Apple Watch via an integrated fast-charge puck, and AirPods "
            "on a dedicated 5W Qi pad. The angled MagSafe puck positions iPhone in "
            "StandBy mode landscape orientation out of the box."
        ),
        "features": (
            "15W MagSafe, Apple Watch fast charge, 5W AirPods pad, MFi certified, "
            "USB-C cable included, StandBy compatible, folding legs, compact footprint"
        ),
        "image":    "https://images.unsplash.com/photo-1615526675159-e248c3021d3f?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0047",
        "title":        "Samsung 45W Super Fast Charger 2.0",
        "brand":        "Samsung",
        "price":        49.99,
        "category_l1":  "Electronics",
        "category_l2":  "Smartphones & Accessories",
        "category_l3":  "Chargers & Cables",
        "avg_rating":   4.5,
        "rating_count": 7600,
        "description":  (
            "Samsung's 45W Super Fast Charger 2.0 supports the highest wired "
            "charging speeds on Galaxy S23, S24, and compatible Galaxy Tab models. "
            "PPS (Programmable Power Supply) protocol negotiation ensures efficient "
            "charging without excess heat generation during extended sessions."
        ),
        "features": (
            "45W Super Fast Charging 2.0, PPS protocol, USB-C PD 3.0, "
            "foldable plug, GaN design, 100-240V universal voltage, compact"
        ),
        "image":    "https://images.unsplash.com/photo-1609091839311-d5365f9ff1c5?w=500&h=500&fit=crop",
    },

    # --- Screen Protectors (4) ---
    {
        "product_id":   "P0048",
        "title":        "Belkin UltraGlass 2 Screen Protector for iPhone 15 Pro",
        "brand":        "Belkin",
        "price":        14.99,
        "category_l1":  "Electronics",
        "category_l2":  "Smartphones & Accessories",
        "category_l3":  "Screen Protectors",
        "avg_rating":   4.3,
        "rating_count": 4800,
        "description":  (
            "UltraGlass 2 is made from ion-strengthened glass that achieves 2× "
            "the hardness of standard tempered glass protectors. The TrueClear "
            "coating maintains the vivid colours and contrast of the iPhone's "
            "Super Retina XDR display with no perceptible colour shift."
        ),
        "features": (
            "ion-strengthened glass, 9H hardness, case compatible, TrueClear coating, "
            "anti-fingerprint, easy install tray, full display coverage, touch sensitive"
        ),
        "image":    "https://images.unsplash.com/photo-1601972602237-8c79241e468b?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0049",
        "title":        "Samsung Galaxy S24 Ultra Privacy Screen Protector",
        "brand":        "Samsung",
        "price":        19.99,
        "category_l1":  "Electronics",
        "category_l2":  "Smartphones & Accessories",
        "category_l3":  "Screen Protectors",
        "avg_rating":   4.1,
        "rating_count": 3100,
        "description":  (
            "This privacy screen protector limits viewing angle to 30 degrees, "
            "ensuring on-screen content is visible only to the person holding "
            "the device. The hardened tempered glass layer provides 9H scratch "
            "resistance while maintaining full S Pen sensitivity."
        ),
        "features": (
            "30-degree privacy angle, 9H tempered glass, S Pen compatible, "
            "anti-fingerprint coating, bubble-free install, case compatible, oleophobic"
        ),
        "image":    "https://images.unsplash.com/photo-1574944985070-8f3ebc6b79d2?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0050",
        "title":        "Anker Easy On Screen Protector for iPhone 15 (2-Pack)",
        "brand":        "Anker",
        "price":        9.99,
        "category_l1":  "Electronics",
        "category_l2":  "Smartphones & Accessories",
        "category_l3":  "Screen Protectors",
        "avg_rating":   4.4,
        "rating_count": 7200,
        "description":  (
            "Anker's EasyOn installation tray removes the most common complaint "
            "about screen protectors — air bubbles and misalignment. Each pack "
            "contains two 0.33 mm tempered glass protectors with an oleophobic "
            "coating to reduce fingerprints from everyday use."
        ),
        "features": (
            "EasyOn installation tray, 0.33 mm tempered glass, oleophobic coating, "
            "9H hardness, 2-pack, case compatible, anti-bubble, touch sensitivity preserved"
        ),
        "image":    "https://images.unsplash.com/photo-1585060544812-6b45742d762f?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0051",
        "title":        "Belkin InvisiGlass Ultra for Samsung Galaxy A54",
        "brand":        "Belkin",
        "price":        12.99,
        "category_l1":  "Electronics",
        "category_l2":  "Smartphones & Accessories",
        "category_l3":  "Screen Protectors",
        "avg_rating":   4.2,
        "rating_count": 2400,
        "description":  (
            "InvisiGlass Ultra is manufactured to precise tolerances to ensure "
            "full-display edge-to-edge coverage without interfering with the "
            "fingerprint reader or in-display speakers. The scratch-resistant "
            "coating maintains clarity comparable to the bare screen."
        ),
        "features": (
            "full-display coverage, in-display fingerprint compatible, 9H hardness, "
            "oleophobic coating, anti-scratch, edge-to-edge, case compatible"
        ),
        "image":    "https://images.unsplash.com/photo-1512054502232-10a0a035d672?w=500&h=500&fit=crop",
    },

    # --- Power Banks (4) ---
    {
        "product_id":   "P0052",
        "title":        "Anker 737 Power Bank (PowerCore 26K)",
        "brand":        "Anker",
        "price":        109.99,
        "category_l1":  "Electronics",
        "category_l2":  "Smartphones & Accessories",
        "category_l3":  "Power Banks",
        "avg_rating":   4.7,
        "rating_count": 8900,
        "description":  (
            "PowerCore 26K packs 26,800 mAh into a smart battery with a built-in "
            "LCD screen displaying charge percentage and wattage in real time. "
            "The 140W USB-C port charges MacBook Pro at full speed while the "
            "secondary 60W USB-C port charges a second device simultaneously."
        ),
        "features": (
            "26,800 mAh, 140W + 60W USB-C, LCD display, USB-A 22.5W, "
            "PowerIQ 4.0, 3-port simultaneous charging, bi-directional USB-C, compact"
        ),
        "image":    "https://images.unsplash.com/photo-1609091839311-d5365f9ff1c5?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0053",
        "title":        "Belkin BoostCharge 10K MagSafe Power Bank",
        "brand":        "Belkin",
        "price":        79.99,
        "category_l1":  "Electronics",
        "category_l2":  "Smartphones & Accessories",
        "category_l3":  "Power Banks",
        "avg_rating":   4.3,
        "rating_count": 4100,
        "description":  (
            "This MagSafe-compatible power bank attaches magnetically to the back "
            "of any MagSafe iPhone, creating a wireless charging solution without "
            "any cables. The 10,000 mAh capacity provides approximately 2.5 full "
            "charges for iPhone 15, and the USB-C port recharges the bank itself."
        ),
        "features": (
            "MagSafe wireless, 10,000 mAh, 7.5W MagSafe output, USB-C recharge, "
            "LED indicator, compact form factor, kickstand mode, MFi certified"
        ),
        "image":    "https://images.unsplash.com/photo-1585338447937-7082f8fc763d?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0054",
        "title":        "Anker Nano Power Bank 10K with USB-C Connector",
        "brand":        "Anker",
        "price":        35.99,
        "category_l1":  "Electronics",
        "category_l2":  "Smartphones & Accessories",
        "category_l3":  "Power Banks",
        "avg_rating":   4.5,
        "rating_count": 6200,
        "description":  (
            "The Nano Power Bank integrates a folding USB-C plug directly into "
            "the body, eliminating the need for a separate cable when charging "
            "USB-C devices. At 196g and the size of a deck of cards, the "
            "10,000 mAh capacity provides meaningful top-up power without bulk."
        ),
        "features": (
            "built-in USB-C plug, 10,000 mAh, 22.5W USB-C output, 12W USB-A, "
            "foldable connector, LED indicator, 196g, compact, simultaneous charging"
        ),
        "image":    "https://images.unsplash.com/photo-1625315714730-fae74fae9c10?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0055",
        "title":        "Samsung 10,000mAh 25W Super Fast Charging Power Bank",
        "brand":        "Samsung",
        "price":        49.99,
        "category_l1":  "Electronics",
        "category_l2":  "Smartphones & Accessories",
        "category_l3":  "Power Banks",
        "avg_rating":   4.4,
        "rating_count": 5300,
        "description":  (
            "Samsung's official power bank supports 25W Super Fast Charging for "
            "compatible Galaxy devices and standard USB-C PD for other phones and "
            "tablets. The two-way fast charging system also rapidly recharges the "
            "power bank itself at 25W for minimal downtime between trips."
        ),
        "features": (
            "25W Super Fast Charging, 10,000 mAh, USB-C in/out, USB-A 15W, "
            "Samsung official, 2-way fast charge, compact, LED indicator"
        ),
        "image":    "https://images.unsplash.com/photo-1626806787461-102c1bfaaea1?w=500&h=500&fit=crop",
    },

    # =========================================================================
    # LAPTOPS & COMPUTERS  (20 products, P0056–P0075)
    # =========================================================================

    # --- Laptops (8) ---
    {
        "product_id":   "P0056",
        "title":        "Apple MacBook Pro 14-inch M3 Pro 512GB",
        "brand":        "Apple",
        "price":        1999.00,
        "category_l1":  "Electronics",
        "category_l2":  "Laptops & Computers",
        "category_l3":  "Laptops",
        "avg_rating":   4.9,
        "rating_count": 8700,
        "description":  (
            "M3 Pro delivers a 12-core CPU and 18-core GPU with 18 GB unified "
            "memory in a compact 14-inch chassis that achieves up to 18 hours of "
            "battery life. Hardware-accelerated ray tracing and mesh shading make "
            "it the most capable portable workstation Apple has ever made."
        ),
        "features": (
            "M3 Pro chip, 18 GB unified memory, 14-inch Liquid Retina XDR, "
            "18-hour battery, MagSafe 3, Thunderbolt 4 ×3, HDMI, SD card, 120 Hz ProMotion"
        ),
        "image":    "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0057",
        "title":        "Dell XPS 15 9530 Intel Core i9 32GB 1TB",
        "brand":        "Dell",
        "price":        2299.99,
        "category_l1":  "Electronics",
        "category_l2":  "Laptops & Computers",
        "category_l3":  "Laptops",
        "avg_rating":   4.6,
        "rating_count": 4200,
        "description":  (
            "XPS 15 9530 pairs Intel Core i9-13900H with NVIDIA RTX 4070 in "
            "Dell's thinnest 15-inch chassis, cooling both chips with a revised "
            "dual-fan system. The 15.6-inch OLED display achieves 100% DCI-P3 "
            "colour coverage with 0.2 ms response time for content creators."
        ),
        "features": (
            "Core i9-13900H, RTX 4070 8GB, 32 GB DDR5, OLED 3.5K 120 Hz, "
            "Thunderbolt 4 ×2, 86 Whr battery, 130W USB-C charging, CNC aluminium"
        ),
        "image":    "https://images.unsplash.com/photo-1593642702821-c8da6771f0c6?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0058",
        "title":        "Lenovo ThinkPad X1 Carbon Gen 11 i7 16GB",
        "brand":        "Lenovo",
        "price":        1749.00,
        "category_l1":  "Electronics",
        "category_l2":  "Laptops & Computers",
        "category_l3":  "Laptops",
        "avg_rating":   4.7,
        "rating_count": 3800,
        "description":  (
            "ThinkPad X1 Carbon Gen 11 weighs just 1.12 kg yet achieves MIL-STD-810H "
            "certification across 12 test categories for durability in demanding "
            "field conditions. The 14-inch IPS display with Eyesafe certification "
            "reduces blue light emission for extended professional use."
        ),
        "features": (
            "Core i7-1365U, 16 GB LPDDR5, 14-inch IPS 2.8K, MIL-STD-810H, "
            "Thunderbolt 4 ×2, 57 Whr battery, 1.12 kg, backlit keyboard, 4G LTE option"
        ),
        "image":    "https://images.unsplash.com/photo-1588872657578-7efd1f1555ed?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0059",
        "title":        "ASUS ROG Zephyrus G14 2024 AMD Ryzen 9 RTX 4070",
        "brand":        "ASUS",
        "price":        1799.99,
        "category_l1":  "Electronics",
        "category_l2":  "Laptops & Computers",
        "category_l3":  "Laptops",
        "avg_rating":   4.7,
        "rating_count": 5100,
        "description":  (
            "Zephyrus G14 2024 features a 3K OLED display with 120 Hz refresh "
            "and 0.2 ms response time inside a 1.65 kg chassis reinforced with "
            "aerospace-grade magnesium-aluminium. AMD Ryzen 9 and RTX 4070 deliver "
            "workstation-class performance for gaming and creative tasks alike."
        ),
        "features": (
            "Ryzen 9 8945HS, RTX 4070 8GB, 3K OLED 120 Hz, 32 GB DDR5, "
            "1 TB PCIe 4.0, MUX Switch, Thunderbolt 4, 73 Whr battery, 1.65 kg"
        ),
        "image":    "https://images.unsplash.com/photo-1603302576837-37561b2e2302?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0060",
        "title":        "HP Spectre x360 14 2-in-1 Intel Core Ultra 7",
        "brand":        "HP",
        "price":        1649.99,
        "category_l1":  "Electronics",
        "category_l2":  "Laptops & Computers",
        "category_l3":  "Laptops",
        "avg_rating":   4.5,
        "rating_count": 3300,
        "description":  (
            "Spectre x360 14 is HP's premium convertible, featuring a 2.8K OLED "
            "touchscreen that rotates 360 degrees for tablet, tent, and stand modes. "
            "Intel Core Ultra 7 with NPU acceleration handles AI-enhanced features "
            "like Live Captions and Background Blur in video calls natively."
        ),
        "features": (
            "Core Ultra 7 155H, 2.8K OLED touch, 360° hinge, 32 GB, "
            "Thunderbolt 4 ×2, HP Tilt Pen included, 83 Whr, Intel Arc iGPU, fingerprint"
        ),
        "image":    "https://images.unsplash.com/photo-1544731612-de7f96afe55f?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0061",
        "title":        "Lenovo IdeaPad 5 15 AMD Ryzen 7 16GB",
        "brand":        "Lenovo",
        "price":        649.99,
        "category_l1":  "Electronics",
        "category_l2":  "Laptops & Computers",
        "category_l3":  "Laptops",
        "avg_rating":   4.3,
        "rating_count": 6700,
        "description":  (
            "IdeaPad 5 offers mainstream laptop performance with Ryzen 7 5700U "
            "and AMD Radeon integrated graphics at a mid-range price. The 15.6-inch "
            "FHD IPS display covers 300 nits brightness with 72% NTSC colour for "
            "comfortable everyday productivity and media consumption."
        ),
        "features": (
            "Ryzen 7 5700U, 16 GB DDR4, 512 GB SSD, 15.6-inch FHD IPS, "
            "USB-C, HDMI, Wi-Fi 6, Bluetooth 5.1, backlit keyboard, 56 Whr"
        ),
        "image":    "https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0062",
        "title":        "Apple MacBook Air 13-inch M2 256GB Midnight",
        "brand":        "Apple",
        "price":        1099.00,
        "category_l1":  "Electronics",
        "category_l2":  "Laptops & Computers",
        "category_l3":  "Laptops",
        "avg_rating":   4.8,
        "rating_count": 11200,
        "description":  (
            "MacBook Air M2 eliminates the fan for completely silent operation "
            "while delivering up to 18-hour battery life in a wedge-free flat "
            "design. The Liquid Retina display with 500 nits brightness and "
            "P3 wide colour is the sharpest screen ever in a MacBook Air."
        ),
        "features": (
            "M2 chip, 8-core GPU, 8 GB unified memory, 13.6-inch Liquid Retina, "
            "fanless design, 18-hour battery, MagSafe, Thunderbolt ×2, 1080p webcam"
        ),
        "image":    "https://images.unsplash.com/photo-1611186871348-b1ce696e52c9?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0063",
        "title":        "Dell Inspiron 15 3000 Intel Core i5 8GB",
        "brand":        "Dell",
        "price":        549.99,
        "category_l1":  "Electronics",
        "category_l2":  "Laptops & Computers",
        "category_l3":  "Laptops",
        "avg_rating":   4.1,
        "rating_count": 8900,
        "description":  (
            "A reliable everyday laptop, the Inspiron 15 3000 combines Intel Core "
            "i5-1135G7 with 8 GB RAM and a 256 GB SSD for responsive performance "
            "in office applications and web browsing. The 15.6-inch anti-glare "
            "display reduces reflections in bright office environments."
        ),
        "features": (
            "Core i5-1135G7, 8 GB DDR4, 256 GB SSD, 15.6-inch anti-glare FHD, "
            "Wi-Fi 5, Bluetooth 5.0, USB-A ×3, USB-C, HDMI, 54 Whr battery"
        ),
        "image":    "https://images.unsplash.com/photo-1525547719571-a2d4ac8945e2?w=500&h=500&fit=crop",
    },

    # --- Monitors (5) ---
    {
        "product_id":   "P0064",
        "title":        "LG 27GP950-B 27-inch 4K Nano IPS 160Hz Gaming Monitor",
        "brand":        "LG",
        "price":        749.99,
        "category_l1":  "Electronics",
        "category_l2":  "Laptops & Computers",
        "category_l3":  "Monitors",
        "avg_rating":   4.7,
        "rating_count": 4500,
        "description":  (
            "LG's Nano IPS technology achieves 98% DCI-P3 colour coverage at "
            "4K resolution with 160 Hz refresh for simultaneous professional colour "
            "grading and gaming. HDMI 2.1 connectivity enables 4K 144Hz from "
            "PS5 and Xbox Series X without any compression artifacts."
        ),
        "features": (
            "27-inch 4K Nano IPS, 160 Hz, HDMI 2.1 ×2, DisplayPort 1.4, "
            "NVIDIA G-Sync, AMD FreeSync Premium, 1ms GtG, USB-C 90W, HDR600, VESA"
        ),
        "image":    "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0065",
        "title":        "Dell UltraSharp U2723DE 27-inch 4K USB-C Monitor",
        "brand":        "Dell",
        "price":        699.99,
        "category_l1":  "Electronics",
        "category_l2":  "Laptops & Computers",
        "category_l3":  "Monitors",
        "avg_rating":   4.6,
        "rating_count": 3700,
        "description":  (
            "UltraSharp U2723DE targets content creators with factory-calibrated "
            "colour accuracy (Delta E < 2) across 100% sRGB and 98% DCI-P3. "
            "The 90W USB-C connection charges a MacBook or ThinkPad while passing "
            "4K video signal through a single cable for a clean desk setup."
        ),
        "features": (
            "27-inch 4K IPS, Delta E < 2, 100% sRGB, 90W USB-C, Thunderbolt 4, "
            "USB hub built-in, HDMI 2.0, DisplayPort 1.4, height adjustable, VESA, 60 Hz"
        ),
        "image":    "https://images.unsplash.com/photo-1585792180666-f7347c490ee2?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0066",
        "title":        "Samsung Odyssey G7 32-inch 1440p 240Hz Curved Monitor",
        "brand":        "Samsung",
        "price":        549.99,
        "category_l1":  "Electronics",
        "category_l2":  "Laptops & Computers",
        "category_l3":  "Monitors",
        "avg_rating":   4.5,
        "rating_count": 5800,
        "description":  (
            "Odyssey G7 uses a 1000R curve radius — matching the curvature of the "
            "human eye — to deliver an immersive 32-inch gaming experience with "
            "240 Hz refresh and 1 ms GtG response. QLED quantum dot colour "
            "technology expands the colour volume to 95% DCI-P3."
        ),
        "features": (
            "32-inch 1000R curved QLED, 2560×1440, 240 Hz, 1ms GtG, "
            "G-Sync compatible, FreeSync Premium Pro, HDR600, HDMI 2.0 ×2, DisplayPort 1.4"
        ),
        "image":    "https://images.unsplash.com/photo-1616711906333-23cf6b04d35b?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0067",
        "title":        "LG 34WP65C-B 34-inch Ultrawide QHD Curved Monitor",
        "brand":        "LG",
        "price":        449.99,
        "category_l1":  "Electronics",
        "category_l2":  "Laptops & Computers",
        "category_l3":  "Monitors",
        "avg_rating":   4.4,
        "rating_count": 3900,
        "description":  (
            "The 34-inch ultrawide format provides a 21:9 aspect ratio that "
            "eliminates the need for dual-monitor setups in productivity workflows. "
            "The 160 Hz panel with HDR10 and FreeSync Premium maintains fluid "
            "motion in both gaming and video editing timelines."
        ),
        "features": (
            "34-inch QHD IPS curved, 3440×1440, 160 Hz, FreeSync Premium, "
            "HDR10, USB-C 65W, HDMI ×2, DisplayPort, 1ms GtG, KVM switch, VESA"
        ),
        "image":    "https://images.unsplash.com/photo-1547394765-185e1e68f34e?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0068",
        "title":        "ASUS ProArt PA278QV 27-inch 1440p Professional Monitor",
        "brand":        "ASUS",
        "price":        319.99,
        "category_l1":  "Electronics",
        "category_l2":  "Laptops & Computers",
        "category_l3":  "Monitors",
        "avg_rating":   4.5,
        "rating_count": 4100,
        "description":  (
            "PA278QV arrives pre-calibrated with a Delta E < 2 report verifying "
            "sRGB accuracy for colour-critical applications. A full ergonomic stand "
            "with 120 mm height adjustment, ±90° pivot, and swivel serves "
            "photographers and designers who work in both landscape and portrait orientation."
        ),
        "features": (
            "27-inch IPS 1440p, Delta E < 2, 100% sRGB, 100% Rec.709, "
            "75 Hz, HDMI ×2, DisplayPort, USB hub, full ergonomic stand, HDR10, VESA"
        ),
        "image":    "https://images.unsplash.com/photo-1586210579191-33b45e38fa2c?w=500&h=500&fit=crop",
    },

    # --- Keyboards & Mice (4) ---
    {
        "product_id":   "P0069",
        "title":        "Logitech MX Keys S Wireless Illuminated Keyboard",
        "brand":        "Logitech",
        "price":        109.99,
        "category_l1":  "Electronics",
        "category_l2":  "Laptops & Computers",
        "category_l3":  "Keyboards & Mice",
        "avg_rating":   4.6,
        "rating_count": 7800,
        "description":  (
            "MX Keys S features spherically-dished key caps that cup each fingertip "
            "for precise, comfortable typing at speed. Smart Illumination adjusts "
            "backlight brightness automatically based on ambient light and hand "
            "proximity, and multi-device pairing connects up to three computers."
        ),
        "features": (
            "spherical key dish, smart backlight, multi-device ×3, Easy Switch, "
            "USB-C, 10-day battery (backlit), USB receiver + Bluetooth, Windows/macOS"
        ),
        "image":    "https://images.unsplash.com/photo-1587829741301-dc798b83add3?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0070",
        "title":        "Logitech MX Master 3S Wireless Performance Mouse",
        "brand":        "Logitech",
        "price":        99.99,
        "category_l1":  "Electronics",
        "category_l2":  "Laptops & Computers",
        "category_l3":  "Keyboards & Mice",
        "avg_rating":   4.7,
        "rating_count": 13400,
        "description":  (
            "MX Master 3S combines an 8000 DPI optical sensor with MagSpeed "
            "electromagnetic scrolling that accelerates through 1000-line documents "
            "in less than one second. Quiet click technology reduces click noise "
            "by 90% compared to conventional mice while maintaining tactile feedback."
        ),
        "features": (
            "8000 DPI sensor, MagSpeed scrolling, quiet clicks, thumb wheel, "
            "multi-device ×3, USB-C, 70-day battery, Easy Switch, Bolt USB receiver"
        ),
        "image":    "https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0071",
        "title":        "Apple Magic Keyboard with Touch ID and Numeric Keypad",
        "brand":        "Apple",
        "price":        129.00,
        "category_l1":  "Electronics",
        "category_l2":  "Laptops & Computers",
        "category_l3":  "Keyboards & Mice",
        "avg_rating":   4.5,
        "rating_count": 9200,
        "description":  (
            "Apple's full-size Magic Keyboard integrates Touch ID for secure "
            "authentication and Apple Pay without Face ID. The low-profile scissor "
            "mechanism provides 1 mm key travel with responsive, comfortable "
            "feedback, and the numeric keypad aids financial and spreadsheet work."
        ),
        "features": (
            "Touch ID, scissor mechanism, numeric keypad, USB-C charging, "
            "Bluetooth, 1 mm key travel, Lightning to USB-C cable included, full size"
        ),
        "image":    "https://images.unsplash.com/photo-1558618666-fcd25c85f82e?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0072",
        "title":        "Dell Pro Wireless Mouse WM126",
        "brand":        "Dell",
        "price":        26.99,
        "category_l1":  "Electronics",
        "category_l2":  "Laptops & Computers",
        "category_l3":  "Keyboards & Mice",
        "avg_rating":   4.2,
        "rating_count": 11000,
        "description":  (
            "WM126 is a no-nonsense wireless mouse designed for productivity "
            "with a 1000 DPI optical sensor and 12-month battery life on a single "
            "AA cell. The nano USB receiver stores in the mouse body for travel, "
            "and the ambidextrous design accommodates both left and right-handed users."
        ),
        "features": (
            "1000 DPI optical, 12-month battery, nano USB receiver storage, "
            "ambidextrous, 2.4 GHz wireless, 3 button + scroll, plug and play"
        ),
        "image":    "https://images.unsplash.com/photo-1605773527852-c546a8584ea3?w=500&h=500&fit=crop",
    },

    # --- Webcams (3) ---
    {
        "product_id":   "P0073",
        "title":        "Logitech Brio 4K Ultra HD Webcam",
        "brand":        "Logitech",
        "price":        179.99,
        "category_l1":  "Electronics",
        "category_l2":  "Laptops & Computers",
        "category_l3":  "Webcams",
        "avg_rating":   4.5,
        "rating_count": 8700,
        "description":  (
            "Brio 4K streams at 4K 30fps or 1080p 60fps with HDR enabled by "
            "RightLight 3 technology, which automatically adjusts exposure to "
            "balance subjects against bright windows or dark rooms. Windows "
            "Hello facial recognition is supported for passwordless sign-in."
        ),
        "features": (
            "4K 30fps, 1080p 60fps, HDR RightLight 3, Windows Hello, "
            "5× digital zoom, noise-cancelling dual mic, USB-C, privacy shutter, 90° FOV"
        ),
        "image":    "https://images.unsplash.com/photo-1596742578443-7682ef5251cd?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0074",
        "title":        "Anker PowerConf C300 1080p AI Webcam",
        "brand":        "Anker",
        "price":        79.99,
        "category_l1":  "Electronics",
        "category_l2":  "Laptops & Computers",
        "category_l3":  "Webcams",
        "avg_rating":   4.4,
        "rating_count": 4300,
        "description":  (
            "PowerConf C300 uses an AI auto-framing algorithm to keep you centred "
            "in frame as you move around your workspace. The Sony Starvis sensor "
            "delivers 1080p 60fps video with HDR, producing clear images even in "
            "the challenging backlit conditions of home office environments."
        ),
        "features": (
            "AI auto-framing, Sony Starvis 1080p 60fps, HDR, 65° / 78° / 90° FOV, "
            "noise-cancelling mic, USB-C, privacy cover, plug and play, 6× zoom"
        ),
        "image":    "https://images.unsplash.com/photo-1611532736597-de2d4265fba3?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0075",
        "title":        "Dell UltraSharp Webcam WB7022 4K",
        "brand":        "Dell",
        "price":        199.99,
        "category_l1":  "Electronics",
        "category_l2":  "Laptops & Computers",
        "category_l3":  "Webcams",
        "avg_rating":   4.3,
        "rating_count": 2800,
        "description":  (
            "Dell UltraSharp 4K Webcam uses AI-based auto-framing and background "
            "blurring to produce professional video quality without an external "
            "capture card. The Sony STARVIS 2 sensor achieves low-light performance "
            "at ISO 6400, keeping faces sharp in poorly lit rooms."
        ),
        "features": (
            "4K 30fps, Sony STARVIS 2, AI auto-framing, background blur, "
            "4× digital zoom, dual stereo mic, USB-C, magnetic mount, privacy shutter"
        ),
        "image":    "https://images.unsplash.com/photo-1623949556303-b0d17d198863?w=500&h=500&fit=crop",
    },

    # =========================================================================
    # CAMERAS & PHOTOGRAPHY  (15 products, P0076–P0090)
    # =========================================================================

    {
        "product_id":   "P0076",
        "title":        "Canon EOS R6 Mark II Mirrorless Camera Body",
        "brand":        "Canon",
        "price":        2499.00,
        "category_l1":  "Electronics",
        "category_l2":  "Cameras & Photography",
        "category_l3":  "Mirrorless Cameras",
        "avg_rating":   4.8,
        "rating_count": 3200,
        "description":  (
            "EOS R6 Mark II houses a 40 MP full-frame CMOS sensor with Canon's "
            "DIGIC X processor, enabling continuous shooting at 40 fps with "
            "full autofocus. The subject tracking system recognises people, animals, "
            "vehicles, and aircraft automatically, locking on with single-digit millisecond precision."
        ),
        "features": (
            "40 MP full-frame CMOS, 40fps continuous, dual UHS-II SD, "
            "6K RAW video, in-body 8-stop stabilisation, dual pixel CMOS AF, Canon RF mount"
        ),
        "image":    "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0077",
        "title":        "Sony Alpha A7 IV Full-Frame Mirrorless Camera",
        "brand":        "Sony",
        "price":        2499.99,
        "category_l1":  "Electronics",
        "category_l2":  "Cameras & Photography",
        "category_l3":  "Mirrorless Cameras",
        "avg_rating":   4.8,
        "rating_count": 4100,
        "description":  (
            "A7 IV's 33 MP back-illuminated CMOS sensor combines with the latest "
            "Bionz XR processor to deliver exceptional dynamic range and low-light "
            "performance to ISO 51200. Real-time eye tracking follows humans and "
            "animals across the frame even during rapid, unpredictable movement."
        ),
        "features": (
            "33 MP BSI-CMOS, 10fps, 4K 60fps video, 5-axis IBIS, dual card slots, "
            "real-time eye AF, USB-C PD charging, CFexpress Type A + SD, Sony E-mount"
        ),
        "image":    "https://images.unsplash.com/photo-1502920917128-1aa500764cbd?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0078",
        "title":        "Nikon Z6 III Full-Frame Mirrorless Camera",
        "brand":        "Nikon",
        "price":        2199.95,
        "category_l1":  "Electronics",
        "category_l2":  "Cameras & Photography",
        "category_l3":  "Mirrorless Cameras",
        "avg_rating":   4.7,
        "rating_count": 1800,
        "description":  (
            "Z6 III introduces Nikon's first partial stacked CMOS sensor, allowing "
            "120fps continuous shooting at 24.5 MP with zero blackout. 6K RAW "
            "video output and ProRes recording internally make this a hybrid "
            "powerhouse for photojournalists and commercial filmmakers."
        ),
        "features": (
            "24.5 MP partial stacked CMOS, 120fps, 6K ProRes RAW, "
            "8-stop IBIS, subject detection AF, dual card slots, USB-C, Nikon Z-mount"
        ),
        "image":    "https://images.unsplash.com/photo-1510127034890-ba27508e9f1c?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0079",
        "title":        "Canon EOS 90D DSLR Camera Body",
        "brand":        "Canon",
        "price":        1149.00,
        "category_l1":  "Electronics",
        "category_l2":  "Cameras & Photography",
        "category_l3":  "DSLR Cameras",
        "avg_rating":   4.7,
        "rating_count": 4500,
        "description":  (
            "EOS 90D offers the traditional DSLR experience with a 32.5 MP APS-C "
            "sensor, optical viewfinder, and physical controls cherished by "
            "enthusiasts. The 45-point all-cross-type AF system covers a wide "
            "area of the frame for reliable focus during sports and wildlife."
        ),
        "features": (
            "32.5 MP APS-C, 10fps, 45-point all-cross AF, 4K 30fps UHD video, "
            "dual UHS-II SD, optical viewfinder, articulating touchscreen, Canon EF-S mount"
        ),
        "image":    "https://images.unsplash.com/photo-1564466809058-bf4114d55352?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0080",
        "title":        "Nikon D7500 DSLR Camera Body",
        "brand":        "Nikon",
        "price":        897.00,
        "category_l1":  "Electronics",
        "category_l2":  "Cameras & Photography",
        "category_l3":  "DSLR Cameras",
        "avg_rating":   4.6,
        "rating_count": 5200,
        "description":  (
            "D7500 brings the 20.9 MP sensor from the flagship D500 to a lighter "
            "body, making it one of the most capable APS-C DSLRs for its price. "
            "100 RAW buffer depth and 8fps continuous shooting handle fast subjects, "
            "and the tilting touchscreen simplifies low-angle compositions."
        ),
        "features": (
            "20.9 MP sensor from D500, 8fps, 100 RAW buffer, 4K UHD video, "
            "Nikon AF-P compatible, tilting touchscreen, dual SD slots, Nikon F-mount"
        ),
        "image":    "https://images.unsplash.com/photo-1617005082133-548c4dd27f35?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0081",
        "title":        "GoPro HERO12 Black Action Camera",
        "brand":        "GoPro",
        "price":        399.99,
        "category_l1":  "Electronics",
        "category_l2":  "Cameras & Photography",
        "category_l3":  "Action Cameras",
        "avg_rating":   4.6,
        "rating_count": 7800,
        "description":  (
            "HERO12 Black records 5.3K60 video and 27 MP photos in a waterproof "
            "housing rated to 10 m without a separate case. HyperSmooth 6.0 video "
            "stabilisation eliminates camera shake across all video modes, and "
            "the 1.9× lens maximises wide-angle capture for immersive action footage."
        ),
        "features": (
            "5.3K60 video, 27 MP photo, waterproof to 10m, HyperSmooth 6.0, "
            "Max Lens Mod compatible, Bluetooth + Wi-Fi, USB-C, 2.27-hour battery"
        ),
        "image":    "https://images.unsplash.com/photo-1526170375885-4d8ecf77b99f?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0082",
        "title":        "DJI Osmo Action 4 Waterproof Action Camera",
        "brand":        "DJI",
        "price":        249.00,
        "category_l1":  "Electronics",
        "category_l2":  "Cameras & Photography",
        "category_l3":  "Action Cameras",
        "avg_rating":   4.5,
        "rating_count": 3900,
        "description":  (
            "Osmo Action 4 uses a 1/1.3-inch CMOS sensor — significantly larger "
            "than most action cameras — to deliver exceptional dynamic range and "
            "low-light sensitivity. RockSteady 3.0+ stabilisation and HorizonSteady "
            "keep footage smooth even during extreme sports with 360° rotation."
        ),
        "features": (
            "1/1.3-inch CMOS, 4K 120fps, RockSteady 3.0+ stabilisation, "
            "10m waterproof, -20°C cold resistance, magnetic quick-release, USB-C"
        ),
        "image":    "https://images.unsplash.com/photo-1547394765-185e1e68f34e?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0083",
        "title":        "Canon RF 50mm f/1.8 STM Camera Lens",
        "brand":        "Canon",
        "price":        224.99,
        "category_l1":  "Electronics",
        "category_l2":  "Cameras & Photography",
        "category_l3":  "Camera Lenses",
        "avg_rating":   4.7,
        "rating_count": 5600,
        "description":  (
            "The RF 50mm f/1.8 STM is Canon's entry-level prime for R-system cameras, "
            "providing a natural 50mm perspective on full-frame or 80mm equivalent "
            "on APS-C. The wide f/1.8 maximum aperture produces shallow depth "
            "of field for portrait work and performs well in low-light conditions."
        ),
        "features": (
            "50mm f/1.8, STM autofocus motor, 9-blade aperture diaphragm, "
            "Canon RF mount, 43mm filter thread, 160g, weather sealing, optical IS"
        ),
        "image":    "https://images.unsplash.com/photo-1617005082133-548c4dd27f35?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0084",
        "title":        "Sony FE 24-70mm f/2.8 GM II Zoom Lens",
        "brand":        "Sony",
        "price":        2299.99,
        "category_l1":  "Electronics",
        "category_l2":  "Cameras & Photography",
        "category_l3":  "Camera Lenses",
        "avg_rating":   4.9,
        "rating_count": 1200,
        "description":  (
            "G Master II represents the pinnacle of Sony's E-mount zoom lens "
            "engineering, delivering corner-to-corner sharpness at f/2.8 that "
            "rivals prime lenses. The Extreme Aspherical XA element controls "
            "aberration and the dual linear motors achieve near-silent focus even during video."
        ),
        "features": (
            "24-70mm f/2.8, XA element, dual linear AF motors, 9-blade aperture, "
            "weather sealing, 695g, 82mm filter, Sony E-mount, optical IS compatible"
        ),
        "image":    "https://images.unsplash.com/photo-1495707902641-75cac588d2e9?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0085",
        "title":        "Nikon NIKKOR Z 85mm f/1.8 S Portrait Lens",
        "brand":        "Nikon",
        "price":        749.95,
        "category_l1":  "Electronics",
        "category_l2":  "Cameras & Photography",
        "category_l3":  "Camera Lenses",
        "avg_rating":   4.8,
        "rating_count": 2100,
        "description":  (
            "NIKKOR Z 85mm f/1.8 S produces smooth, creamy bokeh thanks to "
            "a nine-blade aperture and Nikon's Multi-Focus System using two "
            "separate focus groups for fast, accurate AF across the full frame. "
            "Internal focusing ensures the physical length never changes during operation."
        ),
        "features": (
            "85mm f/1.8, Nikon Z-mount, 9-blade diaphragm, internal focus, "
            "weather sealed, nano crystal coat, 67mm filter, 470g, silent AF, 0.8m MFD"
        ),
        "image":    "https://images.unsplash.com/photo-1606986628253-49e5c32b45df?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0086",
        "title":        "Joby GorillaPod 5K Flexible Tripod System",
        "brand":        "Joby",
        "price":        89.95,
        "category_l1":  "Electronics",
        "category_l2":  "Cameras & Photography",
        "category_l3":  "Tripods",
        "avg_rating":   4.5,
        "rating_count": 7200,
        "description":  (
            "GorillaPod 5K's flexible legs with rubber-coated joints wrap around "
            "poles, branches, and railings for unconventional camera positions "
            "impossible with traditional tripods. The 5 kg payload capacity "
            "supports mirrorless cameras with medium telephoto lenses attached."
        ),
        "features": (
            "5 kg payload, flexible legs, Arca-Swiss compatible quick release, "
            "bubble level, 360° ball head, wrap around mounting, compact when folded"
        ),
        "image":    "https://images.unsplash.com/photo-1542567455-cd733f23fbb1?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0087",
        "title":        "Manfrotto MT190XPRO4 Aluminium Tripod",
        "brand":        "Manfrotto",
        "price":        149.95,
        "category_l1":  "Electronics",
        "category_l2":  "Cameras & Photography",
        "category_l3":  "Tripods",
        "avg_rating":   4.6,
        "rating_count": 4800,
        "description":  (
            "MT190XPRO4's patented 90-degree column rotation pivots the centre "
            "column horizontally for macro or overhead shooting without a separate "
            "boom arm. The four-section aluminium legs provide a maximum height of "
            "163 cm with the column extended, supporting loads up to 7 kg."
        ),
        "features": (
            "90° column rotation, 4-section aluminium legs, 163 cm max height, "
            "7 kg load capacity, Easy Link connector, half ball leg angle, 1.9 kg"
        ),
        "image":    "https://images.unsplash.com/photo-1616423640778-28d1b53229bd?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0088",
        "title":        "Peak Design Travel Tripod Carbon Fibre",
        "brand":        "Peak Design",
        "price":        599.95,
        "category_l1":  "Electronics",
        "category_l2":  "Cameras & Photography",
        "category_l3":  "Tripods",
        "avg_rating":   4.8,
        "rating_count": 2600,
        "description":  (
            "Peak Design Travel Tripod collapses to just 39 cm in a cylindrical "
            "form factor that packs into a camera backpack side pocket without "
            "protruding. The 5-leg hub design allows ultra-low 6 cm shooting height "
            "while the inverted leg fold enables legs-as-monopod versatility."
        ),
        "features": (
            "carbon fibre, 39 cm folded length, 5-leg hub, 6 cm low-angle height, "
            "Arca-Swiss compatible, 1625g, 9 kg payload, aluminium ball head, carrying bag"
        ),
        "image":    "https://images.unsplash.com/photo-1617912324022-c41543e5fa09?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0089",
        "title":        "DJI Mini 4 Pro Drone with RC 2 Remote",
        "brand":        "DJI",
        "price":        959.00,
        "category_l1":  "Electronics",
        "category_l2":  "Cameras & Photography",
        "category_l3":  "Action Cameras",
        "avg_rating":   4.8,
        "rating_count": 3500,
        "description":  (
            "Mini 4 Pro weighs under 249 g, placing it below the registration "
            "threshold in most countries, while featuring a 48 MP quad-Bayer sensor "
            "with f/1.7 aperture for exceptional aerial low-light photography. "
            "Omnidirectional obstacle sensing and 34-minute flight time maximise creative opportunities."
        ),
        "features": (
            "under 249g, 48 MP f/1.7, 4K 100fps, 34-min flight time, "
            "omnidirectional obstacle sensing, 20 km video transmission, RC 2 included"
        ),
        "image":    "https://images.unsplash.com/photo-1473968512647-3e447244af8f?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0090",
        "title":        "GoPro HERO11 Black Mini Compact Action Camera",
        "brand":        "GoPro",
        "price":        299.99,
        "category_l1":  "Electronics",
        "category_l2":  "Cameras & Photography",
        "category_l3":  "Action Cameras",
        "avg_rating":   4.4,
        "rating_count": 4200,
        "description":  (
            "HERO11 Black Mini strips the screen and removable battery from the "
            "standard HERO11 to create the most compact GoPro ever made that "
            "can record 5.3K video. The mounting tabs are integrated directly "
            "into the body for a lower profile on helmet and body mounts."
        ),
        "features": (
            "5.3K60 video, HyperSmooth 5.0, waterproof to 10m, 8× slow motion, "
            "integrated mounting tabs, internal battery, Wi-Fi, Bluetooth, USB-C"
        ),
        "image":    "https://images.unsplash.com/photo-1519608487953-e999c86e7455?w=500&h=500&fit=crop",
    },

    # =========================================================================
    # SMART HOME & IoT  (15 products, P0091–P0105)
    # =========================================================================

    {
        "product_id":   "P0091",
        "title":        "Amazon Echo Show 10 (3rd Gen) Smart Display",
        "brand":        "Amazon",
        "price":        249.99,
        "category_l1":  "Electronics",
        "category_l2":  "Smart Home & IoT",
        "category_l3":  "Smart Displays",
        "avg_rating":   4.4,
        "rating_count": 8900,
        "description":  (
            "Echo Show 10 features a 10.1-inch HD display mounted on a motorised "
            "base that rotates to keep you in frame during video calls as you move "
            "around the room. The directional speaker array follows the display "
            "rotation, ensuring audio stays focused towards your current position."
        ),
        "features": (
            "10.1-inch HD display, motorised rotating base, 13 MP camera, "
            "Alexa, Zigbee hub, directional speakers, privacy shutter, Wi-Fi 5"
        ),
        "image":    "https://images.unsplash.com/photo-1543512214-318c7553f230?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0092",
        "title":        "Google Nest Hub Max 10-inch Smart Display",
        "brand":        "Google",
        "price":        229.99,
        "category_l1":  "Electronics",
        "category_l2":  "Smart Home & IoT",
        "category_l3":  "Smart Displays",
        "avg_rating":   4.4,
        "rating_count": 6700,
        "description":  (
            "Nest Hub Max uses Face Match to recognise household members and "
            "display personalised calendars, commute times, and media "
            "recommendations automatically. The 6.5 MP camera enables video calls "
            "via Google Meet and Duo, and photo-frame mode pulls from Google Photos."
        ),
        "features": (
            "10-inch HD display, 6.5 MP camera, Face Match, Google Assistant, "
            "Nest cam integration, stereo speakers, Wi-Fi, Bluetooth, Thread"
        ),
        "image":    "https://images.unsplash.com/photo-1558089687-f282ffcbc126?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0093",
        "title":        "Amazon Echo (4th Gen) Smart Speaker",
        "brand":        "Amazon",
        "price":        99.99,
        "category_l1":  "Electronics",
        "category_l2":  "Smart Home & IoT",
        "category_l3":  "Smart Speakers",
        "avg_rating":   4.5,
        "rating_count": 14200,
        "description":  (
            "Echo 4th Gen delivers premium 360-degree sound from a three-speaker "
            "array with a dedicated woofer and two tweeters, alongside a built-in "
            "Zigbee hub that controls compatible smart home devices without an "
            "additional hub. Alexa Guard detects smoke alarms and glass breaking sounds."
        ),
        "features": (
            "3-speaker 360° audio, built-in Zigbee hub, Alexa Guard, "
            "temperature sensor, Wi-Fi 5, Bluetooth 5.0, 3.5 mm aux output, fabric design"
        ),
        "image":    "https://images.unsplash.com/photo-1512446816042-444d641267d4?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0094",
        "title":        "Google Nest Audio Smart Speaker",
        "brand":        "Google",
        "price":        99.99,
        "category_l1":  "Electronics",
        "category_l2":  "Smart Home & IoT",
        "category_l3":  "Smart Speakers",
        "avg_rating":   4.5,
        "rating_count": 9800,
        "description":  (
            "Nest Audio uses Media EQ to automatically tune its sound profile "
            "depending on whether you are playing music, podcasts, or audiobooks. "
            "Multi-room audio via Google Cast links multiple Nest speakers for "
            "synchronised audio across different rooms without perceptible lag."
        ),
        "features": (
            "75 mm woofer + 19 mm tweeter, Media EQ, Google Cast, "
            "Google Assistant, Wi-Fi 5, Bluetooth 5.0, fabric exterior, 3 mics"
        ),
        "image":    "https://images.unsplash.com/photo-1543512214-318c7553f230?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0095",
        "title":        "Philips Hue White and Colour Ambiance Starter Kit",
        "brand":        "Philips",
        "price":        199.99,
        "category_l1":  "Electronics",
        "category_l2":  "Smart Home & IoT",
        "category_l3":  "Smart Lighting",
        "avg_rating":   4.5,
        "rating_count": 7400,
        "description":  (
            "The Hue starter kit includes three A19 colour ambiance bulbs and the "
            "Hue Bridge, unlocking 16 million colours and dynamic lighting scenes "
            "synced to music, movies, and games. Geofencing automation switches "
            "lights on as you arrive home and off when you leave."
        ),
        "features": (
            "16M colours, Zigbee bridge, 3 smart bulbs, voice control, "
            "Bluetooth fallback, Entertainment sync, geofencing, app automation, dimming"
        ),
        "image":    "https://images.unsplash.com/photo-1558002038-1055907df827?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0096",
        "title":        "Philips Hue Play HDMI Sync Box 4K",
        "brand":        "Philips",
        "price":        279.99,
        "category_l1":  "Electronics",
        "category_l2":  "Smart Home & IoT",
        "category_l3":  "Smart Lighting",
        "avg_rating":   4.3,
        "rating_count": 3100,
        "description":  (
            "Hue Play HDMI Sync Box analyses colour from any 4K HDR source connected "
            "through its four HDMI inputs and extends those colours to surrounding "
            "Hue lights in real time with less than 60 ms latency. Dolby Vision and "
            "HDR10+ pass-through preserves the full video quality of premium content."
        ),
        "features": (
            "4K Dolby Vision HDR pass-through, 4 HDMI inputs, < 60ms sync latency, "
            "Hue integration, Wi-Fi, iOS/Android app, automatic game/movie/music modes"
        ),
        "image":    "https://images.unsplash.com/photo-1550009158-9ebf69173e03?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0097",
        "title":        "TP-Link Kasa Smart Plug Mini EP25 Matter",
        "brand":        "TP-Link",
        "price":        15.99,
        "category_l1":  "Electronics",
        "category_l2":  "Smart Home & IoT",
        "category_l3":  "Smart Plugs",
        "avg_rating":   4.5,
        "rating_count": 9200,
        "description":  (
            "EP25 supports the Matter smart home standard, enabling direct "
            "compatibility with Apple Home, Google Home, Amazon Alexa, and Samsung "
            "SmartThings without brand-specific bridges. Real-time energy monitoring "
            "tracks power consumption at the socket level through the Kasa app."
        ),
        "features": (
            "Matter compatible, energy monitoring, 15A, no hub required, "
            "Alexa/Google/Apple HomeKit, schedule automation, Wi-Fi, compact design"
        ),
        "image":    "https://images.unsplash.com/photo-1556155092-490a1ba16284?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0098",
        "title":        "Amazon Smart Plug Mini with Energy Monitoring",
        "brand":        "Amazon",
        "price":        12.99,
        "category_l1":  "Electronics",
        "category_l2":  "Smart Home & IoT",
        "category_l3":  "Smart Plugs",
        "avg_rating":   4.4,
        "rating_count": 11800,
        "description":  (
            "Amazon's own smart plug fits side by side in a standard dual outlet "
            "without blocking the second socket, unlike most competitors. "
            "Alexa energy monitoring provides daily, monthly, and yearly usage "
            "data with cost estimates based on your electricity rate."
        ),
        "features": (
            "compact side-by-side fit, energy monitoring, 15A, Alexa native, "
            "schedule and timer, Wi-Fi, no hub, away mode automation"
        ),
        "image":    "https://images.unsplash.com/photo-1558618666-fcd25c85f82e?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0099",
        "title":        "Google Nest Cam (Outdoor, Wired) Security Camera",
        "brand":        "Google",
        "price":        99.99,
        "category_l1":  "Electronics",
        "category_l2":  "Smart Home & IoT",
        "category_l3":  "Smart Security",
        "avg_rating":   4.3,
        "rating_count": 5700,
        "description":  (
            "Nest Cam wired performs intelligent event detection on-device, "
            "distinguishing between people, animals, and vehicles with no subscription "
            "required. Three hours of free event history comes included, while "
            "Nest Aware extends this to 30 days of continuous recording."
        ),
        "features": (
            "1080p HDR, on-device AI detection, 3-hour free event history, "
            "IP54 weather resistant, night vision, two-way audio, Wi-Fi, Google Home"
        ),
        "image":    "https://images.unsplash.com/photo-1558002038-1055907df827?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0100",
        "title":        "Amazon Blink Outdoor 4 Wireless Security Camera 3-Pack",
        "brand":        "Amazon",
        "price":        109.99,
        "category_l1":  "Electronics",
        "category_l2":  "Smart Home & IoT",
        "category_l3":  "Smart Security",
        "avg_rating":   4.2,
        "rating_count": 8100,
        "description":  (
            "Blink Outdoor 4's two-year battery life from a pair of AA lithium cells "
            "eliminates the need to run outdoor power cables. Enhanced motion detection "
            "with bird's-eye zone selection reduces false alerts from passing cars "
            "or swaying trees by focusing only on defined activity zones."
        ),
        "features": (
            "2-year battery life, 1080p HDR, bird's-eye zone detection, "
            "two-way audio, night vision, Alexa, Blink Sync Module 2 included, IP65"
        ),
        "image":    "https://images.unsplash.com/photo-1580745294949-1c1f4b4cd817?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0101",
        "title":        "Amazon Echo Dot (5th Gen) with Clock",
        "brand":        "Amazon",
        "price":        59.99,
        "category_l1":  "Electronics",
        "category_l2":  "Smart Home & IoT",
        "category_l3":  "Smart Speakers",
        "avg_rating":   4.5,
        "rating_count": 13600,
        "description":  (
            "Echo Dot 5th Gen with Clock features an LED display showing time, "
            "weather, alarms, and now song titles from Amazon Music. The redesigned "
            "speaker delivers bigger sound than the previous generation, and a "
            "built-in temperature sensor provides room readings through Alexa."
        ),
        "features": (
            "LED display, temperature sensor, improved 1.73-inch speaker, "
            "Alexa, tap gestures, Wi-Fi 5, Bluetooth 5.0, 3.5 mm output, Motion detect"
        ),
        "image":    "https://images.unsplash.com/photo-1543512214-318c7553f230?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0102",
        "title":        "TP-Link Tapo C200 Pan/Tilt Indoor Security Camera",
        "brand":        "TP-Link",
        "price":        29.99,
        "category_l1":  "Electronics",
        "category_l2":  "Smart Home & IoT",
        "category_l3":  "Smart Security",
        "avg_rating":   4.4,
        "rating_count": 12400,
        "description":  (
            "Tapo C200 provides 360-degree horizontal pan and 130-degree tilt to "
            "monitor every corner of a room without blind spots. Person detection "
            "alerts distinguish humans from general motion for fewer false "
            "notifications, and two-way audio enables communication from the app."
        ),
        "features": (
            "360° pan, 114° tilt, 1080p, person detection, night vision 9m, "
            "two-way audio, SD card local storage, cloud optional, Alexa/Google, Wi-Fi"
        ),
        "image":    "https://images.unsplash.com/photo-1590874103328-eac38a683ce7?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0103",
        "title":        "Philips Hue Lightstrip Plus 2m Base Kit",
        "brand":        "Philips",
        "price":        79.99,
        "category_l1":  "Electronics",
        "category_l2":  "Smart Home & IoT",
        "category_l3":  "Smart Lighting",
        "avg_rating":   4.4,
        "rating_count": 5600,
        "description":  (
            "Hue Lightstrip Plus delivers 1600 lumens across an 80 CRI spectrum "
            "with each metre of strip individually addressable, enabling gradient "
            "lighting effects that transition smoothly through different colours "
            "along the length. Extension strips in 1m increments attach without tools."
        ),
        "features": (
            "16M colours, 1600 lumens, individually addressable segments, "
            "Hue bridge required, extensible to 10m, adhesive backing, cuts to fit, 2m base"
        ),
        "image":    "https://images.unsplash.com/photo-1550009158-9ebf69173e03?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0104",
        "title":        "Amazon Smart Air Quality Monitor",
        "brand":        "Amazon",
        "price":        69.99,
        "category_l1":  "Electronics",
        "category_l2":  "Smart Home & IoT",
        "category_l3":  "Smart Plugs",
        "avg_rating":   4.1,
        "rating_count": 3200,
        "description":  (
            "Amazon's air quality monitor tracks particulates (PM2.5), humidity, "
            "temperature, carbon monoxide, and total volatile organic compounds "
            "simultaneously, displaying all readings on its LED ring and in the "
            "Alexa app. Alexa routines can trigger a smart plug air purifier automatically."
        ),
        "features": (
            "PM2.5, CO, humidity, temperature, TVOC sensors, LED ring display, "
            "Alexa integration, smart home automation, historical trends, Wi-Fi"
        ),
        "image":    "https://images.unsplash.com/photo-1585771724684-38269d6639fd?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0105",
        "title":        "TP-Link Kasa Smart Light Bulb Multicolour A19",
        "brand":        "TP-Link",
        "price":        13.99,
        "category_l1":  "Electronics",
        "category_l2":  "Smart Home & IoT",
        "category_l3":  "Smart Lighting",
        "avg_rating":   4.4,
        "rating_count": 7800,
        "description":  (
            "Kasa Smart A19 offers 16 million colours and 2500–6500 K tunable "
            "white light in an E26 base compatible with any standard lamp. "
            "No hub is required — the bulb connects directly to your 2.4 GHz "
            "Wi-Fi and is controllable via the Kasa app, Alexa, or Google Home."
        ),
        "features": (
            "16M colours, 2500-6500K tunable white, E26 base, no hub required, "
            "800 lumens, Wi-Fi, Alexa/Google/SmartThings, schedule, away mode"
        ),
        "image":    "https://images.unsplash.com/photo-1565849904461-04a58ad377e0?w=500&h=500&fit=crop",
    },

    # =========================================================================
    # GAMING  (15 products, P0106–P0120)
    # =========================================================================

    {
        "product_id":   "P0106",
        "title":        "SteelSeries Arctis Nova Pro Wireless Gaming Headset",
        "brand":        "SteelSeries",
        "price":        349.99,
        "category_l1":  "Electronics",
        "category_l2":  "Gaming",
        "category_l3":  "Gaming Headsets",
        "avg_rating":   4.7,
        "rating_count": 4200,
        "description":  (
            "Arctis Nova Pro Wireless features a dual-battery hot-swap system "
            "so you never have to stop playing to recharge — a fully charged spare "
            "lives in the base station. Active Noise Cancellation and Transparency "
            "mode are tuned specifically for gaming, reducing engine sounds and "
            "notifying you of teammate audio in game chat."
        ),
        "features": (
            "dual hot-swap battery, ANC, transparency mode, 40 mm Nova drivers, "
            "lossless 2.4 GHz + Bluetooth, 22-hour battery, parametric EQ, base station"
        ),
        "image":    "https://images.unsplash.com/photo-1599669454699-248893623440?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0107",
        "title":        "HyperX Cloud Alpha Wireless Gaming Headset",
        "brand":        "HyperX",
        "price":        199.99,
        "category_l1":  "Electronics",
        "category_l2":  "Gaming",
        "category_l3":  "Gaming Headsets",
        "avg_rating":   4.6,
        "rating_count": 6800,
        "description":  (
            "Cloud Alpha Wireless achieves up to 300 hours of battery life — an "
            "extraordinary duration enabled by DTS Headphone:X and the dual-chamber "
            "driver design that separates bass and mid-high frequencies. The "
            "aluminium frame with leatherette earpads delivers comfort for marathon gaming sessions."
        ),
        "features": (
            "300-hour battery, dual-chamber drivers, DTS Headphone:X, "
            "2.4 GHz wireless, noise-cancelling detachable mic, aluminium frame, USB-A"
        ),
        "image":    "https://images.unsplash.com/photo-1618366712010-f4ae9c647dcb?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0108",
        "title":        "Razer BlackShark V2 HyperSpeed Gaming Headset",
        "brand":        "Razer",
        "price":        129.99,
        "category_l1":  "Electronics",
        "category_l2":  "Gaming",
        "category_l3":  "Gaming Headsets",
        "avg_rating":   4.5,
        "rating_count": 5100,
        "description":  (
            "BlackShark V2 HyperSpeed supports simultaneous 2.4 GHz and Bluetooth "
            "connections, enabling PC game audio on the wireless channel while "
            "taking phone calls on Bluetooth without pausing the session. "
            "Razer's TriForce Titanium drivers independently tune bass, mid, and treble frequencies."
        ),
        "features": (
            "2.4 GHz + Bluetooth simultaneous, TriForce Titanium drivers, "
            "detachable mic, Razer Synapse EQ, 70-hour battery, USB-C, PC/PS5/Switch"
        ),
        "image":    "https://images.unsplash.com/photo-1583394838336-acd977736f90?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0109",
        "title":        "Logitech G Pro X Superlight 2 Gaming Mouse",
        "brand":        "Logitech",
        "price":        159.99,
        "category_l1":  "Electronics",
        "category_l2":  "Gaming",
        "category_l3":  "Gaming Mice",
        "avg_rating":   4.7,
        "rating_count": 7300,
        "description":  (
            "At only 60 g, Superlight 2 is among the lightest high-performance "
            "wireless gaming mice ever made. The HERO 2 sensor delivers 32,000 DPI "
            "with 500+ IPS tracking accuracy and zero smoothing, acceleration, "
            "or filtering — what the sensor sees is what moves on screen."
        ),
        "features": (
            "60g weight, HERO 2 sensor 32K DPI, LIGHTSPEED 2.4 GHz, "
            "95-hour battery, PTFE feet, USB-C, 5 buttons, LightSync RGB, zero smoothing"
        ),
        "image":    "https://images.unsplash.com/photo-1615663245857-ac93bb7c39e7?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0110",
        "title":        "Razer DeathAdder V3 HyperSpeed Wireless Gaming Mouse",
        "brand":        "Razer",
        "price":        109.99,
        "category_l1":  "Electronics",
        "category_l2":  "Gaming",
        "category_l3":  "Gaming Mice",
        "avg_rating":   4.6,
        "rating_count": 5400,
        "description":  (
            "DeathAdder V3 HyperSpeed refines the iconic ergonomic shape for right-handed "
            "users with a lighter 81 g construction and an asymmetric form factor "
            "validated by professional esports players. The Focus X sensor achieves "
            "26,000 DPI with 500 IPS tracking speed in a no-frills, performance-focused package."
        ),
        "features": (
            "81g, Focus X 26K DPI sensor, Razer HyperSpeed 2.4 GHz, "
            "280-hour battery, Speedflex cable option, USB-C, Bluetooth, right-handed"
        ),
        "image":    "https://images.unsplash.com/photo-1629131726692-1accd0c53ce0?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0111",
        "title":        "SteelSeries Aerox 5 Wireless Gaming Mouse",
        "brand":        "SteelSeries",
        "price":        139.99,
        "category_l1":  "Electronics",
        "category_l2":  "Gaming",
        "category_l3":  "Gaming Mice",
        "avg_rating":   4.5,
        "rating_count": 3200,
        "description":  (
            "Aerox 5 Wireless features a honeycomb shell that brings the weight "
            "to just 74 g while an IP54 splashproof rating protects against desk "
            "drink spills — practical for the real gaming environment. The TrueMove "
            "Air sensor with quantum optical technology eliminates click latency entirely."
        ),
        "features": (
            "74g honeycomb, IP54 splashproof, TrueMove Air 18K DPI, "
            "2.4 GHz + Bluetooth, 80-hour battery, 9 programmable buttons, USB-C"
        ),
        "image":    "https://images.unsplash.com/photo-1527814050087-3793815479db?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0112",
        "title":        "Razer BlackWidow V4 Pro Wireless Mechanical Keyboard",
        "brand":        "Razer",
        "price":        249.99,
        "category_l1":  "Electronics",
        "category_l2":  "Gaming",
        "category_l3":  "Gaming Keyboards",
        "avg_rating":   4.6,
        "rating_count": 3800,
        "description":  (
            "BlackWidow V4 Pro uses Razer's HyperPolling Wireless Dongle to "
            "achieve 4000 Hz wireless polling, meaning the keyboard reports its "
            "state to the PC every 0.25 ms for lower input latency than most "
            "wired keyboards. The media dial, dedicated macro keys, and per-key RGB "
            "Chroma complete the professional setup."
        ),
        "features": (
            "4000 Hz wireless polling, Razer Yellow switches, per-key RGB Chroma, "
            "media dial, macro keys, USB passthrough, aluminium top plate, 2.4 GHz + BT"
        ),
        "image":    "https://images.unsplash.com/photo-1595225476474-87563907a212?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0113",
        "title":        "SteelSeries Apex Pro TKL Wireless Gaming Keyboard",
        "brand":        "SteelSeries",
        "price":        219.99,
        "category_l1":  "Electronics",
        "category_l2":  "Gaming",
        "category_l3":  "Gaming Keyboards",
        "avg_rating":   4.5,
        "rating_count": 4100,
        "description":  (
            "Apex Pro TKL Wireless features OmniPoint 2.0 adjustable magnetic "
            "switches with actuation point adjustable from 0.2 to 3.8 mm per key. "
            "This allows competitive FPS players to set triggers at 0.2 mm for "
            "maximum responsiveness while keeping movement keys at 1.5 mm to "
            "prevent accidental activation."
        ),
        "features": (
            "OmniPoint 2.0 adjustable switches, 0.2–3.8mm actuation, "
            "TKL layout, 2.4 GHz + Bluetooth, per-key RGB, OLED smartdisplay, USB-C, 36h battery"
        ),
        "image":    "https://images.unsplash.com/photo-1618384887929-16ec33fab9ef?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0114",
        "title":        "HyperX Alloy Origins 65 Mechanical Gaming Keyboard",
        "brand":        "HyperX",
        "price":        89.99,
        "category_l1":  "Electronics",
        "category_l2":  "Gaming",
        "category_l3":  "Gaming Keyboards",
        "avg_rating":   4.5,
        "rating_count": 5700,
        "description":  (
            "Origins 65 packs a 65% layout with dedicated arrow keys and a page "
            "cluster into a compact aircraft-grade aluminium chassis. HyperX "
            "Red linear switches deliver 45 g actuation with 1.8 mm pre-travel "
            "for a fast, smooth keystroke popular in competitive gaming."
        ),
        "features": (
            "65% layout, HyperX Red linear, aluminium body, per-key RGB, "
            "detachable USB-C, HyperX NGENUITY software, N-key rollover, 3 switch options"
        ),
        "image":    "https://images.unsplash.com/photo-1541140532154-b024d705b90a?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0115",
        "title":        "ASUS ROG Swift PG279QM 27-inch QHD 240Hz Gaming Monitor",
        "brand":        "ASUS",
        "price":        799.99,
        "category_l1":  "Electronics",
        "category_l2":  "Gaming",
        "category_l3":  "Gaming Monitors",
        "avg_rating":   4.7,
        "rating_count": 3600,
        "description":  (
            "PG279QM is certified for NVIDIA G-Sync Ultimate with hardware HDR "
            "capable of 384 local dimming zones, achieving 1000 nits peak brightness "
            "for HDR content. The 27-inch IPS panel runs at 240 Hz with 1 ms GtG "
            "response, combining competitive speed with professional colour accuracy."
        ),
        "features": (
            "27-inch 1440p IPS, 240 Hz, 1ms GtG, G-Sync Ultimate, 384 zones HDR1000, "
            "HDMI 2.0, DisplayPort 1.4, USB hub, ASUS Aura RGB, ELMB-Sync, VESA"
        ),
        "image":    "https://images.unsplash.com/photo-1593305841991-05c297ba4575?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0116",
        "title":        "LG 27GR83Q-B 27-inch 1440p 240Hz IPS Gaming Monitor",
        "brand":        "LG",
        "price":        499.99,
        "category_l1":  "Electronics",
        "category_l2":  "Gaming",
        "category_l3":  "Gaming Monitors",
        "avg_rating":   4.6,
        "rating_count": 4800,
        "description":  (
            "LG's 27GR83Q pairs an IPS panel with a 240 Hz refresh rate and "
            "1 ms GtG response for competitive gaming without the colour compromises "
            "of TN alternatives. The Nano IPS technology achieves 98% DCI-P3 so "
            "the same monitor serves dual-purpose content creation and gaming."
        ),
        "features": (
            "27-inch 1440p Nano IPS, 240 Hz, 1ms GtG, 98% DCI-P3, "
            "G-Sync compatible, FreeSync Premium, HDMI 2.0 ×2, DisplayPort 1.4, USB hub"
        ),
        "image":    "https://images.unsplash.com/photo-1616711906333-23cf6b04d35b?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0117",
        "title":        "Sony DualSense Edge Wireless Controller for PS5",
        "brand":        "Sony",
        "price":        199.99,
        "category_l1":  "Electronics",
        "category_l2":  "Gaming",
        "category_l3":  "Controllers",
        "avg_rating":   4.5,
        "rating_count": 5200,
        "description":  (
            "DualSense Edge is Sony's professional-grade PS5 controller with swappable "
            "stick caps in three heights and back button paddles that attach without "
            "tools. Adaptive trigger dead-zone adjustment lets competitive players "
            "set hair-trigger sensitivity on L2 and R2 for faster response in "
            "first-person shooters."
        ),
        "features": (
            "swappable stick caps, back paddles, adaptive trigger adjustment, "
            "haptic feedback, built-in mic, USB-C cable included, BT 5.1, profile saving"
        ),
        "image":    "https://images.unsplash.com/photo-1592840496694-26d035b52b48?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0118",
        "title":        "Xbox Elite Wireless Controller Series 2",
        "brand":        "Microsoft",
        "price":        179.99,
        "category_l1":  "Electronics",
        "category_l2":  "Gaming",
        "category_l3":  "Controllers",
        "avg_rating":   4.4,
        "rating_count": 7900,
        "description":  (
            "Elite Series 2 includes four interchangeable paddles, three tension "
            "levels for both thumb sticks, adjustable hair trigger locks, and "
            "a charging dock with 40-hour battery life built in. Xbox Accessories "
            "app stores three custom profiles directly on the controller."
        ),
        "features": (
            "4 interchangeable paddles, 3 thumbstick tensions, hair trigger locks, "
            "40-hour battery, USB-C, Bluetooth + USB, 3 on-board profiles, charging dock"
        ),
        "image":    "https://images.unsplash.com/photo-1600080972464-8e5f35f63d08?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0119",
        "title":        "Razer Wolverine V2 Chroma Wired Controller Xbox",
        "brand":        "Razer",
        "price":        149.99,
        "category_l1":  "Electronics",
        "category_l2":  "Gaming",
        "category_l3":  "Controllers",
        "avg_rating":   4.3,
        "rating_count": 3400,
        "description":  (
            "Wolverine V2 Chroma features Razer's Mecha-Tactile action buttons "
            "with a 0.65 mm actuation distance for faster response than standard "
            "controller buttons. Four multi-function buttons are programmable "
            "through Razer's mobile app, and per-key Chroma RGB illuminates "
            "the face buttons independently."
        ),
        "features": (
            "Mecha-Tactile face buttons, 4 multi-function buttons, per-key Chroma RGB, "
            "hair trigger mode, 3.5 mm audio jack, USB-C wired, Xbox + PC, rubberised grip"
        ),
        "image":    "https://images.unsplash.com/photo-1605901309584-818e25960a8f?w=500&h=500&fit=crop",
    },
    {
        "product_id":   "P0120",
        "title":        "SteelSeries Apex 9 Mini Gaming Keyboard 60%",
        "brand":        "SteelSeries",
        "price":        59.99,
        "category_l1":  "Electronics",
        "category_l2":  "Gaming",
        "category_l3":  "Gaming Keyboards",
        "avg_rating":   4.4,
        "rating_count": 4400,
        "description":  (
            "Apex 9 Mini uses OptiPoint optical switches with an actuation distance "
            "adjustable between 1.0 mm and 2.0 mm via the SteelSeries GG software. "
            "The 60% layout eliminates the numpad and F-row to maximise desk space "
            "for aggressive low-DPI mouse movements popular in FPS gaming."
        ),
        "features": (
            "60% layout, OptiPoint optical switches, adjustable 1.0-2.0mm actuation, "
            "per-key RGB, USB-C, aircraft-grade aluminium, n-key rollover, SteelSeries GG"
        ),
        "image":    "https://images.unsplash.com/photo-1595225476474-87563907a212?w=500&h=500&fit=crop",
    },
]

# ---------------------------------------------------------------------------
# Derived lookups — O(1) access for DataLoader and recommenders
# ---------------------------------------------------------------------------

PRODUCT_BY_ID: dict[str, dict] = {p["product_id"]: p for p in PRODUCTS}

ALL_PRODUCT_IDS: list[str] = [p["product_id"] for p in PRODUCTS]

ALL_BRANDS: list[str] = sorted({p["brand"] for p in PRODUCTS})
ALL_CATEGORY_L1: list[str] = sorted({p["category_l1"] for p in PRODUCTS})
ALL_CATEGORY_L2: list[str] = sorted({p["category_l2"] for p in PRODUCTS})
ALL_CATEGORY_L3: list[str] = sorted({p["category_l3"] for p in PRODUCTS})

# ---------------------------------------------------------------------------
# Quick sanity check at import time
# ---------------------------------------------------------------------------
assert len(PRODUCTS) == 120, f"Expected 120 products, got {len(PRODUCTS)}"
assert len(PRODUCT_BY_ID) == 120, "Duplicate product_ids detected"