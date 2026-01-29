# QTL Colocalization Pipeline

**Goal:** Showcase a reproducible statistical genetics workflow for colocalizing GWAS signals with QTLs (eQTL/pQTL/sQTL).

## What this includes
- GWAS summary stats ingestion
- QTL downloads (GTEx eQTL/sQTL, pQTL sources)
- Variant harmonization (chr/pos/alleles)
- Locus extraction (±1 Mb)
- Colocalization with `coloc.abf` (R)

## Data sources
- GWAS Catalog: https://www.ebi.ac.uk/gwas/
- GTEx v8 (eQTL/sQTL): https://gtexportal.org/home/
- SCALLOP pQTL: https://www.scallop.org/

## Notes
This repo is a workflow showcase (implementation‑focused rather than results‑focused). Coloc yield depends on overlap and harmonization quality.

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
