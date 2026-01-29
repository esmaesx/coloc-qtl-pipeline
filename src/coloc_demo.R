# QTL colocalization demo with synthetic data
# Produces a minimal coloc.abf output without reporting real results

suppressPackageStartupMessages({
  library(coloc)
})

set.seed(42)

simulate_locus <- function(n=200, effect_sd=0.1) {
  beta1 <- rnorm(n, 0, effect_sd)
  se1 <- runif(n, 0.05, 0.15)
  maf <- runif(n, 0.05, 0.45)

  beta2 <- beta1 + rnorm(n, 0, 0.05)
  se2 <- runif(n, 0.05, 0.15)

  snp <- paste0("rs", 1:n)

  gwas <- list(beta=beta1, varbeta=se1^2, N=5000, MAF=maf, type="quant", snp=snp)
  qtl  <- list(beta=beta2, varbeta=se2^2, N=400, MAF=maf, type="quant", snp=snp)

  list(gwas=gwas, qtl=qtl)
}

run_coloc <- function(gwas, qtl) {
  res <- coloc.abf(gwas, qtl)
  return(res$summary)
}

# Run multiple synthetic loci to show looping and aggregation
summaries <- list()
for (i in 1:5) {
  locus <- simulate_locus(n=200, effect_sd=0.08)
  s <- run_coloc(locus$gwas, locus$qtl)
  summaries[[i]] <- data.frame(
    locus=i,
    PP.H0=s["PP.H0.abf"],
    PP.H1=s["PP.H1.abf"],
    PP.H2=s["PP.H2.abf"],
    PP.H3=s["PP.H3.abf"],
    PP.H4=s["PP.H4.abf"]
  )
}

out <- do.call(rbind, summaries)
print(out)
