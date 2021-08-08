# -*- coding: utf-8 -*-
"""
Read inputs
Created on Mon Jul 26 14:43:45 2021

Python code to read text file containing input variables

Setup:
Line by line input start with variable name (no space) followed by space
and variable value
comment line must follow the same pattern
e.g.
# comment_description_with_no_space

Customization in the code:
use the same variable names designated in the input file
for this sample code, read_inputs_test.txt is the corresponding input file
to read variables from

Note: input variable can be in any vertical order


This version of reading file will read input file as long as comma characters
are not existance in the input file & the variable name cannot have space

@author: Tri Deri Setiyono
"""

file = open('read_inputs_test.txt')
for line in file:
    fields = line.strip().split()
    if fields[0] == 'var_A': var_A = fields[1]
    if fields[0] == 'var_B': var_B = fields[1]
    if fields[0] == 'var_C': var_C = fields[1]
    if fields[0] == 'var_D': var_D = fields[1]


# Test by printing variables being read
print('var_D ', var_D)
print('var_C ', var_C)         
print('var_B ', var_B)         
print('var_A ', var_A)                  