# QTL colocalization demo with synthetic data
# Produces a minimal coloc.abf output without reporting real results

suppressPackageStartupMessages({
  library(coloc)
})

set.seed(42)

n <- 200
beta1 <- rnorm(n, 0, 0.1)
se1 <- runif(n, 0.05, 0.15)
maf <- runif(n, 0.05, 0.45)

beta2 <- beta1 + rnorm(n, 0, 0.05)
se2 <- runif(n, 0.05, 0.15)

snp <- paste0("rs", 1:n)

gwas <- list(beta=beta1, varbeta=se1^2, N=5000, MAF=maf, type="quant", snp=snp)
qtl  <- list(beta=beta2, varbeta=se2^2, N=400, MAF=maf, type="quant", snp=snp)

res <- coloc.abf(gwas, qtl)
print(res$summary)
