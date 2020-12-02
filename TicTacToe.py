from IPython.display import clear_output
from collections import Counter
import random
import os

def display(*args):
    clear_output(wait=True)
    os.system('clear')
    for arg in args:
        print(arg)


def remove_entry(row, column, entries):
    if ('row' + row) in entries:    
        if ('column' + column) in entries['row' + row]:
            del entries['row' + row]['column' + column]
        else:
            return False
    else: 
        return False

    if len(entries['row' + row]) == 0:
        del entries['row' + row]
    
    return True

def computer_move(entries):
    rowchoice = random.choice([row for row in entries.keys()])
    columnchoice = random.choice([column for column in entries[rowchoice].keys()]).replace('column', '')
    rowchoice = rowchoice.replace('row', '')

    remove_entry(str(rowchoice), str(columnchoice), entries)
    return [int(rowchoice), int(columnchoice)-1]

def determine_winner(rows):

    column1 = [rows[1][0], rows[2][0], rows[3][0]]
    column2 = [rows[1][1], rows[2][1], rows[3][1]]
    column3 = [rows[1][2], rows[2][2], rows[3][2]]

    diagonal1 = [rows[1][0], rows[2][1], rows[3][2]]
    diagonal2 = [rows[3][0], rows[2][1], rows[1][2]]

    if Counter(column1)['X'] == 3 or Counter(column2)['X'] == 3 or Counter(column3)['X'] == 3 or Counter(rows[1])['X'] == 3 or Counter(rows[2])['X'] == 3 or Counter(rows[3])['X'] == 3 or Counter(diagonal1)['X'] == 3 or Counter(diagonal2)['X'] == 3:
        return "Player is the winner"
    elif Counter(column1)['O'] == 3 or Counter(column2)['O'] == 3 or Counter(column3)['O'] == 3 or Counter(rows[1])['X'] == 3 or Counter(rows[2])['O'] == 3 or Counter(rows[3])['O'] == 3 or Counter(diagonal1)['O'] == 3 or Counter(diagonal2)['O'] == 3:
        return "Computer is the winner"
    else:
        return 0

def get_input(errormsg):
    message = "Please choose cell to insert your X (1,1 = row 1, col 1): "  
    if len(errormsg) > 0:
        message = errormsg + message
    
    while True:
        choice = input(message)
        if ',' in choice:
            choice = choice.split(',')        
            if choice[0].isdigit() and choice[1].isdigit():
                return choice
        

        errormsg = "Invalid Entry, please try again....."

row1 = [' ', ' ', ' ']
row2 = [' ', ' ', ' ']
row3 = [' ', ' ', ' ']

rows = {1: row1, 2: row2, 3: row3}

availableentries = {'row1': {'column1' : '', 'column2' : '', 'column3' : ''},
                    'row2': {'column1' : '', 'column2' : '', 'column3' : ''},
                    'row3': {'column1' : '', 'column2' : '', 'column3' : ''}}

display(row1, row2, row3)
answer = 0
errmsg = ''
while len(availableentries) > 0 and answer == 0:
    choice = get_input(errmsg)    

    row = int(choice[0])
    column = int(choice[1])
    
    if remove_entry(str(row), str(column), availableentries):
    
        rows[row][column-1] = "X"
        answer = determine_winner(rows)
        errmsg = ''
        if answer == 0:

            if len(availableentries) > 0:
                computerchoice = computer_move(availableentries)
                rows[computerchoice[0]][computerchoice[1]] = "O"
            
            display(row1, row2, row3)
        else:
            display(row1, row2, row3)
            print("\n" + str(answer))
    else:
        errmsg = "Invalid Entry, please try again....."