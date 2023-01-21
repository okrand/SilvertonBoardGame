from random import randint
def dice():
    return randint(1,6)

def twodice():
    return randint(1, 6) + randint(1, 6)

gold_range=[150,175,200,225,250,250,275,300,325,350]
copper_range=[100,120,140,160,200,200,240,280,320,400]
silver_range=[100,120,160,180,200,200,200,240,300,400]
lumber_range=[30,40,60,80,100,120,160,200,240,300]
coal_range=[20,20,30,40,60,60,80,100,120,140]

cities = ['denver', 'slc', 'pueblo', 'santafe', 'elpaso']

def update_gold(input, _):
    input = input + dice()
    result = 0
    match input:
        case 1: result = 2
        case num if num == 2 or num == 3: result = 1
        case num if num == 6 or num == 7: result = -1
        case num if num > 7: result = -2
    return result

def update_copper(input, _):
    input = input + dice()
    result = 0
    match input:
        case 1: result = 3
        case 2: result = 2
        case 3: result = 1
        case num if num == 6 or num ==7: result = -1
        case num if num == 8 or num == 9: result = -2
        case num if num == 10 or num == 11: result = -3
        case num if num > 11: result = -4
    return result

def update_silver(input, idn):
    input = input + twodice() - idn
    result = 0
    match input:
        case num if num < 1: result = 0
        case 1: result = 4
        case 2: result = 3
        case 3: result = 2
        case num if num == 4 or num == 5: result = 1
        case num if num == 8 or num == 9: result = -1
        case num if num == 10 or num == 11: result = -2
        case 12: result = -3
        case 13: result = -4
        case 14: result = -5
        case 15: result = -6
        case num if num > 15: result = -7
    return result

def update_lumber(input, idn):
    input = input + twodice() - idn
    result = 0
    match input:
        case num if num < 2: result=3
        case num if num == 2 or num == 3: result=2
        case num if num == 4 or num == 5: result = 1
        case num if num == 7 or num ==8: result = -1
        case num if num == 9 or num == 10: result = -2
        case num if num == 11 or num == 12: result = -3
        case num if num > 12: result = -4
    return result

def update_coal_1(input, idn):
    input = round(input/2) + twodice() - idn
    result = 0
    match input:
        case num if num < 2: result = 3
        case num if num == 2 or num == 3: result = 2
        case num if num == 4 or num == 5: result = 1
        case num if num == 9 or num == 10: result = -1
        case num if num == 11 or num == 12: result = -2
        case num if num > 12: result = -3
    return result

def update_coal_2(input, idn):
    input = input + twodice()-idn
    result = 0
    match input:
        case num if num < 2: result = 3
        case num if num == 2 or num == 3: result = 2
        case num if num == 4 or num == 5: result = 1
        case num if num == 9 or num == 10: result = -1
        case num if num == 11 or num == 12: result = -2
        case num if num > 12: result = -3
    return result

def prompt_user(label, limit):
    prompt = 'How many sold: '+ label + '\n'
    how_many = input(prompt)
    try:
        how_many = int(how_many)
    except ValueError:
        print('Try entering a number')
        how_many = prompt_user(label, limit)
    while how_many > limit:
        print('You can\'t sell that much '+ label +'!')
        how_many = prompt_user(label, limit)

    return how_many

