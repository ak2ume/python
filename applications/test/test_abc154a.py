# -*- coding: utf-8 -*-

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from AtCoder import abc154a

def test_abc154a(input, exp):
    ngCnt = 0
    (res_a, res_b) = abc154a.abc154a(input[0], input[1], input[2], input[3], input[4])
    if(res_a != exp[0]):
        ngCnt += 1
        #print("res_a NG!!!")
    if(res_b != exp[1]):
        ngCnt += 1
        #print("res_b NG!!!")
    return ngCnt

####
# main

test_result = 0

# test1
input1 = ("red", "blue", 3, 4, "red")
exp1 = (2, 4)
if( 0 < test_abc154a(input1, exp1) ):
    print("test_abc154a pattern1 NG!!!")
    test_result += 1

# test2
input2 = ("red", "blue", 5, 5, "blue")
exp2 = (5, 4)
if( 0 < test_abc154a(input2, exp2) ):
    print("test_abc154a pattern2 NG!!!")
    test_result += 1

if(test_result == 0):
    print("test_abc154a PASSED!!")

print("test_abc154a finished.")
