# QTL Colocalization Pipeline

**Goal:** Showcase a reproducible genomics workflow for colocalizing GWAS signals with QTLs across eQTL, pQTL, and sQTL.

## What this includes
- GWAS summary stats ingestion
- QTL downloads for eQTL, pQTL, and sQTL
- Variant harmonization
- Locus extraction
- Colocalization with `coloc.abf`

## Notes
This repo is a workflow showcase and does not report study results. Colocalization yield depends on overlap and harmonization quality.

## Real data ingestion
Clean and standardize QTL summary stats:
```
python src/ingest_qtl.py data/raw_qtl.tsv data/qtl_clean.csv
```

## Demo code
Run a minimal coloc demo with synthetic data:
```
Rscript src/coloc_demo.R
```

## Data sources
- GWAS Catalog: https://www.ebi.ac.uk/gwas/
- GTEx v8 (eQTL and sQTL): https://gtexportal.org/home/
- SCALLOP pQTL: https://www.scallop.org/

## Repo structure
```
coloc-qtl-pipeline/
  data/
  notebooks/
  src/
  reports/
  README.md
  LICENSE
```
