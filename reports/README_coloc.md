# Coloc Pipeline (Showcase)

## Pipelines
- Bulk eQTL (GTEx v8)
- sQTL (GTEx v8)

## Steps
1) GWAS ingestion
2) GTEx QTL download
3) Variant harmonization (chr/pos/alleles)
4) Locus extraction (±1 Mb)
5) Coloc with `coloc.abf`

## Notes
Yield depends on overlap + harmonization. This repo focuses on transparent workflow.
