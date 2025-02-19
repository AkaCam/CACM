cycle_lengths = {}

def calculate_cycle_length(number):
    if number in cycle_lengths:
        return cycle_lengths[number]

    if number <= 1:
        return 1

    if number % 2 == 1:
        next_number = 3 * number + 1
    else:
        next_number = number // 2

    cycle_lengths[number] = calculate_cycle_length(next_number) + 1
    return cycle_lengths[number]

while True:
    try:
        start, end = map(int, input().split())
    except EOFError:
        break

    max_cycle_length = 0
    for number in range(min(start, end), max(start, end) + 1):
        cycle_length = calculate_cycle_length(number)
        
        if cycle_length > max_cycle_length:
            max_cycle_length = cycle_length

    print(start, end, max_cycle_length)