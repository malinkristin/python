cat("Analysis of the Esoph dataset")
analyse <- function() {
  x <- nrow(esoph)
  cat("\nAnzahl Daten in diesem Datensatz: ", x)
  cat("\nSummary of the data:\n")
  print(summary(esoph))
  
  cat("\nCases per age group (alcohol):")
  print(table(esoph$agegp, esoph$alcgp))
  cat("\nCases per age group (tobacco):")
  print(table(esoph$agegp, esoph$tobgp))
}

analyse()