# -*- coding: utf-8 -*-

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from AtCoder import abc154a

test_result = 0

# test1
(res_a1, res_b1) = abc154a.abc154a("red", "blue", 3, 4, "red")
(exp_a1, exp_b1) = (2, 4)
if(res_a1 != exp_a1):
    test_result += 1
    print("test1a NG!!!")
if(res_b1 != exp_b1):
    test_result += 1
    print("test1b NG!!!")

# test2
(res_a2, res_b2) = abc154a.abc154a("red", "blue", 5, 5, "blue")
(exp_a2, exp_b2) = (5, 4)
if(res_a2 != exp_a2):
    test_result += 1
    print("test2a NG!!!")
if(res_b2 != exp_b2):
    test_result += 1
    print("test2b NG!!!")

# finished
if(test_result == 0):
    print("test PASSED!!")

print("test finished.")
