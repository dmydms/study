n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
count = []

for row in range(0, n - 7):
    for col in range(0, m - 7): 
        n0 = 0
        n1 = 0
        for r in range(row, row + 8):
            for c in range(col, col + 8):
                if (r + c) % 2 == 0:
                    if board[r][c] != 'W':
                        n0 += 1
                    if board[r][c] != 'B':
                        n1 += 1
                else:
                    if board[r][c] != 'B':
                        n0 += 1
                    if board[r][c] != 'W':
                        n1 += 1
        count.append(min(n0, n1))

print(min(count))