import Tkinter as Tk

class KnightGame:
    def __init__(self):
        self.canvas_width = 500
        self.canvas_height = 500
        self.tiles = {}
        self.canvas = Tk.Canvas(root, width = self.canvas_width, height = self.canvas_height) 
        self.canvas.pack()
        self.currentRow = 0
        self.currentColumn = 0
    def knight_tour(self, n):
        numRows = n
        numColumns = n
        cellWidth = int(self.canvas_width/numColumns)
        cellHeight = int(self.canvas_height/numRows)
        for column in range(numColumns):
            for row in range(numRows):
                x1 = column * cellWidth
                y1 = row * cellHeight
                x2 = x1 + cellWidth
                y2 = y1 + cellHeight
                tile = self.canvas.create_rectangle(x1,y1,x2,y2, fill='white')
                self.tiles[row, column] = tile
                self.canvas.tag_bind(tile, "<1>", lambda event, row=row, column=column: self.newTile(row, column)) 
        currentTile = self.canvas.itemconfigure(self.tiles[0,0], fill="orange") 
    def newTile(self, row, column): #make current tile orange
        tile = self.tiles[row, column]
        tile_color = self.canvas.itemcget(tile, "fill")
        new_color = "orange"
        old_color = "blue"
        dx = abs(row - self.currentRow)
        dy = abs(column - self.currentColumn)
        oldTile = self.tiles[self.currentRow, self.currentColumn]
        #if legal, change to orange & change old tile to blue & push positions to variables row and column 
        if (dx==1 and dy==2) or (dx==2 and dy==1):
            self.canvas.itemconfigure(tile, fill=new_color) #change current tile to orange
            self.canvas.itemconfigure(oldTile, fill=old_color) #change old tile to blue
            self.currentRow = row
            self.currentColumn = column
        #if not legal, dont do anything
        else:
            print("Illegal move. Try again.")

root = Tk.Tk()
gui = KnightGame()
gui.knight_tour(5) #takes in any value 'n' to make board
root.mainloop()
