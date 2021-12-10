#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 10:40:30 2021

@author: mati
"""

total = 0
with open('input.txt', 'r') as f:
	while True:
		parts = f.readline().split('|')
		if len(parts)!=2:
			break
		examples = parts[0].split()
		seven = set([example for example in examples if len(example)==3][0])
		four = set([example for example in examples if len(example)==4][0])
		lower_left = set([example for example in examples if len(example)==7][0])
		for el in (four.union(seven)):
			lower_left.discard(el)
		digits = parts[1].split()
		i = 0
		output = [0,0,0,0]
		for digit in digits:
			digit = set(digit)
			if len(digit) == 2:
				output[i] = 1
			elif len(digit) == 3:
				output[i] = 7
			elif len(digit) == 4:
				output[i] = 4
			elif len(digit) == 7:
				output[i] = 8
			elif len(digit) == 6:
				if four < digit:
					output[i] = 9
				elif seven < digit:
					output[i] = 0
				else:
					output[i] = 6
			else:
				if seven < digit:
					output[i] = 3
				elif lower_left < digit:
					output[i] = 2
				else:
					output[i] = 5
			i = i+1
		output = output[3]+10*output[2]+100*output[1]+1000*output[0]
		total = total + output
print(total)
