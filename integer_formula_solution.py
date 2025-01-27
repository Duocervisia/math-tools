def multiply_matrices(matrix1, matrix2):
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    print_matrix(result)
    return result

#prints a 2x2 matrix in a readable way
def print_matrix(matrix):
    for row in matrix:
        print(row)
    print()

# a) Calculate the gcd of 2406 and 654 (=größter gemeinsamer Teiler/ ggT)
a = 2406    
b = 654
result = 24
array = []

temp_a = a
temp_b = b



while temp_b != 0:
    print(f"{temp_a} = {temp_a // temp_b} * {temp_b} + {temp_a % temp_b}")
    array.append((temp_a // temp_b))
    temp_a, temp_b = temp_b, temp_a % temp_b
gcd = temp_a
print(f"ggT({a}, {b}) = {gcd}")

if(result == 0):

    print("Da Ergebnis = 0, gibt es eine einfache Lösung für die Geichung")
    print(f"{a} * -{b} + {b} * {a} = {result} | : {gcd}")
    print(f"{a} * -{b // gcd} + {b} * {a // gcd} = {result // gcd}")
    exit()

print("\n")
print("Baue Matrizen für Determinantenmethode:")

matrices = []
for i in range(len(array)):
    matrix = ([array[i], 1], [1, 0])
    print_matrix(matrix)
    matrices.append(matrix)

print("Multipliziere Matrizen:")

# multiply all matrices until only one is left
result_matrix = matrices[0]
for i in range(1, len(matrices)):
    result_matrix = multiply_matrices(result_matrix, matrices[i])

print(f"Det Q = {result_matrix[0][0]} * {result_matrix[1][1]} - {result_matrix[1][0]} * {result_matrix[0][1]} = {result_matrix[0][0] * result_matrix[1][1] - result_matrix[0][1] * result_matrix[1][0]} | * {gcd}")
multiplication_factor = int(result/gcd)
print(f"{a} * {result_matrix[1][1]} + {b} * -{result_matrix[0][1]} = {gcd} | * {multiplication_factor}")
print(f"{a} * {result_matrix[1][1]} * {multiplication_factor} + {b} * -{result_matrix[0][1]} * {multiplication_factor} = {result}")
result_for_a = result_matrix[1][1] * multiplication_factor
result_for_b = result_matrix[0][1] * multiplication_factor

print(f"{a} * {result_for_a} + {b} * -{result_for_b} = {result}")
print("\n")
print(f"Allgemeine Lösung:")

print(f"{a} * -{b} + {b} * {a} = {0} | : {gcd}")
print(f"{a} * -{b // gcd} + {b} * {a // gcd} = {0 // gcd}")
print("\n")
print(f"x=p+x(klein h)")  
mod_result_for_a = result_for_a % (b // gcd)
mod_result_for_b = result_for_b % (a // gcd)

print(f"{a} * ({mod_result_for_a} + {b// gcd} * t) - {b} * ({mod_result_for_b} + {a // gcd} * t) = {result}")



