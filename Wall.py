class Wall:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def isDestroyed(self):
        return (self.__health <= 0)

    def getHealth(self):
        return self.__health

    def hit(self, round):
        self.__health -= round.getDamage()

    def getHitSound(self):
        pass

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y
