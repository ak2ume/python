# -*- coding: utf-8 -*-

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from AtCoder import abc158d

def test_abc158d(input, exp):
    ngCnt = 0
    res_a = abc158d.abc158d(input[0], input[1], input[2])
    if(res_a != exp[0]):
        ngCnt += 1
        #print("res_a NG!!!")
    return ngCnt

####
# main

test_result = 0

# test1
input1_init = "a"
input1_num = 4
input1_query = [
    ["2", "1", "p", ],
    ["1", ],
    ["2", "2", "c", ],
    ["1", ],
]
input1 = (input1_init, input1_num, input1_query)
exp1 = ["cpa"]
if( 0 < test_abc158d(input1, exp1) ):
    print("test pattern1 NG!!!")
    test_result += 1

# test2
input2_init = "a"
input2_num = 6
input2_query = [
    ["2", "2", "a", ],
    ["2", "1", "b", ],
    ["1", ],
    ["2", "2", "c", ],
    ["1", ],
    ["1", ],
]
input2 = (input2_init, input2_num, input2_query)
exp2 = ["aabc"]
if( 0 < test_abc158d(input2, exp2) ):
    print("test pattern2 NG!!!")
    test_result += 1

# test3
input3_init = "y"
input3_num = 1
input3_query = [
    ["2", "1", "x", ],
]
input3 = (input3_init, input3_num, input3_query)
exp3 = ["xy"]
if( 0 < test_abc158d(input3, exp3) ):
    print("test pattern3 NG!!!")
    test_result += 1


if(test_result == 0):
    print("test PASSED!!")

print("test_abc158d finished.")
