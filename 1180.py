# https://www.beecrowd.com.br/judge/pt/problems/view/1180

n = int(input())

numbers = map(int, input().split())

smallest = next(numbers)
index = 0
for i, number in enumerate(numbers, 1):
    if number < smallest:
        smallest = number
        index = i
    
print(f'Menor valor: {smallest}')
print(f'Posicao: {index}')