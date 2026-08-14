# Phytochemical & Antioxidant Data Analysis of Medicinal Plants

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/hafizamuntaha-fatima/phyto-antioxidant-analysis/blob/main/notebooks/01_phytochemical_antioxidant_analysis.ipynb)

> ▶️ Click the badge to open and run the analysis in Google Colab (free, no install).

Reproducible analysis of the relationship between **phenolic/flavonoid content** and
**antioxidant activity** across 38 medicinal plants, using Python (pandas, NumPy, Matplotlib).

This project sits alongside my BS Biochemistry research on plant-derived flavonoids
(*Camellia sinensis*) and thymoquinone (*Nigella sativa*) as an anti-virulence strategy
against *Streptococcus pyogenes* — here I approach the same chemistry from a **computational,
data-analysis angle**.

## Research question
Do phenolic-rich and flavonoid-rich medicinal plants show stronger antioxidant activity,
and how do my two thesis species compare to the wider panel?

## What the analysis does
- Validates and cleans the dataset (missing values, impossible values, duplicates)
- Summarises distributions of TPC, TFC, DPPH IC50, and FRAP
- Tests Pearson correlations between phenolic/flavonoid content and antioxidant activity
- Ranks the strongest antioxidant plants and compares botanical families
- Highlights *Camellia sinensis* and *Nigella sativa* against the panel

## Key figures
Generated into `reports/figures/`:
`distributions.png`, `correlation_heatmap.png`, `antioxidant_vs_content.png`, `top10_antioxidant.png`.

## How to run
```bash
pip install -r requirements.txt

# Option A: run the notebook
jupyter notebook notebooks/01_phytochemical_antioxidant_analysis.ipynb

# Option B: run the script version (writes all figures)
python src/analysis.py
```

## Data
`data/medicinal_plants_phytochemistry.csv` — an educational dataset compiled from typical
published assay ranges. Full provenance and columns are documented in
[`data/DATASET.md`](data/DATASET.md). Values are illustrative for reproducible-analysis
practice and are **not** original laboratory measurements.

## Repository layout
```
data/        CSV dataset + provenance
notebooks/   Jupyter analysis notebook
src/         script version of the analysis
reports/     generated figures
```

## License
MIT — see [LICENSE](LICENSE).
