class Tank:

    def __init__(self, coords):
        print("Tank created!")
        self.__health = 100
        self.__coords = coords

    def isKilled(self):
        return (self.__health <= 0)

    def getHealth(self):
        return self.__health

    def hit(self, round):
        self.__health -= round.getDamage()

    def getHitSound(self):
        pass

    def isPlayer(self):
        pass

    def getCoords(self):
        return self.__coords
