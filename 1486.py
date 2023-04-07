# https://www.beecrowd.com.br/judge/pt/problems/view/1486

p, n, c = map(int, input().split())

while p != 0 and n != 0 and c != 0:
    processing_points = [[] for _ in range(p)]

    for _ in range(n):
        measurements = [int(x) for x in input().split()]
        for i, measurement in enumerate(measurements):
            processing_points[i].append(measurement)

    sticks_of_interest = 0
    for processing_point in processing_points:
        stick_size = 0
        for measurement in processing_point:
            if measurement == 1:
                stick_size += 1
            
            else:
                if stick_size >= c:
                    sticks_of_interest += 1
                stick_size = 0

        if stick_size >= c:
            sticks_of_interest += 1

    print(sticks_of_interest)

    p, n, c = map(int, input().split())
