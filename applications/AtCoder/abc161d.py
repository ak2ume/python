# -*- coding: utf-8 -*-

def abc161d(k):
    lunArr = [[] for _ in range(10)]
    lunArr[0] = [1, 2, 3, 4, 5, 6, 7, 8, 9,]

    for keta in range(1,10):
        for elem in lunArr[keta-1]:
            base = elem % 10
            if base == 0:
                lunArr[keta].append(elem * 10 + base)
                lunArr[keta].append(elem * 10 + base+1)
            elif base == 9:
                lunArr[keta].append(elem * 10 + base-1)
                lunArr[keta].append(elem * 10 + base)
            else:
                lunArr[keta].append(elem * 10 + base-1)
                lunArr[keta].append(elem * 10 + base)
                lunArr[keta].append(elem * 10 + base+1)

    target = k
    for keta in range(10):
        t_arr = lunArr[keta]
        if target < len(t_arr):
            return t_arr[target-1]
        else:
            target -= len(t_arr)
    else:
        print("k is too large")
        print(target)


###
# main
if(__name__ == '__main__'):
    # input
    k = int(input())
    
    ans = abc161d(k)
    
    # output
    print(ans)
# else:
    # do nothing
