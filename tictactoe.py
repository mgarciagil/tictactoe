#A Beginners Guide To Python 3 Programing ultimo capitulo
#Ejercicio Tic Tac Toe

from abc import ABCMeta, abstractmethod, ABC
import random

class Game ():
    def __init__(self):
        self.board = Board()
        self.human = HumanPlayer(self.board)
        self.computer = ComputerPlayer(self.board)
        self.next_player = None
        self.winner = None
        
    def play(self):
        print('Welcome to TicTacToe')
        end_game = False
        self.select_player_counter()
        self.select_player_to_go_first()
        
        while end_game == False:
            if self.next_player == self.human:
                print(self.board)
                print('Make your move!')
                move = self.human.get_move()
                self.board.add_move(move)
                #esto no puede ir aqui porque entra en el else despues???
                self.next_player = self.computer
            else:
                print ('The computer will make their move')
                move = self.computer.get_move()
                self.board.add_move(move)
                self.next_player = self.human
        
            if self.board.check_for_winner(self.human) == self.human.counter:
                self.winner = self.human
                print('The winner is the human!')
                end_game = True
            elif self.board.check_for_winner(self.computer) == self.computer.counter:
                self.winner = self.computer
                print('The winner is the computer!')
                end_game = True
            if self.board.is_full():
                print('The board is full, the game is a tie')
                end_game = True   
        print (self.board)
    
    def select_player_to_go_first(self):
        if random.randint(0, 1) == 0:
            self.next_player = self.human
        else:
            self.next_player = self.computer

    def select_player_counter(self):
        counter = ''
        while not counter == 'X' or counter == 'O':
            print ('Do you want to be X or O?')
            counter = input().upper()
            if counter != 'X' or counter != 'O':
                print ('Input must be X or O')
        if counter == 'X':
            self.human.counter = 'X'
            self.computer.counter = 'O'
        else:
            self.human.counter = 'O'
            self.computer.counter = 'X'

class Board ():
    def __init__(self):
        self.cells = [['', '', ''], ['', '', ''], ['', '', '']]
        # importante añadir salto de linea para print
        self.separator = '\n' + ('-' * 11) + '\n'
    
    def __str__(self):
        row1 = ' ' + str(self.cells[0][0]) + ' | ' + str(self.cells[0][1]) + ' | ' + str(self.cells[0][2])
        row2 = ' ' + str(self.cells[1][0]) + ' | ' + str(self.cells[1][1]) + ' | ' + str(self.cells[1][2])
        row3 = ' ' + str(self.cells[2][0]) + ' | ' + str(self.cells[2][1]) + ' | ' + str(self.cells[2][2])
        return row1 + self.separator + row2 + self.separator + row3

    def add_move(self, move):
        row = self.cells [move.x]
        row[move.y] = move.counter
        return

    def is_cell_empty(self, row, column):
        return self.cells[row][column] == ''
    
    def is_full(self):
        for row in range (0, 3):
            for column in range (0, 3):
                if self.is_cell_empty(row, column):
                    return False
        
    def check_for_winner(self, player):
        c = player.counter
        if ((self.cell_contains(c, 0, 0) and self.cell_contains(c, 0, 1) and self.cell_contains(c, 0, 2))
        or (self.cell_contains(c, 1, 0) and self.cell_contains(c, 1, 1) and self.cell_contains(c, 1, 2))
        or (self.cell_contains(c, 2, 0) and self.cell_contains(c, 2, 1) and self.cell_contains(c, 2, 2))
        or (self.cell_contains(c, 0, 0) and self.cell_contains(c, 1, 0) and self.cell_contains(c, 2, 0))
        or (self.cell_contains(c, 0, 1) and self.cell_contains(c, 1, 1) and self.cell_contains(c, 2, 1))
        or (self.cell_contains(c, 0, 2) and self.cell_contains(c, 1, 2) and self.cell_contains(c, 2, 2))
        or (self.cell_contains(c, 0, 0) and self.cell_contains(c, 1, 1) and self.cell_contains(c, 2, 2))
        or (self.cell_contains(c, 2, 0) and self.cell_contains(c, 1, 1) and self.cell_contains(c, 0, 2))):
            return c
        else:
            return False

    def cell_contains(self, counter, row, column):
     # comprueba si la celda tiene un contenido determinado
        return self.cells[row][column] == Counter

class Player (metaclass=ABCMeta):
 # Clase abstracta que representa un jugador y su counter
 # NPI de las metaclases    
    def __init__(self, board):
        self.board = board
        # hay que establecer el tablero de juego
        self._counter = None
    
    @property
    def counter(self):
        return self._counter
    
    @counter.setter
    def counter(self, value):
        self._counter = value

    @abstractmethod 
        #pero ni idea colega
    def get_move(self): pass

    def __str__(self):
        return self.__class__.__name__ + '[' + str(self.counter) + ']'

class Counter:
 # Each counter used on board
    def __init__(self, string):
        self.label = string

    def __str__(self):
        return self.label

class Move:
 # Each move made
    def __init__(self, counter, x, y):
        self.x = x
        self.y = y
        self.counter = counter
        # hay que saber qué counter ha hecho qué movimiento.

class HumanPlayer(Player):
    def __init__(self, board):
        super().__init__(board)

    def get_user_input(self, prompt):
        invalid_input = True
        while invalid_input:
            print(prompt)
            user_input = input()
            if not user_input.isdigit():
                print('Input must be a number')
            else:
                user_input_int = int(user_input)
                if user_input_int < 1 or user_input_int > 3:
                    print ('Input must be a number in the range 1 to 3')
                else:
                    invalid_input = False
        return user_input_int - 1 
        # porque python indexa en 0

    def get_move(self):
        while True:
            row = self.get_user_input('Please input the row:')
            column = self.get_user_input('Please input the column')
            if self.board.is_cell_empty(row, column):
                return Move(self.counter, row, column)
            else:
                print('That position is not free')
                print('Please try again')

class ComputerPlayer(Player):
    def __init__(self, board):
        super().__init__(board)
    
    def random_select_cell(self):
     # en caso de no encontrar un hueco que nos guste, se elige al azar
        while True:
            row = random.randint(0, 2)
            column = random.randint(0, 2)
            if self.board.is_cell_empty(row, column):
                return Move(self.counter, row, column)

    def get_move(self):
     # """ Provide a very simple algorithm for selecting a move"""
        if self.board.is_cell_empty(1, 1):
        # Choose the center
            return Move(self.counter, 1, 1)
        elif self.board.is_cell_empty(0, 0):
            # Choose the top left
            return Move(self.counter, 0, 0)
        elif self.board.is_cell_empty(2, 2):
            # Choose the bottom right
            return Move(self.counter, 2, 2)
        elif self.board.is_cell_empty(0, 2):
            # Choose the top right
            return Move(self.counter, 0, 2)
        elif self.board.is_cell_empty(0, 2):
            # Choose the top right
            return Move(self.counter, 2, 0)
        else:
            return self.random_select_cell()

#Set up counter globals
X = Counter('X')
O = Counter ('O')

def main():
    game = Game()
    game.play()


if __name__ == '__main__':
    main()