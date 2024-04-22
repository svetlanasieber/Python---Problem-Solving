def next_possition(row, col, direction):
    poss_dict = {'right':lambda r, c:[r, col + 1], 'left':lambda r, c:[r, col - 1],
                 'down':lambda r, c:[r + 1, col], 'up':lambda r, c:[r - 1, col]}
    return poss_dict[direction](row, col)

def in_matrix(row, col):
    return 0 <= row < rows and 0 <= col < cols

def new_possition(row, col, rows, cols):
    if row < 0:
        row = rows - 1
    if row >= rows:
        row = 0
    if col < 0:
        col = cols - 1
    if col >= cols:
        col = 0
    return row, col

rows, cols = [int(x) for x in input().split(', ')]
rev_dict = {'D':'Christmas decorations', 'G':'Gifts', 'C':'Cookies'}
item_dict = {'Christmas decorations':0, 'Gifts':0, 'Cookies':0}
result = ""
item_list = ['D', 'G', 'C']
item_counter = 0
p_row, p_col = 0, 0
matrix = []
for row in range(rows):
    temp_row = input().split(' ')
    for col in range(cols):
        if temp_row[col] == 'Y':
            p_row, p_col = row, col
        if temp_row[col] in item_list:
            item_counter += 1
    matrix.append(temp_row)
while item_counter > 0:
    command = input()
    if command == "End":
        break
    else:
        command = command.split("-")
        direction, steps = command[0], int(command[1])
        for _ in range(steps):
            matrix[p_row][p_col] = "x"
            p_row, p_col = next_possition(p_row, p_col, direction)
            if not in_matrix(p_row, p_col):
                p_row, p_col = new_possition(p_row, p_col, rows, cols)
            if matrix[p_row][p_col] in item_list:
                some_item = matrix[p_row][p_col]
                count_item = rev_dict[some_item]
                item_dict[count_item] += 1
                item_counter -= 1
            if item_counter == 0:
                print("Merry Christmas!")
                break
            matrix[p_row][p_col] = "x"

matrix[p_row][p_col] = "Y"
print("You've collected:")
for k, v in item_dict.items():
    result += f"- {v} {k}\n"
for row in matrix:
    result += f'{" ".join(row)}\n'
print(result)

