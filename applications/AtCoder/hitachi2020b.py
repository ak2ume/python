# -*- coding: utf-8 -*-

def hitachi2020b(a, b, discount):
    min_a = a[0]
    for i in range(len(a)):
        if a[i] < min_a:
            min_a = a[i]
    min_b = b[0]
    for i in range(len(b)):
        if b[i] < min_b:
            min_b = b[i]
    min_val = min_a + min_b

    for k in range(len(discount)):
        disc = discount[k]
        cand_a = disc[0] - 1
        cand_b = disc[1] - 1
        cand_val = a[cand_a] + b[cand_b] - disc[2]
        if cand_val < min_val:
            min_val = cand_val

    return min_val

###
# main
if(__name__ == '__main__'):
    # input
    num_a, num_b, m = map(int, input().split(" "))
    val_a = list(map(int, input().split(" ")))
    val_b = list(map(int, input().split(" ")))

    discount = []
    for k in range(m):
        discount.append(list(map(int, input().split(" "))))
    
    accomplishment = hitachi2020b(val_a, val_b, discount)
    
    # output
    print(accomplishment)
# else:
    # do nothing
