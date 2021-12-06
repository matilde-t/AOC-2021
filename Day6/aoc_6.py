#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 18:41:02 2021

@author: mati
"""
import time
start = time.time()
days = 256
with open('input.txt', 'r') as file:
	fishes = list(map(int, file.readline().split(',')))
n_fishes = [fishes.count(i) for i in range(0,9)]
for day in range(0, days):
	zeros = n_fishes[0]
	for i in range(1, len(n_fishes)):
		n_fishes[i-1] = n_fishes[i]
	n_fishes[6] = n_fishes[6] + zeros
	n_fishes[8] = zeros
print('Fishes: '+ str(sum(n_fishes)))
end = time.time()
print('Execution time: ' + str(end-start))