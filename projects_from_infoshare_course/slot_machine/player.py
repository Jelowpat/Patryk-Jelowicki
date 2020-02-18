# a class for defining a player that is currently playing the slot machine

import json


class Player:
    def __init__(self, name, surname, result=0):
        self.credits = 0            # current credits of a player
        self.result = result        # players score during all of the visits
        self.name = name
        self.surname = surname

    def deposit(self, amount):      # depositing money on the slot machine
        self.credits += amount
        self.result -= amount

    def withdraw(self):             # withdrawing money from the slot machine
        self.result = self.result + self.credits
        self.credits = 0

    def save(self):                 # saving players result to a json file
        self.withdraw()

        with open(f"players.json") as file:
            exists = False
            data = json.load(file)
            for x in data["players"]:
                if x["name"] == self.name and x["surname"] == self.surname:
                    x.update({"result": self.result, "credits": self.credits})
                    exists = True
                    break
            if exists is False:
                data["players"].append(self.__dict__)

        with open(f"players.json", "w") as file:
            json.dump(data, file)