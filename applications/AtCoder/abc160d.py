# -*- coding: utf-8 -*-
def abs(n):
    if n < 0:
        return -n
    else:
        return n

def min(a, b):
    if a < b:
        return a
    else:
        return b

def abc160d(n, x_in, y_in):
    d_arr = [0 for _ in range(n-1)]
    x = x_in - 1
    y = y_in - 1
    for a in range(0,n):
        for tgt in range(a+1,n):
            d_normal = tgt - a
            d_min = d_normal - 1
            if tgt < x or y < a:
                pass
            else:
                d_short = abs(x-a) + 1 + abs(y-tgt)
                d_min = min(d_normal, d_short) - 1

            d_arr[d_min] += 1

    return d_arr    

###
# main
if(__name__ == '__main__'):
    # input
    n, x, y = map(int, input().split(" "))
    
    ans = abc160d(n, x, y)
    
    # output
    for a in ans:
        print(a)
# else:
    # do nothing
