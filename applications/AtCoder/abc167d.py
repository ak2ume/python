# -*- coding: utf-8 -*-

###
# main
if(__name__ == '__main__'):
    # input
    n, k = map(int, input().split(" "))
    a = list(map(int, input().split(" ")))

    pos_li = []
    tele_dic = {}
    current = 0
    ans = 0
    for i in range(k):
        if current in tele_dic:
            # detect loop
            cycle = i - tele_dic[current]
            mod = (k - tele_dic[current]) % cycle
            ans = pos_li[tele_dic[current]+mod]
            break
        else:
            pos_li.append(current)
            tele_dic[current] = i
            current = a[current]-1
    else:
        ans = current

    # output
    print(ans+1)
# else:
    # do nothing
