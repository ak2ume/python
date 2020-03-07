# -*- coding: utf-8 -*-

def abc158b(n, a, b):
    num_b = 0
    if a+b != 0:
        rep = n // (a+b)
        mod = n % (a+b)
        num_b = rep * a
        if mod < a:
            num_b += mod
        else:
            num_b += a

    return num_b

###
# main
if(__name__ == '__main__'):
    # input
    n, a, b = map(int, input().split(" "))
    
    accomplishment = abc158b(n, a, b)
    
    # output
    print(accomplishment)
# else:
    # do nothing
