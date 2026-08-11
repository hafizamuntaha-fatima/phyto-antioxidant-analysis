"""Reproducible phytochemical & antioxidant analysis (script version of the notebook).

Runs the full analysis from the command line and writes all figures to reports/figures/.
Usage:
    python src/analysis.py
"""
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")  # headless: save figures without a display
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "medicinal_plants_phytochemistry.csv"
FIG = ROOT / "reports" / "figures"
FIG.mkdir(parents=True, exist_ok=True)

NUMERIC = ["TPC_mg_GAE_per_g", "TFC_mg_QE_per_g", "DPPH_IC50_ug_per_mL", "FRAP_umol_Fe_per_g"]
GREEN, RED, BLUE = "#4C7A34", "#B8442A", "#1f4e79"


def load_and_validate() -> pd.DataFrame:
    df = pd.read_csv(DATA)
    assert df[NUMERIC].isna().sum().sum() == 0, "Unexpected missing values"
    assert (df[NUMERIC] > 0).all().all(), "Non-positive numeric values found"
    assert df["scientific_name"].duplicated().sum() == 0, "Duplicate species"
    print(f"Loaded and validated {len(df)} plants.")
    return df


def correlations(df: pd.DataFrame) -> None:
    corr = df[NUMERIC].corr()
    print("\nPearson correlations:\n", corr.round(3))
    fig, ax = plt.subplots(figsize=(6, 5))
    im = ax.imshow(corr, cmap="RdYlGn", vmin=-1, vmax=1)
    labels = ["TPC", "TFC", "DPPH IC50", "FRAP"]
    ax.set_xticks(range(4)); ax.set_yticks(range(4))
    ax.set_xticklabels(labels, rotation=45, ha="right"); ax.set_yticklabels(labels)
    for i in range(4):
        for j in range(4):
            ax.text(j, i, f"{corr.iloc[i, j]:.2f}", ha="center", va="center", fontsize=9)
    ax.set_title("Correlation heatmap")
    fig.colorbar(im, ax=ax, shrink=0.8)
    fig.tight_layout(); fig.savefig(FIG / "correlation_heatmap.png", bbox_inches="tight")
    plt.close(fig)


def scatter_relationships(df: pd.DataFrame) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    for ax, xcol, label in zip(axes, ["TPC_mg_GAE_per_g", "TFC_mg_QE_per_g"],
                               ["Total Phenolic Content (mg GAE/g)", "Total Flavonoid Content (mg QE/g)"]):
        ax.scatter(df[xcol], df["DPPH_IC50_ug_per_mL"], color=GREEN, alpha=0.75)
        m, b = np.polyfit(df[xcol], df["DPPH_IC50_ug_per_mL"], 1)
        xs = np.linspace(df[xcol].min(), df[xcol].max(), 50)
        ax.plot(xs, m * xs + b, "--", color=RED)
        r = df[xcol].corr(df["DPPH_IC50_ug_per_mL"])
        ax.set_xlabel(label); ax.set_ylabel("DPPH IC50 (ug/mL)"); ax.set_title(f"r = {r:.2f}")
        for name in ["Camellia sinensis", "Nigella sativa"]:
            row = df[df["scientific_name"] == name]
            ax.scatter(row[xcol], row["DPPH_IC50_ug_per_mL"], color=BLUE, s=90, zorder=5)
            ax.annotate(name.split()[0], (row[xcol].values[0], row["DPPH_IC50_ug_per_mL"].values[0]),
                        textcoords="offset points", xytext=(6, 6), fontsize=9)
    fig.suptitle("Antioxidant activity vs phenolic/flavonoid content")
    fig.tight_layout(); fig.savefig(FIG / "antioxidant_vs_content.png", bbox_inches="tight")
    plt.close(fig)


def top_antioxidants(df: pd.DataFrame) -> None:
    top10 = df.sort_values("DPPH_IC50_ug_per_mL").head(10)
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.barh(top10["plant_common_name"][::-1], top10["DPPH_IC50_ug_per_mL"][::-1], color=GREEN)
    ax.set_xlabel("DPPH IC50 (ug/mL) — lower is stronger")
    ax.set_title("Top 10 antioxidant medicinal plants")
    fig.tight_layout(); fig.savefig(FIG / "top10_antioxidant.png", bbox_inches="tight")
    plt.close(fig)
    print("\nTop 5 antioxidants:")
    print(top10[["plant_common_name", "TPC_mg_GAE_per_g", "DPPH_IC50_ug_per_mL"]].head().to_string(index=False))


def main() -> None:
    df = load_and_validate()
    print("\nSummary statistics:\n", df[NUMERIC].describe().round(2))
    correlations(df)
    scatter_relationships(df)
    top_antioxidants(df)
    print(f"\nFigures written to {FIG}")


if __name__ == "__main__":
    main()
