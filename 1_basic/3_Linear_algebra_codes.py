## 선형대수
# zip 을 사용하여 vector 계산하기
u = [2, 2]
v = [2, 3]
z = [3, 5]

result = [sum(t) for t in zip(u, v, z)] # 같은 인덱스 값을 뽑음
print(result)


# Scalar-Vector product
u = [1, 2, 3]
v = [4, 5, 6]
alpha = 5

result = [5*sum(z) for z in zip(u, v)]
print(result)


# Matrix addition
# zip(matrix_a,matrix_b) -> ([3,6], [5,8])
# zip(*t) -> [3,6]
#            [5,8]
# 열끼리 합
matrix_a  = [[3, 6], [4, 5]]
matrix_b  = [[5, 8], [6, 7]]

result = [[sum(row) for row in zip(*t)] for t in zip(matrix_a, matrix_b)]

print(result)


# Scalar-Matrix Product
matrix_a = [[3, 6], [4, 5]]
alpha = 4
result = [[alpha * element for element in t] for t in matrix_a]

print(result)


# Matrix Transpose
matrix_a = [[1, 2, 3], [4, 5, 6]]
result = [[element for element in t] for t in zip(*matrix_a)]

print(result)


# Matrix Product
matrix_a = [[1, 1, 2], [2, 1, 1]]
matrix_b = [[1, 1], [2, 1], [1, 3]]
result = [[sum(a * b for a, b in zip(row_a, column_b))
        for column_b in zip(*matrix_b)] for row_a in matrix_a]
print(result)