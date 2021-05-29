while True:
	words = input()

	if words == '4':
		while True:
			print('10110101001100101010101'*10 + 'БЕСКОНЕЧНОСТЬ НЕ ПРЕДЕЛ')
	elif words.lower() == 'кирил':
		print('Человек')
	elif words.lower() == 'что я делаю':
		print('сижу')
	else:
		print(words)