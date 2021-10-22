##def is_word_guessed(secret_word, letters_guessed):
##    '''
##    secret_word: string, the word the user is guessing; assumes all letters are
##      lowercase
##    letters_guessed: list (of letters), which letters have been guessed so far;
##      assumes that all letters are lowercase
##    returns: boolean, True if all the letters of secret_word are in letters_guessed;
##      False otherwise
##    '''    
##    sw=list(secret_word)
##    total=0
##    for e in sw:
##        total += 1
##        if e in letters_guessed:
##            print("")
##    print(total)
from math import * 

def add_up(num):
    y=0
    for x in range(0,num+1):
        y += x
    return y
def returnsides(length):
    l1=length*2
    l2=round(sqrt(3)*length,2)
    return l1,l2
def is_curzon(num):
    a=2**num +1
    b=2*num+1
    if a%b==0:
        return True
    else:
        return False
def add_name(obj, name, value):
    obj1={}
    obj1.update(obj)
    obj1[name]=value
    return obj1
def factorial(num):
    y=1
    for x in range(1,num+1):
       y=y*x
    return y
def upload_count(dates, month):
    matching = [s for s in dates if month in s]
    return len(matching)
