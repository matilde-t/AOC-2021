#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 12:13:41 2021

@author: mati
"""

import time
start = time.time()
with open('input.txt', 'r') as file:
	crabs = list(map(int, file.readline().split(',')))
min_fuel = float('inf')
for pos in range(min(crabs), max(crabs)+1):
	fuel = 0
	for crab in crabs:
		fuel = fuel + ((abs(crab-pos))*(abs(crab-pos)+1)/2)
	min_fuel = min(fuel, min_fuel)
print('Min fuel: ' + str(min_fuel))
end = time.time()
print('Execution time: ' + str(end-start))