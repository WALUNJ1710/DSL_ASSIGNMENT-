result = [[0,0,0], 
        [0,0,0], 
        [0,0,0]] 

X= [[1,2,3],
    [4 ,5,6],
    [7 ,8,9]]
 
Y = [[9,8,7],
    [6,5,4],
    [3,2,1]]
print("X=",X)
print("Y=",Y)
# Addition of matrix 

for i in range(len(X)):    
    for j in range(len(X[0])): 
        result[i][j] = X[i][j] + Y[i][j] 
print("\nAddition of two Matrices:\n")  
for results in result: 
    print(results)

# Subtraction of matrix 

for i in range(len(X)):    
    for j in range(len(X[0])): 
        result[i][j] = X[i][j] - Y[i][j] 
print("\nSubtraction of two Matrices:\n")  
for results in result: 
    print(results)

# Multiplication of matrix 

for i in range(len(X)):  
    for j in range(len(Y[0])):  
        for k in range(len(Y)): 
            result[i][j] += X[i][k] * Y[k][j] 
print("\nMultiplication of two Matrices:\n")  
for results in result: 
    print(results)

# Transpose of matrix 

A = [ [1, 0, 0, 1], 
      [2, 0, 0, 2], 
      [3, 0, 0, 3], 
      [4, 0, 0, 4]]
print("A=",A)    
for i in range(4): 
    for j in range(i+1, 4): 
        A[i][j], A[j][i] = A[j][i], A[i][j] 
print("\nMultiplication of two Matrices:\n")
for i in range(4):
  print(A[i])
