# https://www.beecrowd.com.br/judge/pt/problems/view/1318

n, m = map(int, input().split())

while n != 0:
    tickets = list(map(int, input().split()))

    original_tickets_count = {number: 0 for number in range(1, n + 1)}

    for ticket in tickets:
        original_tickets_count[ticket] += 1

    cloned_tickets = 0
    for count in original_tickets_count.values():
        if count > 1:
            cloned_tickets += 1

    print(cloned_tickets)

    n, m = map(int, input().split())
