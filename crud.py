size = 6
matrix = []

for row in range(size):
    matrix.append(input().split())

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

my_pos_str = input()
my_pos = [int(x) for x in my_pos_str if x.isdigit()]

while True:
    command, *element = input().split(', ')

    if command == 'Stop':
        break

    if command == 'Create':
        direction = element[0]
        row = my_pos[0] + directions[direction][0]
        col = my_pos[1] + directions[direction][1]
        my_pos = [row, col]
        position = matrix[row][col]
        if position == '.':
            matrix[row][col] = element[1]
    elif command == 'Update':
        direction = element[0]
        row = my_pos[0] + directions[direction][0]
        col = my_pos[1] + directions[direction][1]
        my_pos = [row, col]
        position = matrix[row][col]
        if position != '.':
            matrix[row][col] = element[1]
    elif command == 'Delete':
        direction = element[0]
        row = my_pos[0] + directions[direction][0]
        col = my_pos[1] + directions[direction][1]
        my_pos = [row, col]
        position = matrix[row][col]
        if position != '.':
            matrix[row][col] = '.'
    elif command == 'Read':
        direction = element[0]
        row = my_pos[0] + directions[direction][0]
        col = my_pos[1] + directions[direction][1]
        my_pos = [row, col]
        position = matrix[row][col]
        if position != '.':
            print(matrix[row][col])


[print(*row) for row in matrix]