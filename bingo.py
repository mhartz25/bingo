#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 18:45:56 2021

@author: matthewhartz
"""


import pandas as pd 
from numpy import random

#create the bingo card and answer card as arrays
data = [
        [1,16,31,46,61],
        [2,17,32,47,62],
        [3,18,33,48,63],
        [4,19,34,49,64],
        [5,20,35,50,65]
        ]
  
answer = [
        [False, False, False, False, False], 
        [False, False, False, False, False],
        [False, False, True, False, False],
        [False, False, False, False, False],
        [False, False, False, False, False] 
        ]


#Create Bingo Card and Answer Key as Df


def manually_draw_number(letter, num):
    for i in range(0,5):
        if bingo_card[:,i] == num:
            answer_key[letter,i]= True
        else:
            return "nope"



def vert_bingo_check(card):
    print('u')

def horz_bingo_check(card):
    print('u')

def diag_bingo_check(card):
    print('u')

def draw_number(card):
    number = random.randint(1,75)
    
    print(f'Number is {number}')

    for i in range(1,6):
        for j in range(1,6):
            if data[i][j] == number:
                print(f"you had that number at index {i},{j}")
                answer[i][j] = True 
                
                print(answer)
                
                return 
            else:
                print("No")




# print(data[2][2])

# data[2][2] = 37

# print(data[2][2])

draw_number(data)