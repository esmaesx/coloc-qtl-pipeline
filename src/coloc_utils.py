from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

import numpy as np
import pandas as pd


@dataclass
class LocusData:
    gwas: pd.DataFrame
    qtl: pd.DataFrame


def simulate_locus(n: int = 200, seed: int = 42, effect_sd: float = 0.1) -> LocusData:
    rng = np.random.default_rng(seed)
    chrom = rng.integers(1, 23, n)
    pos = rng.integers(1, 1_000_000, n)
    snp = [f"rs{seed}_{i+1}" for i in range(n)]
    maf = rng.uniform(0.05, 0.45, n)

    beta_gwas = rng.normal(0, effect_sd, n)
    beta_qtl = beta_gwas + rng.normal(0, 0.05, n)

    se_gwas = rng.uniform(0.05, 0.15, n)
    se_qtl = rng.uniform(0.05, 0.15, n)

    gwas = pd.DataFrame(
        {
            "snp": snp,
            "chrom": chrom,
            "pos": pos,
            "beta": beta_gwas,
            "se": se_gwas,
            "maf": maf,
        }
    )
    qtl = pd.DataFrame(
        {
            "snp": snp,
            "chrom": chrom,
            "pos": pos,
            "beta": beta_qtl,
            "se": se_qtl,
            "maf": maf,
        }
    )

    return LocusData(gwas=gwas, qtl=qtl)


def harmonize_sumstats(gwas: pd.DataFrame, qtl: pd.DataFrame) -> pd.DataFrame:
    merged = gwas.merge(qtl, on="snp", suffixes=("_gwas", "_qtl"))
    merged = merged[merged["maf_gwas"].between(0, 1)]
    merged = merged[merged["maf_qtl"].between(0, 1)]
    merged = merged[merged["chrom_gwas"].between(1, 22)]
    merged = merged[merged["chrom_qtl"].between(1, 22)]
    return merged


def coloc_metrics(merged: pd.DataFrame, top_n: int = 10) -> Tuple[float, float]:
    if merged.empty:
        return float("nan"), float("nan")

    corr = float(np.corrcoef(merged["beta_gwas"], merged["beta_qtl"])[0, 1])
    merged = merged.copy()
    merged["z_gwas"] = merged["beta_gwas"] / merged["se_gwas"]
    merged["z_qtl"] = merged["beta_qtl"] / merged["se_qtl"]

    top_gwas = set(merged.nlargest(top_n, "z_gwas")["snp"])
    top_qtl = set(merged.nlargest(top_n, "z_qtl")["snp"])
    overlap = len(top_gwas & top_qtl) / max(1, top_n)

    return corr, overlap
