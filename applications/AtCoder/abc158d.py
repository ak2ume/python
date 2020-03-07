# -*- coding: utf-8 -*-

def abc158d(s_init, n, query):
    head = ""
    tail = ""
    reverse = 0
    for i in range(n):
        tgt = query[i]
        if tgt[0] == "1":
            reverse = (reverse + 1) % 2
        elif tgt[0] == "2":
            if tgt[1] == "1":
                if reverse == 0:
                    head += tgt[2]
                else:
                    tail += tgt[2]
            elif tgt[1] == "2":
                if reverse == 0:
                    tail += tgt[2]
                else:
                    head += tgt[2]
            else:
                print("invalid query!!:" + str(tgt[0]) + str(tgt[1]))
        else:
            print("invalid query!!:" + str(tgt[0]))
    if reverse == 0:
        return head[::-1] + s_init + tail
    else:
        return tail[::-1] + s_init[::-1] + head

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
