game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

full_cells, winner = 0, 0
players = {1: 'X', 2: 'O'}


def line_match(game):
    if game[1][1]:  # cheking for diagonal winner and returns winner's number
        if game[1][1] == game[0][0] == game[2][2] or \
                game[1][1] == game[0][2] == game[2][0]:
            return list(players.keys())[list(players.values()).index(game[1][1])]

    for i in range(len(game)):
        if game[i][0] == game[i][1] == game[i][2] != 0:  # cheking for row winner and returns winner's number
            return list(players.keys())[list(players.values()).index(game[i][0])]
        elif game[0][i] == game[1][i] == game[2][i] != 0:  # cheking for column winner and returns winner's number
            return list(players.keys())[list(players.values()).index(game[0][i])]


def player_turn(player: int):
    global full_cells
    player_choice = ''
    while not player_choice and full_cells != len(game) ** 2:
        player_choice = input(f'Player {player}, what is Your move? (row,col): ')
        try:
            row, col = int(player_choice.split(',')[0]), int(player_choice.split(',')[1].replace(" ", ""))
            if not game[row-1][col-1]:
                game[row-1][col-1] = players[player]
                full_cells += 1
                break
            else:
                print("This position is already full")
                player_choice = ''
        except (ValueError, IndexError) as e:
            print(e)
            player_choice = ''


def draw_gameboard(game):
    for row in game:
        print(*row)


# MAIN LOOP
while True:
    player_turn(1)
    winner = line_match(game)
    if winner:
        draw_gameboard(game)
        print(f"Congratulations, Player {winner}! You win!")
        break
    draw_gameboard(game)  # draw the gameboard

    if full_cells == len(game) ** 2:
        print("It's a tie. Game over!")
        break

    player_turn(2)
    winner = line_match(game)
    if winner:
        draw_gameboard(game)
        print(f"Congratulations, Player {winner}! You win!")
        break
    draw_gameboard(game)
