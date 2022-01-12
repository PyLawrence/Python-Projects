from abc import ABC, abstractmethod

class Sprite(ABC):
    # in python, polymorphism will act similar to an abstract method
    # I'm not quite sure how we would use them differently
    # the only major difference I see is that with polymorphism, the original class functions and does things
    # but with abstract classes, we create the blueprint but don't actually use it
    x = 0
    y = 0

    @abstractmethod
    def spawn(self):
        pass

    # not abstract, but can still be overridden
    def jump(self):
        self.y += 10

class Player(Sprite):
    def spawn(self):
        self.x = 5
        self.y = 1

    # override jump method
    def jump(self):
        self.y += 15

class Enemy(Sprite):
    def spawn(self):
        self.x = 30
        self.y = 1



