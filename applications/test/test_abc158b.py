# -*- coding: utf-8 -*-

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from AtCoder import abc158b

def test_abc158b(input, exp):
    ngCnt = 0
    res_a = abc158b.abc158b(input[0], input[1], input[2])
    if(res_a != exp[0]):
        ngCnt += 1
        #print("res_a NG!!!")
    return ngCnt

####
# main

test_result = 0

# test1
input1 = [
    8, 3, 4,
]
exp1 = [4, ]
if( 0 < test_abc158b(input1, exp1) ):
    print("test pattern1 NG!!!")
    test_result += 1

# test2
input2 = [
    8, 0, 4,
]
exp2 = [0, ]
if( 0 < test_abc158b(input2, exp2) ):
    print("test pattern2 NG!!!")
    test_result += 1

# test3
input3 = [
    6, 2, 4,
]
exp3 = [2, ]
if( 0 < test_abc158b(input3, exp3) ):
    print("test pattern3 NG!!!")
    test_result += 1

if(test_result == 0):
    print("test PASSED!!")

print("test_abc158b finished.")
