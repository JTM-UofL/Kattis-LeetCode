def printb(A):
    for i in range(4):
        for j in range(4):
            print(A[i][j], end=" ")
        print("", end="\n")

def transpose(A, b):
    if b == "r" or b == "l":
        rotated_arr = [[0 for _ in range(4)] for _ in range(4)]
        rotated_arr = A[::-1]
        return rotated_arr
    elif b == "u":
        rotated_arr = [[0 for _ in range(4)] for _ in range(4)]
        for i in range(4):
            for j in range(4):
                rotated_arr[3 - j][i] = A[i][j]
        return rotated_arr
    elif b == "d":
        rotated_arr = [[0 for _ in range(4)] for _ in range(4)]
        for i in range(4):
            for j in range(4):
                rotated_arr[i][3 - j] = A[j][i]
        return rotated_arr
    else:
        print("Non acceptable transposition detected\n")
        exit(1)


def shiftl(A, i, j):
    if j <= 0:
        print(quit)
        quit()
    j -= 1
    while j < 3:
        A[i][j] = A[i][j+1]
        j += 1
    A[i][j] = 0

def lefthelper(A, i):
    j = 0
    flag = 0
    for j in range(3, 0, -1):
            if board[i][j - 1] == 0 and board[i][j] != 0:
                shiftl(A, i, j)
                flag = 0
            elif board[i][j] == board[i][j - 1] and flag == 0:
                board[i][j] = 0
                board[i][j - 1] *= 2
                shiftl(A, i, j+1)
                flag = 1
            else:
                flag == 0
def left(A):
    for i in range(4):
        lefthelper(A, i)

def right(A):
    A = transpose(A, "r")
    left(A)
    A = transpose(A, "l")

def down(A):
    A = transpose(A, "d")
    left(A)
    A = transpose(A, "u")

def up(A):
    A = transpose(A, "u")
    left(A)
    A = transpose(A, "d")

board = [list(map(int, input().split())) for x in range(4)]
printb(board)
print("\n")
board = transpose(board, "r")
printb(board)
