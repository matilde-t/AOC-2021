#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 15:34:36 2021

@author: mati
"""

f = open("./input", "r")
lines_original = f.readlines()
ox_lines = lines_original.copy()
co2_lines = lines_original.copy()

### oxygen ###
# for every position
for i in range (0, len(ox_lines[0])-1):
	one_occ = 0
	zero_occ = 0
	ox_list = []
	# count '1' or '0'
	for line in ox_lines:
		if line[i] == '1':
			one_occ = one_occ + 1
		else:
			zero_occ = zero_occ + 1
	# select the values according to the most common value
	if one_occ >= zero_occ:
		for line in ox_lines:
			if line[i] == "1":
				ox_list.append(line)
	else:
		for line in ox_lines:
			if line[i] == "0":
				ox_list.append(line)
	ox_lines = ox_list
	# check if a single value is reached
	if len(ox_list) == 1:
		break

### CO2 ###
# for every position
for i in range (0, len(co2_lines[0])-1):
	one_occ = 0
	zero_occ = 0
	co2_list = []
	# count '1' or '0'
	for line in co2_lines:
		if line[i] == '1':
			one_occ = one_occ + 1
		else:
			zero_occ = zero_occ + 1
	# select the values according to the least common value
	if zero_occ <= one_occ:
		for line in co2_lines:
			if line[i] == "0":
				co2_list.append(line)
	else:
		for line in co2_lines:
			if line[i] == "1":
				co2_list.append(line)
	co2_lines = co2_list
	# check if a single value is reached
	if len(co2_list) == 1:
		break

result = int(ox_list[0], base = 2) * int(co2_list[0], base = 2)
print(result)

f.close()