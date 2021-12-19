#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 11:54:02 2021

@author: mati
"""

import math

def magnitude(tot):
	while True:
		if len(tot) == 1:
			return tot[0]
		idx = -1
		for char in tot:
			idx = idx + 1
			if type(char) == int and type(tot[idx+2]) == int:
				val = 3*char + 2*tot[idx+2]
				tot[idx-1] = val
				tot = tot[:idx] + tot[idx+4:]
				break

def explode(tot, idx):
	arr = []
	if type(tot[idx+2]) != int:
		arr.append(tot)
		arr.append(False)
		return arr
	val = tot.pop(idx)
	j = idx
	while j>0:
		if type(tot[j]) == int:
			tot[j] = tot[j] + val
			break
		else:
			j = j-1
	tot.pop(idx)
	val = tot.pop(idx)
	j = idx
	while j<len(tot):
		if type(tot[j]) == int:
			tot[j] = tot[j] + val
			break
		else:
			j = j+1
	tot.pop(idx)
	tot[idx-1] = 0
	arr.append(tot)
	arr.append(True)
	return arr

def split(tot, idx):
	val = tot[idx]
	tot[idx] = '['
	tot.insert(idx+1, math.floor(val/2))
	tot.insert(idx+2, ',')
	tot.insert(idx+3, math.ceil(val/2))
	tot.insert(idx+4, ']')

def reduce(tot):
	action = True
	while action:
		leftbr = 0
		action = False
		idx = -1
		expl = False
		for char in tot:
			idx = idx + 1
			if char == '[':
				leftbr = leftbr + 1
			elif char == ']':
				leftbr = leftbr - 1
			elif char == ',':
				continue
			elif leftbr >= 5:
				arr = explode(tot, idx)
				tot = arr[0]
				action = arr[1]
				if action:
					expl = True
					break
		if not expl:
			idx = -1
			for char in tot:
				idx = idx + 1
				if type(char) == int and char >= 10:
					split(tot, idx)
					action = True
					break
	return tot

def add(tot, number):
	res = []
	res.append('[')
	res.extend(tot)
	res.append(',')
	res.extend(number)
	res.extend(']')
	return res

def transform(number):
	res = []
	num = ''
	for char in number:
		if char == '[':
			res.append(char)
		elif char == ']':
			if len(num) != 0:
				res.append(int(num))
				num = ''
			res.append(char)
		elif char == ',':
			if len(num) != 0:
				res.append(int(num))
				num = ''
			res.append(char)
		else:
			num = num + char
	return res

with open('input', 'r') as file:
	lines = file.readlines()

### part 1 ###
tot = transform(lines[0].strip())
for i in range(1, len(lines)):
		tot = reduce(add(tot, transform(lines[i].strip())))
mag = magnitude(tot)
print('Final magnitude: ' + str(mag))

### part 2 ###
maxmag = -float('inf')
for i in range(0, len(lines)):
	for j in range(0, len(lines)):
		mag = magnitude(reduce(add(transform(lines[i].strip()),\
							  transform(lines[j].strip()))))
		if mag > maxmag:
			maxmag = mag
print('Largest magnitude: ' + str(maxmag))