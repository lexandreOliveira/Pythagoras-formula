import math
import menu 
import os
from time import sleep

class color():
    vermelho= '\033[91m'
    verde= '\033[1;32m'
    yellow= '\033[1;33m'
    cyan= '033[1;36m'
    azul= '\033[1;34m'
    branco= '\033[1;97m'

color()

class Pythagoras():
    def __init__(self):
        pass
        
        
    def starting(self):
        os.system('cls')
        menu.menu()
        calculator.user_decision()

    def user_decision(self):
        while True:
            decision=input(f'{color.verde}Choose an option!\n ')
            if decision.lower() == 'h':
                calculator.hypotenuse()
                
            elif decision.lower() == 'b':
                calculator.cathetus_b()
                
            elif decision.lower() == 'c':
                calculator.cathetus_c()
                
            else:
                print(f'{color.vermelho}Mistake!!!\nPlease enter a valid option!!!')

    def hypotenuse(self):
        cathetus_b=float(input(f'{color.yellow}Enter the value of the cathetus B: '))
        cathetus_c=float(input('Enter the value of the cathetus C: '))
        if cathetus_b % 3 == 0 and cathetus_c % 4 == 0:
            hypotenuse = (cathetus_b **2) + (cathetus_c **2)
            print(f'{color.branco}The value of the hypotenuse is: {color.verde}{str((math.sqrt(hypotenuse)))}')
            back_to_start = input(f'{color.branco}Would you like to continue? y/n ')
            if back_to_start.lower() == 'y':
                calculator.starting()
            else:
                print('Thank you!!!')
                sleep(2)
                exit()
        else:
            print(f'{color.vermelho}Sorry, but the triangle you are requesting is not a right triangle!!!')
            retorno=input(f'{color.verde}Would you like to try one more time?\nIf desired, enter "s" for YES and "n" for EXIT: ')
            if retorno.lower() == 's':       
                sleep(2)
                os.system('cls')
                calculator.starting()
            else:
                print(f'{color.verde}See ya...')
                print('Going out...')
 
    def cathetus_b(self):
        hypotenuse=float(input(f'{color.yellow}Enter the value of the hypotenuse: '))
        cathetus_c=float(input('Enter the value of the cathetus C: '))
        if hypotenuse % 5 == 0 and cathetus_c % 4 == 0:                
            cathetus_b = (hypotenuse**2) - (cathetus_c **2)
            print(f'{color.branco} The value of the Cathetus "B" is: {color.verde}{str((math.sqrt(cathetus_b)))}')
            back_to_start_two = input(f'{color.branco}Would you like to continue? y/n ')
            if back_to_start_two.lower() == 'y':
                calculator.starting()
            else:
                print('Thank you!!!')
                sleep(2)
                exit()
        else:
            print(f'{color.vermelho}Sorry, but the triangle you are requesting is not a right triangle!')
            retorno=input(f'{color.verde}Would you like to try one more time?\nIf desired, enter "s" for YES and "n" for EXIT: ')
            if retorno.lower() == 's':       
                sleep(2)
                os.system('cls')
                calculator.starting()
            else:
                print('See ya...')
                print('Going out...')
    
    def cathetus_c(self):
        hypotenuse=float(input(f'{color.yellow}Enter the value of the hypotenuse: '))
        cathetus_b=float(input('Enter the value of the cathetus B: '))
        if hypotenuse % 5 == 0 and cathetus_b % 3 == 0:                
            cathetus_c = (hypotenuse**2) - (cathetus_b **2)
            print(f'{color.branco}The value of the cathetus "C" is: {color.verde}{str((math.sqrt(cathetus_c)))}')
            back_to_start_three = input(f'{color.branco}Would you like to continue? y/n ')
            if back_to_start_three.lower() == 'y':
                calculator.starting()
            else:
                print('Thank you!!!')
                sleep(2)
                exit()
        else:
            print(f'{color.vermelho}Sorry, but the triangle you are requesting is not a right triangle!')
            retorno=input(f'{color.verde}Would you like to try one more time?\nIf desired, enter "s" for YES and "n" for EXIT: ')
            if retorno.lower() == 's':       
                sleep(2)
                os.system('cls')
                calculator.starting()
            else:
                print('See ya...')
                print('Going out...')
                exit()

calculator = Pythagoras() 
calculator.starting()
  

    





