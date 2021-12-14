#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 22:23:12 2021

@author: mati
"""

import time
start = time.time()
with open('input', 'r') as file:
	template = file.readline().strip()
	file.readline()
	rules = {}
	while True:
		line = file.readline().strip()
		line = line.split(' -> ')
		if len(line) != 2:
			break
		rules[line[0]] = line[1]
pairs = {}
for i in range(0,len(template)-1):
	pair = template[i:i+2]
	if pair in pairs:
		pairs[pair] = pairs[pair] + 1
	else:
		pairs[pair] = 1
occ = {template[0]:1}
for step in range(0,40):
	polymer = {}
	for key in pairs:
		letter = rules[key]
		pair = ''.join([key[0], letter])
		if pair in polymer:
			polymer[pair] = polymer[pair] + pairs[key]
		else:
			polymer[pair] = pairs[key]
		pair = ''.join([letter, key[1]])
		if pair in polymer:
			polymer[pair] = polymer[pair] + pairs[key]
		else:
			polymer[pair] = pairs[key]
	pairs = polymer.copy()
for key in pairs:
	if key[1] not in occ:
		occ[key[1]] = pairs[key]
	else:
		occ[key[1]] = occ[key[1]] + pairs[key]
answer = max(occ.values()) - min(occ.values())
print('Answer: ' + str(answer))
end = time.time()
print('Execution time: ' + str(end-start))