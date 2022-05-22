# prompt function
prompt <- function() {
  input <- readline(prompt = "Guess a number between 0 and 100.\n")
  return (as.integer(input))
}

# functionality
play <- function() {
  # choose random number
  correctNumber <- sample(0:100, 1)
  
  num <- -1
  while (num != correctNumber) {
    num <- prompt()
    
    if (num == correctNumber) {
      cat("That's the one!")
    }
    else if (num < correctNumber) {
      cat("Guess higher!\n")
    }
    else if (num > correctNumber) {
      cat("Guess lower!\n")
    }
  }
}

play()
