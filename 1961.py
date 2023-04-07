# https://www.beecrowd.com.br/judge/pt/problems/view/1961

p, n = map(int, input().split())

heights = list(map(int, input().split()))

won = True
for current_height, next_height in zip(heights, heights[1:]):
    if abs(next_height - current_height) > p:
        won = False
        
if won:
    print('YOU WIN')

else:
    print('GAME OVER')
        