queens_board = []
n = 100001
def Create_Solution():
    for i in range(n):
        if i%2 == 1:
            queens_board.append(i)
    for i in range(n):
        if i%2 == 0:
            queens_board.append(i)
def check():
    for i in range (n):
        for j in range(i):
            if (queens_board[j] == queens_board[i] ) or (abs(queens_board[i]-queens_board[j]) == abs(i-j)):
                return False
    return True
def main():
    Create_Solution()
    print (queens_board)
main()