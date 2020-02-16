# -*- coding: utf-8 -*-

def abc155a(s):
    b = False
    if( s[0] == s[1] ):
        if(s[2] != s[0]):
            b = True
    if( s[1] == s[2] ):
        if(s[0] != s[1]):
            b = True
    if( s[2] == s[0] ):
        if(s[1] != s[2]):
            b = True
    return(b)

###
# main
if(__name__ == '__main__'):
    # input
    s = input().split(" ")

    b = abc155a(s)

    # output
    if( True == b ):
        print("Yes")
    else:
        print("No")
# else:
    # do nothing
