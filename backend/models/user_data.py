"""
backend/models/user_data.py

40 realistic users across 8 distinct personas with interaction histories that
produce meaningfully different recommendation results across all 4 methods.

Persona distribution (5 users each):
  1 — Audiophile              U001–U005
  2 — Mobile Power User       U006–U010
  3 — Professional Photographer U011–U015
  4 — Home Gamer              U016–U020
  5 — Smart Home Enthusiast   U021–U025
  6 — Budget Shopper          U026–U030
  7 — Tech Professional       U031–U035
  8 — Casual Consumer         U036–U040
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Users
# ---------------------------------------------------------------------------

USERS: list[dict] = [

    # =========================================================================
    # PERSONA 1 — AUDIOPHILE (U001–U005)
    # Loves Headphones & Audio (4–5 ★), respects Gaming Headsets (3–4 ★),
    # occasionally buys Smartphones and regrets it (2–3 ★)
    # =========================================================================

    {
        "user_id": "U001",
        "name": "Marcus Chen",
        "interactions": [
            {"product_id": "P0001", "rating": 5.0, "timestamp": 1700000000},  # Sony WH-1000XM5
            {"product_id": "P0003", "rating": 5.0, "timestamp": 1700100000},  # Sennheiser HD 660S2
            {"product_id": "P0005", "rating": 4.0, "timestamp": 1700200000},  # Sony MDR-7506
            {"product_id": "P0009", "rating": 5.0, "timestamp": 1700300000},  # Sennheiser IE 300
            {"product_id": "P0013", "rating": 4.0, "timestamp": 1700400000},  # Bose QC Earbuds II
            {"product_id": "P0020", "rating": 5.0, "timestamp": 1700500000},  # Sennheiser MTW3
            {"product_id": "P0002", "rating": 4.0, "timestamp": 1700600000},  # Bose QC45
            {"product_id": "P0106", "rating": 3.0, "timestamp": 1700700000},  # SteelSeries Arctis Nova Pro
            {"product_id": "P0107", "rating": 3.0, "timestamp": 1700800000},  # HyperX Cloud Alpha
            {"product_id": "P0034", "rating": 2.0, "timestamp": 1700900000},  # Samsung Galaxy A54
            {"product_id": "P0006", "rating": 4.0, "timestamp": 1701000000},  # Sennheiser HD 560S
        ],
    },
    {
        "user_id": "U002",
        "name": "Priya Nair",
        "interactions": [
            {"product_id": "P0001", "rating": 5.0, "timestamp": 1698000000},  # Sony WH-1000XM5
            {"product_id": "P0002", "rating": 5.0, "timestamp": 1698100000},  # Bose QC45
            {"product_id": "P0014", "rating": 5.0, "timestamp": 1698200000},  # Sony WF-1000XM5
            {"product_id": "P0015", "rating": 4.0, "timestamp": 1698300000},  # AirPods Pro 2
            {"product_id": "P0008", "rating": 4.0, "timestamp": 1698400000},  # Philips Fidelio X3
            {"product_id": "P0026", "rating": 4.0, "timestamp": 1698500000},  # JBL Charge 5
            {"product_id": "P0027", "rating": 5.0, "timestamp": 1698600000},  # Bose SoundLink Flex
            {"product_id": "P0108", "rating": 3.0, "timestamp": 1698700000},  # Razer BlackShark V2
            {"product_id": "P0038", "rating": 2.0, "timestamp": 1698800000},  # iPhone SE 3rd Gen
            {"product_id": "P0010", "rating": 4.0, "timestamp": 1698900000},  # Sony IER-M9
        ],
    },
    {
        "user_id": "U003",
        "name": "Darius Okafor",
        "interactions": [
            {"product_id": "P0003", "rating": 5.0, "timestamp": 1695000000},  # Sennheiser HD 660S2
            {"product_id": "P0009", "rating": 5.0, "timestamp": 1695100000},  # Sennheiser IE 300
            {"product_id": "P0006", "rating": 5.0, "timestamp": 1695200000},  # Sennheiser HD 560S
            {"product_id": "P0010", "rating": 5.0, "timestamp": 1695300000},  # Sony IER-M9
            {"product_id": "P0005", "rating": 4.0, "timestamp": 1695400000},  # Sony MDR-7506
            {"product_id": "P0007", "rating": 4.0, "timestamp": 1695500000},  # Bose 700
            {"product_id": "P0021", "rating": 4.0, "timestamp": 1695600000},  # Sony HT-A7000
            {"product_id": "P0029", "rating": 4.0, "timestamp": 1695700000},  # Anker Motion X600
            {"product_id": "P0107", "rating": 3.0, "timestamp": 1695800000},  # HyperX Cloud Alpha
            {"product_id": "P0031", "rating": 2.0, "timestamp": 1695900000},  # iPhone 15 Pro Max
            {"product_id": "P0011", "rating": 3.0, "timestamp": 1696000000},  # Anker P20i
            {"product_id": "P0013", "rating": 4.0, "timestamp": 1696100000},  # Bose QC Earbuds II
        ],
    },
    {
        "user_id": "U004",
        "name": "Hana Kimura",
        "interactions": [
            {"product_id": "P0004", "rating": 5.0, "timestamp": 1692000000},  # AirPods Max
            {"product_id": "P0015", "rating": 5.0, "timestamp": 1692100000},  # AirPods Pro 2
            {"product_id": "P0001", "rating": 5.0, "timestamp": 1692200000},  # Sony WH-1000XM5
            {"product_id": "P0013", "rating": 5.0, "timestamp": 1692300000},  # Bose QC Earbuds II
            {"product_id": "P0022", "rating": 4.0, "timestamp": 1692400000},  # Samsung HW-Q990C
            {"product_id": "P0023", "rating": 4.0, "timestamp": 1692500000},  # Bose Soundbar 600
            {"product_id": "P0028", "rating": 4.0, "timestamp": 1692600000},  # Sony SRS-XB43
            {"product_id": "P0106", "rating": 3.0, "timestamp": 1692700000},  # Arctis Nova Pro
            {"product_id": "P0035", "rating": 3.0, "timestamp": 1692800000},  # iPhone 15
        ],
    },
    {
        "user_id": "U005",
        "name": "Tobias Brandt",
        "interactions": [
            {"product_id": "P0007", "rating": 5.0, "timestamp": 1689000000},  # Bose 700
            {"product_id": "P0002", "rating": 5.0, "timestamp": 1689100000},  # Bose QC45
            {"product_id": "P0023", "rating": 5.0, "timestamp": 1689200000},  # Bose Soundbar 600
            {"product_id": "P0027", "rating": 5.0, "timestamp": 1689300000},  # Bose SoundLink Flex
            {"product_id": "P0013", "rating": 5.0, "timestamp": 1689400000},  # Bose QC Earbuds II
            {"product_id": "P0021", "rating": 4.0, "timestamp": 1689500000},  # Sony HT-A7000
            {"product_id": "P0014", "rating": 4.0, "timestamp": 1689600000},  # Sony WF-1000XM5
            {"product_id": "P0026", "rating": 4.0, "timestamp": 1689700000},  # JBL Charge 5
            {"product_id": "P0108", "rating": 3.0, "timestamp": 1689800000},  # Razer BlackShark V2
            {"product_id": "P0034", "rating": 2.0, "timestamp": 1689900000},  # Galaxy A54
            {"product_id": "P0012", "rating": 3.0, "timestamp": 1690000000},  # JBL Tune 230NC
        ],
    },

    # =========================================================================
    # PERSONA 2 — MOBILE POWER USER (U006–U010)
    # Loves Smartphones & Accessories (4–5 ★), tolerates Laptops/Smart Home (3 ★)
    # =========================================================================

    {
        "user_id": "U006",
        "name": "Aaliyah Torres",
        "interactions": [
            {"product_id": "P0031", "rating": 5.0, "timestamp": 1700000000},  # iPhone 15 Pro Max
            {"product_id": "P0032", "rating": 5.0, "timestamp": 1700100000},  # Galaxy S24 Ultra
            {"product_id": "P0043", "rating": 5.0, "timestamp": 1700200000},  # Anker 737 GaN 120W
            {"product_id": "P0052", "rating": 5.0, "timestamp": 1700300000},  # Anker PowerCore 26K
            {"product_id": "P0035", "rating": 4.0, "timestamp": 1700400000},  # iPhone 15
            {"product_id": "P0046", "rating": 4.0, "timestamp": 1700500000},  # Belkin 3-in-1 MagSafe
            {"product_id": "P0054", "rating": 4.0, "timestamp": 1700600000},  # Anker Nano 10K
            {"product_id": "P0048", "rating": 4.0, "timestamp": 1700700000},  # Belkin UltraGlass 2
            {"product_id": "P0062", "rating": 3.0, "timestamp": 1700800000},  # MacBook Air M2
            {"product_id": "P0093", "rating": 3.0, "timestamp": 1700900000},  # Echo 4th Gen
            {"product_id": "P0039", "rating": 5.0, "timestamp": 1701000000},  # Apple MagSafe Case
        ],
    },
    {
        "user_id": "U007",
        "name": "Leon Fischer",
        "interactions": [
            {"product_id": "P0032", "rating": 5.0, "timestamp": 1697000000},  # Galaxy S24 Ultra
            {"product_id": "P0047", "rating": 5.0, "timestamp": 1697100000},  # Samsung 45W charger
            {"product_id": "P0055", "rating": 5.0, "timestamp": 1697200000},  # Samsung 10K powerbank
            {"product_id": "P0037", "rating": 4.0, "timestamp": 1697300000},  # Galaxy Z Flip5
            {"product_id": "P0040", "rating": 4.0, "timestamp": 1697400000},  # Anker 360 case S24
            {"product_id": "P0042", "rating": 4.0, "timestamp": 1697500000},  # Galaxy S24 Ultra case
            {"product_id": "P0049", "rating": 4.0, "timestamp": 1697600000},  # Galaxy S24 screen
            {"product_id": "P0034", "rating": 5.0, "timestamp": 1697700000},  # Galaxy A54
            {"product_id": "P0056", "rating": 3.0, "timestamp": 1697800000},  # MacBook Pro M3
            {"product_id": "P0097", "rating": 3.0, "timestamp": 1697900000},  # TP-Link Smart Plug
        ],
    },
    {
        "user_id": "U008",
        "name": "Simone Dupont",
        "interactions": [
            {"product_id": "P0033", "rating": 5.0, "timestamp": 1694000000},  # Pixel 8 Pro
            {"product_id": "P0036", "rating": 5.0, "timestamp": 1694100000},  # Pixel 7a
            {"product_id": "P0019", "rating": 4.0, "timestamp": 1694200000},  # Pixel Buds Pro
            {"product_id": "P0043", "rating": 5.0, "timestamp": 1694300000},  # Anker 737 GaN
            {"product_id": "P0045", "rating": 4.0, "timestamp": 1694400000},  # Anker 240W cable
            {"product_id": "P0052", "rating": 4.0, "timestamp": 1694500000},  # Anker 26K powerbank
            {"product_id": "P0050", "rating": 4.0, "timestamp": 1694600000},  # Anker screen protector
            {"product_id": "P0099", "rating": 3.0, "timestamp": 1694700000},  # Nest Cam Outdoor
            {"product_id": "P0092", "rating": 3.0, "timestamp": 1694800000},  # Nest Hub Max
            {"product_id": "P0063", "rating": 3.0, "timestamp": 1694900000},  # Dell Inspiron 15
            {"product_id": "P0054", "rating": 5.0, "timestamp": 1695000000},  # Anker Nano 10K
        ],
    },
    {
        "user_id": "U009",
        "name": "Kwame Asante",
        "interactions": [
            {"product_id": "P0031", "rating": 5.0, "timestamp": 1691000000},  # iPhone 15 Pro Max
            {"product_id": "P0015", "rating": 5.0, "timestamp": 1691100000},  # AirPods Pro 2
            {"product_id": "P0044", "rating": 4.0, "timestamp": 1691200000},  # Apple 20W charger
            {"product_id": "P0046", "rating": 5.0, "timestamp": 1691300000},  # Belkin 3-in-1 MagSafe
            {"product_id": "P0053", "rating": 4.0, "timestamp": 1691400000},  # Belkin MagSafe 10K
            {"product_id": "P0039", "rating": 4.0, "timestamp": 1691500000},  # Apple MagSafe Case
            {"product_id": "P0048", "rating": 4.0, "timestamp": 1691600000},  # Belkin UltraGlass 2
            {"product_id": "P0041", "rating": 4.0, "timestamp": 1691700000},  # Belkin SheerForce
            {"product_id": "P0035", "rating": 4.0, "timestamp": 1691800000},  # iPhone 15
            {"product_id": "P0062", "rating": 3.0, "timestamp": 1691900000},  # MacBook Air M2
            {"product_id": "P0091", "rating": 3.0, "timestamp": 1692000000},  # Echo Show 10
        ],
    },
    {
        "user_id": "U010",
        "name": "Fatima Al-Rashid",
        "interactions": [
            {"product_id": "P0032", "rating": 5.0, "timestamp": 1688000000},  # Galaxy S24 Ultra
            {"product_id": "P0037", "rating": 5.0, "timestamp": 1688100000},  # Galaxy Z Flip5
            {"product_id": "P0034", "rating": 4.0, "timestamp": 1688200000},  # Galaxy A54
            {"product_id": "P0047", "rating": 5.0, "timestamp": 1688300000},  # Samsung 45W
            {"product_id": "P0042", "rating": 4.0, "timestamp": 1688400000},  # Galaxy S24 case
            {"product_id": "P0055", "rating": 4.0, "timestamp": 1688500000},  # Samsung 10K
            {"product_id": "P0049", "rating": 4.0, "timestamp": 1688600000},  # Galaxy privacy screen
            {"product_id": "P0016", "rating": 4.0, "timestamp": 1688700000},  # Galaxy Buds2 Pro
            {"product_id": "P0058", "rating": 3.0, "timestamp": 1688800000},  # ThinkPad X1 Carbon
            {"product_id": "P0093", "rating": 3.0, "timestamp": 1688900000},  # Echo 4th Gen
        ],
    },

    # =========================================================================
    # PERSONA 3 — PROFESSIONAL PHOTOGRAPHER (U011–U015)
    # Loves Cameras & Photography (4–5 ★), values Laptops for editing (4 ★)
    # =========================================================================

    {
        "user_id": "U011",
        "name": "Cormac Sullivan",
        "interactions": [
            {"product_id": "P0076", "rating": 5.0, "timestamp": 1700000000},  # Canon R6 Mark II
            {"product_id": "P0083", "rating": 5.0, "timestamp": 1700100000},  # Canon RF 50mm
            {"product_id": "P0088", "rating": 5.0, "timestamp": 1700200000},  # Peak Design Tripod
            {"product_id": "P0056", "rating": 4.0, "timestamp": 1700300000},  # MacBook Pro M3
            {"product_id": "P0077", "rating": 5.0, "timestamp": 1700400000},  # Sony A7 IV
            {"product_id": "P0084", "rating": 4.0, "timestamp": 1700500000},  # Sony 24-70 GM II
            {"product_id": "P0086", "rating": 4.0, "timestamp": 1700600000},  # Joby GorillaPod
            {"product_id": "P0065", "rating": 4.0, "timestamp": 1700700000},  # Dell UltraSharp U2723DE
            {"product_id": "P0079", "rating": 4.0, "timestamp": 1700800000},  # Canon 90D
            {"product_id": "P0087", "rating": 4.0, "timestamp": 1700900000},  # Manfrotto MT190XPRO4
        ],
    },
    {
        "user_id": "U012",
        "name": "Anastasia Volkov",
        "interactions": [
            {"product_id": "P0077", "rating": 5.0, "timestamp": 1697000000},  # Sony A7 IV
            {"product_id": "P0084", "rating": 5.0, "timestamp": 1697100000},  # Sony 24-70 GM II
            {"product_id": "P0085", "rating": 5.0, "timestamp": 1697200000},  # Nikon 85mm f/1.8
            {"product_id": "P0088", "rating": 5.0, "timestamp": 1697300000},  # Peak Design Tripod
            {"product_id": "P0057", "rating": 4.0, "timestamp": 1697400000},  # Dell XPS 15
            {"product_id": "P0078", "rating": 4.0, "timestamp": 1697500000},  # Nikon Z6 III
            {"product_id": "P0087", "rating": 4.0, "timestamp": 1697600000},  # Manfrotto Tripod
            {"product_id": "P0064", "rating": 4.0, "timestamp": 1697700000},  # LG 4K 160Hz monitor
            {"product_id": "P0081", "rating": 3.0, "timestamp": 1697800000},  # GoPro HERO12
            {"product_id": "P0073", "rating": 3.0, "timestamp": 1697900000},  # Logitech Brio 4K
        ],
    },
    {
        "user_id": "U013",
        "name": "Rafael Mendez",
        "interactions": [
            {"product_id": "P0079", "rating": 5.0, "timestamp": 1694000000},  # Canon 90D
            {"product_id": "P0083", "rating": 5.0, "timestamp": 1694100000},  # Canon RF 50mm
            {"product_id": "P0076", "rating": 5.0, "timestamp": 1694200000},  # Canon R6 II
            {"product_id": "P0086", "rating": 5.0, "timestamp": 1694300000},  # Joby GorillaPod
            {"product_id": "P0056", "rating": 4.0, "timestamp": 1694400000},  # MacBook Pro M3
            {"product_id": "P0087", "rating": 4.0, "timestamp": 1694500000},  # Manfrotto Tripod
            {"product_id": "P0089", "rating": 4.0, "timestamp": 1694600000},  # DJI Mini 4 Pro
            {"product_id": "P0068", "rating": 4.0, "timestamp": 1694700000},  # ASUS ProArt Monitor
            {"product_id": "P0081", "rating": 4.0, "timestamp": 1694800000},  # GoPro HERO12
            {"product_id": "P0070", "rating": 3.0, "timestamp": 1694900000},  # Logitech MX Master 3S
        ],
    },
    {
        "user_id": "U014",
        "name": "Yuki Tanaka",
        "interactions": [
            {"product_id": "P0078", "rating": 5.0, "timestamp": 1691000000},  # Nikon Z6 III
            {"product_id": "P0085", "rating": 5.0, "timestamp": 1691100000},  # Nikon 85mm f/1.8
            {"product_id": "P0080", "rating": 5.0, "timestamp": 1691200000},  # Nikon D7500
            {"product_id": "P0088", "rating": 5.0, "timestamp": 1691300000},  # Peak Design Tripod
            {"product_id": "P0082", "rating": 4.0, "timestamp": 1691400000},  # DJI Osmo Action 4
            {"product_id": "P0058", "rating": 4.0, "timestamp": 1691500000},  # ThinkPad X1 Carbon
            {"product_id": "P0065", "rating": 4.0, "timestamp": 1691600000},  # Dell UltraSharp
            {"product_id": "P0087", "rating": 4.0, "timestamp": 1691700000},  # Manfrotto Tripod
            {"product_id": "P0073", "rating": 4.0, "timestamp": 1691800000},  # Logitech Brio 4K
            {"product_id": "P0005", "rating": 3.0, "timestamp": 1691900000},  # Sony MDR-7506
            {"product_id": "P0069", "rating": 3.0, "timestamp": 1692000000},  # Logitech MX Keys S
        ],
    },
    {
        "user_id": "U015",
        "name": "Ingrid Larsen",
        "interactions": [
            {"product_id": "P0077", "rating": 5.0, "timestamp": 1688000000},  # Sony A7 IV
            {"product_id": "P0084", "rating": 5.0, "timestamp": 1688100000},  # Sony 24-70 GM II
            {"product_id": "P0089", "rating": 5.0, "timestamp": 1688200000},  # DJI Mini 4 Pro
            {"product_id": "P0082", "rating": 5.0, "timestamp": 1688300000},  # DJI Osmo Action 4
            {"product_id": "P0086", "rating": 4.0, "timestamp": 1688400000},  # Joby GorillaPod
            {"product_id": "P0057", "rating": 4.0, "timestamp": 1688500000},  # Dell XPS 15
            {"product_id": "P0064", "rating": 4.0, "timestamp": 1688600000},  # LG 4K Monitor
            {"product_id": "P0090", "rating": 4.0, "timestamp": 1688700000},  # GoPro HERO11 Mini
            {"product_id": "P0073", "rating": 4.0, "timestamp": 1688800000},  # Logitech Brio 4K
            {"product_id": "P0001", "rating": 3.0, "timestamp": 1688900000},  # Sony WH-1000XM5
            {"product_id": "P0069", "rating": 3.0, "timestamp": 1689000000},  # Logitech MX Keys S
        ],
    },

    # =========================================================================
    # PERSONA 4 — HOME GAMER (U016–U020)
    # Loves Gaming peripherals (4–5 ★), Gaming Monitors (4–5 ★),
    # tolerates Laptops (3 ★) and dislikes Smart Home (2–3 ★)
    # =========================================================================

    {
        "user_id": "U016",
        "name": "Tyler Nguyen",
        "interactions": [
            {"product_id": "P0106", "rating": 5.0, "timestamp": 1700000000},  # Arctis Nova Pro
            {"product_id": "P0109", "rating": 5.0, "timestamp": 1700100000},  # Logitech G Pro X
            {"product_id": "P0112", "rating": 5.0, "timestamp": 1700200000},  # Razer BlackWidow V4 Pro
            {"product_id": "P0115", "rating": 5.0, "timestamp": 1700300000},  # ASUS ROG PG279QM
            {"product_id": "P0117", "rating": 4.0, "timestamp": 1700400000},  # DualSense Edge
            {"product_id": "P0110", "rating": 4.0, "timestamp": 1700500000},  # Razer DeathAdder V3
            {"product_id": "P0116", "rating": 4.0, "timestamp": 1700600000},  # LG 27GR83Q
            {"product_id": "P0113", "rating": 4.0, "timestamp": 1700700000},  # Apex Pro TKL
            {"product_id": "P0059", "rating": 3.0, "timestamp": 1700800000},  # ASUS ROG Zephyrus G14
            {"product_id": "P0097", "rating": 2.0, "timestamp": 1700900000},  # TP-Link Smart Plug
        ],
    },
    {
        "user_id": "U017",
        "name": "Zara Ahmed",
        "interactions": [
            {"product_id": "P0107", "rating": 5.0, "timestamp": 1697000000},  # HyperX Cloud Alpha
            {"product_id": "P0114", "rating": 5.0, "timestamp": 1697100000},  # HyperX Alloy Origins 65
            {"product_id": "P0109", "rating": 5.0, "timestamp": 1697200000},  # Logitech G Pro X
            {"product_id": "P0115", "rating": 5.0, "timestamp": 1697300000},  # ASUS ROG Monitor
            {"product_id": "P0111", "rating": 4.0, "timestamp": 1697400000},  # SteelSeries Aerox 5
            {"product_id": "P0118", "rating": 4.0, "timestamp": 1697500000},  # Xbox Elite Series 2
            {"product_id": "P0116", "rating": 4.0, "timestamp": 1697600000},  # LG 240Hz Monitor
            {"product_id": "P0120", "rating": 4.0, "timestamp": 1697700000},  # SteelSeries Apex 9 Mini
            {"product_id": "P0061", "rating": 3.0, "timestamp": 1697800000},  # Lenovo IdeaPad 5
            {"product_id": "P0098", "rating": 2.0, "timestamp": 1697900000},  # Amazon Smart Plug
        ],
    },
    {
        "user_id": "U018",
        "name": "Enzo Rossi",
        "interactions": [
            {"product_id": "P0108", "rating": 5.0, "timestamp": 1694000000},  # Razer BlackShark V2
            {"product_id": "P0110", "rating": 5.0, "timestamp": 1694100000},  # Razer DeathAdder V3
            {"product_id": "P0112", "rating": 5.0, "timestamp": 1694200000},  # Razer BlackWidow V4 Pro
            {"product_id": "P0119", "rating": 4.0, "timestamp": 1694300000},  # Razer Wolverine V2
            {"product_id": "P0115", "rating": 4.0, "timestamp": 1694400000},  # ASUS ROG Monitor
            {"product_id": "P0106", "rating": 4.0, "timestamp": 1694500000},  # Arctis Nova Pro
            {"product_id": "P0116", "rating": 4.0, "timestamp": 1694600000},  # LG Gaming Monitor
            {"product_id": "P0113", "rating": 4.0, "timestamp": 1694700000},  # Apex Pro TKL
            {"product_id": "P0059", "rating": 3.0, "timestamp": 1694800000},  # ROG Zephyrus G14
            {"product_id": "P0091", "rating": 2.0, "timestamp": 1694900000},  # Echo Show 10
            {"product_id": "P0117", "rating": 4.0, "timestamp": 1695000000},  # DualSense Edge
        ],
    },
    {
        "user_id": "U019",
        "name": "Mia Johansson",
        "interactions": [
            {"product_id": "P0109", "rating": 5.0, "timestamp": 1691000000},  # Logitech G Pro X
            {"product_id": "P0113", "rating": 5.0, "timestamp": 1691100000},  # Apex Pro TKL
            {"product_id": "P0106", "rating": 5.0, "timestamp": 1691200000},  # Arctis Nova Pro
            {"product_id": "P0116", "rating": 5.0, "timestamp": 1691300000},  # LG Monitor
            {"product_id": "P0111", "rating": 4.0, "timestamp": 1691400000},  # SteelSeries Aerox 5
            {"product_id": "P0120", "rating": 4.0, "timestamp": 1691500000},  # Apex 9 Mini
            {"product_id": "P0117", "rating": 4.0, "timestamp": 1691600000},  # DualSense Edge
            {"product_id": "P0059", "rating": 3.0, "timestamp": 1691700000},  # ROG Zephyrus G14
            {"product_id": "P0093", "rating": 3.0, "timestamp": 1691800000},  # Echo 4th Gen
            {"product_id": "P0029", "rating": 3.0, "timestamp": 1691900000},  # Anker X600 Speaker
        ],
    },
    {
        "user_id": "U020",
        "name": "Jerome Washington",
        "interactions": [
            {"product_id": "P0115", "rating": 5.0, "timestamp": 1688000000},  # ASUS ROG Monitor
            {"product_id": "P0116", "rating": 5.0, "timestamp": 1688100000},  # LG Gaming Monitor
            {"product_id": "P0112", "rating": 5.0, "timestamp": 1688200000},  # Razer BlackWidow V4
            {"product_id": "P0118", "rating": 5.0, "timestamp": 1688300000},  # Xbox Elite Series 2
            {"product_id": "P0108", "rating": 4.0, "timestamp": 1688400000},  # Razer BlackShark V2
            {"product_id": "P0110", "rating": 4.0, "timestamp": 1688500000},  # Razer DeathAdder V3
            {"product_id": "P0119", "rating": 4.0, "timestamp": 1688600000},  # Razer Wolverine V2
            {"product_id": "P0114", "rating": 4.0, "timestamp": 1688700000},  # HyperX Alloy Origins
            {"product_id": "P0063", "rating": 3.0, "timestamp": 1688800000},  # Dell Inspiron 15
            {"product_id": "P0101", "rating": 2.0, "timestamp": 1688900000},  # Echo Dot
        ],
    },

    # =========================================================================
    # PERSONA 5 — SMART HOME ENTHUSIAST (U021–U025)
    # Loves Smart Home & IoT (4–5 ★), Audio (4 ★), tolerates Smartphones (3–4 ★)
    # =========================================================================

    {
        "user_id": "U021",
        "name": "Claire Moreau",
        "interactions": [
            {"product_id": "P0093", "rating": 5.0, "timestamp": 1700000000},  # Echo 4th Gen
            {"product_id": "P0095", "rating": 5.0, "timestamp": 1700100000},  # Philips Hue Starter
            {"product_id": "P0091", "rating": 5.0, "timestamp": 1700200000},  # Echo Show 10
            {"product_id": "P0097", "rating": 5.0, "timestamp": 1700300000},  # TP-Link EP25 Matter
            {"product_id": "P0099", "rating": 4.0, "timestamp": 1700400000},  # Nest Cam Outdoor
            {"product_id": "P0103", "rating": 4.0, "timestamp": 1700500000},  # Hue Lightstrip Plus
            {"product_id": "P0104", "rating": 4.0, "timestamp": 1700600000},  # Amazon Air Monitor
            {"product_id": "P0026", "rating": 4.0, "timestamp": 1700700000},  # JBL Charge 5
            {"product_id": "P0094", "rating": 5.0, "timestamp": 1700800000},  # Nest Audio
            {"product_id": "P0033", "rating": 4.0, "timestamp": 1700900000},  # Pixel 8 Pro
            {"product_id": "P0105", "rating": 4.0, "timestamp": 1701000000},  # TP-Link Kasa Bulb
        ],
    },
    {
        "user_id": "U022",
        "name": "Sebastien Dupuis",
        "interactions": [
            {"product_id": "P0094", "rating": 5.0, "timestamp": 1697000000},  # Nest Audio
            {"product_id": "P0092", "rating": 5.0, "timestamp": 1697100000},  # Nest Hub Max
            {"product_id": "P0099", "rating": 5.0, "timestamp": 1697200000},  # Nest Cam Outdoor
            {"product_id": "P0095", "rating": 5.0, "timestamp": 1697300000},  # Philips Hue Starter
            {"product_id": "P0096", "rating": 4.0, "timestamp": 1697400000},  # Philips Hue Sync Box
            {"product_id": "P0103", "rating": 4.0, "timestamp": 1697500000},  # Hue Lightstrip
            {"product_id": "P0105", "rating": 4.0, "timestamp": 1697600000},  # TP-Link Kasa Bulb
            {"product_id": "P0027", "rating": 4.0, "timestamp": 1697700000},  # Bose SoundLink Flex
            {"product_id": "P0033", "rating": 3.0, "timestamp": 1697800000},  # Pixel 8 Pro
            {"product_id": "P0098", "rating": 5.0, "timestamp": 1697900000},  # Amazon Smart Plug Mini
        ],
    },
    {
        "user_id": "U023",
        "name": "Natalia Reyes",
        "interactions": [
            {"product_id": "P0101", "rating": 5.0, "timestamp": 1694000000},  # Echo Dot 5th Gen
            {"product_id": "P0097", "rating": 5.0, "timestamp": 1694100000},  # TP-Link EP25
            {"product_id": "P0100", "rating": 5.0, "timestamp": 1694200000},  # Blink Outdoor 4
            {"product_id": "P0102", "rating": 4.0, "timestamp": 1694300000},  # TP-Link C200
            {"product_id": "P0098", "rating": 4.0, "timestamp": 1694400000},  # Amazon Smart Plug
            {"product_id": "P0104", "rating": 4.0, "timestamp": 1694500000},  # Amazon Air Monitor
            {"product_id": "P0095", "rating": 4.0, "timestamp": 1694600000},  # Philips Hue Starter
            {"product_id": "P0093", "rating": 4.0, "timestamp": 1694700000},  # Echo 4th Gen
            {"product_id": "P0036", "rating": 3.0, "timestamp": 1694800000},  # Pixel 7a
            {"product_id": "P0011", "rating": 3.0, "timestamp": 1694900000},  # Anker P20i
        ],
    },
    {
        "user_id": "U024",
        "name": "Ali Hassan",
        "interactions": [
            {"product_id": "P0093", "rating": 5.0, "timestamp": 1691000000},  # Echo 4th Gen
            {"product_id": "P0091", "rating": 5.0, "timestamp": 1691100000},  # Echo Show 10
            {"product_id": "P0100", "rating": 5.0, "timestamp": 1691200000},  # Blink Outdoor 4
            {"product_id": "P0098", "rating": 5.0, "timestamp": 1691300000},  # Amazon Smart Plug
            {"product_id": "P0101", "rating": 5.0, "timestamp": 1691400000},  # Echo Dot
            {"product_id": "P0104", "rating": 4.0, "timestamp": 1691500000},  # Amazon Air Monitor
            {"product_id": "P0096", "rating": 4.0, "timestamp": 1691600000},  # Philips Hue Sync Box
            {"product_id": "P0029", "rating": 4.0, "timestamp": 1691700000},  # Anker Motion X600
            {"product_id": "P0032", "rating": 3.0, "timestamp": 1691800000},  # Galaxy S24 Ultra
            {"product_id": "P0105", "rating": 4.0, "timestamp": 1691900000},  # TP-Link Kasa Bulb
        ],
    },
    {
        "user_id": "U025",
        "name": "Miriam Osei",
        "interactions": [
            {"product_id": "P0095", "rating": 5.0, "timestamp": 1688000000},  # Philips Hue Starter
            {"product_id": "P0096", "rating": 5.0, "timestamp": 1688100000},  # Philips Hue Sync Box
            {"product_id": "P0103", "rating": 5.0, "timestamp": 1688200000},  # Hue Lightstrip Plus
            {"product_id": "P0105", "rating": 5.0, "timestamp": 1688300000},  # TP-Link Kasa Bulb
            {"product_id": "P0102", "rating": 4.0, "timestamp": 1688400000},  # TP-Link C200
            {"product_id": "P0094", "rating": 4.0, "timestamp": 1688500000},  # Nest Audio
            {"product_id": "P0092", "rating": 4.0, "timestamp": 1688600000},  # Nest Hub Max
            {"product_id": "P0026", "rating": 4.0, "timestamp": 1688700000},  # JBL Charge 5
            {"product_id": "P0036", "rating": 4.0, "timestamp": 1688800000},  # Pixel 7a
            {"product_id": "P0097", "rating": 5.0, "timestamp": 1688900000},  # TP-Link EP25
        ],
    },

    # =========================================================================
    # PERSONA 6 — BUDGET SHOPPER (U026–U030)
    # Prefers anything under $100, moderate ratings across categories (3–4 ★)
    # =========================================================================

    {
        "user_id": "U026",
        "name": "Sandra Park",
        "interactions": [
            {"product_id": "P0011", "rating": 4.0, "timestamp": 1700000000},  # Anker P20i ($26)
            {"product_id": "P0044", "rating": 4.0, "timestamp": 1700100000},  # Apple 20W ($19)
            {"product_id": "P0045", "rating": 4.0, "timestamp": 1700200000},  # Anker 240W cable ($16)
            {"product_id": "P0097", "rating": 4.0, "timestamp": 1700300000},  # TP-Link Smart Plug ($16)
            {"product_id": "P0098", "rating": 4.0, "timestamp": 1700400000},  # Amazon Smart Plug ($13)
            {"product_id": "P0101", "rating": 4.0, "timestamp": 1700500000},  # Echo Dot ($60)
            {"product_id": "P0050", "rating": 3.0, "timestamp": 1700600000},  # Anker screen prot ($10)
            {"product_id": "P0051", "rating": 3.0, "timestamp": 1700700000},  # Belkin InvisiGlass ($13)
            {"product_id": "P0105", "rating": 4.0, "timestamp": 1700800000},  # TP-Link Kasa Bulb ($14)
            {"product_id": "P0012", "rating": 3.0, "timestamp": 1700900000},  # JBL Tune 230NC ($80)
            {"product_id": "P0072", "rating": 3.0, "timestamp": 1701000000},  # Dell WM126 ($27)
        ],
    },
    {
        "user_id": "U027",
        "name": "Victor Almeida",
        "interactions": [
            {"product_id": "P0045", "rating": 4.0, "timestamp": 1697000000},  # Anker cable ($16)
            {"product_id": "P0050", "rating": 4.0, "timestamp": 1697100000},  # Anker screen prot ($10)
            {"product_id": "P0072", "rating": 4.0, "timestamp": 1697200000},  # Dell mouse ($27)
            {"product_id": "P0097", "rating": 4.0, "timestamp": 1697300000},  # TP-Link plug ($16)
            {"product_id": "P0054", "rating": 4.0, "timestamp": 1697400000},  # Anker Nano 10K ($36)
            {"product_id": "P0011", "rating": 4.0, "timestamp": 1697500000},  # Anker P20i ($26)
            {"product_id": "P0105", "rating": 3.0, "timestamp": 1697600000},  # TP-Link Kasa Bulb ($14)
            {"product_id": "P0051", "rating": 3.0, "timestamp": 1697700000},  # Belkin InvisiGlass ($13)
            {"product_id": "P0012", "rating": 3.0, "timestamp": 1697800000},  # JBL Tune 230NC ($80)
            {"product_id": "P0098", "rating": 4.0, "timestamp": 1697900000},  # Amazon plug ($13)
        ],
    },
    {
        "user_id": "U028",
        "name": "Olga Petersen",
        "interactions": [
            {"product_id": "P0011", "rating": 4.0, "timestamp": 1694000000},  # Anker P20i ($26)
            {"product_id": "P0072", "rating": 4.0, "timestamp": 1694100000},  # Dell mouse ($27)
            {"product_id": "P0044", "rating": 4.0, "timestamp": 1694200000},  # Apple 20W ($19)
            {"product_id": "P0098", "rating": 4.0, "timestamp": 1694300000},  # Amazon plug ($13)
            {"product_id": "P0097", "rating": 4.0, "timestamp": 1694400000},  # TP-Link plug ($16)
            {"product_id": "P0050", "rating": 3.0, "timestamp": 1694500000},  # Anker screen ($10)
            {"product_id": "P0030", "rating": 3.0, "timestamp": 1694600000},  # JBL Flip 6 ($130)
            {"product_id": "P0054", "rating": 4.0, "timestamp": 1694700000},  # Anker Nano 10K ($36)
            {"product_id": "P0051", "rating": 3.0, "timestamp": 1694800000},  # Belkin InvisiGlass ($13)
            {"product_id": "P0101", "rating": 4.0, "timestamp": 1694900000},  # Echo Dot ($60)
            {"product_id": "P0105", "rating": 3.0, "timestamp": 1695000000},  # TP-Link bulb ($14)
        ],
    },
    {
        "user_id": "U029",
        "name": "Dmitri Kozlov",
        "interactions": [
            {"product_id": "P0045", "rating": 4.0, "timestamp": 1691000000},  # Anker cable ($16)
            {"product_id": "P0044", "rating": 4.0, "timestamp": 1691100000},  # Apple 20W ($19)
            {"product_id": "P0050", "rating": 4.0, "timestamp": 1691200000},  # Anker screen ($10)
            {"product_id": "P0054", "rating": 4.0, "timestamp": 1691300000},  # Anker Nano 10K ($36)
            {"product_id": "P0097", "rating": 4.0, "timestamp": 1691400000},  # TP-Link plug ($16)
            {"product_id": "P0012", "rating": 3.0, "timestamp": 1691500000},  # JBL Tune 230NC ($80)
            {"product_id": "P0018", "rating": 3.0, "timestamp": 1691600000},  # Anker Liberty 4 ($80)
            {"product_id": "P0072", "rating": 3.0, "timestamp": 1691700000},  # Dell mouse ($27)
            {"product_id": "P0098", "rating": 4.0, "timestamp": 1691800000},  # Amazon plug ($13)
            {"product_id": "P0051", "rating": 3.0, "timestamp": 1691900000},  # Belkin InvisiGlass ($13)
        ],
    },
    {
        "user_id": "U030",
        "name": "Amara Diallo",
        "interactions": [
            {"product_id": "P0011", "rating": 4.0, "timestamp": 1688000000},  # Anker P20i ($26)
            {"product_id": "P0054", "rating": 4.0, "timestamp": 1688100000},  # Anker Nano 10K ($36)
            {"product_id": "P0098", "rating": 4.0, "timestamp": 1688200000},  # Amazon plug ($13)
            {"product_id": "P0045", "rating": 4.0, "timestamp": 1688300000},  # Anker cable ($16)
            {"product_id": "P0050", "rating": 4.0, "timestamp": 1688400000},  # Anker screen ($10)
            {"product_id": "P0072", "rating": 3.0, "timestamp": 1688500000},  # Dell mouse ($27)
            {"product_id": "P0030", "rating": 3.0, "timestamp": 1688600000},  # JBL Flip 6 ($130)
            {"product_id": "P0012", "rating": 3.0, "timestamp": 1688700000},  # JBL Tune 230NC ($80)
            {"product_id": "P0063", "rating": 3.0, "timestamp": 1688800000},  # Dell Inspiron ($550)
            {"product_id": "P0105", "rating": 3.0, "timestamp": 1688900000},  # TP-Link bulb ($14)
        ],
    },

    # =========================================================================
    # PERSONA 7 — TECH PROFESSIONAL (U031–U035)
    # Loves Laptops & Computers (4–5 ★), Cameras (4 ★),
    # appreciates Smart Home and Headphones for focus (3–4 ★)
    # =========================================================================

    {
        "user_id": "U031",
        "name": "Yusuf Ibrahim",
        "interactions": [
            {"product_id": "P0056", "rating": 5.0, "timestamp": 1700000000},  # MacBook Pro M3
            {"product_id": "P0062", "rating": 5.0, "timestamp": 1700100000},  # MacBook Air M2
            {"product_id": "P0069", "rating": 5.0, "timestamp": 1700200000},  # Logitech MX Keys S
            {"product_id": "P0070", "rating": 5.0, "timestamp": 1700300000},  # Logitech MX Master 3S
            {"product_id": "P0073", "rating": 4.0, "timestamp": 1700400000},  # Logitech Brio 4K
            {"product_id": "P0065", "rating": 4.0, "timestamp": 1700500000},  # Dell UltraSharp
            {"product_id": "P0001", "rating": 4.0, "timestamp": 1700600000},  # Sony WH-1000XM5
            {"product_id": "P0057", "rating": 4.0, "timestamp": 1700700000},  # Dell XPS 15
            {"product_id": "P0099", "rating": 3.0, "timestamp": 1700800000},  # Nest Cam
            {"product_id": "P0071", "rating": 4.0, "timestamp": 1700900000},  # Apple Magic Keyboard
        ],
    },
    {
        "user_id": "U032",
        "name": "Elena Stavros",
        "interactions": [
            {"product_id": "P0057", "rating": 5.0, "timestamp": 1697000000},  # Dell XPS 15
            {"product_id": "P0058", "rating": 5.0, "timestamp": 1697100000},  # ThinkPad X1 Carbon
            {"product_id": "P0065", "rating": 5.0, "timestamp": 1697200000},  # Dell UltraSharp
            {"product_id": "P0068", "rating": 4.0, "timestamp": 1697300000},  # ASUS ProArt Monitor
            {"product_id": "P0069", "rating": 4.0, "timestamp": 1697400000},  # Logitech MX Keys S
            {"product_id": "P0070", "rating": 5.0, "timestamp": 1697500000},  # Logitech MX Master 3S
            {"product_id": "P0074", "rating": 4.0, "timestamp": 1697600000},  # Anker C300 Webcam
            {"product_id": "P0076", "rating": 4.0, "timestamp": 1697700000},  # Canon R6 II
            {"product_id": "P0001", "rating": 4.0, "timestamp": 1697800000},  # Sony WH-1000XM5
            {"product_id": "P0094", "rating": 3.0, "timestamp": 1697900000},  # Nest Audio
        ],
    },
    {
        "user_id": "U033",
        "name": "Finn Andersen",
        "interactions": [
            {"product_id": "P0059", "rating": 5.0, "timestamp": 1694000000},  # ASUS ROG Zephyrus
            {"product_id": "P0056", "rating": 5.0, "timestamp": 1694100000},  # MacBook Pro M3
            {"product_id": "P0064", "rating": 5.0, "timestamp": 1694200000},  # LG 4K Monitor
            {"product_id": "P0070", "rating": 5.0, "timestamp": 1694300000},  # Logitech MX Master 3S
            {"product_id": "P0073", "rating": 4.0, "timestamp": 1694400000},  # Logitech Brio 4K
            {"product_id": "P0077", "rating": 4.0, "timestamp": 1694500000},  # Sony A7 IV
            {"product_id": "P0069", "rating": 4.0, "timestamp": 1694600000},  # Logitech MX Keys S
            {"product_id": "P0001", "rating": 4.0, "timestamp": 1694700000},  # Sony WH-1000XM5
            {"product_id": "P0092", "rating": 3.0, "timestamp": 1694800000},  # Nest Hub Max
            {"product_id": "P0058", "rating": 4.0, "timestamp": 1694900000},  # ThinkPad X1 Carbon
        ],
    },
    {
        "user_id": "U034",
        "name": "Leila Mansouri",
        "interactions": [
            {"product_id": "P0060", "rating": 5.0, "timestamp": 1691000000},  # HP Spectre x360
            {"product_id": "P0056", "rating": 5.0, "timestamp": 1691100000},  # MacBook Pro M3
            {"product_id": "P0067", "rating": 4.0, "timestamp": 1691200000},  # LG Ultrawide
            {"product_id": "P0068", "rating": 4.0, "timestamp": 1691300000},  # ASUS ProArt
            {"product_id": "P0075", "rating": 4.0, "timestamp": 1691400000},  # Dell 4K Webcam
            {"product_id": "P0069", "rating": 5.0, "timestamp": 1691500000},  # Logitech MX Keys S
            {"product_id": "P0070", "rating": 4.0, "timestamp": 1691600000},  # Logitech MX Master 3S
            {"product_id": "P0079", "rating": 4.0, "timestamp": 1691700000},  # Canon 90D
            {"product_id": "P0097", "rating": 3.0, "timestamp": 1691800000},  # TP-Link plug
            {"product_id": "P0002", "rating": 4.0, "timestamp": 1691900000},  # Bose QC45
        ],
    },
    {
        "user_id": "U035",
        "name": "Aryan Sharma",
        "interactions": [
            {"product_id": "P0058", "rating": 5.0, "timestamp": 1688000000},  # ThinkPad X1 Carbon
            {"product_id": "P0062", "rating": 5.0, "timestamp": 1688100000},  # MacBook Air M2
            {"product_id": "P0069", "rating": 5.0, "timestamp": 1688200000},  # Logitech MX Keys S
            {"product_id": "P0071", "rating": 5.0, "timestamp": 1688300000},  # Apple Magic Keyboard
            {"product_id": "P0065", "rating": 4.0, "timestamp": 1688400000},  # Dell UltraSharp
            {"product_id": "P0074", "rating": 4.0, "timestamp": 1688500000},  # Anker C300 Webcam
            {"product_id": "P0070", "rating": 4.0, "timestamp": 1688600000},  # Logitech MX Master 3S
            {"product_id": "P0099", "rating": 3.0, "timestamp": 1688700000},  # Nest Cam
            {"product_id": "P0014", "rating": 4.0, "timestamp": 1688800000},  # Sony WF-1000XM5
            {"product_id": "P0066", "rating": 4.0, "timestamp": 1688900000},  # Samsung Odyssey G7
        ],
    },

    # =========================================================================
    # PERSONA 8 — CASUAL CONSUMER (U036–U040)
    # No strong category preference, moderate ratings (3–4 ★), diverse purchases
    # =========================================================================

    {
        "user_id": "U036",
        "name": "Brooke Mitchell",
        "interactions": [
            {"product_id": "P0015", "rating": 4.0, "timestamp": 1700000000},  # AirPods Pro 2
            {"product_id": "P0035", "rating": 4.0, "timestamp": 1700100000},  # iPhone 15
            {"product_id": "P0063", "rating": 3.0, "timestamp": 1700200000},  # Dell Inspiron 15
            {"product_id": "P0093", "rating": 3.0, "timestamp": 1700300000},  # Echo 4th Gen
            {"product_id": "P0030", "rating": 4.0, "timestamp": 1700400000},  # JBL Flip 6
            {"product_id": "P0044", "rating": 4.0, "timestamp": 1700500000},  # Apple 20W
            {"product_id": "P0081", "rating": 3.0, "timestamp": 1700600000},  # GoPro HERO12
            {"product_id": "P0097", "rating": 3.0, "timestamp": 1700700000},  # TP-Link plug
            {"product_id": "P0040", "rating": 3.0, "timestamp": 1700800000},  # Anker Galaxy case
        ],
    },
    {
        "user_id": "U037",
        "name": "James O'Brien",
        "interactions": [
            {"product_id": "P0036", "rating": 4.0, "timestamp": 1697000000},  # Pixel 7a
            {"product_id": "P0016", "rating": 4.0, "timestamp": 1697100000},  # Galaxy Buds2 Pro
            {"product_id": "P0061", "rating": 3.0, "timestamp": 1697200000},  # Lenovo IdeaPad 5
            {"product_id": "P0100", "rating": 3.0, "timestamp": 1697300000},  # Blink Outdoor 4
            {"product_id": "P0028", "rating": 4.0, "timestamp": 1697400000},  # Sony SRS-XB43
            {"product_id": "P0054", "rating": 4.0, "timestamp": 1697500000},  # Anker Nano 10K
            {"product_id": "P0082", "rating": 3.0, "timestamp": 1697600000},  # DJI Osmo Action 4
            {"product_id": "P0072", "rating": 3.0, "timestamp": 1697700000},  # Dell WM126 mouse
            {"product_id": "P0046", "rating": 3.0, "timestamp": 1697800000},  # Belkin 3-in-1
        ],
    },
    {
        "user_id": "U038",
        "name": "Ayasha Running Bear",
        "interactions": [
            {"product_id": "P0018", "rating": 4.0, "timestamp": 1694000000},  # Anker Liberty 4 NC
            {"product_id": "P0034", "rating": 4.0, "timestamp": 1694100000},  # Galaxy A54
            {"product_id": "P0062", "rating": 3.0, "timestamp": 1694200000},  # MacBook Air M2
            {"product_id": "P0101", "rating": 3.0, "timestamp": 1694300000},  # Echo Dot
            {"product_id": "P0030", "rating": 4.0, "timestamp": 1694400000},  # JBL Flip 6
            {"product_id": "P0052", "rating": 4.0, "timestamp": 1694500000},  # Anker 26K powerbank
            {"product_id": "P0086", "rating": 3.0, "timestamp": 1694600000},  # Joby GorillaPod
            {"product_id": "P0072", "rating": 3.0, "timestamp": 1694700000},  # Dell WM126
            {"product_id": "P0097", "rating": 3.0, "timestamp": 1694800000},  # TP-Link plug
        ],
    },
    {
        "user_id": "U039",
        "name": "Chidi Okeke",
        "interactions": [
            {"product_id": "P0026", "rating": 4.0, "timestamp": 1691000000},  # JBL Charge 5
            {"product_id": "P0038", "rating": 3.0, "timestamp": 1691100000},  # iPhone SE
            {"product_id": "P0066", "rating": 4.0, "timestamp": 1691200000},  # Samsung Odyssey G7
            {"product_id": "P0099", "rating": 3.0, "timestamp": 1691300000},  # Nest Cam
            {"product_id": "P0011", "rating": 4.0, "timestamp": 1691400000},  # Anker P20i
            {"product_id": "P0074", "rating": 3.0, "timestamp": 1691500000},  # Anker C300 Webcam
            {"product_id": "P0054", "rating": 4.0, "timestamp": 1691600000},  # Anker Nano 10K
            {"product_id": "P0081", "rating": 3.0, "timestamp": 1691700000},  # GoPro HERO12
            {"product_id": "P0043", "rating": 3.0, "timestamp": 1691800000},  # Anker 737 GaN
        ],
    },
    {
        "user_id": "U040",
        "name": "Sophie Bernstein",
        "interactions": [
            {"product_id": "P0017", "rating": 4.0, "timestamp": 1688000000},  # JBL Live Pro 2
            {"product_id": "P0033", "rating": 4.0, "timestamp": 1688100000},  # Pixel 8 Pro
            {"product_id": "P0063", "rating": 3.0, "timestamp": 1688200000},  # Dell Inspiron 15
            {"product_id": "P0102", "rating": 4.0, "timestamp": 1688300000},  # TP-Link C200
            {"product_id": "P0028", "rating": 3.0, "timestamp": 1688400000},  # Sony SRS-XB43
            {"product_id": "P0043", "rating": 4.0, "timestamp": 1688500000},  # Anker 737 GaN
            {"product_id": "P0089", "rating": 3.0, "timestamp": 1688600000},  # DJI Mini 4 Pro
            {"product_id": "P0070", "rating": 3.0, "timestamp": 1688700000},  # Logitech MX Master 3S
            {"product_id": "P0055", "rating": 4.0, "timestamp": 1688800000},  # Samsung 10K
        ],
    },
]

# ---------------------------------------------------------------------------
# Derived lookups — O(1) access for DataLoader
# ---------------------------------------------------------------------------

USER_BY_ID: dict[str, dict] = {u["user_id"]: u for u in USERS}

ALL_INTERACTIONS: list[dict] = [
    {"user_id": u["user_id"], **interaction}
    for u in USERS
    for interaction in u["interactions"]
]

USER_RATINGS: dict[str, dict[str, float]] = {
    u["user_id"]: {i["product_id"]: i["rating"] for i in u["interactions"]}
    for u in USERS
}

USER_PRODUCTS: dict[str, set[str]] = {
    u["user_id"]: {i["product_id"] for i in u["interactions"]}
    for u in USERS
}


# ---------------------------------------------------------------------------
# Data quality validation — called at import time so problems surface immediately
# ---------------------------------------------------------------------------

def validate_user_data() -> None:
    """Validate mock user data integrity. Raises AssertionError on any violation."""
    from backend.models.product_datar import PRODUCT_BY_ID

    for user in USERS:
        seen: set[str] = set()
        positive_count = 0

        for interaction in user["interactions"]:
            pid    = interaction["product_id"]
            rating = interaction["rating"]

            assert pid in PRODUCT_BY_ID, (
                f"User {user['user_id']} references unknown product {pid}"
            )
            assert pid not in seen, (
                f"User {user['user_id']} has duplicate interaction for {pid}"
            )
            assert rating in {1.0, 2.0, 3.0, 4.0, 5.0}, (
                f"Invalid rating {rating} for user {user['user_id']} / product {pid}"
            )
            seen.add(pid)
            if rating >= 3.0:
                positive_count += 1

        assert positive_count >= 5, (
            f"User {user['user_id']} has only {positive_count} positive interactions "
            f"(minimum required: 5)"
        )

    assert len(USERS) == 40, f"Expected 40 users, got {len(USERS)}"
    assert len(USER_BY_ID) == 40, "Duplicate user_ids detected"


validate_user_data()  # run at import — problems surface before any recommender starts