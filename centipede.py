import sys #sys.exit()
import random #random.choice()

class Centipede:

    def  __init__(self, length): #constructor
        self.length = length
        self.solved_centipede = list(range(1, length + 1))
        self.current_centipede = self.solved_centipede.copy()
        self.scramble()

    def start(self): #start messages
        print(f"You must solve into: {self.solved_centipede}")
        print(f"Your scrambled state is {self.current_centipede}")
        
    def generate(self): #generates possible moves
        moves = []
        for i in range(self.length):
            if self.validate(i, "+"):
                moves.append((i, "+"))
            if self.validate(i, "-"):
                moves.append((i, "-"))
        return moves
    
    def scramble(self): #scrambles using generated moves
        for _ in range(self.length*self.length):
            i, sign = random.choice(self.generate())
            self. swap(i, sign)

    def permute(self, i, sign): #main puzzle mechanic
        if self.validate(i, sign):
            self.swap(i, sign)
            print(f"Current state: {self.current_centipede}")
            return True
        return False

    def validate(self, i, sign): #validates moves (either generated or input ones)
        if i < 0 or i >= self.length:
            #print("Illegal move; position not in bounds. ") ~ possible error message (TBI)
            return False
        if sign == "+" and i + 1 >= self.length:
            #print("Illegal move; right is an impossible direction for given position. ") ~ possible error message (TBI)
            return False
        if sign == "-" and i - 1 < 0:
            #print("Illegal move; left is an impossible direction for given position. ") ~ possible error message (TBI)
            return False
        return True

    def swap(self, i, sign): #main puzzle logic. used for scrambling and solving
        if sign == "+":
            self.current_centipede[i], self.current_centipede[i+1]  = -self.current_centipede[i+1], -self.current_centipede[i]
        else:
            self.current_centipede[i], self.current_centipede[i-1]  = -self.current_centipede[i-1], -self.current_centipede[i]
    
    def check(self,x): #if solved, ends program
        if self.current_centipede == self.solved_centipede:
            print(f"Congratulations! You solved it in {x} moves!")
            sys.exit()

