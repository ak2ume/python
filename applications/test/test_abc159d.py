# -*- coding: utf-8 -*-

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from AtCoder import abc159d

def test_abc159d(input, exp):
    ngCnt = 0
    res_a = abc159d.abc159d(input[0], input[1])
    if(res_a != exp[0]):
        ngCnt += 1
        #print("res_a NG!!!")
    return ngCnt

####
# main

test_result = 0

# test1
input1_num = 5
input1_arr = [
    "1", "1", "2", "1", "2", 
]
input1 = (input1_num, input1_arr)
exp1 = [
    [2, 2, 3, 2, 3,]
]
if( 0 < test_abc159d(input1, exp1) ):
    print("test pattern1 NG!!!")
    test_result += 1

# test2
input2_num = 4
input2_arr = [
    "1", "2", "3", "4", 
]
input2 = (input2_num, input2_arr)
exp2 = [
    [0, 0, 0, 0,]
]
if( 0 < test_abc159d(input2, exp2) ):
    print("test pattern2 NG!!!")
    test_result += 1

# test3
input3_num = 8
input3_arr = [
    "1", "2", "1", "4", "2", "1", "4", "1", 
]
input3 = (input3_num, input3_arr)
exp3 = [
    [5, 7, 5, 7, 7, 5, 7, 5,]
]
if( 0 < test_abc159d(input3, exp3) ):
    print("test pattern3 NG!!!")
    test_result += 1


if(test_result == 0):
    print("test PASSED!!")

print("test_abc159d finished.")
