import json

class Player:
    def __init__(self, name, surname, result=0):
        self.credits = 0
        self.result = result
        self.name = name
        self.surname = surname

    def deposit(self, amount):
        self.credits += amount
        self.result -= amount

    def withdraw(self):
        self.result = self.result + self.credits
        self.credits = 0

    def save(self):
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


object2 = Player("martyna", "wlodarczyk", 200000)
object1 = Player("patryk", "jelowicki", 10000)
object1.deposit(20000)
object1.save()
object2.save()