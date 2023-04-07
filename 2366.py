# https://www.beecrowd.com.br/judge/pt/problems/view/2366

n, m = map(int, input().split())

absolute_positions = list(map(int, input().split()))
absolute_positions.append(42195)

finished = True

for current_position, next_position in zip(absolute_positions, absolute_positions[1:]):
    if next_position - current_position > m:
        finished = False
        break

if finished:
    print('S')

else:
    print('N')
