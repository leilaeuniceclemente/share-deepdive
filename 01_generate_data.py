"""
01_generate_data.py
Customer Share Deepdive Console — synthetic data generator
Outputs CSV files consumed by 02_build_tool.py

Run: python 01_generate_data.py
"""

import csv
import os

OUT = "data"
os.makedirs(OUT, exist_ok=True)


# ── 1. SHARE TABLE ────────────────────────────────────────────────────────────
share_table = [
    # label, weight_pct, group_level (0=total, 1=subgroup, 2=row),
    # s1, c1, i1,  s3, c3, i3,  s6, c6, i6,  sy, cy, iy
    ("TOTAL CUSTOMER",              100, 0, 8.4,-0.2,98,  8.6,-0.1,99,  8.5,-0.1,99,  8.4,-0.8,97),
    ("Total (measured categories)",  24, 1, 13.1,-0.2,98, 13.4,-0.8,95, 13.6,-1.1,94, 13.2,-1.4,94),
    ("Cat A",                        11, 2, 11.3, 0.1,101,11.0,-0.8,94, 11.2,-1.5,91, 11.4,-1.4,92),
    ("Cat B",                        13, 2, 14.8, 0.1,101,14.9,-0.5,97, 15.1,-0.4,97, 15.0,-0.6,97),
    ("Total (other categories)",     76, 1,  5.8,-0.1,99,  5.9, 0.1,101, 5.7, 0.0,100, 5.8,-0.1,99),
    ("Cat C",                        10, 2, 12.1,-0.2,98, 12.0,-0.3,97, 12.2,-0.1,99, 12.0,-0.2,98),
    ("Cat D",                         8, 2,  3.7,-0.2,95,  3.9, 0.0,100, 3.7,-0.1,99,  3.8,-0.2,97),
    ("Cat E",                        17, 2,  4.4, 0.3,107, 4.2, 0.2,105, 4.1, 0.3,108, 4.3, 0.3,107),
    ("Cat F",                         9, 2, 52.3,-1.2,102,51.0, 0.4,101,50.8, 0.5,101,50.6, 0.6,101),
    ("Cat G",                         8, 2, 71.2, 2.0,104,69.8, 2.4,103,69.4, 2.2,103,69.3, 2.1,103),
]

fields = [
    "category", "weight_pct", "group_level",
    "share_1m", "chg_1m", "index_1m",
    "share_3m", "chg_3m", "index_3m",
    "share_6m", "chg_6m", "index_6m",
    "share_fy", "chg_fy",  "index_fy",
]

