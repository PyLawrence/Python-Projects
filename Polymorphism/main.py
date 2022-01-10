class Sprite:
    image = ""
    x = 0
    y = 0

    def setup(self):
        self.x = 10
        self.y = 1

    def printDetails(self):
        print("x:{} y:{}\nType:{}".format(self.x, self.y, type(self)))



class Enemy(Sprite):
    difficulty = 5
    canJump = False

    def setup(self):
        self.x = 30
        self.y = 1

class Player(Sprite):
    name = ""
    attackType = "Fire"

    def setup(self):
        self.name = input("What is your name, son?\n")
        super().setup()

    def printDetails(self):
        super().printDetails()
        print("My name is, {}!\n".format(self.name))



player = Player()
enemy = Enemy()

player.setup()
enemy.setup()

player.printDetails()
enemy.printDetails()

