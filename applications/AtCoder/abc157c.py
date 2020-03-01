# -*- coding: utf-8 -*-

def abc157c(n, m, constraint):
    # check constraint
    for i in range(m):
        if n > 1:
            if (constraint[i][0] == 1) and (constraint[i][1] == 0):
                return -1
        if constraint[i][0] > n:
            return -1
        for j in range(i+1, m):
            if constraint[i][0] == constraint[j][0]:
                if constraint[i][1] != constraint[j][1]:
                    return -1

    min_val = 0
    if n > 1:
        min_val = 10**(n-1)
    
    for tgt in range(min_val, 10**n):
        match = True
        for c in constraint:
            exp = n - c[0]
#            print("exp="+str(exp))
            if (tgt // 10**exp) % 10 == c[1]:
#                print("match!"+str(c[0])+str(c[1]))
                continue
            else:
                match = False
                break
        if match:
            return tgt
    
    return -1

###
# main
if(__name__ == '__main__'):
    # input
    n, m = map(int, input().split())

    constraint = [[] for _ in range(m)]
    for i in range(m):
        constraint[i] = list(map(int, input().split(" ")))
    
    ans = abc157c(n, m, constraint)
    
    # output
    print(ans)
# else:
    # do nothing
