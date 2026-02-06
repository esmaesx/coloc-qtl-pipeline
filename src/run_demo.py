from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

from coloc_utils import simulate_locus, harmonize_sumstats, coloc_metrics


def main():
    root = Path(__file__).resolve().parents[1]
    reports = root / "reports"
    reports.mkdir(exist_ok=True)

    rows = []
    scatter_df = None

    for locus_id, seed in enumerate([11, 29, 47], start=1):
        locus = simulate_locus(n=200, seed=seed, effect_sd=0.1)
        merged = harmonize_sumstats(locus.gwas, locus.qtl)
        corr, overlap = coloc_metrics(merged, top_n=10)

        rows.append(
            {
                "locus": locus_id,
                "n_variants": len(merged),
                "beta_corr": round(corr, 3),
                "top10_overlap": round(overlap, 3),
            }
        )

        if scatter_df is None:
            scatter_df = merged.copy()

    summary = pd.DataFrame(rows)
    summary_path = reports / "coloc_demo_summary.csv"
    summary.to_csv(summary_path, index=False)

    if scatter_df is not None and not scatter_df.empty:
        plt.figure(figsize=(5, 4))
        plt.scatter(scatter_df["beta_gwas"], scatter_df["beta_qtl"], s=12, alpha=0.7)
        plt.axhline(0, color="#999", linewidth=0.8)
        plt.axvline(0, color="#999", linewidth=0.8)
        plt.xlabel("GWAS beta")
        plt.ylabel("QTL beta")
        plt.title("Synthetic locus effect agreement")
        plt.tight_layout()
        plot_path = reports / "coloc_demo_scatter.png"
        plt.savefig(plot_path, dpi=160)
        plt.close()

    print(f"Wrote {summary_path}")


if __name__ == "__main__":
    main()
