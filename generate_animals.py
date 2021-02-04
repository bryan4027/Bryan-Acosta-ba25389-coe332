
import json
import petname
import random

def choose_head():
	n = random.randint(1,5)
	if (n == 1):
		return( f'snake')
	if (n == 2):
                return( f'bull')
	if (n == 3):
                return( f'lion')
	if (n == 4):
                return( f'raven')
	if (n == 5):
                return( f'bunny')	 
def choose_body():
	return(petname.name() + '-' + petname.name())


def choose_arms():
	x = random.randint(2,10)
	return(x)
def choose_legs():
	y = random.randint(3,12)
	return(y)
def calculate_tails(x,y):
	tails = x + y
	return(tails)
	
output = {}
output['animals'] = [] 

for i in range(20):
	x = choose_arms()
	y = choose_legs()
	output['animals'].append( {'head': choose_head(), 'body':choose_body(),'arms':x, 'legs': y, 'tails': calculate_tails(x,y)})

with open('animals.json','w') as out:
	json.dump(output, out, indent = 2)
