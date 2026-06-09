def list_num(l):
    l0 = []
    for i in l:
        try:
            l0.append(int(i))
        except:
            l0.append(float(i))
    return l0

row1 = int(input("Enter number of rows of matrix 1: "))
column1 = int(input("Enter number of column of matrix 1: "))

'''C1 C2 C3 C4
R1:4  4  2  1  
R2:3  2  1  0
R3:1  2  3  4
R4:3  5  2  0 .... use nested lists
'''

matrix_1 = []
for i in range(0,row1):
    matrix_1.append(list_num(input(f"R{i+1}:").split()))#

row2 = int(input("Enter number of rows of matrix 2: "))
column2 = int(input("Enter number of column of matrix 2: "))

if not column1==row2:
    print("NOT POSSIBLE")
    exit()

matrix_2 = []
for i in range(0,row2):
    matrix_2.append(list_num(input(f"R{i+1}:").split()))#

result_matrix = []#row 1 x column 2
# A[r-1][c-1] = sigma(matrix_1[r-1][j-1]*matrix_2[j-1][c-1]) for 1<=j<=row2

for r in range(1,row1+1):
    matrix_row_r = []
    for c in range(1,column2+1):
        a = 0
        for j in range(1,row2+1):
            a += matrix_1[r-1][j-1]*matrix_2[j-1][c-1]
        matrix_row_r.append(a)
    result_matrix.append(matrix_row_r)

print(result_matrix)

