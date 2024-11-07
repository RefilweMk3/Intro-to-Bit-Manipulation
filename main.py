def circuit_output(A, B, C):
    A1 = A and B
    A2 = B and C
    A3 = A and C
    
    Q = A1 or A2 or A3
    
    return Q
A = 1
B = 1
C = 0
output = circuit_output(A, B, C)
print(f"The output of the circuit is: {output}")
