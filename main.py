#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 19:36:39 2021

@author: matthewhartz
"""

import utils
import numpy as np

bingo_card = [
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



custom_numbers =[61,2,5,8,16,3,4,10,12,19,20,35,50,65, 27, 1, 31]
list_of_pulls=[]




set_of_nums = set()




def main():
    
    num_of_games = 0
    bingo = False
    turn_in_game = 0
    list_of_indices = []
    moves_per_game = []
    list_to_pull_from = []
    
    while num_of_games < 10000:
        
        bingo = False
        
        list_to_pull_from = [i for i in range(1,76)]
        
        turn_in_game = 0
        
        answer = [
        [False, False, False, False, False], 
        [False, False, False, False, False],
        [False, False, True, False, False],
        [False, False, False, False, False],
        [False, False, False, False, False] 
        ]
        
        while not bingo: 
            
            num = utils.pull_number(list_to_pull_from)
            
            turn_in_game += 1
            
            index = utils.mark_card(num, bingo_card, answer)
            
            list_of_indices.append(index)
            
            number_to_mark = list_of_indices[-1]
            
            if number_to_mark is not None:
        
                x_value = number_to_mark[0]
    
                y_value = number_to_mark[1]
        
                answer[x_value][y_value] = True
            
                if utils.horz_bingo_check(answer) or utils.vert_bingo_check(answer) or utils.diag_bingo_check(answer):
                
                    moves_per_game.append(turn_in_game)
                    bingo = True
                
            
    
            
        num_of_games += 1
    
    
        
    utils.make_graph(moves_per_game)
    
    mean = np.mean(moves_per_game)
    
    std = np.std(moves_per_game)
    #need a function for some descriptive statistics

    print(mean)
    
    print(std)

if __name__ == "__main__":
    main()
    

  






    
    
