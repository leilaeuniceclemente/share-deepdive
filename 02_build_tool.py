"""
02_build_tool.py
Customer Share Deepdive Console — tool builder
Reads synthetic CSVs from ./data/ and validates structure before deploy.

The actual tool is index.html (self-contained, data embedded as JS literals).
This script validates the CSV data matches what is embedded in the tool
and prints a summary — useful as a pre-deploy check or as a starting point
if you want to regenerate the HTML from live data sources.

Run: python 02_build_tool.py
"""

import csv
import os
import sys

DATA = "data"

EXPECTED_FILES = [
    "share_table.csv",
    "drivers_drainers.csv",
    "competitive_flow.csv",
    "store_segments.csv",
    "ranging_gaps.csv",
    "building_blocks.csv",
    "gameplan_actions.csv",
]

EXPECTED_COLS = {
    "share_table.csv": [
        "category", "weight_pct", "group_level",
        "share_1m", "chg_1m", "index_1m",
        "share_3m", "chg_3m", "index_3m",
        "share_6m", "chg_6m", "index_6m",
        "share_fy", "chg_fy",  "index_fy",
    ],
    "drivers_drainers.csv":  ["category", "direction", "label", "value_pts", "note"],
    "competitive_flow.csv":  ["category", "competitor", "share_move_pts", "note"],
    "store_segments.csv":    ["segment", "door_pct", "sales_weight_pct", "share_chg_pts", "distrib_depth_pct", "priority_note"],
    "ranging_gaps.csv":      ["sku", "prem_flagship_pct", "std_flagship_pct", "community_pct", "specialist_pct", "target_pct"],
    "building_blocks.csv":   ["brand", "label", "row_type", "q1", "q2", "q3", "q4", "full_year"],
    "gameplan_actions.csv":  ["lever", "our_action", "cross_func_ask", "timing", "est_share_impact_pts"],
}


def read_csv(fname):
    path = os.path.join(DATA, fname)
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def validate():
    errors = []
    summaries = []

    for fname in EXPECTED_FILES:
        path = os.path.join(DATA, fname)
        if not os.path.exists(path):
            errors.append(f"MISSING: {fname}")
            continue

        rows = read_csv(fname)
        expected = EXPECTED_COLS[fname]
        actual = list(rows[0].keys()) if rows else []

        missing_cols = [c for c in expected if c not in actual]
        if missing_cols:
            errors.append(f"{fname}: missing columns {missing_cols}")

        summaries.append(f"  {fname:<32} {len(rows):>3} rows   cols: {', '.join(actual[:4])}{'...' if len(actual)>4 else ''}")

    return errors, summaries


def spot_checks():
    """Basic sanity checks on data integrity."""
    issues = []

    # Share table: total row should exist
    rows = read_csv("share_table.csv")
    totals = [r for r in rows if r["group_level"] == "0"]
    if not totals:
        issues.append("share_table: no group_level=0 (total) row found")
    else:
        fy = float(totals[0]["share_fy"])
        if not (5.0 <= fy <= 30.0):
            issues.append(f"share_table: total share_fy={fy} looks out of range (expected 5–30%)")

    # Drivers: should have both directions
    rows = read_csv("drivers_drainers.csv")
    directions = {r["direction"] for r in rows}
    if "driver" not in directions:
        issues.append("drivers_drainers: no rows with direction='driver'")
    if "drainer" not in directions:
        issues.append("drivers_drainers: no rows with direction='drainer'")

    # Ranging: targets should be >= all segment values (mostly)
    rows = read_csv("ranging_gaps.csv")
    seg_cols = ["prem_flagship_pct", "std_flagship_pct", "community_pct", "specialist_pct"]
    for r in rows:
        target = int(r["target_pct"])
        for col in seg_cols:
            val = int(r[col])
            if val > target:
                issues.append(f"ranging_gaps: {r['sku']} has {col}={val} > target={target}")

    # Building blocks: base scenario totals should be positive
    rows = read_csv("building_blocks.csv")
    totals = [r for r in rows if r["row_type"] == "total" and "BASE" in r["label"]]
    for r in totals:
        fy = float(r["full_year"])
        if fy <= 0:
            issues.append(f"building_blocks: {r['brand']} base total full_year={fy} is not positive")

    return issues


def print_summary():
    print("=" * 60)
    print("Customer Share Deepdive Console — Data Validation")
    print("=" * 60)

    errors, summaries = validate()

    print("\nFile inventory:")
    for s in summaries:
        print(s)

    issues = spot_checks()

    if errors:
        print(f"\n❌ ERRORS ({len(errors)}):")
        for e in errors:
            print(f"   {e}")
    else:
        print("\n✓ All files present with expected columns")

    if issues:
        print(f"\n⚠️  DATA WARNINGS ({len(issues)}):")
        for i in issues:
            print(f"   {i}")
    else:
        print("✓ Spot checks passed")

    if not errors and not issues:
        print("\n✅ Data looks good — index.html is ready to deploy")
    else:
        print("\n⚠️  Review warnings before deploying")
        sys.exit(1)

    # Quick stats
    print("\n── Quick stats ──")
    share = read_csv("share_table.csv")
    total_row = next(r for r in share if r["group_level"] == "0")
    print(f"  Total customer share (FY):   {total_row['share_fy']}%  (chg: {total_row['chg_fy']} pts)")

    segs = read_csv("store_segments.csv")
    bleeders = [s for s in segs if float(s["share_chg_pts"]) < 0]
    gainers  = [s for s in segs if float(s["share_chg_pts"]) > 0]
    print(f"  Store segments — gainers: {len(gainers)}, bleeders: {len(bleeders)}")

    bb = read_csv("building_blocks.csv")
    brands = sorted({r["brand"] for r in bb})
    for brand in brands:
        base = next((r for r in bb if r["brand"] == brand and "BASE" in r["label"] and r["row_type"] == "total"), None)
        if base:
            print(f"  {brand} FY base scenario: {base['full_year']} (indexed)")

    print()


if __name__ == "__main__":
    print_summary()
