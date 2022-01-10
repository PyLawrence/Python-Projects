class Vehicle:
    weight = 0
    fuelType = ""
    volant = False
    topSpeed = 0

class Car(Vehicle):
    doorCount = 4
    turnRadius = 10
    gearCount = 6

class Boat(Vehicle):
    boatType = ""  # e.g. carrier
    engineType = ""  # e.g. steam
    reversible = False


