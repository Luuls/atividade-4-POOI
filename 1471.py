# https://www.beecrowd.com.br/judge/pt/problems/view/1471

while True:
    try:
        n, r = map(int, input().split())

        ids = set(range(1, n + 1))
        returned = set(map(int, input().split()))
        not_returned = list(ids.difference(returned))
        not_returned.sort()

        if n == r:
            print('*')

        else:
            for volunteers in not_returned:
                print(volunteers, end=' ')
            
            print('')
            
    except EOFError:
        break