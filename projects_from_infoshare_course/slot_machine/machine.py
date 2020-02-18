import random


# a class for the elements of the machine
class Cherry:

    def __init__(self, sign, multip, ratio):
        self.sign = sign
        self.multi = multip         # multiplayer of the score for an element
        self.ratio = ratio          # chance for drawing an element


class OneArmBandit:

    # the elements that can be drew during a spin
    elements = [
        Cherry("!", 1, 75),
        Cherry("@", 2, 50),
        Cherry("#", 3, 30),
        Cherry("$", 100, 2),
        Cherry("%", 5, 10),
        Cherry("^", 10, 5),
        Cherry("&", 3, 30)
    ]
    # the lines on which we will look for winning patterns. 2 options - 7 lines and 11
    cases_7 = [
        range(0, 5),
        range(5, 10),
        range(10, 15),
        range(15, 20),
        range(20, 25),
        range(4, 21, 4),
        range(0, 25, 5)
    ]
    cases_11 = cases_7.copy()
    cases_11.extend([(0, 6, 12, 8, 4), (20, 16, 12, 18, 24), (10, 6, 2, 7, 14), (10, 16, 22, 18, 24)])

    cases = [{"patterns": cases_7, "number": 7}, {"patterns": cases_11, "number": 11}]

    # defining winning conditions for a line
    conditions_5 = ["!!!!!", "@@@@@", "#####", "$$$$$", "%%%%%", "^^^^^", "&&&&&"]
    conditions_4 = ["!!!!", "@@@@", "####", "$$$$", "%%%%", "^^^^", "&&&&"]
    conditions_3 = ["!!!", "@@@", "####", "$$$", "%%%", "^^^", "&&&"]

    def __init__(self):
        self.board = [Cherry("$", 0, 0) for x in range(25)]
        self.flag = 0                                       # flag for number of lines
        self.lines = self.cases[self.flag]["number"]

    def spin(self, bet, credits):
        if credits < bet * self.lines:
            return False
        else:
            for x in range(25):
                self.board[x] = random.choices(OneArmBandit.elements,
                                               [x.ratio for x in OneArmBandit.elements])[0]
            return True

    # overriding str function for the machine
    def __str__(self):
        screen = ""
        for pos, el in enumerate(self.board):
            screen += f"{el.sign}   " if pos % 5 != 4 else f"{el.sign}\n"
        return screen

    # function for checking the result of a spin
    def result(self):
        payout = 0
        for x in OneArmBandit.cases[self.flag]["patterns"]:
            line = ""               # this variable will hold a emporary pattern of a line
            multi = None            # here the program will hold the multiplication
                                    #  of the element that it's checking for
            for y in x:
                line += self.board[y].sign
                if multi is None:
                    multi = self.board[y].multi
            if line in OneArmBandit.conditions_5:
                payout += 100 * multi
                continue
            if line[:4] in OneArmBandit.conditions_4:
                payout += 10 * multi
                continue
            if line[:3] in OneArmBandit.conditions_3:
                payout += multi
        if payout:
            return payout
        else:
            return 0

    # changing the amount of lines we are playing on
    def swap(self):
        if self.flag == 0:
            self.flag = 1
        else:
            self.flag = 0
        self.lines = self.cases[self.flag]["number"]
