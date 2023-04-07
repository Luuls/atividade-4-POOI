# https://www.beecrowd.com.br/judge/pt/problems/view/1877

n, k = map(int, input().split())

tower_heights = list(map(int, input().split()))

peaks = 0
valleys = 0
last_was_peak = False
for current_tower, next_tower in zip(tower_heights, tower_heights[1:]):
    if last_was_peak:
        if next_tower > current_tower:
            valleys += 1
            last_was_peak = False
            
    else:
        if next_tower < current_tower:
            peaks += 1
            last_was_peak = True

if peaks == k and valleys == k - 1:
    print('beautiful')

else:
    print('ugly')
            