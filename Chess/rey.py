from tkinter import *
from pieza import Pieza

import PIL.Image
import PIL.ImageTk

class Rey(Pieza):
	
	def __init__(self, name, color, coordX, coordY, imagen_archivo):
		self.name = name
		self.color = color
		self.coordX = coordX
		self.coordY = coordY
		#self.image = PhotoImage(file=imagen_archivo)
		image = PIL.Image.open(imagen_archivo)
		self.image = PIL.ImageTk.PhotoImage(image)
		self.image.photo = self.image
		self.noMove = True
        
        
	def printCoords(self):
		print("Color es: "+ self.getColor() + " y coordenadas(x,y) son: " + str(self.getCoordX()) + " " + str(self.getCoordY()))
		
	def getImage(self):
		return self.image
		
	# Function that returns if the King is allowed to do the castling-step
	def noFirstMove(self):
		if (self.getColor() == 'b' and self.getCoordX() == 0 and self.getCoordY() == 4 and self.noMove == True):
			return True
		if (self.getColor() == 'w' and self.getCoordX() == 7 and self.getCoordY() == 4 and self.noMove == True):
			return True
		return False
		
		
	# Function that checks if the board is free and the pieces are available to do the
	# castling move between the king and the rook
	def rookCastling(self, chessBoard, possible_moves):
		
		# Variable for checking the free way from the king to the rook
		freeRow = True
		
		if (self.noFirstMove()):
			
			# Checks for the right side of the actual row
			for index in range(2):	
				# the index + 1 is for not to count the actual position of the king
				if ( not (chessBoard.isEmpty(self.getCoordX(), self.getCoordY() + (index + 1))) ):
					freeRow = False
					
			# Checks if right side of the row is free and if the rook for the castling has not been moved
			if (freeRow and chessBoard.board[self.getCoordX()][7].noFirstMove()):
				possible_moves.append((self.getCoordX(), self.getCoordY() + 2))
				
			freeRow = True
				
			# Checks for the left side of the actual row
			for index in range(3):	
				# the index + 1 is for not to count the actual position of the king
				if ( not (chessBoard.isEmpty(self.getCoordX(), self.getCoordY()- (index + 1))) ):
					freeRow = False
					
			# Checks if left side of the row is free and if the rook for the castling has not been moved
			if (freeRow and chessBoard.board[self.getCoordX()][0].noFirstMove()):
				possible_moves.append((self.getCoordX(), self.getCoordY() - 2))
		
	
	# Function that returns the tuples with the possible moves of the piece
	def canMove(self, chessBoard):
		actual_coordX = self.getCoordX()
		actual_coordY = self.getCoordY()
		
		# Creates an empty list
		possible_moves = []
		
		# Sets the possible coordenates of the movements for the king
		coordsX = [-1, 0, 1, -1, 1, -1, 0, 1]
		coordsY = [-1, -1, -1, 0, 0, 1, 1, 1]
		
		for index in range(8):
			
			# Checks if the position is empty
			if ( chessBoard.isEmpty(actual_coordX + coordsX[index], actual_coordY + coordsY[index]) ):
				possible_moves.append((actual_coordX + coordsX[index], actual_coordY + coordsY[index]))
				
			# Checks if the position is occupied by an enemy
			if ( chessBoard.isEnemy(self.getColor(), actual_coordX + coordsX[index], actual_coordY + coordsY[index]) ):
				possible_moves.append((actual_coordX + coordsX[index], actual_coordY  + coordsY[index]))
		
		# Calls to function for checking castling
		self.rookCastling(chessBoard, possible_moves)
		
		return possible_moves
		
		
	# Makes the King movement
	def movePiece(self, newCoordinates):
		# Checks and sets the no movement variable
		if (self.noFirstMove()):
			self.noMove = False
		self.setCoordX(newCoordinates[0])
		self.setCoordY(newCoordinates[1])
		
'''root = Tk()
reicito = Rey('b', 0, 4, "images/bk.gif")
reicito.printCoords()'''
