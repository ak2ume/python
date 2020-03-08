# -*- coding: utf-8 -*-

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from AtCoder import hitachi2020b

def test_hitachi2020b(input, exp):
    ngCnt = 0
    res_a = hitachi2020b.hitachi2020b(input[0], input[1], input[2])
    if(res_a != exp[0]):
        ngCnt += 1
        #print("res_a NG!!!")
    return ngCnt

####
# main

test_result = 0

# test1
input1_a = [
    3, 3,
]

input1_b = [
    3, 3, 3,
]

input1discount = [
    [1, 2, 1, ],
]

input1 = (input1_a, input1_b, input1discount)
exp1 = [5]
if( 0 < test_hitachi2020b(input1, exp1) ):
    print("test pattern1 NG!!!")
    test_result += 1

# test2
input2_a = [
    10,
]

input2_b = [
    10,
]

input2discount = [
    [1, 1, 5, ],
    [1, 1, 10, ],
]

input2 = (input2_a, input2_b, input2discount)
exp2 = [10]
if( 0 < test_hitachi2020b(input2, exp2) ):
    print("test pattern2 NG!!!")
    test_result += 1

# test3
input3_a = [
    3, 5,
]

input3_b = [
    3, 5,
]

input3discount = [
    [2, 2, 2, ],
]

input3 = (input3_a, input3_b, input3discount)
exp3 = [6]
if( 0 < test_hitachi2020b(input3, exp3) ):
    print("test pattern3 NG!!!")
    test_result += 1

if(test_result == 0):
    print("test PASSED!!")

print("test_hitachi2020b finished.")
