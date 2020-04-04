# -*- coding: utf-8 -*-

def abc161e(n, k, c, s):
    num_cluster_f = 0
    start = []
    cursor = 0
    while cursor < n:
        if s[cursor] == "x":
            cursor += 1
            continue
        else:
            num_cluster_f += 1
            start.append(cursor)
            cursor += c+1

    if k < num_cluster_f:
        return []

    num_cluster_b = 0
    end = []
    cursor = n-1

    while 0 <= cursor:
        if s[cursor] == "x":
            cursor -= 1
            continue
        else:
            num_cluster_b += 1
            end.append(cursor)
            cursor -= c+1

    if k < num_cluster_b:
        return []

    ans = []
    if num_cluster_b < num_cluster_f:
        num_cluster_f = num_cluster_b
    for s, e in zip(start, end[::-1]):
        if s == e:
            ans.append(s+1)

    return ans

###
# main
if(__name__ == '__main__'):
    # input
    n, k, c = map(int, input().split(" "))
    s = input()
    
    ans = abc161e(n, k, c, s)
    
    # output
    for a in ans:
        print(a)
# else:
    # do nothing
