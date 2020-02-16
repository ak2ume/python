# -*- coding: utf-8 -*-

def abc154a(s, t, a, b, u):
    if(s == u):
        a -= 1
    else:
        b -= 1
    return(a, b)

###
# main
if(__name__ == '__main__'):
    # input
    (s, t) = input().split()
    (a, b) = map(int, input().split())
    u = input()
    
    (new_a, new_b) = abc154a(s, t, a, b, u)
    
    # output
    print(str(new_a) + " " + str(new_b))
# else:
    # do nothing
