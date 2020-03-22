# -*- coding: utf-8 -*-

def abc159d(n, arr):
    dic = {}
    for a in arr:
        if a in dic:
            dic[a] += 1
        else:
            dic[a] = 1
    
    # delete non-paired ball
    del_list = []
    for k, val in dic.items():
        if val == 1:
            del_list.append(k)
    for item in del_list:
        del dic[item]

    typ_ans = 0
    for val in dic.values():
        typ_ans += val * (val-1) // 2
    
    ans = []
    for a in arr:
        sum = typ_ans
        if a in dic:
            sum -= dic[a] * (dic[a]-1) // 2
            new_val = dic[a] - 1
            sum += new_val * (new_val-1) // 2

        ans.append(sum)

    return ans

###
# main
if(__name__ == '__main__'):
    # input
    n = int(input())
    arr = input().split(" ")
    
    ans = abc159d(n, arr)
    
    # output
    for a in ans:
        print(a)
# else:
    # do nothing
