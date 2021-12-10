#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec	9 10:31:10 2021

@author: mati
"""

with open('input.txt', 'r') as file:
	lines = 0
	map = {}
	while True:
		line = file.readline()
		if len(line) < 2:
			break
		map[lines] = [int(line[i]) for i in range(0,len(line)-1)]
		lines = lines +1
level =0
for i in range(0,lines):
	for j in range(0,len(map[0])):
		min = 0
		if i > 0:
			if map[i][j] < map[i-1][j]:
				min = min + 1
		else:
			min = min + 1
		if i < lines-1:
			if map[i][j] < map[i+1][j]:
				min = min + 1
		else:
			min = min + 1
		if j > 0:
			if map[i][j] < map[i][j-1]:
				min = min + 1
		else:
			min = min + 1
		if j < len(map[0])-1:
			if map[i][j] < map[i][j+1]:
				min = min + 1
		else:
			min = min + 1
		if min==4:
			level = level + map[i][j] + 1
print(level)