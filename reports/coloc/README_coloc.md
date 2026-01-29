# Colocalization Pipeline (Showcase)

This folder documents the coloc workflow used to connect GWAS signals to GTEx QTL data.

## Pipelines included
- **Bulk RNA eQTL** (skin + whole blood)
- **sQTL** (splicing QTL; skin + whole blood)

## Steps
1) GWAS summary stats ingestion
2) GTEx v8 QTL download (bulk eQTL + sQTL)
3) Variant harmonization (chr/pos/alleles)
4) Locus extraction (±1 Mb around lead SNPs)
5) Coloc using `coloc.abf`

## Notes
- GTEx files are large; we use only significant variant‑gene pairs.
- Final coloc yield depends on overlap and variant harmonization.
- This repo is intended as a transparent, reproducible workflow showcase.
