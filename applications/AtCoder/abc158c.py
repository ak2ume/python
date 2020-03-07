# -*- coding: utf-8 -*-

def abc158c(a, b):
    min_b = b * 10
    for cand in range(min_b, min_b+10):
        if int(cand * 0.08) == a:
            return cand
    
    return -1

###
# main
if(__name__ == '__main__'):
    # input
    a, b = map(int, input().split(" "))
    
    accomplishment = abc158c(a, b)
    
    # output
    print(accomplishment)
# else:
    # do nothing
