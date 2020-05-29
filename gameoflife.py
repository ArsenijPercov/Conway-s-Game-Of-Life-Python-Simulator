import tkinter
import time
import numpy

class Grid:
    def __init__(self, size):
        self.grid = [[0 for x in range(size)] for y in range (size)]

    def createCell(self,x,y):
        self.grid[x][y]=1
    
    def killCell(self,x,y):
        self.grid[x][y]=0

    def isAlive(self,x,y):
        return self.grid[x][y]

class Game:
    def __init__(self, size):
        self.grid = Grid(size)
        self.size = size

    def createCell(self,x,y):
        self.grid.createCell(x,y)
    
    def killCell(self,x,y):
        self.grid.killCell(x,y)

    def print(self):
        print(numpy.array(self.grid.grid))

    def enforceRules(self):
        destinedToDie = []
        toBeCreated = []
        for x in range(self.size):
            for y in range(self.size):
                n = self.checkNeigbhors(x,y)
                alive = self.grid.isAlive(x,y)
                if not (n == 2 or n==3) and alive:
                    destinedToDie.append((x,y))
                elif (n==3) and not alive:
                    toBeCreated.append((x,y))
        for i in destinedToDie:
            self.grid.killCell(i[0],i[1])
        
        for j in toBeCreated:
            self.grid.createCell(j[0],j[1])
        
        
    def checkNeigbhors(self,x,y):
        result = 0
        for i in range (-1,2):
            for j in range(-1,2):
                #print(i,j)
                xn = x+i
                yn = y+j
                #print(xn,yn)
                if (not (xn == x and yn == y) and xn >= 0 and yn >=0 and xn<self.size and yn<self.size):
                    if self.grid.isAlive(xn,yn):
                        #print(x,y,xn,yn,202)
                        result += 1
                elif not (xn == x and yn == y):
                    if (xn<0):
                        xn = self.size+xn-1    
                    if (yn<0):
                        yn = self.size+yn-1
                    if (xn >= self.size):
                        xn = xn - self.size
                    if (yn >= self.size):
                        yn = yn - self.size

                    if self.grid.isAlive(xn,yn):
                        result += 1

        return result


