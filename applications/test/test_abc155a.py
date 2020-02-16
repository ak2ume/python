# -*- coding: utf-8 -*-

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from AtCoder import abc155a

def test_abc155a(input, exp):
    ngCnt = 0
    res = abc155a.abc155a(input)
    if(res != exp):
        ngCnt += 1
    return ngCnt

####
# main

test_result = 0

# test1
input1 = (5, 7, 5)
exp1   = True
if( 0 < test_abc155a(input1, exp1) ):
    print("test_abc155a pattern1 NG!!!")
    test_result += 1

# test2
input2 = (4, 4, 4)
exp2   = False
if( 0 < test_abc155a(input2, exp2) ):
    print("test_abc155a pattern2 NG!!!")
    test_result += 1

# test3
input3 = (4, 9, 6)
exp3   = False
if( 0 < test_abc155a(input3, exp3) ):
    print("test_abc155a pattern3 NG!!!")
    test_result += 1

if(test_result == 0):
    print("test_abc155a PASSED!!")

print("test_abc155a finished.")
