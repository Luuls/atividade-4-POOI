n, m = map(int, input().split())

rocks_markup = [0] * n
frogs_jump_distance = {}

for _ in range(m):
    p, d = map(int, input().split())
    frogs_jump_distance[p] = d

for frog_position, distance in frogs_jump_distance.items():
    rocks_markup[frog_position - 1] = 1

    position = frog_position 
    while position - distance >= 1:
        position -= distance
        rocks_markup[position - 1] = 1

    position = frog_position 
    while position + distance <= n:
        position += distance
        rocks_markup[position - 1] = 1

for rock in rocks_markup:
    print(rock)

