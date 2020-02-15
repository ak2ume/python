# -*- coding: utf-8 -*-

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from AtCoder import abc154b

def test_abc154b(input, exp):
    ngCnt = 0
    res = abc154b.abc154b(input)
    if(res != exp):
        ngCnt += 1
    return ngCnt

####
# main

test_result = 0

# test1
input1 = "sardine"
exp1   = "xxxxxxx"
if( 0 < test_abc154b(input1, exp1) ):
    print("test_abc154b pattern1 NG!!!")
    test_result += 1

# test2
input2 = "xxxx"
exp2   = "xxxx"
if( 0 < test_abc154b(input2, exp2) ):
    print("test_abc154b pattern2 NG!!!")
    test_result += 1

# test3
input3 = "gone"
exp3   = "xxxx"
if( 0 < test_abc154b(input3, exp3) ):
    print("test_abc154b pattern3 NG!!!")
    test_result += 1

if(test_result == 0):
    print("test_abc154b PASSED!!")

print("test_abc154b finished.")
