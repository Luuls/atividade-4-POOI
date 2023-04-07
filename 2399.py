# https://www.beecrowd.com.br/judge/pt/problems/view/2399

n = int(input())

table = [[int(input()), 0] for _ in range(n)]

if len(table) == 1:
    if table[0][0] == 1:
        table[0][1] += 1
else:       
    for edge in [0, -1]:
        if table[edge][0] == 1:
            table[edge][1] += 1

    if table[0 + 1][0] == 1:
        table[0][1] += 1

    if table[-1 - 1][0] == 1:
        table[-1][1] += 1

    for left, middle, right in zip(table, table[1:], table[2:]):
        if middle[0] == 1:
            middle[1] += 1
        
        if left[0] == 1:
            middle[1] += 1

        if right[0] == 1:
            middle[1] += 1

for masked_cell in table:
    print(masked_cell[1])
