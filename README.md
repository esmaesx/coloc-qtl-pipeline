# QTL Colocalization Pipeline

Minimal, runnable demo of colocalization-style logic using synthetic GWAS and QTL summary stats. It simulates matched loci, harmonizes variant rows, and reports effect agreement and top-variant overlap as a lightweight proxy for full coloc. The code is meant to show the pipeline shape without pulling real studies.

Why it matters
- Coloc signals depend on harmonization and QC, not just statistical machinery.
- Fast synthetic demos help debug data contracts before downloading big QTL files.
- Clear summaries let you compare loci without drowning in per-variant detail.

Quickstart
```bash
make setup
make demo
make test
```

What you get
- `reports/coloc_demo_summary.csv` (per-locus beta correlation and top-10 overlap)
- `reports/coloc_demo_scatter.png` (GWAS vs QTL beta scatter for one locus)

Notes / assumptions
- Synthetic inputs include `snp`, `chrom`, `pos`, `beta`, `se`, `maf` (see `src/coloc_utils.py`).
- QC in `harmonize_sumstats` drops rows with MAF outside [0,1] or chromosomes outside 1–22.
- The demo uses beta correlation and top-10 overlap as a proxy for colocalization strength.

Status
Ready for demo; real-data ingest lives in `src/ingest_qtl.py`.
