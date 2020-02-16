# -*- coding: utf-8 -*-

def abc155b(num, s):
    b = True

    for i in range(0, num):
        if(s[i] % 2 == 0):
            if(s[i] % 3 == 0):
                continue
            elif(s[i] % 5 == 0):
                continue
            else:
                b = False

    return(b)

###
# main
if(__name__ == '__main__'):
    # input
    num = int(input())
    s = list(map(int, input().split(" ")))

    b = abc155b(num, s)

    # output
    if( True == b ):
        print("APPROVED")
    else:
        print("DENIED")
# else:
    # do nothing
