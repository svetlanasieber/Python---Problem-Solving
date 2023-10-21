from collections import deque

places_in_fly = [x for x in input().split(', ')]  # this is str for matching
first_line = deque(map(int, input().split(', ')))
second_line = list(map(int, input().split(', ')))

seat_matches = []
count = 0

while len(seat_matches) < 3:
    if count == 10:
        break
    first_num = first_line.popleft()
    second_num = second_line.pop()
    sum_numbers = chr(first_num + second_num)
    first_combo = str(first_num) + sum_numbers
    second_combo = str(second_num) + sum_numbers
    count += 1

    if first_combo in places_in_fly and first_combo not in seat_matches:
        seat_matches.append(first_combo)
    elif second_combo in places_in_fly and second_combo not in seat_matches:
        seat_matches.append(second_combo)
    else:
        first_line.append(first_num)
        second_line.insert(0, second_num)

print(f'Seat matches: {", ".join(seat_matches)}\nRotations count: {count}')