with open(f"{OUT}/share_table.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(fields)
    for row in share_table:
        w.writerow(row)

print("✓ share_table.csv")


# ── 2. DRIVERS / DRAINERS ─────────────────────────────────────────────────────
drivers = [
    # category, direction (driver/drainer), label, value_pts, note
    ("Cat A", "driver",  "Form X growth",                  2.8,  "Fastest-growing form; over-indexed vs channel average"),
    ("Cat A", "driver",  "New store uplift",                1.4,  "Store expansion contributing net new volume"),
    ("Cat A", "driver",  "Larger pack adoption",            0.9,  "Shoppers trading up to larger formats in core variants"),
    ("Cat A", "drainer", "Core variant delistings",        -2.2,  "Removed SKUs directly cost ~0.7 pts; benefit space gap widened"),
    ("Cat A", "drainer", "Benefit space gap",              -1.8,  "100% of share loss going to brands in hydration / anti-aging spaces"),
    ("Cat A", "drainer", "Distribution gap — Prem Flagship",-1.1,"Form X depth <50% in highest-value segment"),
    ("Cat A", "drainer", "Shelf placement pressure",       -0.6,  "Inconsistent placement; emerging brands securing better shelf positions"),
    ("Cat B", "driver",  "Sub-cat B2 stable",               0.3,  "Core sub-category maintained share; premium variants growing"),
    ("Cat B", "driver",  "Large-pack format growth",        0.6,  "Shopper premiumization driving larger-pack adoption"),
    ("Cat B", "driver",  "New store contribution",          0.8,  "Store expansion net positive despite declining share"),
    ("Cat B", "drainer", "Legacy variant delisting",       -1.4,  "High-volume SKU removed; ~8% headwind in H1 before lapping"),
    ("Cat B", "drainer", "Premium import brands",          -1.0,  "Structurally overdeveloped in flagship format"),
    ("Cat B", "drainer", "Emerging mid-tier",              -0.5,  "Mid-tier naturals capturing treatment and benefit-care shoppers"),
    ("Cat B", "drainer", "Refill under-ranging",           -0.3,  "Fastest-growing pack type but lowest distribution depth"),
    ("Cat E", "driver",  "Premium mix tailwind",            1.2,  "Shopper mix shifting to premium; portfolio well-positioned"),
    ("Cat E", "driver",  "Premium format indexing",         0.8,  "Premium-store format over-indexed to Cat E spend"),
    ("Cat E", "driver",  "Recent innovation",               0.4,  "Recent launches performing above plan in premium formats"),
    ("Cat E", "drainer", "Emerging niche brands",          -0.7,  "Niche imported brands growing fast in Premium Flagship"),
    ("Cat E", "drainer", "Benefit sub-category gap",       -0.5,  "Serum / treatment sub-category underdeveloped vs trend"),
]

with open(f"{OUT}/drivers_drainers.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["category", "direction", "label", "value_pts", "note"])
    w.writerows(drivers)

print("✓ drivers_drainers.csv")


# ── 3. COMPETITIVE FLOW ───────────────────────────────────────────────────────
comp_flow = [
    ("Cat A", "Emerging Brand X",         2.4,  "Hydration; premium tier; exclusive premium-format placement"),
    ("Cat A", "Competitor Intl Brand Y",  1.8,  "Anti-aging; strong loyalty reach"),
    ("Cat A", "Local mid-tier brand",     0.6,  "Naturals; value price; gaining in standard-tier stores"),
    ("Cat A", "Our brand",               -1.4,  "Gaps: benefit space, distribution in premium formats, delisting effect"),
    ("Cat B", "Premium Import A",         1.2,  "Exclusive to Premium Flagship; benefit-forward proposition"),
    ("Cat B", "Premium Import B",         0.8,  "Natural-origin; over-ranged in Standard Flagship"),
    ("Cat B", "Emerging local naturals",  0.5,  "Mid-tier price; fastest-growing brand in this customer"),
    ("Cat B", "Our brand",               -0.6,  "Recovering from delistings; innovation pipeline is recovery path"),
    ("Cat E", "Niche Import Brand Z",     0.9,  "Treatment / serum; fast-growing in Premium Flagship"),
    ("Cat E", "Local value brand",        0.3,  "Natural-angle; under-priced vs our range"),
    ("Cat E", "Our brand",               0.3,  "Holding position; watch treatment gap vs niche imports"),
]

with open(f"{OUT}/competitive_flow.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["category", "competitor", "share_move_pts", "note"])
    w.writerows(comp_flow)

print("✓ competitive_flow.csv")


# ── 4. STORE SEGMENTS ─────────────────────────────────────────────────────────
segments = [
    # segment, door_pct, sales_weight_pct, share_chg_pts, distrib_depth_pct, priority
    ("Premium Flagship",   12, 22, -2.1, 42, "Priority: close distribution gaps, innovation first"),
    ("Standard Flagship",  19, 26, -0.9, 62, "Priority: assortment completion, trial activation"),
    ("Community Standard", 42, 35,  0.2, 81, "Protect: maintain presence, defend promo efficiency"),
    ("Specialist Format",  18, 12,  0.0, 74, "Watch: upcoming innovation pipeline has fit here"),
    ("Convenience Express",11,  5,  0.4, 88, "Low priority: small sales weight, limited upside"),
]

with open(f"{OUT}/store_segments.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["segment", "door_pct", "sales_weight_pct", "share_chg_pts", "distrib_depth_pct", "priority_note"])
    w.writerows(segments)

print("✓ store_segments.csv")


# ── 5. RANGING GAPS ───────────────────────────────────────────────────────────
ranging = [
    # sku, prem_flagship_pct, std_flagship_pct, community_pct, specialist_pct, target_pct
    ("Brand 1 · Form X · Pack M",          42, 58, 79, 61, 100),
    ("Brand 1 · Variant Alpha · Refill",    18, 24, 31, 19,  80),
    ("Brand 2 · Form Y · Pack S",           35, 44, 72, 68,  80),
    ("Brand 2 · Form Y · Pack L",           20, 28, 41, 33,  70),
    ("Launch SKU A (innovation)",            0,  0,  0,  0, 100),
    ("Brand 2 · Variant Beta · Pack M",     81, 76, 55, 88,  90),
]

with open(f"{OUT}/ranging_gaps.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["sku", "prem_flagship_pct", "std_flagship_pct", "community_pct", "specialist_pct", "target_pct"])
    w.writerows(ranging)

print("✓ ranging_gaps.csv")


# ── 6. BUILDING BLOCKS ────────────────────────────────────────────────────────
bb_rows = [
    # brand, label, type, q1, q2, q3, q4, full_year
    ("Brand 1", "Form Y base (+7% trend)",           "base",   32.1, 35.5, 31.2, 30.4, 129.2),
    ("Brand 1", "Form X base (+13% trend)",          "base",   65.9, 81.1, 74.5, 72.5, 294.0),
    ("Brand 1", "Incremental from building blocks",  "bb",     10.8, 16.1, 14.8, 15.1,  56.8),
    ("Brand 1", "Innovation A — Form X launch",      "sub",     1.9,  2.9,  2.7,  3.0,  10.5),
    ("Brand 1", "Innovation A — Form Y extension",   "sub",     0.0,  0.3,  0.4,  0.6,   1.3),
    ("Brand 1", "Trial mechanic (Form X)",           "sub",     7.3,  8.9,  8.2,  7.9,  32.3),
    ("Brand 1", "Loyalty trial program",             "sub",     0.0,  0.4,  0.4,  0.5,   1.3),
    ("Brand 1", "Pack-size ranging push",            "sub",     1.6,  1.8,  1.6,  1.5,   6.5),
    ("Brand 1", "Cannibalization / overlap",         "risk",   -9.2, -6.4, -5.2, -5.1, -25.9),
    ("Brand 1", "TOTAL — BASE SCENARIO",             "total", 100.0,127.0,116.0,113.0, 456.0),
    ("Brand 1", "Growth index vs prior year",        "iya",   113.0,120.0,121.0,122.0, 119.0),
    ("Brand 1", "Innovation A trial offer (upside)", "sub",     0.2,  0.3,  0.3,  0.3,   1.0),
    ("Brand 1", "Digital / creator push (upside)",   "sub",     0.0,  0.5,  0.5,  0.5,   1.5),
    ("Brand 1", "Ranging gap close (upside)",        "sub",     0.0,  0.0,  1.1,  1.1,   2.2),
    ("Brand 1", "TOTAL — UPSIDE SCENARIO",           "total", 100.0,128.0,118.0,115.0, 461.0),
    ("Brand 1", "Growth index (upside)",             "iya",   113.0,121.0,124.0,125.0, 121.0),
    ("Brand 2", "Pack L base (+9% trend)",           "base",   54.4, 58.0, 57.5, 51.6, 221.5),
    ("Brand 2", "Pack S base (+5% trend)",           "base",   13.1, 12.4, 13.0, 12.3,  50.8),
    ("Brand 2", "Refill format base (+40% trend)",   "base",    1.2,  1.4,  1.5,  1.4,   5.5),
    ("Brand 2", "Incremental from building blocks",  "bb",      7.9, 15.9, 17.1, 20.9,  61.8),
    ("Brand 2", "Innovation B (functional)",         "sub",     6.9,  9.2,  8.6, 10.4,  35.1),
    ("Brand 2", "Innovation C (naturals)",           "sub",     0.0,  4.7,  6.2,  7.8,  18.7),
    ("Brand 2", "Loyalty trial — Innovation C",      "sub",     0.0,  0.7,  0.9,  1.2,   2.8),
    ("Brand 2", "Loyalty trial — Innovation B",      "sub",     1.0,  1.4,  1.3,  1.6,   5.3),
    ("Brand 2", "Cannibalization / overlap",         "risk",   -3.6, -4.8, -5.4, -5.0, -18.8),
    ("Brand 2", "TOTAL — BASE SCENARIO",             "total",  73.0, 83.0, 84.0, 81.0, 321.0),
    ("Brand 2", "Growth index vs prior year",        "iya",    97.0,107.0,106.0,113.0, 106.0),
    ("Brand 2", "Pack-size ranging push (upside)",   "sub",     0.0,  0.0,  0.8,  0.8,   1.6),
    ("Brand 2", "Innovation B trial mechanic (upside)","sub",   0.7,  0.7,  0.7,  0.5,   2.6),
    ("Brand 2", "Innovation C trial offer (upside)", "sub",     0.0,  0.9,  1.2,  1.6,   3.7),
    ("Brand 2", "Digital creator push (upside)",     "sub",     0.7,  0.9,  0.9,  1.0,   3.5),
    ("Brand 2", "TOTAL — UPSIDE SCENARIO",           "total",  74.0, 86.0, 87.0, 85.0, 332.0),
    ("Brand 2", "Growth index (upside)",             "iya",    99.0,111.0,112.0,119.0, 110.0),
]

with open(f"{OUT}/building_blocks.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["brand", "label", "row_type", "q1", "q2", "q3", "q4", "full_year"])
    w.writerows(bb_rows)

print("✓ building_blocks.csv")


# ── 7. GAMEPLAN ACTIONS ───────────────────────────────────────────────────────
gameplan = [
    ("Innovation A",    "Full ranging in Premium Flagship (100%) + standard floors (80%) by launch week 4", "Confirm shelf slot timing; fund loyalty activation on launch window",       "H1 Q1",        0.4),
    ("Innovation B",    "Scale to 90% distribution in Specialist + Premium Flagship by H2",                 "Joint digital creator campaign; shelf space allocation",                   "H1–H2",        0.5),
    ("Trial activation","Trial mechanic on Form X; deep promotion on Innovation C at launch window",         "Confirm promotion execution depth; test online vs in-store split",        "H2",           0.3),
    ("Ranging",         "Store-level priority analysis → prioritized SKU list by segment",                   "Range review slot inclusion; placement alignment with buyer",             "H2 (cycle)",   0.2),
    ("Visibility",      "Propose good / better / best shelf concept; test dual-placement pilot",             "Space-to-sales discussion with buyer; resolve bottom-shelf placement",    "H2 pilot",     0.2),
    ("Total scenario",  "If all building blocks execute on upside scenario",                                 "Dependent on cross-functional delivery",                                  "Full yr exit", 1.0),
]

with open(f"{OUT}/gameplan_actions.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["lever", "our_action", "cross_func_ask", "timing", "est_share_impact_pts"])
    w.writerows(gameplan)

print("✓ gameplan_actions.csv")

print("\nAll CSVs written to ./data/")
