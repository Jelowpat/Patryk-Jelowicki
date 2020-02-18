from Projects.tic_tac_toe.classes_board import Board
import os


def display(game, note, result=False):
    printing = []
    if note == "type in one of the visible numbers to play" or game.move == 0:  # a print for instruction
        if not note:
            note = "type in one of the visible numbers to play"
        for x in range(1, 10):
            if game.elements[x - 1] == " ":
                printing.append(x)
            else:
                printing.append(game.elements[x - 1])
    else:
        printing = [x for x in game.elements]  # a print for normal display
    print("|===========|")
    for row in range(0, 9, 3):
        print("| ", printing[row], " | ", printing[row + 1], " | ", printing[row + 2], " |", sep="")
        print("|===========|")
    print(note)
    if result is False:
        print("press 'i' for instruction, 'b' to revert a move and 'q' to quit", )


def option(game):
    if decision == "q":
        print("\n\n\n\nthanks for playing :)\n\n\n\n")
        exit()
    elif decision == "b":
        return game.undo()
    elif decision == "r":
        return game.redo()
    elif decision == "i":
        return False, "type in one of the visible numbers to play"
    else:
        return True, ""


clear = lambda: os.system('cls')
game = Board()
note = ""

while True:

    display(game, note)
    decision = input(f"'{game.player}' to play:").lower()
    clear()
    valid, note = option(game)
    if valid:
        valid, note = game.insert(decision)
    if not valid:
        continue

    result = game.checking()
    if result:
        if result == "TIE":
            note = "A TIE!!!"
        else:
            note = f"'{result}' won!!!"
        display(game, note, result=True)
        play_again = input("press any key to play again or 'q' to quit\n").lower
        clear()
        if play_again == "q":
            print("\n\n\n\nthanks for playing :)\n\n\n\n")
            break
        else:
            game.new_game()
            note = ""
