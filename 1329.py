# https://www.beecrowd.com.br/judge/pt/problems/view/1329

while (n := int(input())) != 0:
    mary, john = 0, 0
    
    results = map(int, input().split())
    
    for result in results:
        if result == 0:
            mary += 1
        else:
            john += 1

    print(f'Mary won {mary} times and John won {john} times')
