# -*- coding: utf-8 -*-

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from AtCoder import abc160d

def test_abc160d(input, exp):
    ngCnt = 0
    res_a = abc160d.abc160d(input[0], input[1], input[2])
    if(res_a != exp[0]):
        ngCnt += 1
        #print("res_a NG!!!")
    return ngCnt

####
# main

test_result = 0

# test1
input1 = [5, 2, 4]
exp1 = [
    [5, 4, 1, 0,]
]
if( 0 < test_abc160d(input1, exp1) ):
    print("test pattern1 NG!!!")
    test_result += 1

# test2
input2 = [3, 1, 3]
exp2 = [
    [3, 0,]
]
if( 0 < test_abc160d(input2, exp2) ):
    print("test pattern2 NG!!!")
    test_result += 1

# test3
input3 = [7, 3, 7]
exp3 = [
    [7, 8, 4, 2, 0, 0,]
]
if( 0 < test_abc160d(input3, exp3) ):
    print("test pattern3 NG!!!")
    test_result += 1

# test4
input4 = [10, 4, 8]
exp4 = [
    [10, 12, 10, 8, 4, 1, 0, 0, 0,]
]
if( 0 < test_abc160d(input4, exp4) ):
    print("test pattern4 NG!!!")
    test_result += 1


if(test_result == 0):
    print("test PASSED!!")

print("test_abc160d finished.")
