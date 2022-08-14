#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 18:45:56 2021

@author: matthewhartz
"""

list_of_pulls=[]
from numpy import random
from matplotlib import pyplot as plt

#create the bingo card and answer card as arrays


#Create Bingo Card and Answer Key as Df


def pull_number(list_to_pull_from):
    '''need to create some sort of set so itll only give unique number'''
    
    number = random.choice(list_to_pull_from)
    
    list_to_pull_from.remove(number)
    
    return number
    
    
    



def vert_bingo_check(answer):
    '''docstring'''
    combine = []
    
    column_one = all([index[0] for index in answer]) 
    combine.append(column_one) 
    
    column_two = all([index[1] for index in answer])
    combine.append(column_two)
        
    column_three = all([index[2] for index in answer])
    combine.append(column_three)
        
    column_four = all([index[3] for index in answer])
    combine.append(column_four)
        
    column_five = all([index[4] for index in answer])
    combine.append(column_five)
    
    if any(combine):
        
        return True
    
    else:
        
        return False
                

def horz_bingo_check(answer):
    '''check for horz bingo
    right now it is only looking at the first row'''
    for row in range(0,5):
        if all(answer[row]):
            
            
            return True
        
        else:
            return False
        
            
        
    
def diag_bingo_check(answer):
    top_left_bottom_right = []
    top_right_bottom_left = []
    
    for i in range(0,5):
        
        top_left_bottom_right.append(answer[i][i])
        
        top_right_bottom_left.append(answer[i][-(i+1)])
        
    if all(top_left_bottom_right):
        
        return True
    
    elif all(top_right_bottom_left):
        
        return True
       
    else:
        return False
            
            
            


def manual_pull(num_list, bingo_card, answer):
    
    temp_list = answer[:]
    
    for i in range(0,5):
        for j in range(0,5):
            if bingo_card[i][j] == num_list[i]:
                temp_list[i][j] = True
                print(temp_list)
                return temp_list
            else:
                break
    
    


def mark_card(num, bingo_card, answer):
    
    

    for i in range(0,5):
        for j in range(0,5):
            if bingo_card[i][j] == num:
                
                return [i,j]
            else:
                pass 
        
        
def make_graph(moves_per_game):
    plt.hist(moves_per_game, bins = 75, color = 'Orange')
    plt.show()
    
                