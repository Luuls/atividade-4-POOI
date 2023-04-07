# https://www.beecrowd.com.br/judge/pt/problems/view/1796

q = int(input())

votes = map(int, input().split())

agreed = 0
disagreed = 0

for vote in votes:
    if vote == 0:
        agreed += 1
    
    else:
        disagreed += 1

if agreed > disagreed:
    print('Y')

else:
    print('N')
    