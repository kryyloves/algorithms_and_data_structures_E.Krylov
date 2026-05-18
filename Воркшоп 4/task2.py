mat = [
    [0, 0, 0],
    [0, 1, 0],
    [1, 1, 1]
]

m = len(mat)
n = len(mat[0])
res = []

for i in range(m):
    new_row = []
    for j in range(n):
        if mat[i][j] == 0:
            new_row.append(0)
        else:
            min_dist = 999999
            for r in range(m):
                for c in range(n):
                    if mat[r][c] == 0:
                        dist = abs(i - r) + abs(j - c)
                        if dist < min_dist:
                            min_dist = dist
            new_row.append(min_dist)
    res.append(new_row)

for row in res:
    print(row)