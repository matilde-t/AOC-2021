#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 19:19:51 2021

@author: mati
"""

with open('original_example.txt', 'r') as fin:
	with open('my_example.txt', 'w') as fout:
		while True:
			line = list(map(int, fin.readline().split(',')))
			if len(line) == 0:
				break
			print(str(len(line)), file=fout)