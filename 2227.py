a, v = map(int, input().split())
test_number = 1

while a != 0 and v != 0:
    
    airports_traffics = [0] * a

    for _ in range(v):
        departure, arrival = map(int, input().split())
        airports_traffics[departure - 1] += 1
        airports_traffics[arrival - 1] += 1

    most_traffic = airports_traffics[0]
    for traffic in airports_traffics[1:]:
        if traffic > most_traffic:
            most_traffic = traffic

    airports_with_most_traffic = []
    for index, traffic in enumerate(airports_traffics):
        if traffic == most_traffic:
            airports_with_most_traffic.append(index)

    print(f'Teste {test_number}')
    for airport in airports_with_most_traffic:
        print(airport + 1, end=' ')
    print('\n')
    
    test_number += 1

    a, v = map(int, input().split())
