def create_grid(input_cells):
    print('---------')
    print('| ', end='')
    for i in range(3):
        print(input_cells[i] + " ", end="")
    print("|")
    print('| ', end='')
    for i in range(3, 6):
        print(input_cells[i] + " ", end="")
    print("|")
    print('| ', end='')
    for i in range(6, 9):
        print(input_cells[i] + " ", end="")
    print("|")
    print('---------')
    

def empty_cells(input_cells):
    is_empty = True
    for i in range(9):
        if input_cells[i] in ('X', 'O'):
            is_empty = False
            break
    return is_empty


def filled_cells(input_cells):
    is_full = True
    for i in range(9):
        if input_cells[i] not in ('X', 'O'):
            is_full = False
            break
    return is_full


def x_wins(input_cells):
    wins = False
    if input_cells[0] == 'X' and input_cells[1] == 'X' and input_cells[2] == 'X':
        wins = True
    if input_cells[3] == 'X' and input_cells[4] == 'X' and input_cells[5] == 'X':
        wins = True
    if input_cells[6] == 'X' and input_cells[7] == 'X' and input_cells[8] == 'X':
        wins = True
    if input_cells[0] == 'X' and input_cells[3] == 'X' and input_cells[6] == 'X':
        wins = True
    if input_cells[1] == 'X' and input_cells[4] == 'X' and input_cells[7] == 'X':
        wins = True
    if input_cells[2] == 'X' and input_cells[5] == 'X' and input_cells[8] == 'X':
        wins = True
    if input_cells[0] == 'X' and input_cells[4] == 'X' and input_cells[8] == 'X':
        wins = True
    if input_cells[2] == 'X' and input_cells[4] == 'X' and input_cells[6] == 'X':
        wins = True
    return wins


def o_wins(input_cells):
    wins = False
    if input_cells[0] == 'O' and input_cells[1] == 'O' and input_cells[2] == 'O':
        wins = True
    if input_cells[3] == 'O' and input_cells[4] == 'O' and input_cells[5] == 'O':
        wins = True
    if input_cells[6] == 'O' and input_cells[7] == 'O' and input_cells[8] == 'O':
        wins = True
    if input_cells[0] == 'O' and input_cells[3] == 'O' and input_cells[6] == 'O':
        wins = True
    if input_cells[1] == 'O' and input_cells[4] == 'O' and input_cells[7] == 'O':
        wins = True
    if input_cells[2] == 'O' and input_cells[5] == 'O' and input_cells[8] == 'O':
        wins = True
    if input_cells[0] == 'O' and input_cells[4] == 'O' and input_cells[8] == 'O':
        wins = True
    if input_cells[2] == 'O' and input_cells[4] == 'O' and input_cells[6] == 'O':
        wins = True
    return wins
    

def display_results(input_cells):
    count_x = 0
    count_o = 0
    for i in range(9):
        if input_cells[i] == 'X':
            count_x += 1
        elif input_cells[i] == 'O':
            count_o += 1
    if abs(count_x - count_o) > 1:
        print('Impossible')
        return True
    else:
        if x_wins(input_cells) and o_wins(input_cells):
            print('Impossible')
            return True
        else:
            if not x_wins(input_cells) and not o_wins(input_cells) and filled_cells(input_cells):
                print('Draw')
                return True
            elif x_wins(input_cells):
                print('X wins')
                return True
            elif o_wins(input_cells):
                print('O wins')
                return True
            else:
                return False


def valid_coordinates(input_cords):
    try:
        if 1 <= int(input_cords[0]) <= 3 and 1 <= int(input_cords[1]) <= 3:
            return True
        else:
            print('Coordinates should be from 1 to 3!')
            return False
    except ValueError:
        print('You should enter numbers!')
        return False


def not_occupied(input_cells, input_cords):
    i = 0
    if int(input_cords[0]) == 2:
        i = 3
    elif int(input_cords[0]) == 3:
        i = 6
    if int(input_cords[1]) == 2:
        i += 1
    elif int(input_cords[1]) == 3:
        i += 2
    if input_cells[i] not in ('X', 'O'):
        return True
    else:
        print('This cell is occupied! Choose another one!')
        return False


def mark_coordinates(input_cells, input_cords, mark):
    i = 0
    if int(input_cords[0]) == 2:
        i = 3
    elif int(input_cords[0]) == 3:
        i = 6
    if int(input_cords[1]) == 2:
        i += 1
    elif int(input_cords[1]) == 3:
        i += 2
    return_list = []
    for count, element in enumerate(input_cells):
        if count == i:
            return_list.append(mark)
        else:
            return_list.append(element)
    return "".join(return_list)

    
if __name__ == '__main__':
    input_cells_list = "         "
    create_grid(input_cells_list)
    initial = 'X'
    while True:
        print('Enter the coordinates: ', end='')
        input_cord_list = input().split()
        if valid_coordinates(input_cord_list):
            if not_occupied(input_cells_list, input_cord_list):
                input_cells_list = mark_coordinates(input_cells_list, input_cord_list, initial)
                create_grid(input_cells_list)
                if display_results(input_cells_list):
                    break
                else:
                    if initial == 'X':
                        initial = 'O'
                    else:
                        initial = 'X'
