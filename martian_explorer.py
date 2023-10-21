from collections import deque

size = 6

matrix = []
my_pos = []
element = set()

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row in range(size):
    matrix.append(input().split())

    if 'E' in matrix[row]:
        my_pos = [row, matrix[row].index('E')]

direction = deque(input().split(', '))

while len(direction) != 0:
    direct = direction.popleft()

    for key, value in directions.items():
        if direct == key:
            row = my_pos[0] + value[0]
            col = my_pos[1] + value[1]

            if row == size:
                row = 0
            elif col == size:
                col = 0
            elif row == -1:
                row = 5
            elif col == -1:
                col = 5

            my_pos = [row, col]
            position = matrix[row][col]

            if position == 'R':
                print(f"Rover got broken at ({row}, {col})")
                break
            elif position == 'W':
                print(f"Water deposit found at ({row}, {col})")
                element.add('W')
            elif position == 'M':
                print(f"Metal deposit found at ({row}, {col})")
                element.add('M')
            elif position == 'C':
                print(f"Concrete deposit found at ({row}, {col})")
                element.add('C')

if len(element) == 3:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")