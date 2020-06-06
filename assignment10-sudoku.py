sudoku = [
    [0, 0, 0, 0, 6, 4, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 3, 9, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 2, 0, 6, 0],
    [0, 8, 0, 4, 0, 0, 0, 0, 0],
    [3, 5, 0, 6, 0, 0, 0, 7, 0],
    [0, 0, 2, 0, 0, 0, 1, 0, 3],
    [0, 0, 1, 0, 5, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 7, 0, 0]
]

for i in range(len(sudoku) + 1):
    if i == 0 or i == 3 or i == 6:
        for k in range(29):
            if k == 28: print('-')
            elif k % 2: print('-', end=' ')
        for j in range(len(sudoku[i])):
            if j == 8: print(sudoku[i][j])
            elif j == 3 or j == 6: print('|', sudoku[i][j], end='  ')
            else: print(sudoku[i][j], end='  ')
    elif i == 9:
        for k in range(29):
            if k == 28: print('-')
            elif k % 2: print('-', end=' ')
    else:
        for j in range(len(sudoku[i])):
            if j == 8: print(sudoku[i][j])
            elif j == 3 or j == 6: print('|', sudoku[i][j], end='  ')
            else: print(sudoku[i][j], end='  ')
