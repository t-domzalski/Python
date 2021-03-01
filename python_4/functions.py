import random
from datetime import datetime

tabli =[["-", "-", "-"],
        ["-", "-", "-"],
        ["-", "-", "-"]]

# Wstawianie X przez gracza

def game_board_player(game_map, symbol="X", just_display=False):
    while True:
        try:
            row = int(input("Row: "))
            column = int(input("Column: "))

            if not just_display and game_map[row][
                column] == "-":
                game_map[row][column] = symbol
                print("    0    1    2")

                for count, row in enumerate(tabli):
                    print(count, row)
                return game_map
                break

            else:
                print("Try somwhere else: ")
                continue
        except ValueError:
            print("nope, again")

        except IndexError:
            print("nope, next time choose a possible row/column")


# Wstawianie O przez komputer

def game_board_comp(game_map, symbol = "O"):
    while True:
        row = random.randint(0, 2)
        column = random.randint(0, 2)

        if game_map[row][column] == "-":
            game_map[row][column] = symbol
            print("    0    1    2")

            for count, row in enumerate(tabli):
                print(count, row)
            return game_map
            break

# Sprawdzanie wygranych

def check_if_win(current_game):  # horizontal win

    for row in tabli:
        if row.count(row[0]) == len(row) and row[0] != '-':
            print(f"{row[0]} is the winner!")
            return f"{row[0]} is the winner!"

    for col in range(len(tabli)):  # vertical
        columns = []
        for row in tabli:
            columns.append(row[col])

        if columns.count(columns[0]) == len(columns) and columns[0] != '-':
            print(f"{columns[0]} is the winner!")
            return f"{columns[0]} is the winner!"

    diagonal = []
    for col, row in enumerate(reversed(range(len(tabli)))):
        diagonal.append(tabli[row][col])

    if diagonal.count(diagonal[0]) == len(diagonal) and diagonal[0] != '-':
        print(f"{diagonal[0]} is the winner!")
        return f"{diagonal[0]} is the winner!"

    diagonal = []
    for idx in range(len(tabli)):
        diagonal.append(tabli[idx][idx])

    if diagonal.count(diagonal[0]) == len(diagonal) and diagonal[0] != '-':
        print(f"{diagonal[0]} is the winner!")
        return f"{diagonal[0]} is the winner!"

    draw = sum(tabli, [])
    if all(e != "-" for e in draw):
        return "ain't no badass over here!"

# Funkcje obsługujące tworzenie loguf


def save_name():
    return str(datetime.today())


def save_game(game_map, savename):
    with open("save" + savename + ".txt", "a") as file:
        file.write(f"{game_map}\n")


def save_game_end(game_map, savename):
    with open("save" + savename + ".txt", "a") as file:
        file.write(f"Game is finnished: {game_map}\n {winner}")