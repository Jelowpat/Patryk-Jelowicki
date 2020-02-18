import random


class Cherry:

    def __init__(self, sign, multip, ratio):
        self.sign = sign
        self.multi = multip
        self.ratio = ratio


class OneArmBandit:

    elements = [
        Cherry("!", 1, 75),
        Cherry("@", 2, 50),
        Cherry("#", 3, 30),
        Cherry("$", 100, 2),
        Cherry("%", 5, 10),
        Cherry("^", 10, 5),
        Cherry("&", 3, 30)
    ]
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

    conditions_5 = ["!!!!!", "@@@@@", "#####", "$$$$$", "%%%%%", "^^^^^", "&&&&&"]
    conditions_4 = ["!!!!", "@@@@", "####", "$$$$", "%%%%", "^^^^", "&&&&"]
    conditions_3 = ["!!!", "@@@", "####", "$$$", "%%%", "^^^", "&&&"]

    def __init__(self, money=0):
        self.board = [Cherry("$", 0, 0) for x in range(25)]
        # self.bet = 10
        self.flag = 0
        self.lines = self.cases[self.flag]["number"]
        # self.credits = money
        # self.announcement = ""
        # self.deposit(init=True)

    # def deposit(self, init=False):
    #     while True:
    #         print(self, self.announcement, sep="")
    #         bankroll = input("how mouch money would you like to deposit (min 70, 'c' to cancel)")
    #         if init is False:
    #             if bankroll.lower() == "c":
    #                 self.announcement = ""
    #                 break
    #         try:
    #             bankroll = int(bankroll)
    #             if bankroll >= 70:
    #                 self.credits = bankroll
    #                 self.announcement = f"credits increased by {bankroll}"
    #                 break
    #             else:
    #                 raise ValueError
    #         except ValueError:
    #             self.announcement = "insert a number (minimum 10)"
    #             continue

    def spin(self, bet, credits):
        if credits < bet * self.lines:
            return False
        else:
            for x in range(25):
                self.board[x] = random.choices(OneArmBandit.elements,
                                               [x.ratio for x in OneArmBandit.elements])[0]
            return True

    def __str__(self):
        screen = ""
        # screen = str(self.credits) + "\n"
        for pos, el in enumerate(self.board):
            screen += f"{el.sign}   " if pos % 5 != 4 else f"{el.sign}\n"
        # screen += f"total bet: {self.bet * self.lines} ({self.bet}*lines)\n"
        # screen += f"lines: {self.lines}\n"
        return screen

    def result(self):
        payout = 0
        for x in OneArmBandit.cases[self.flag]["patterns"]:
            line = ""
            multi = None
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

    # def insert(self):
    #     decision = input("any to spin, 'u' to increase the bet, 'l' to lower the bet,\n"
    #                      "'w' to withdraw all, 'd' to deposit, 's' to switch number of lines")
    #     if decision == "w":
    #         self.announcement = f"you have just collected {self.credits} credits!!!"
    #         self.credits = 0
    #         print(self, self.announcement, sep="")
    #         self.deposit(init=True)
    #         return False
    #     if decision == "d":
    #         self.deposit()
    #         return False
    #     if decision == "u":
    #         self.bet += 10
    #         self.announcement = "bet increased by 10 * lines"
    #         return False
    #     if decision == "l":
    #         if self.bet >= 10:
    #             self.bet -= 10
    #             self.announcement = "bet decreased by 10 * lines"
    #         else:
    #             self.announcement = "that's the lowest bet"
    #         return False
    #     if decision == 's':
    #         self.swap()
    #         self.announcement = f'changed to {OneArmBandit.cases[self.flag]["number"]}'
    #         return False
    #     else:
    #         return True

    def swap(self):
        if self.flag == 0:
            self.flag = 1

        else:
            self.flag = 0
        self.lines = self.cases[self.flag]["number"]
