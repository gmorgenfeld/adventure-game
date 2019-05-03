from random import *
from time import *
from type import *
#intro
user=input('Please enter you name: ')
type('Welcome ' + user + ' to the dangerously, amazing world of medieval land! You have been challenged to become the greatest explorer and fighter in all the land!')
sleep(1)
#skills

type('You have special skills. What are they? You only have 20 points, so use wisely!')
points = 20
strength=int(input('Strength (0-10): '))
points = points - strength
type('You have ' + str(points) + ' left!') #'You have ' + str(points) + '  left!'
speed=input('Speed (0-10): ')
points = points - speed
type('You have ' + str(points) + ' left!')
points = points - strength
percpt=input('Perception (0-10): ')
type('You have ' + str(points) + ' left!')
chrsma=input('Charisma (0-10): ')
type('You have ' + str(points) + ' left!')
