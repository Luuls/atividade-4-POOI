# https://www.beecrowd.com.br/judge/pt/problems/view/1366

while (n := int(input())) != 0:
    sticks_amount = [int(input.split()[1]) for _ in range(n)]

    sum_of_max_rectangles = 0
    for amount in sticks_amount:
        sum_of_max_rectangles += amount // 2

    max_amount_rectangles = sum_of_max_rectangles // 2
    print(max_amount_rectangles)
