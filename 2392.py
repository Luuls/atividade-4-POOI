# https://www.beecrowd.com.br/judge/pt/problems/view/2392

n, m = map(int, input().split())

frogs_jump_distance = [(p, d) for p, d in [map(int, input().split()) for _ in range(m)]]

rocks_markup = [0] * n
for frog in frogs_jump_distance:
    position = frog[0] 
    while position >= 1:
        rocks_markup[position - 1] = 1
        position -= frog[1]

    position = frog[0] + frog[1]
    while position <= n:
        rocks_markup[position - 1] = 1
        position += frog[1]

for rock in rocks_markup:
    print(rock)

