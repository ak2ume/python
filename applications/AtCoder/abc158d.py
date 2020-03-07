# -*- coding: utf-8 -*-

def abc158d(s_init, n, query):
    ans = s_init
    reverse = 0
    for i in range(n):
        tgt = query[i]
        if tgt[0] == "1":
            reverse = (reverse + 1) % 2
        elif tgt[0] == "2":
            if tgt[1] == "1":
                if reverse == 0:
                    ans = tgt[2] + ans
                else:
                    ans = ans + tgt[2]
            elif tgt[1] == "2":
                if reverse == 0:
                    ans = ans + tgt[2]
                else:
                    ans = tgt[2] + ans
            else:
                print("invalid query!!:" + str(tgt[0]) + str(tgt[1]))
        else:
            print("invalid query!!:" + str(tgt[0]))
    if reverse == 0:
        return ans
    else:
        return ans[::-1]

###
# main
if(__name__ == '__main__'):
    # input
    s_init = input()
    n = int(input())
    query = []
    for i in range(n):
        query.append(input().split(" "))
    
    accomplishment = abc158d(s_init, n, query)
    
    # output
    print(accomplishment)
# else:
    # do nothing
