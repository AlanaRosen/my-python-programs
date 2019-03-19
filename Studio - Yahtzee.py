import random

def roll_dice(num_dice, num_rolls):
    double_list = [[0 for i in range(num_dice)] for j in range(num_rolls)]
    for roll in range(0, len(double_list)):
      for die in range(0, len(double_list[roll])):
          double_list[roll][die] = (int)(random.random()*6 + 1)
    return double_list

def sum_of_roll(double_list):
    new_double_list = []
    for each in double_list:
        new_double_list = new_double_list + [sum(each)]
    return(new_double_list)

def yahtzee(double_list):
    new_total = 0
    for each in double_list: 
        total = 0           
        for every in each:              
            if each[0] != every:        
                total = total + 0
            else:
                total = total + 1
        if total == (len(each)):
            new_total = new_total + 1
    return(new_total)

def main():
    total = 0 #Just here for the purposes of the below.

if __name__ == "__main__":
    main()
