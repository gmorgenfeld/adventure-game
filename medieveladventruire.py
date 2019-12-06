from random import *
from time import *
from type import *
#strength power setp
attack = 0
rage = False
determine = False
#speed power setp
agile = False
runner = False
#chrsma power setp
peacemake = False
talker = False
leader = False
#precpt power setp
ears = False
seecoming = False
looter = False
#intro

type('You there!')
sleep(1)
type('Yes you! What is your name!')
name=input('What is your name?: ')


type (name + '!')
type ('By the order of the King of Ceteron, I order you to join our Great Army in the fight against the ruthless, pillaging Yothil Dynasty!')
sleep(2)
type('The man takes you to a caravan. You get in, not realizeing that that would be the last time you would see peace for a while')
sleep(5)
type('Two weeks later')
sleep(1)
type('You\'re on the frontlines, all you can see is smoke and fire. People around you fall to their knees. Chests filled with the Dynastys deadly arrows.')
sleep(1)
type('All you can think about is where you could be besides here, then someone yells to get in the trenches.')
type('You do so, as it is a safer place')
sleep(1)
type('Then a boulder, one from the catapults, rolls over the trench, crushing people and collapsing the dirt around you. You barely get the chance to drop down and you are saved by inches from the boulder.')
sleep(1)
type('Time passes, nobody comes to help. You realize that you are going to have to get off the battlefield alone.')
sleep(1)
type('You slowly slip out from under the boulder, careful not to collapse anything else. You step through puddles of blood and flesh. Finally you make it out. It is much calmer now, but still deadly')
sleep(1)
type('You see a forest through the smoke and you sprint for it, trying to stay low. The arrows whiz past your ear and one hits your ankle. You dive into the brush and sit for a minute')
sleep(1)
type('Your character is your character and needs to be customized. You have a set of skills. Strength, speed, perception, and charisma. If you have 8 or more points in a catagory, you get to choose a power! You only have 20 points, so choose wisely!')
sleep(1)
#skills

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
             
#super stats
        
    if strength >= 8:
        done = False
        
        type('You are strong enough to choose a special power!')
        type('(One): Determined: +' + str(strength) + ' extra attack per level up')
        type('(Two): Rage: *3 attack on choice of one attack in battle, once per battle')
        type('(Three): Rough Beginnings: +25 attack right from start')
        while not done:
            strengthpower = input('Which power? (One, Two, Three): ').lower()
            if strengthpower == 'one':
                type('You have selected Determined: +' + str(strength) + ' extra attack per level up. ')
                done = True
                determine = True
            elif strengthpower == 'two':
                type('You have selected: Rage: *3 attack on choice of one attack in battle, once per battle')
                rage = True
                done = True

            elif strengthpower == 'three':
                type('You have selected: Rough Beginnings: +25 attack right from start')
                attack =+ 25
                type('You now have ' + str(attack) + ' attack!')
                done = True

            else:
                done = True
                
                type('Please choose one of the options')
           
        
    if speed >= 8:
        done = False

        type('You are fast enough to choose a special power!')
        type('(One): Runner: Allows you to run from any battle with an enemy 5 levels away from you. (No bosses)')
        type('(Two): Agile: Allows you to attack twice, once per battle')
        type('(Three): Not the strongest: -2 strength, +2 speed')
        while not done:
            speedpower = input('Which power? (One, Two, Three): ').lower()
            if speedpower == 'one':
                type('You chose Runner: Allows you to run from any battle with an enemy 5 levels away from you. (No bosses)')
                runner = True
                done = True
            elif speedpower == 'two':
                type('You chose: Agile: Allows you to attack twice, once per battle')
                agile = True
                done = True
            elif speedpower == 'three':
                type('You chose: Not the strongest: -2 strength, +2 speed')
                strength -= 2
                speed += 2

                type('You now have ' + str(speed) + ' speed!')
                done = True
            else:
                
                type('Please choose one of the options')
                done = True
#ADD REAL STATS HERE NEXT
    if chrsma >= 8:
        done = False

        type('You can persuade so well, you can choose a special power!')
        type('(One): Smooth Talker: All prices are lowered by 25% from any seller')
        type('(Two): Peacemaker: You can call off any battle with any enemy within 5 levels of you, and you regain all health from that fight')
        type('(Three): Great Leader: All followers are 1.5* as effective')
        while not done:
            chrsmapower = input('Which power? (One, Two, Three): ').lower()
            if chrsmapower == 'one':
                type('You chose: Smooth Talker: All prices are lowered by 25% from any seller')
                talker = True

                done =True

            elif chrsmapower == 'two':
                type('You chose: Peacemaker: You can call off any battle with any enemy within 5 levels of you, and you regain all health from that fight')
                peacemake = True
                done = True

            elif chrsmapower == 'three':
                type('You chose: Great Leader: All followers are 1.5* as effective')
                leader = True
                done = True

            else:

                type('Please choose one of the options')
                done = True


    if percpt >= 8:
        done = False

        type('You have such great perception, you can choose a special power!')
        type('(One): Big Ears: You are able to see who you will be fighting before you enter the battle')
        type('(Two): See It Coming: You can no longer be jump attacked')
        type('(Three): Looter: You now have a better chance to find more effective items')
        while not done:
            percptpower = input('Which power? (One, Two, Three): ').lower()
            if percptpower == 'one':
                type('You chose: Big Ears: You are able to see who you will be fighting before you enter the battle')
                ears = True
                done =True

            elif percptpower == 'two':
                type('You chose: See It Coming: You can no longer be jump attacked')
                seecoming = True
                done = True

            elif percptpower == 'three':
                type('You chose: Looter: You now have a better chance to find more effective items')
                looter = True
                done = True

            else:

                type('Please choose one of the options')
                done = True

    


    makesure=input('This will be your character for the game. Is this how you want it? (y/n):  ')
    if makesure == 'n':
        game()




    #JOURNEY BEGINS HERE

    escape = True
    
    type ('You now hear voices in the distance, coming towards you.')
    sleep(1)
    type ('You quickly turn your head to the forest to find an escape.')
    sleep(1)
    type ('You see a waterfall that drops far below, a dense forest, and a steep uphill into snow and ice.')
    while escape == True:
        firstescape=input('What do you use to escape: 1. Waterfall, 2. Forest, 3. Uphill: ').lower()

        if firstescape == 'waterfall':
            type ('You decide that taking your chance in the water is the best choice. You sprint to the waterfall and take a dive......')
            sleep(3)
            type('After a long, wet, travel, you wind up in a shallow river. You check your surroundings to find a small village with a fisherman on a pier staring at you.')
            type('You swim to him, and he pulls you out of the water.')
            type('Good sir! Are you ok? I will give you some dry clothing. He then fetches you a new set of clothes.')
            sleep(1)
            type('You now own a sturdier set of clothes, which gives you a boost to attack')
            escape = False
        elif firstescape == 'forest':
            type ('You decide that cover in the forest is the best option. You jump in the trees and run without being able see because of the trees.....')
            escape = False
        elif firstescape == 'uphill':
            type ('You trust your legs and endurance in running up a hill. You begin up the hill into the icey cold......')
            
            escape = False
        else:
            escape = True
            
#ADD REAL STATS HERE NEXT

game()
    
            
