from string import ascii_lowercase, ascii_uppercase, digits, punctuation, octdigits
from random import randint, choice 
from wechsel import Components

class newComponents(Components):
        def __init__(self):
           super().__init__()
           

def upperCase():
     newComponents().generic.insert(randint(3,5), choice(ascii_uppercase))
def lowCase(): 
     newComponents().generic.insert(randint(3,7), choice(ascii_lowercase))
def punctuation(): 
     newComponents().generic.insert(randint(5,7),choice(punctuation))
def numero():
     newComponents().generic.insert(randint(1,5), choice(digits))
def octdigits():
     newComponents().generic.insert(7,choice(octdigits))
# call on UI tab 
def iterator(a = int,b =int) -> int:
        return randint(a,b)

def charm(permuatation): 
        for i in range(permuatation): 
                lowCase()
                punctuation()
                upperCase()
                numero()
        pass 