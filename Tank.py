class Tank:

    def __init__(self, x, y):
        self.__health = 100
        self.__x = x
        self.__y = y


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

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def moveLeft(self):
        self.__x -= 3

    def moveRight(self):
        self.__x += 3

    def moveUp(self):
        self.__y -= 3

    def moveDown(self):
        self.__y += 3

    def speak(self):
        print("JUST!")
