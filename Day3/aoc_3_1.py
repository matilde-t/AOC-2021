#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 15:34:36 2021

@author: mati
"""

import numpy as np
f = open("./input", "r")
lines = f.readlines()
one_occ = np.zeros([len(lines[0])-1,1])
zero_occ = np.zeros([len(lines[0])-1,1])
for line in lines:
  for i in range(0,len(line)-1):
    if line[i] == "1":
      one_occ[i]=one_occ[i]+1
    else:
      zero_occ[i]=zero_occ[i]+1
gamma_bool = one_occ > zero_occ
gamma_list = [str(int(gamma_bool[i])) for i in range(0,len(gamma_bool))]
gamma = int(''.join(gamma_list), base=2)
epsilon_bool = ~gamma_bool
epsilon_list = [str(int(epsilon_bool[i])) for i in range(0,len(epsilon_bool))]
epsilon = int(''.join(epsilon_list), base=2)
print(gamma*epsilon)

