#!/usr/bin/python
from random import random, randrange, getrandbits, randint
import random as rand

import time


class generate():
	def random_number():
		return int(randint(1,100))

def reversed_str():
	a = input()
	b = ''.join((reversed(list(a))))
	c = ''
	i = 0
	while True:
		if (i == 0):
			c += a
			i = 1
		else:
			c += b
			i = 0
		print(c)


words = input()
while True:
	
	if words == '4':
		reversed_str()
	elif words.lower() == 'Кирилл':
		print('Человек')
	elif words.lower() == '5':
		i = 0
		while True:
			if (i != 100 and i <= 100):
			 	print('Взлом Пентагона {0}% \n'.format(i))
			 	i = i + 1
			 	time.sleep(rand.uniform(0.000001,0.02))
			elif (i == 100):
				a = generate()
				if (a == 50):
					print('Пентагон успешно взломан')
					print('Что выхотите знать?')
					i = 101
				else:
					print('ERROR, TRY AGAIN \n')
					i = 0
			elif (i == 101):
				words = '4'
				reversed_str()
	elif words.lower() == '6':
		print(rand, type(rand))
	elif words.lower() == 'что я делаю':
		print('сижу')
	else:
		print(words)