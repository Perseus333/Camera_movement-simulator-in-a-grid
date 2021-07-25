import random
import numpy as np


boardHeight = int(input('Insert Height: '))
boardWidth = int(input('Insert Width: '))


def cell_content():
    content = random.randint(0, 1)
    if content == 0:
        return "O"
    else:
        return "/"


board = []
i = 0
while i < boardHeight:
    board.append([])
    j = 0
    while j < boardWidth:
        board[i].append(cell_content())
        j += 1
    i += 1


camera_x = boardWidth // 2
camera_y = boardHeight // 2

camera_range = 1
camera_range_diameter = camera_range * 2 + 1
cells_seen = []


# Sub list selector
x_counter = 0
chosen_x = []
staring_x = camera_x - camera_range

while x_counter < camera_range * 2 + 1:
    chosen_x.append(staring_x + x_counter)
    x_counter += 1
print(chosen_x)


# List selector
y_counter = 0
chosen_y = []
starting_y = camera_y - camera_range

while y_counter < camera_range * 2 + 1:
    chosen_y.append(starting_y + y_counter)
    y_counter += 1
print(chosen_y)

for y in chosen_y:
    selected_y = y
    for x in chosen_x:
        selected_x = x
        cells_seen.append(board[selected_y][selected_x])

final_list = []
two_split = np.array_split(cells_seen, camera_range_diameter)
for array in two_split:
    final_list.append(list(array))

SEP = ' '
i = 0
lines = []
while i < camera_range_diameter:
    line = SEP.join(final_list[i])
    lines.append(line)
    i += 1
s = '\n'.join(lines)

print(s)
