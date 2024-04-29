matriks = [[98, 88, 78], [77, 78, 79], [66, 67, 68], [32, 33, 31]]

result= [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

for row in range(len(matriks)):
    for column in range(len(matriks[0])):
        result[column][row] = matriks[row][column]

for r in result:
    print(r)