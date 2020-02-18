# a game of x and o

# a function for displaying the board with notes
def display(board, note_):
    print("|===========|")
    for row in range(0, 9, 3):
        print("| ", board[row], " | ", board[row+1], " | ", board[row+2], " |", sep="")
        print("|===========|")
    print(note_)
    if result == 0:
        print("press 'i' for instruction, 'b' to revert a move and 'q' to quit", sep="\n")


# a function for modifying the state of the game
def new_board():
    new_state = state[move].copy()
    new_state[decision] = player
    return new_state


# a function for checking if anybody has won
def checking():
    cases = [
        state[move][0:3],
        state[move][3:6],
        state[move][6:9],
        state[move][0::3],
        state[move][1::3],
        state[move][2::3],
        state[move][0::4],
        state[move][2:7:2],
    ]
    for element in cases:
        if element == ["x", "x", "x"] or element == ["o", "o", "o"]:
            return 1
    return 0


# a function for checking if the game can result in a win for any player
def checking_ahead():
    cases = [
        state[move][0:3],
        state[move][3:6],
        state[move][6:9],
        state[move][0::3],
        state[move][1::3],
        state[move][2::3],
        state[move][0::4],
        state[move][2:7:2],
    ]
    for element in cases:
        if not ("x" in element and "o" in element):
            if move == 8 and "o" in element:
                pass
            elif move == 7 and element.count(" ") == 2:
                pass
            elif move == 6 and element.count("o") == 1 or element.count(" ") == 3:
                pass
            else:
                return 0
    return 2


# a function for displaying the instruction
def instruction():
    numbers = []
    for element in range(1, 10):
        if state[move][element-1] == " ":
            numbers.append(element)
        else:
            numbers.append(state[move][element-1])
    note_ = "type in one of the visible numbers to play"
    display(numbers, note_)


# defining basic variables
state = [[" ", " ", " ", " ", " ", " ", " ", " ", " "]]     # a list of states of the game
move = 0                                                    # move counter
result = 0                                                  # result holder
note = ""                                                   # note holder for displaying the board
manual = False                                              # a flag for displaying normally or with instructions


while True:

    # assigning player
    player = "x" if move % 2 == 0 else "o"

    # displaying the board and taking input
    if manual is False:
        if move == 0:
            display("123456789", note)
        else:
            display(state[move], note)
        note = ""
    else:
        manual = False
    decision = input(f"'{player}' to play:").lower()

    # checking the input and taking proper actions and modifying the board
    if decision == "q":
        print("\n\n\n\nthanks for playing :)\n\n\n\n")
        break
    elif decision == "b":
        if move == 0:
            note = "there is nothing to revert!"
            continue
        else:
            state.pop()
            move -= 1
    elif decision == "i":
        instruction()
        manual = True
        continue
    else:
        try:
            decision = int(decision)-1
        except ValueError:
            note = "that is not a number"
            continue

    if decision > 8 or decision < 0:
        note = "that is not a number from 1 to 9!"
        continue
    elif state[move][decision] != " ":
        note = "this place is already taken"
        continue
    else:
        state.append(new_board())
        move += 1

    # checking the result of the game and working accordingly
    if move > 4:
        result = checking()
    if result == 0 and move > 5:
        result = checking_ahead()
    if result != 0:
        if result == 2:
            note = "A TIE!!!"
        else:
            note = f"'{player}' won!!!"
        display(state[move], note)
        note = ""
        play_again = input("press any key to play again or 'q' to quit\n").lower
        if play_again == "q":
            print("\n\n\n\nthanks for playing :)\n\n\n\n")
            break
        else:
            state = [[" ", " ", " ", " ", " ", " ", " ", " ", " "]]
            move = 0
            result = 0
