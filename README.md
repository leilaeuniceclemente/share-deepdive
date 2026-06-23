# Customer Share Deepdive Console

**Interactive multi-source share analysis framework — synthetic data, vanilla JS, self-contained.**

A portfolio tool demonstrating how to stitch disconnected data sources (internal POS, syndicated panel, distribution data, store-level segmentation) into a single repeatable share growth gameplan. Built as a single `index.html` with no dependencies beyond Chart.js (CDN).

---

## What it does

Six interactive tabs covering the full share diagnostic workflow:

| Tab | What it shows |
|-----|--------------|
| **Overview** | KPI summary, share change by category, growth engines vs bleeders waterfall |
| **Share table** | Multi-period share table (1M / 3M / 6M / full year) with three views: absolute share, change vs prior year, growth index |
| **Drivers / drainers** | Category-level diagnostic — what's driving share up, what's costing it, competitive flow, and ranked opportunities |
| **Store segments** | Five-segment store classification with share performance, distribution depth, and ranging gap table by SKU × segment |
| **Building blocks** | Quarterly volume gameplan by brand — base scenario, innovation launches, trial activation, cannibalization, upside scenario |
| **Gameplan** | Action table by lever (innovation, trial, ranging, visibility) with owner split and estimated share impact |

---

## Previews

### Overview
![Overview tab](previews/preview_overview.png)

### Share table — change vs prior year view
![Share table](previews/preview_share-chg.png)

### Drivers / drainers
![Drivers drainers](previews/preview_drivers.png)

### Store segments
![Store segments](previews/preview_store-segments.png)

### Building blocks
![Building blocks](previews/preview_building-blocks.png)

### Gameplan
![Gameplan](previews/preview_gameplan.png)

---

## Files

```
customer-share-deepdive/
├── index.html              # Self-contained tool (open in any browser)
├── 01_generate_data.py     # Generates all synthetic CSVs
├── 02_build_tool.py        # Validates CSV structure and data integrity
├── data/
│   ├── share_table.csv         # Multi-period share with growth index
│   ├── drivers_drainers.csv    # Category-level driver / drainer decomposition
│   ├── competitive_flow.csv    # Share flow by competitor
│   ├── store_segments.csv      # 5-segment store classification + performance
│   ├── ranging_gaps.csv        # SKU distribution depth by segment vs target
│   ├── building_blocks.csv     # Quarterly volume projections by brand
│   └── gameplan_actions.csv    # Actions, owners, timing, estimated impact
└── previews/
    └── preview_*.png           # Tab screenshots
```

---

## Usage

### View the tool
Open `index.html` directly in a browser — no server or build step needed.

### Regenerate synthetic data
```bash
python 01_generate_data.py
```

### Validate before deploy
```bash
python 02_build_tool.py
```
Checks all CSVs are present, columns match expected schema, and runs spot-checks on data integrity.

---

## Methodology notes

**Share table** shows share of customer sales (not total market share) across rolling time windows. Three views:
- *Absolute share* — raw percentage of category sales
- *Change vs prior year* — share point delta, color-coded (green = gaining, red = losing)
- *Growth index* — indexed volume growth (100 = flat); useful to separate volume growth from share movement

**Store segmentation** classifies doors on format, spend tier, and size — collapsed to five actionable labels for ranging and activation targeting. Distribution depth (% of eligible doors carrying the SKU) is the key diagnostic metric.

**Building blocks** show a base scenario (trend extrapolation) plus discrete incremental levers (innovation launches, trial mechanics, ranging pushes, loyalty programs). A cannibalization assumption offsets internal switching. An upside scenario layers on additional activation levers.

---

## Data

All data is **synthetic** — engineered for structural realism, not sourced from any real business. Category names, brand names, SKU labels, and numeric values are illustrative only.

This tool is intended for portfolio demonstration purposes. Not for distribution.

---

## Stack

- Vanilla JS · no framework
- Chart.js 4.4 (CDN, horizontal bar chart)
- CSS custom properties for theming
- `noindex` meta tag set

---

*Built as part of a custom analytics tools portfolio.*
