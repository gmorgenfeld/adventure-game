from random import *
from time import *
from type import *
#intro
user=input('Please enter you name: ')
type('Welcome ' + user + ' to the dangerously, amazing world of medieval land! I am your guide, ernesto! You have been challenged to become the greatest explorer and fighter in all the land!')
sleep(1)
skills
type('You have special skills. Strength, speed, perception, and charisma. You only have 20 points, so use wisely!')
def game() :
    
    points = 20
    strength=int(input('Strength (0-10): '))
    points = points - strength
    if points < 0:
        restrt=input('You have overused your points. Please restart points selection or leave. y/n: ').lower()
        if restrt == 'y':
            game()

        else:
            exit()
             
                
                
    type('You have ' + str(points) + ' left!') 
    speed=int(input('Speed (0-10): '))
    points = points - speed
    if points < 0:
        restrt=input('You have overused your points. Please restart points selection or leave. y/n: ').lower()
        if restrt == 'y':
            game()

        else:
            exit()
         
            
    type('You have ' + str(points) + ' left!')
    percpt=int(input('Perception (0-10): '))
    points = points - percpt
    if points < 0:
        restrt=input('You have overused your points. Please restart points selection or leave. y/n: ').lower()
        if restrt == 'y':
            game()

        else:
            exit()
         
            
    type('You have ' + str(points) + ' left!')
    chrsma=int(input('Charisma (0-10): '))
    points -= chrsma
    if points < 0:
        restrt=input('You have overused your points. Please restart points selection or leave. y/n: ').lower()
        if restrt == 'y':
            game()

        else:
            exit()
             
    
    if strength >= 8:
        type('You are strong enough to choose a special power!')
        type('(One): Determined: +' + str(strength) + ' extra attack per level up')
        type('(Two): Rage: *3 attack on choice of one attack in battle, once per battle')
        type('(Three): Rough Beginnings: +25 attack right from start')
        strengthpower = input('Which power? (One, Two, Three): ').lower()
        if strengthpower == 'one':
            type('You have selected Determined: +' + str(strength) + ' extra attack per level up. ')
#ADD EXTRA STATS HERE NEXT
        if strengthpower == 'two':
            type('You have selected: Rage: *3 attack on choice of one attack in battle, once per battle')

        if strengthpower == 'three':
            type('You have selected: Rough Beginnings: +25 attack right from start')





game()
            

