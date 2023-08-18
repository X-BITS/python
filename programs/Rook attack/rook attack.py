def sum_rows(A, ROWS):
    for i in range (len(A)):
        sum = 0
        for j in range (len(A[i])):
            sum += A[i][j]
        ROWS.append(sum)
    
    return ROWS

def sum_cols(A, COLS):
    for j in range (len(A[0])):
        sum = 0
        for i in range (len(A)):
            sum += A[i][j]
        COLS.append(sum)
    
    return COLS

def rook_matrix(A, ROWS, COLS, ROOK):
    line = []
    for i in range (len(A)):
        line = []
        for j in range (len(A[i])):
            line.append(ROWS[i] + COLS[j] - ( A[i][j] * 2))
        ROOK.append(line)
    print("ROOK MATRIX:")
    for r in ROOK:
        for c in r:
            print(c, end = " ")
        print()            
    return ROOK
   
def rook_attack(ROOK):
    max = 0
    row = 0
    col = 0
    for i in range (len(ROOK)):
        for j in range (len(ROOK[i])):
            if ROOK[i][j] > max:
                max = ROOK[i][j]
                row = i + 1
                col = j + 1
    return row, col
n,m =  map(int, input().split())
A    = []
ROWS = []
COLS = []
ROOK = []

for i in range(n):
    A.append(list(map(int, input().split())))
ROWS = sum_rows(A, ROWS)
COLS = sum_cols(A, COLS)
ROOK = rook_matrix(A, ROWS, COLS, ROOK)
coordinates = rook_attack(ROOK)
print("ROOK ATTAK POSITION IS:")
print(coordinates[0], coordinates[1])
