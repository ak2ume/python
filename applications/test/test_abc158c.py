# -*- coding: utf-8 -*-

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from AtCoder import abc158c

def test_abc158c(input, exp):
    ngCnt = 0
    res_a = abc158c.abc158c(input[0], input[1])
    if(res_a != exp[0]):
        ngCnt += 1
        #print("res_a NG!!!")
    return ngCnt

####
# main

test_result = 0

# test1
input1 = [
    2, 2,
]
exp1 = [25, ]
if( 0 < test_abc158c(input1, exp1) ):
    print("test pattern1 NG!!!")
    test_result += 1

# test2
input2 = [
    8, 10,
]
exp2 = [100, ]
if( 0 < test_abc158c(input2, exp2) ):
    print("test pattern2 NG!!!")
    test_result += 1

# test3
input3 = [
    19, 99,
]
exp3 = [-1, ]
if( 0 < test_abc158c(input3, exp3) ):
    print("test pattern3 NG!!!")
    test_result += 1

if(test_result == 0):
    print("test PASSED!!")

print("test_abc158c finished.")
