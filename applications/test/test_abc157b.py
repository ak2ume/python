# -*- coding: utf-8 -*-

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from AtCoder import abc157b

def test_abc157b(input, exp):
    ngCnt = 0
    res_a = abc157b.abc157b(input[0], input[1])
    if(res_a != exp[0]):
        ngCnt += 1
        #print("res_a NG!!!")
    return ngCnt

####
# main

test_result = 0

# test1
input1Bingo = [
     [84, 97, 66,],
     [79, 89, 11,],
     [61, 59,  7,],
     ]

input1Num = [
    89,
    7,
    87,
    79,
    24,
    84,
    30,
    ]

input1 = (input1Bingo, input1Num)
exp1 = ["Yes"]
if( 0 < test_abc157b(input1, exp1) ):
    print("test_abc157b pattern1 NG!!!")
    test_result += 1

# test2
input2Bingo = [
     [41, 7, 46,],
     [26, 89, 2,],
     [78, 92, 8,],
     ]

input2Num = [
    6,
    45,
    16,
    57,
    17,
    ]

input2 = (input2Bingo, input2Num)
exp2 = ["No"]
if( 0 < test_abc157b(input2, exp2) ):
    print("test_abc157b pattern2 NG!!!")
    test_result += 1

if(test_result == 0):
    print("test_abc157b PASSED!!")

print("test_abc157b finished.")
