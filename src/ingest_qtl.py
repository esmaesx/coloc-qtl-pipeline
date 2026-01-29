"""QTL summary stats ingestion and QC.
Reads a TSV or CSV, validates required fields, harmonizes names, and writes a clean file.
"""
from pathlib import Path
import pandas as pd

REQUIRED = {"chrom", "pos", "beta", "se", "maf"}
ALIASES = {
    "chr": "chrom",
    "chromosome": "chrom",
    "position": "pos",
    "slope": "beta",
    "slope_se": "se",
    "af": "maf",
}


def read_table(path):
    path = Path(path)
    if path.suffix.lower() in {".tsv", ".txt"}:
        return pd.read_csv(path, sep="\t")
    return pd.read_csv(path)


def normalize_columns(df):
    cols = {c: c.strip().lower() for c in df.columns}
    df = df.rename(columns=cols)
    df = df.rename(columns={k: v for k, v in ALIASES.items() if k in df.columns})
    return df


def validate(df):
    missing = REQUIRED - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")


def basic_qc(df):
    df = df.copy()
    df = df[df["maf"].between(0, 1)]
    df = df[df["chrom"].between(1, 22)]
    df = df[df["pos"] > 0]
    return df


def main(in_path, out_path):
    df = read_table(in_path)
    df = normalize_columns(df)
    validate(df)
    df = basic_qc(df)
    df.to_csv(out_path, index=False)
    print(f"Wrote {out_path} with {len(df)} rows")


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        raise SystemExit("Usage: python src/ingest_qtl.py <input.tsv|csv> <output.csv>")
    main(sys.argv[1], sys.argv[2])
