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
for step in range(0,10):
	polymer = []
	polymer.append(template[0])
	for i in range(0, len(template)-1):
		polymer.append(rules[template[i:i+2]])
		polymer.append(template[i+1])
	template = ''.join(polymer).strip()
letters = set(polymer.copy())
occ = [polymer.count(letter) for letter in letters]
answer = max(occ) - min(occ)
print('Answer: ' + str(answer))
end = time.time()
print('Execution time: ' + str(end-start))