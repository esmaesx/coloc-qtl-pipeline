import pandas as pd

from coloc_utils import simulate_locus, harmonize_sumstats, coloc_metrics


def test_simulate_locus_shapes():
    locus = simulate_locus(n=120, seed=3, effect_sd=0.1)
    assert len(locus.gwas) == 120
    assert len(locus.qtl) == 120
    assert {"snp", "chrom", "pos", "beta", "se", "maf"}.issubset(locus.gwas.columns)


def test_harmonize_keeps_intersection():
    locus = simulate_locus(n=50, seed=5, effect_sd=0.1)
    gwas = locus.gwas.copy()
    qtl = locus.qtl.iloc[:40].copy()
    merged = harmonize_sumstats(gwas, qtl)
    assert len(merged) == 40
    assert "beta_gwas" in merged.columns
    assert "beta_qtl" in merged.columns


def test_coloc_metrics_high_correlation():
    merged = pd.DataFrame(
        {
            "snp": ["rs1", "rs2", "rs3"],
            "beta_gwas": [0.2, 0.4, 0.8],
            "beta_qtl": [0.21, 0.39, 0.79],
            "se_gwas": [0.1, 0.1, 0.1],
            "se_qtl": [0.1, 0.1, 0.1],
        }
    )
    corr, overlap = coloc_metrics(merged, top_n=3)
    assert corr > 0.99
    assert overlap == 1.0
