# -*- coding: utf-8 -*-

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from AtCoder import abc155c

def test_abc155c(num, input, exp):
    ngCnt = 0
    res = abc155c.abc155c(num, input)
    for i in range(0, len(exp)):
        if(res[i] != exp[i]):
            ngCnt += 1
    return ngCnt

####
# main

test_result = 0

# test1
input_num1 = 7
input1 = [
    "beat",
    "vet",
    "beet",
    "bed",
    "vet",
    "bet",
    "beet" ]
exp1   = [
    "beet",
    "vet" ]
if( 0 < test_abc155c(input_num1, input1, exp1) ):
    print("test_abc155c pattern1 NG!!!")
    test_result += 1

# test2
input_num2 = 8
input2 = [
    "buffalo",
    "buffalo",
    "buffalo",
    "buffalo",
    "buffalo",
    "buffalo",
    "buffalo",
    "buffalo" ]
exp2   = ["buffalo"]
if( 0 < test_abc155c(input_num2, input2, exp2) ):
    print("test_abc155c pattern2 NG!!!")
    test_result += 1

# test3
input_num3 = 7
input3 = [
    "bass",
    "bass",
    "kick",
    "kick",
    "bass",
    "kick",
    "kick" ]
exp3   = [ "kick" ]
if( 0 < test_abc155c(input_num3, input3, exp3) ):
    print("test_abc155c pattern3 NG!!!")
    test_result += 1

# test4
input_num4 = 4
input4 = [
    "ushi",
    "tapu",
    "nichia",
    "kun" ]
exp4   = [
    "kun",
    "nichia",
    "tapu",
    "ushi" ]
if( 0 < test_abc155c(input_num4, input4, exp4) ):
    print("test_abc155c pattern4 NG!!!")
    test_result += 1

if(test_result == 0):
    print("test_abc155c PASSED!!")

print("test_abc155c finished.")
