matrixA = [3 1; 4 5]
matrixB = [8 3; 2 1]
println("Matrix A:")
display(matrixA)
println("Matrix B:")
display(matrixB)

# Addition
matrixC = matrixA + matrixB
println("A + B =")
display(matrixC)

# Multiplikation
matrixD = matrixA * matrixB
println("A * B =")
display(matrixD)

matrixD = matrixA .* matrixB
println("A .* B =")
display(matrixD)

println("Bei der Multiplikation A*B werden die Reihen der einen Matrix mit den Spalten der
anderen multipliziert und danach addiert, also (3*8)+(1*2) etc. Bei der Multiplikation
A.*B werden nur die einzelnen Zellen der Matrix multipliziert.")

# Division
matrixE = matrixA/matrixB
println("A/B =")
display(matrixE)

matrixE = matrixA\matrixB
println("A\\B =")
display(matrixE)

println("Die erste Division ist eine normale Division von Matrizen, während der zweite
Operator die Inverse von A durch B teilt.")

# 3x3 Matrix Rechnungen
println("\n")
matrix = [2 3 1; 4 2 2; 1 5 3]
display(matrix)

println("\n matrix.+1")
display(matrix.+1)
println("\n matrix.-1")
display(matrix.-1)
println("\n matrix.*2")
display(matrix.*2)
println("\n matrix./2")
display(matrix./2)

# 3x4 Matrix mit Vektor
println("\n")
matrixF = [2 3 1 6; 4 2 2 7; 1 5 3 5]
display(matrixF)
v = [2, 4, 1, 5]
display(v)

println("\nMatrix * Vektor")
display(matrixF * v)