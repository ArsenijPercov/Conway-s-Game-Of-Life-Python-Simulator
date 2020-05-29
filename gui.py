import tkinter as tk
import numpy as nm 
import gameoflife

class GameOfLifeGui(tk.Frame):
    def __init__(self,*args,**kwargs):
        tk.Frame.__init__(self,*args,**kwargs)
        self.size = 50
        self.game = gameoflife.Game(self.size)
        self.cellsize = 20
        self.setup = 1
        self.canvas = tk.Canvas(self,height = self.size*self.cellsize+self.cellsize, width = self.size*self.cellsize)
        self.boxes = [[None for x in range(self.size)] for y in range(self.size)]

        self.canvas.pack(expand=0)

        for i in range(self.size):
            for j in range(self.size):
                self.boxes[j][i] = self.canvas.create_rectangle(i*self.cellsize,j*self.cellsize,(i+1)*self.cellsize,(j+1)*self.cellsize,width=1,outline="purple",fill="black")

    def synchronize(self):
        for x in range(self.size):
            for y in range(self.size):
                if self.game.grid.grid[x][y]:
                    self.updatecell((x,y),1)
                else:
                    self.updatecell((x,y),0)

    def updatecell(self, coord, status):
        if status == 0:
            self.canvas.itemconfig(self.boxes[coord[1]][coord[0]], fill="black")
        else:
            self.canvas.itemconfig(self.boxes[coord[1]][coord[0]], fill="green")
        #print(nm.matrix(self.board))
    
    def getorigin(self,eventorigin):
        x = eventorigin.x
        y = eventorigin.y
        xcell = x//self.cellsize
        ycell = y//self.cellsize
        if self.game.grid.isAlive(xcell,ycell):
            self.game.killCell(xcell,ycell)  
            self.updatecell((xcell,ycell),0)      
        else:
            self.game.createCell(xcell,ycell)
            self.updatecell((xcell,ycell),1)      

    def setup_toggle(self,option):
        if self.setup:
            self.setup = 0
        else:
            self.setup = 1


    def game_loop(self):
        FPS = 1000
        if self.setup == 0:
            self.game.enforceRules()
            self.synchronize()
        mainwindow.update()
        print(nm.array(self.game.grid.grid))
        mainwindow.after(FPS, self.game_loop)

if __name__ == "__main__":
    mainwindow = tk.Tk()
    game = GameOfLifeGui(mainwindow)
    #game.game.createCell(4,5)
    #game.game.createCell(5,4)
    mainwindow.bind("<Button 1>",game.getorigin)
    mainwindow.bind("s",game.setup_toggle)

    game.game.createCell(5,5)
    game.game.createCell(5,6)
    game.game.createCell(5,4)
    game.game.createCell(4,5)
    game.synchronize()
    game.pack(expand=False)
    game.game_loop()
    mainwindow.mainloop()
