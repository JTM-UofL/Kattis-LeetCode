
def printb(A):
    for i in range(4):
        for j in range(4):
            print(A[i][j], end=" ")
        print("", end="\n")

def transpose(A, b):
    if b == "r" or b == "l":
        for i in range(4):
            A[i].reverse()
    elif b == "u":
        B = A[:][:]
        for i in range(4, 0, 1):
            for j in range(4, 0, 1):
                u = A[j][i]
                B[i][j] = u
        A = B

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
    transpose(A, "r")
    for i in range(4):
        lefthelper(A, i)
    transpose(A, "l")

#def down(A):
#
# def down helper(A, i):
#
def up(A):
    transpose(A, "u")
    for i in range(4):
        lefthelper(A,i)
    transpose(A, "d")
# def uphelper(A, i):

board = [list(map(int, input().split())) for x in range(4)]
printb(board)
print("\n")
transpose(board, "u")
printb(board)
