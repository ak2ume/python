# -*- coding: utf-8 -*-

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from AtCoder import abc155b

def test_abc155b(num, input, exp):
    ngCnt = 0
    res = abc155b.abc155b(num, input)
    if(res != exp):
        ngCnt += 1
    return ngCnt

####
# main

test_result = 0

# test1
input_num1 = 5
input1 = (6, 7, 9, 10, 31)
exp1   = True
if( 0 < test_abc155b(input_num1, input1, exp1) ):
    print("test_abc155b pattern1 NG!!!")
    test_result += 1

# test2
input_num2 = 3
input2 = (28, 27, 24)
exp2   = False
if( 0 < test_abc155b(input_num2, input2, exp2) ):
    print("test_abc155b pattern2 NG!!!")
    test_result += 1

if(test_result == 0):
    print("test_abc155b PASSED!!")

print("test_abc155b finished.")
