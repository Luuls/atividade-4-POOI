# https://www.beecrowd.com.br/judge/pt/problems/view/1129

OPTIONS = 'ABCDE'

def count(marks, value):
    counter = 0
    indexes = []
    for i, mark in enumerate(marks):
        if mark == value:
            counter += 1
            indexes.append(i)

    return (counter, indexes)
        
while ((n := int(input())) != 0):
    for _ in range(n):
        options_readings = map(int, input().split())

        options_marks = list(map(lambda x: x <= 127, options_readings))
        total_marks, indexes = count(options_marks, True)

        if total_marks != 1:
            print('*')
        else:
            print(OPTIONS[indexes[0]])
    