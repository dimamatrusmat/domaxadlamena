#!/usr/bin/python
from random import random, randrange, getrandbits, randint
import random as rand

import time


class generate():
	def random_number():
		return int(randint(1,100))

def reversed_str():
	input_text = input()
	rever_text = ''.join((reversed(list(input_text))))
	summintext = ''
	i = 0
	while True:
		if (i == 0):
			summintext += input_text
			i = 1
		else:
			summintext += rever_text
			i = 0
		print(summintext)


words = input()
while True:
	
	if words == '4':
		reversed_str()
	elif words.lower() == 'Кирилл':
		print('Человек')
	elif words.lower() == '5':
		i = 0
		sum_g = 0

		while True:
			rand_g = rand.uniform(0.000001,0.02)
			if (i != 100 and i <= 100):
			 	print('Взлом Пентагона {0}% \n'.format(i))
				
			 	time.sleep(rand_g)
			 	sum_g = sum_g + rand_g
			 	i = i + 1
			elif (i == 100):
				random_number = generate()
				if (random_number == 50):
					print('Пентагон успешно взломан за {0} секунд'.format(round(sum_g, 2)))
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