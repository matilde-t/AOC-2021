#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 10:31:10 2021

@author: mati
"""

count = 0
with open('input.txt', 'r') as f:
	while True:
		parts = f.readline().split('|')
		if len(parts)!=2:
			break
		digits = parts[1].split()
		for digit in digits:
			if len(digit) == 2 or len(digit) == 4 or len(digit) == 3\
				or len(digit) == 7:
					count = count+1
print(count)