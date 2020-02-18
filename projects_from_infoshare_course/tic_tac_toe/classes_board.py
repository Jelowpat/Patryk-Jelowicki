class Board:
    def __init__(self, elements=None):
        if elements is None:
            self.elements = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        else:
            self.elements = elements                                        # elements of the current position of the game
        self.history = [[" ", " ", " ", " ", " ", " ", " ", " ", " "],  # list of positions for undo redo functionality
                        [], [], [], [], [], [], [], [], []]
        self.move = 0                                                   # move tracking                                        # result of the game
        self.player = "x"                                               # next player

    # method for applying a move, changing current, player and initiating checking the result, updating move and history
    def new_move(self, position):
        self.elements[position] = self.player
        self.move += 1
        self.history[self.move] = self.elements.copy()
        if self.move > 4:
            self.checking()
        self.change_player()

    # a method for undo
    def undo(self):
        if self.move > 0:
            self.move -= 1
            self.elements = self.history[self.move].copy()
            self.change_player()
            return False, ""
        else:
            return False, "There is nothing to revert!"

    # a method for redo
    def redo(self):
        if self.history[self.move+1]:
            self.move += 1
            self.elements = self.history[self.move].copy()
            self.change_player()
            return False, ""
        else:
            return False, "There is nothing to redo!"

    # a method for checking the result
    def checking(self):
        cases = [
            self.elements[0:3],
            self.elements[3:6],
            self.elements[6:9],
            self.elements[0::3],
            self.elements[1::3],
            self.elements[2::3],
            self.elements[0::4],
            self.elements[2:7:2],
        ]
        for element in cases:
            if element == ["x", "x", "x"] or element == ["o", "o", "o"]:
                return self.player
        if self.move == 9:
            return "TIE"
        # checking the result in advance
        if self.move > 5:
            for element in cases:
                if not ("x" in element and "o" in element):
                    if self.move == 8 and "o" in element:
                        pass
                    elif self.move == 7 and element.count(" ") == 2:
                        pass
                    elif self.move == 6 and element.count("o") == 1 or element.count(" ") == 3:
                        pass
                    else:
                        return False
            return "TIE"

    # a method for changing player
    def change_player(self):
        if self.player == "x":
            self.player = "o"
        else:
            self.player = "x"

    def insert(self, decision):

        try:
            decision = int(decision) - 1
        except ValueError:
            return False, "that is not a number"
        if decision > 8 or decision < 0:
            return False, "that is not a number from 1 to 9!"
        elif self.elements[decision] != " ":
            return False, "this place is already taken"
        else:
            self.new_move(decision)
            return True, ""

    def __str__(self):
        border = "|===========|\n"
        row_1 = f"| {self.elements[0]} | {self.elements[1]} | {self.elements[2]} |\n" + border
        row_2 = f"| {self.elements[3]} | {self.elements[4]} | {self.elements[5]} |\n" + border
        row_3 = f"| {self.elements[6]} | {self.elements[7]} | {self.elements[8]} |\n" + border

        return border + row_1 + row_2 + row_3

    def __repr__(self):
        return self.elements

    def new_game(self):
        self.__init__()
