class Round:

    def __init__(self, x, y, dx, dy):
        self.__x = x
        self.__y = y
        self.__dy = dy
        self.__dx = dx
        self.__bounces = 0

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getCoords(self):
        intx = int(self.__x)
        inty = int(self.__y)
        return (intx, inty)

    def bounceX(self):
        self.__dx = -self.__dx
        self.__bounces += 1

    def bounceY(self):
        self.__dy = -self.__dy
        self.__bounces += 1


    def updatePosition(self):
        self.__x += self.__dx
        self.__y += self.__dy

    def isDead(self):
        return self.__bounces > 1
