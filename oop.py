# Returning to my bingo simulation to 
# 1. do it in OOP 
# 2. make so there can be N amount of cards in a single game


import random
import matplotlib.pyplot as plt


nums = [i for i in range(1,76)]



class BingoCard:

    numbers = [i for i in range(1,76)]

    B_numbers = [i for i in range(1,16)]
    I_numbers = [i for i in range(16,31)]
    N_numbers = [i for i in range(31,46)]
    G_numbers = [i for i in range(46,61)]
    O_numbers = [i for i in range(61,76)]

    key = [
        [False, False, False, False, False], 
        [False, False, False, False, False],
        [False, False, True, False, False],
        [False, False, False, False, False],
        [False, False, False, False, False] 
        ]
  

    def __init__(self):
        

        self.Bs = random.sample(self.B_numbers, k=5)
        self.Is = random.sample(self.I_numbers, k=5)
        self.Ns = random.sample(self.N_numbers, k=5)
        self.Gs = random.sample(self.G_numbers, k=5)
        self.Os = random.sample(self.O_numbers, k=5) 
        self.bingo = False
        


    def __repr__(self):
        pass

    def answer_key(self):
        pass
        
    def number_called(self,number):
        '''This will allow me to input a number and mark the card'''
        
        if number in self.B_numbers:
            for i in range(0,5):
                if self.Bs[i] == number:
                    self.key[i][0] = True
        elif number in self.I_numbers:
              for i in range(0,5):
                if self.Is[i] == number:
                    self.key[i][1] = True
        elif number in self.N_numbers:
              for i in range(0,5):
                if self.Ns[i] == number:
                    self.key[i][2] = True
        elif number in self.G_numbers:
              for i in range(0,5):
                if self.Gs[i] == number:
                    self.key[i][3] = True
        elif number in self.O_numbers:
              for i in range(0,5):
                if self.Os[i] == number:
                    self.key[i][4] = True

    def call_random(self):
        '''docstring'''
        ball = random.choice(self.numbers)
        self.numbers.remove(ball)
        return ball

    def diagonal_check(self):
        check = []
        reverse_check = []
        for i in range(0,5):
            check.append(self.key[i][i])
            reverse_check.append(self.key[-i][i-1])
        
        return all(check) or all(reverse_check)

    def horizontal_check(self):
        for i in range(0,5):
            if all(self.key[i]):
                return True

    def vertical_check(self):
        '''Unless there's a way to check for Trues in a non-iterative way
        then it probably makes more sense to check for Falses and move along whenever one is found

        can try checking the first row then exclude any columns that return False from each check
        '''
        combine = []
    
        column_one = all([index[0] for index in self.key]) 
        combine.append(column_one) 
        
        column_two = all([index[1] for index in self.key])
        combine.append(column_two)
            
        column_three = all([index[2] for index in self.key])
        combine.append(column_three)
            
        column_four = all([index[3] for index in self.key])
        combine.append(column_four)
            
        column_five = all([index[4] for index in self.key])
        combine.append(column_five)
        
        return any(combine)
            
    def picture_frame_check():
        pass 

    def full_card_check():
        pass

def call_random(nums):
    '''docstring'''
    ball = random.choice(nums)
    nums.remove(ball)
    return ball


def run_bingo(number_of_cards):
    loops = 0
    bingo = False
    cards = []
    #create bingo cards
    for i in range(0,number_of_cards):
        i = BingoCard()
        cards.append(i)
    
    #call number and run checks
    while not bingo:

        ball = call_random(nums)

        for card in cards:
            card.number_called(ball)
        
        for card in cards:
            if card.vertical_check() == True or card.horizontal_check() == True or card.diagonal_check() == True:
                card.bingo = True
                winning_card = card
                bingo = True
                break
        loops += 1
        print(loops)

    return number_of_cards, loops


players = []
turns = []

for j in range(1,20):


    pylrs, lps = run_bingo(j)

    players.append(pylrs)
    turns.append(lps)


plt.scatter(players, turns)
plt.show()

