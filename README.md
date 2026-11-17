# Palembang Land Cover & Spatial Change Analytics Dashboard

![ci](https://github.com/henryferdianto/palembang-land-cover-powerbi/actions/workflows/ci.yml/badge.svg)

> **DATERAQUEST 1.0 — multi-temporal land cover and urban expansion analysis**

## Overview

An interactive Business Intelligence dashboard analyzing multi-temporal land cover changes and urban expansion patterns in Palembang using geospatial and environmental land-use datasets.

## Approach

1. **Data transformation** with Power Query (cleaning, unpivoting, geocoding).
2. **Dimensional model** for land cover, region and time.
3. **DAX measures** for change rates, expansion and sustainability indicators.
4. **Spatial visuals** and trend breakdowns for urban planning insight.

## Repository Structure

```
palembang-land-cover-powerbi/
├── dax/measures.dax
├── docs/data-model.md
├── docs/dashboard-spec.md
├── data/README.md
└── README.md
```

## Tech Stack

`Power BI` · `Power Query` · `DAX` · `Geospatial analytics`

## Getting Started

```bash
git clone https://github.com/henryferdianto/palembang-land-cover-powerbi.git
cd palembang-land-cover-powerbi
pip install -r requirements.txt
```

1. Open Power BI Desktop.
2. Load the land cover dataset described in `data/README.md`.
3. Recreate the measures from `dax/measures.dax`.
4. Build the pages described in `docs/dashboard-spec.md`.


<!-- completed -->

## Quickstart with Sample Data

The repository ships a synthetic data generator so the full pipeline can be run
without any private dataset:

```bash
make sample && python -m src.analyze
```

## Tests

```bash
pip install -r requirements.txt
pytest -q
```

## Project Status

This repository contains the project documentation and a runnable reference
implementation. A synthetic data generator is included so every pipeline stage
can be executed end-to-end; replace the sample data with your own datasets in
`data/raw/` to reproduce real results.

## License

MIT License — see [LICENSE](LICENSE).


---

**Author:** Rifky Henry Ferdianto — Data Science undergraduate at ITERA  
GitHub: [@henryferdianto](https://github.com/henryferdianto) · Portfolio: [rifky-henry-ferdianto](https://github.com/henryferdianto/rifky-henry-ferdianto)
