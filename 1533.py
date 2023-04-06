# https://www.beecrowd.com.br/judge/pt/problems/view/1533

while (n := int(input())) != 0:
    suspects = list(map(int, input().split()))

    most_suspect = suspects[0]

    second_most_suspect = suspects[0]
    index_second_most = 0

    for suspect in suspects[1:]:
        if suspect > most_suspect:
            most_suspect = suspect

    if second_most_suspect == most_suspect:
        second_most_suspect = suspects[1]
        index_second_most = 1

    for i, suspect in enumerate(suspects):
        if second_most_suspect < suspect and suspect < most_suspect:
            second_most_suspect = suspect
            index_second_most = i

    print(index_second_most + 1)