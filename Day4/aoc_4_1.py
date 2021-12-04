#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 13:33:51 2021

@author: mati
"""

import pandas as pd
file = open('input.txt', 'r')
extractions = list(map(int, file.readline().split(',')))
i = 0
tables = {}
while file.readline() == '\n':
	tables[i] = pd.DataFrame([list(map(int, file.readline().split())) for x \
						   in range(5)])
	i = i+1
win = False
for number in extractions:
	for i in range(0, len(tables)):
		tables[i].replace(number, -1, inplace=True)
		if any(tables[i].sum(0) == -5) or any(tables[i].sum(1) == -5):
			win = True
			break
	if win:
		break
tables[i].replace(-1, 0, inplace=True)
print(sum(tables[i].sum())*number)