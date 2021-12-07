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
max_crab = max(crabs)
min_crab = min(crabs)
min_fuel = float('inf')
for pos in range(min_crab, max_crab+1):
	fuel = 0
	for crab in crabs:
		fuel = fuel + ((abs(crab-pos))*(abs(crab-pos)+1)/2)
	if fuel < min_fuel:
		min_fuel = fuel
print('Min fuel: ' + str(min_fuel))
end = time.time()
print('Execution time: ' + str(end-start))