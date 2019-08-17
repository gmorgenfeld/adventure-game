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
user=input('Please enter you name: ')
#type('Welcome ' + user + ' to the dangerously, amazing world of medieval land! I am your guide, ernesto! You have been challenged to become the greatest explorer and fighter in all the land!')
sleep(1)
#skills
#type('You have special skills. Strength, speed, perception, and charisma. You only have 20 points, so choose wisely!')
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
                print (attack)
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

    tutorial = True
    #type('Ok! That\'s quite the skillset you\'ve got there! That will take you very far in this world.')
    #type('Now, you need to know how to use those skills in order for them to be useful, however you may already know!')
    tutorial = input('Take the tutorial?(y/n): ').lower
    if tutorial == 'y':
        tutorial = True
    elif tutorial == 'n':
        tutorial = False
    else:
        tutorial = True

        while tutorial == False:
            exit()
            

        while tutorial == True:
            print('yeet')


        

            
        
        
        
    
            
#ADD REAL STATS HERE NEXT

game()
    
            
