from Wall import *
from Tank import *

class Map:

    def __init__(self, file):
        self.__playerTank = []
        self.__course = []
        self.__walls = []

        with open(file) as f:
            strips = f.read().splitlines()


        for n in range(0, 9):
            row = []
            tick = 0
            for r in strips[n]:
                tick += 1
                row.append(r)
                if (r == "X"):
                    keith = Wall(80*(tick-1), 80*n)
                    self.__walls.append(keith)
                if (r == "Z"):
                    james = Tank(80*(tick-.5), 80*(n+.5))
                    self.__playerTank.append(james)


            self.__course.append(row)

    def loadNextMap(self):
        pass

    def getPlayerTank(self):
        return self.__playerTank[0]

    def getCourse(self):
        return self.__course

    def getWalls(self):
        return self.__walls
