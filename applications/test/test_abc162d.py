# -*- coding: utf-8 -*-

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from AtCoder import abc162d

def test_abc162d(input, exp):
    ngCnt = 0
    res_a = abc162d.abc162d(input[0], input[1])
    if(res_a != exp[0]):
        ngCnt += 1
        #print("res_a NG!!!")
    return ngCnt

####
# test data

input_arr = []
exp_arr = []
fail_str_array = []

# test1
input1_num = 4
input1_arr = "RRGB"
input1 = (input1_num, input1_arr)
exp1 = [
    1,
]
fail_str1 = "test pattern1 NG!!!"
input_arr.append(input1)
exp_arr.append(exp1)
fail_str_array.append(fail_str1)

# test2
input2_num = 39
input2_arr = "RBRBGRBGGBBRRGBBRRRBGGBRBGBRBGBRBBBGBBB"
input2 = (input2_num, input2_arr)
exp2 = [
    1800,
]
fail_str2 = "test pattern2 NG!!!"
input_arr.append(input2)
exp_arr.append(exp2)
fail_str_array.append(fail_str2)


####
# test main

test_result = 0
for input, exp, fail_str in zip(input_arr, exp_arr, fail_str_array):
    if( 0 < test_abc162d(input, exp) ):
        print(fail_str)
        test_result += 1

if(test_result == 0):
    print("test PASSED!!")

print("test_abc162d finished.")
