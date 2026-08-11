# Dataset provenance — `medicinal_plants_phytochemistry.csv`

## What this dataset is
An **educational, compiled dataset** of 38 medicinal plants with four commonly reported
phytochemical / antioxidant measurements. It was assembled to practice **reproducible
data analysis**, not generated in a laboratory.

Each value falls within the **typical published ranges** reported for that species and
assay in the peer-reviewed phytochemistry literature. The numbers are representative and
illustrative; they are **not** original measurements and must not be cited as primary data.

## Columns
| Column | Meaning | Unit |
|---|---|---|
| `plant_common_name` | Common name | — |
| `scientific_name` | Binomial name | — |
| `family` | Botanical family | — |
| `plant_part` | Part extracted | — |
| `extract_solvent` | Extraction solvent | — |
| `TPC_mg_GAE_per_g` | Total Phenolic Content | mg gallic acid equivalents / g |
| `TFC_mg_QE_per_g` | Total Flavonoid Content | mg quercetin equivalents / g |
| `DPPH_IC50_ug_per_mL` | Antioxidant activity (radical scavenging). **Lower = stronger** | µg/mL |
| `FRAP_umol_Fe_per_g` | Ferric reducing antioxidant power | µmol Fe / g |
| `reported_bioactivity` | Commonly reported activities | — |

## How to make this dataset "real" for a stronger portfolio
This project is fully valid as a reproducible-analysis exercise on compiled data. To
upgrade it to primary/public data you can:
1. Replace rows with values you extract yourself from open-access papers (add a `source_doi`
   column and cite each), or
2. Import a public database export (e.g. Dr. Duke's Phytochemical and Ethnobotanical
   Databases, or a Kaggle phytochemistry dataset) and cite it here.

Keep this file updated with the exact source of every value you add.
