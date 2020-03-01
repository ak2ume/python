# -*- coding: utf-8 -*-

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from AtCoder import abc157c

def test_abc157c(input, exp):
    ngCnt = 0
    res_a = abc157c.abc157c(input[0], input[1], input[2])
    if(res_a != exp[0]):
        ngCnt += 1
        #print("res_a NG!!!")
    return ngCnt

####
# main

test_result = 0

# test1
input1n = 3
input1m = 3
input1cnstr = [
    [1,7],
    [3,2],
    [1,7],
    ]

input1 = (input1n, input1m, input1cnstr)
exp1 = [702]
if( 0 < test_abc157c(input1, exp1) ):
    print("test_abc157c pattern1 NG!!!")
    test_result += 1

# test2
input2n = 3
input2m = 2
input2cnstr = [
    [2,1],
    [2,3],
    ]

input2 = (input2n, input2m, input2cnstr)
exp2 = [-1]
if( 0 < test_abc157c(input2, exp2) ):
    print("test_abc157c pattern2 NG!!!")
    test_result += 1

# test3
input3n = 3
input3m = 1
input3cnstr = [
    [1,0],
    ]

input3 = (input3n, input3m, input3cnstr)
exp3 = [-1]
if( 0 < test_abc157c(input3, exp3) ):
    print("test_abc157c pattern3 NG!!!")
    test_result += 1

if(test_result == 0):
    print("test_abc157c PASSED!!")

print("test_abc157c finished.")
