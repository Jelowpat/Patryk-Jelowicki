from Projects.slot_machine.machine import OneArmBandit
from Projects.slot_machine.player import Player
import os, json

clear = lambda: os.system('cls')


def deposit(init=False):
    note = ""
    while True:
        clear()
        print(screen, note, sep="\n")
        bankroll = input("how mouch money would you like to deposit (min 100, 'c' to cancel)\n")
        if init is False:
            if bankroll.lower() == "c":
                return 0, ""
        try:
            bankroll = int(bankroll)
            if bankroll >= 100:
                return bankroll, f"credits increased by {bankroll}"
            else:
                raise ValueError
        except ValueError:
            note = "insert a number (minimum 100)"
            continue


while True:

    player = input("insert your name and surname\n").split()
    try:
        name = player[0].capitalize()
        surname = player[1].capitalize()
        break
    except IndexError:
        clear()
        print("NAME and SURNAME, please")


with open("players.json") as file:
    data = json.load(file)

punter = Player(name, surname)
welcome = f"Welcome, {name} {surname}!!!"
for x in data["players"]:
    if x["name"].lower() == name.lower() and x["surname"].lower() == surname.lower():
        punter = Player(x["name"], x["surname"], x["result"])
        welcome = f"Welcome back, {punter.name.capitalize()} {punter.surname.capitalize()}!!!"
        break

print(welcome)
print(punter.__dict__)
input("press enter to begin")


game = OneArmBandit()
screen = f"credits: 0\n" + str(game) + \
             f"total bet: 10 (10 * lines)\n" + \
             f"lines: 7\n"
money, info = deposit(init=True)
punter.deposit(money)
bet = 10

while True:

    screen = f"credits: {punter.credits}\n" + str(game) + \
             f"total bet: {bet * game.lines} ({bet}*lines)\n" + \
             f"lines: {game.lines}\n"

    clear()
    print(punter.__dict__)
    print(screen, info, sep="\n")
    info = ""
    decision = input("any to spin, 'u' to increase the bet, 'l' to lower the bet,\n"
                     "'w' to withdraw all, 'd' to deposit, 's' to switch number of lines\n")
    if decision == "q":
        punter.save()
        break
    if decision == "w":
        info = f"you have just collected {punter.credits} credits!!!"
        punter.withdraw()
        clear()
        print(screen, info, sep="\n")
        input("press enter to continue")
        money, note = deposit(init=True)
        punter.deposit(money)
        continue
    if decision == "d":
        a_tuple = deposit()
        punter.deposit(a_tuple[0])
        info = a_tuple[1]
        continue
    if decision == "u":
        bet += 10
        info = "bet increased by 10 * lines"
        continue
    if decision == "l":
        if bet >= 10:
            bet -= 10
            info = "bet decreased by 10 * lines"
        else:
            info = "that's the lowest bet"
        continue
    if decision == 's':
        game.swap()
        info = f"changed to {OneArmBandit.cases[game.flag]['number']}"
        continue
    else:
        if game.spin(bet, punter.credits):
            punter.credits -= bet * game.lines
            win = game.result() * bet
            punter.credits += win
            if win:
                info = f"YOU WON {win} credits!!!"
        else:
            info = "deposit more credits or lower the bet"
