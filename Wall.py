class Wall:

    def __init__(self):
        print("Wall created!")

    def isDestroyed(self):
        return (self.__health <= 0)

    def getHealth(self):
        return self.__health

    def hit(self, round):
        self.__health -= round.getDamage()

    def getHitSound(self):
        pass
