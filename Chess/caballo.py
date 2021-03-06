from tkinter import *
from pieza import Pieza
import PIL.Image
import PIL.ImageTk

class Caballo(Pieza):
	
	def __init__(self, name, color, coordX, coordY, imagen_archivo):
		self.name = name
		self.color = color
		self.coordX = coordX
		self.coordY = coordY
		#self.image = PhotoImage(file=imagen_archivo)
		image = PIL.Image.open(imagen_archivo)
		self.image = PIL.ImageTk.PhotoImage(image)
		self.image.photo = image
        
	def printCoords(self):
		print("Color es: "+ self.getColor() + " y coordenadas(x,y) son: " + str(self.getCoordX()) + " " + str(self.getCoordY()))
		
	def getImage(self):
		return self.image
	
	def noFirstMove(self):
		pass
		
	# Function that returns the tuples with the possible moves of the piece		
	def canMove(self, chessBoard):
		
		actual_coordX = self.getCoordX()
		actual_coordY = self.getCoordY()
		
		# Creates an empty list
		possible_moves = []
		
		# Sets the possible coordenates of the movements for the knight
		coordsX = [-2, -2, -1, -1, 1, 1, 2, 2]
		coordsY = [1, -1, -2, 2, 2, -2,-1, 1]
		
		for index in range(8):
			
			if ( chessBoard.isEmpty(actual_coordX + coordsX[index], actual_coordY + coordsY[index]) ):
				possible_moves.append( (actual_coordX + coordsX[index], actual_coordY + coordsY[index]) )
			
			else:
				if ( chessBoard.isEnemy(self.getColor(), actual_coordX + coordsX[index], actual_coordY + coordsY[index]) ):
					possible_moves.append( (actual_coordX + coordsX[index], actual_coordY + coordsY[index]) )
					
		return possible_moves
		
	# Makes the knight movement
	def movePiece(self, newCoordinates):
		
		self.setCoordX(newCoordinates[0])
		self.setCoordY(newCoordinates[1])
		
'''root = Tk()
caballito = Caballo('b', 0, 6, "images/bn.gif")
caballito.printCoords()'''
