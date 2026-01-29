# Colocalization (coloc.abf) — showcase script
# Requires: coloc, data.table

library(coloc)
library(data.table)

files <- list.files(".", pattern="harmonized\\.csv", full.names=TRUE)
results <- list()

for (f in files) {
  d <- fread(f)
  gwas <- list(beta=d$beta_gwas, varbeta=(d$standard_error^2), N=NA, MAF=d$maf, type="cc", s=0.5, snp=d$variant_id)
  eqtl <- list(beta=d$slope, varbeta=(d$slope_se^2), N=NA, MAF=d$maf, type="quant", snp=d$variant_id)
  res <- tryCatch(coloc.abf(dataset1=gwas, dataset2=eqtl), error=function(e) NULL)
  if (!is.null(res)) {
    s <- res$summary
    results[[length(results)+1]] <- data.frame(file=basename(f), PP.H4=s["PP.H4.abf"], PP.H3=s["PP.H3.abf"])
  }
}

resdf <- if (length(results)>0) rbindlist(results) else data.frame()
write.csv(resdf, "coloc_results.csv", row.names=FALSE)

cat("total tests:", nrow(resdf), "\n")
cat("strong colocs (PP.H4>0.8):", ifelse(nrow(resdf)>0, sum(resdf$PP.H4>0.8), 0), "\n")
