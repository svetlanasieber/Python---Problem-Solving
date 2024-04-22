from collections import deque

def find_combination(p1, p2, letter):
    num1, num2 = str(p1), str(p2)
    sym1 = num1+letter
    sym2 = num2+letter
    result = [sym1, sym2]
    return result


def find_letter(p1, p2):
    return chr(p1 + p2)

seats = [str(x) for x in input().split(", ")]
pass1 = deque([int(x) for x in input().split(', ')])
pass2 = deque([int(x) for x in input().split(', ')])

taken_seats = []
counter = 0

while pass1 and pass2 and len(taken_seats) < 6:
    p1 = pass1.popleft()
    p2 = pass2.pop()

    letter = find_letter(p1, p2)
    combination = find_combination(p1, p2, letter)
    if letter not in [(x[-1]) for x in seats]:
        pass1.append(p1)
        pass2.appendleft(p2)

    elif combination[0] in taken_seats or combination[1] in taken_seats:
        continue

    else:
        if combination[0] in seats:
            taken_seats.append(combination[0])
            seats.remove(combination[0])
        if combination[1] in seats:
            taken_seats.append(combination[1])
            seats.remove(combination[1])
    counter += 1

    if len(taken_seats) == 3 or counter == 10:
        break

print(f'Seat matches: {", ".join([str(x) for x in taken_seats])}')

print(f'Rotations count: {counter}')










