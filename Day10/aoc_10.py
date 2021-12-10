#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 19:32:47 2021

@author: mati
"""

import statistics
points = 0
scores = []
flipped = {'(': ')', '[': ']', '{': '}', '<': '>'}
with open('input.txt', 'r') as file:
	while True:
		line = file.readline().strip()
		if len(line) == 0:
			break
		openings = []
		endings = []
		score = 0
		discarded = False
		for char in line:
			if char in ['(', '[', '{', '<']:
				openings.append(char)
			else:
				el = openings.pop()
				if char != flipped[el]:
					discarded = True
					if char == ')':
						points = points + 3
					elif char == ']':
						points = points + 57
					elif char == '}':
						points = points + 1197
					elif char == '>':
						points = points + 25137
					break
		if discarded:
			continue
		else:
			for i in range(0, len(openings)):
				el = openings.pop()
				endings.append(flipped[el])
			for char in endings:
				score = score * 5
				if char == ')':
					score = score + 1
				elif char == ']':
					score = score + 2
				elif char == '}':
					score = score + 3
				elif char == '>':
					score = score + 4
			scores.append(score)
print('Syntax error score: ' + str(points))
print('Middle score: ' + str(statistics.median(scores)))