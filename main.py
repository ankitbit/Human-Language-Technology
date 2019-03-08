#from helpers import helpers
#from transformers import transformers

def multiply(input):
        return(input*input)
def add(input):
        return(input+input)

input_number = 2

def do_something(number):
    multiplied= multiply(number)
    added= add(number)
    print('I just multiplied and added :D')

do_something(2)