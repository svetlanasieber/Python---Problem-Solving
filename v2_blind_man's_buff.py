rows, columns = input().split()
matrix = []
my_pos = []

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}
opponents_in_matrix = 0
for row in range(int(rows)):
    matrix.append(input().split())

    if 'B' in matrix[row]:
        my_pos = [row, matrix[row].index('B')]

for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        current_element = matrix[row][col]
        if current_element == 'P':
            opponents_in_matrix += 1

touched_opponents = 0
moves_made = 0

while True:
    direction = input()

    if direction == "Finish":
        break
    if touched_opponents == opponents_in_matrix:
        break

    row = my_pos[0] + directions[direction][0]
    col = my_pos[1] + directions[direction][1]

    if not (0 <= row < int(rows) and 0 <= col < int(columns)):
        row = my_pos[0]
        col = my_pos[1]
    elif matrix[row][col] == 'O':
        row = my_pos[0]
        col = my_pos[1]
    else:
        my_pos = [row, col]
        position = matrix[row][col]
        if position == 'P':
            touched_opponents += 1
            moves_made += 1
            matrix[row][col] = '-'
        else:
            moves_made += 1

print("Game over!")
print(f"Touched opponents: {touched_opponents} Moves made: {moves_made}")