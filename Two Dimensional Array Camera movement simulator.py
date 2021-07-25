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

i = 0
SEP = ' '
lines = []
while i < boardHeight:
    line = SEP.join(board[i])
    lines.append(line)
    i += 1
pretty_board = '\n'.join(lines)
print(pretty_board)


# -------
# Camera
camera_x = boardWidth // 2
camera_y = boardHeight // 2

camera_range = 1
camera_range_diameter = camera_range * 2 + 1

while True:
    try:
        cells_seen = []
        direction = input('Select direction: u: up, d: down, l: left, r: right').lower()

        if direction == 'r':
            camera_x += 1
        elif direction == 'l':
            camera_x -= 1
        elif direction == 'u':
            camera_y -= 1
        elif direction == 'd':
            camera_y += 1
        else:
            'I do not understand what you mean'

        # Sub list selector
        x_counter = 0
        chosen_x = []
        staring_x = camera_x - camera_range

        while x_counter < camera_range * 2 + 1:
            chosen_x.append(staring_x + x_counter)
            x_counter += 1

        # List selector
        y_counter = 0
        chosen_y = []
        starting_y = camera_y - camera_range

        while y_counter < camera_range * 2 + 1:
            chosen_y.append(starting_y + y_counter)
            y_counter += 1

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
        print('-------')
        print(s)

    except IndexError:
        print('sorry you ended the map, try going back')
