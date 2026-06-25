import random


dice = {
        1: (' _______________',
           '|               |',
           '|               |',
           '|               |',
           '|       o       |',
           '|               |',
           '|               |',
           '|_______________|'),

        2: (' _______________',
           '|               |',
           '|   o           |',
           '|               |',
           '|               |',
           '|          o    |',
           '|               |',
           '|_______________|'),
        3: (' _______________',
           '|               |',
           '|   o           |',
           '|               |',
           '|       o       |',
           '|               |',
           '|           o   |',
           '|_______________|'),
        4: (' _______________',
           '|               |',
           '|   o      o    |',
           '|               |',
           '|               |',
           '|               |',
           '|   o      o    |',
           '|_______________|'),

        5: (' _______________',
           '|               |',
           '|  o        o   |',
           '|               |',
           '|       o       |',
           '|               |',
           '|  o        o   |',
           '|_______________|'),

        6: (' _______________',
           '|               |',
           '|  o        o   |',
           '|               |',
           '|  o        o   |',
           '|               |',
           '|  o        o   |',
           '|_______________|')}


def main(dice):
   roll = True
   num_dice = int(input("enter number of dice you wanna roll: "))
   while roll:
      sum = 0
      rollDice = input(f"roll {num_dice} dice(y/n) : ").lower()
      if rollDice == "y":
         for i in range(num_dice):
            num = random.randint(1,6)
            for x in dice[num]:
               print(x)
            sum+=num    
         print(f"total is {sum}")
      else:
         print('thanks for rolling')
         break
main(dice)

