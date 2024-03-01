#!/usr/bin/env python

# import libraries
import os, sys, string
from Numeric import *
from stats import *
from math import *

# open file for the reading mode
statfile = open('data_1.dat', 'r') ;# the file name is given directly
#statfile = open(sys.argv[1], 'r')   ;# the file name is taken from the prompt line

# variable initialisation
sum_clmn_1 = 0
sum_clmn_2 = 0

# processing the file line by line
for line in statfile:
    words = string.split(line)      ;# split the line word by word and assign
# the resulting words in the "words" array

    sum_clmn_1 += float(words[0])   ;# sum up the data on the 1st column
    sum_clmn_2 += float(words[1])   ;# sum up the data on the 2d column

# compare the sum of two columns
if sum_clmn_1 == sum_clmn_2:
    print sum_clmn_1, '==', sum_clmn_2
else:
    print sum_clmn_1, '!=', sum_clmn_2
