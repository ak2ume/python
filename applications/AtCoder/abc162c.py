# -*- coding: utf-8 -*-
import math

###
# main
if(__name__ == '__main__'):
    # input
    k = int(input())

    sum = 0
    for a in range(1,k+1):
        cand_list = []
        for cand in range(int(math.sqrt(a)),0,-1):
            if a % cand == 0:
                cand_list.append(cand)
                cand_list.append(a//cand)
        cand_list.sort()

        for b in range(a,k+1):
            for c in range(b,k+1):

                gcd = 0
                for tgt in cand_list[::-1]:
                    if b % tgt == 0 and c % tgt == 0:
                        gcd = tgt
                        break

                if a != b:
                    if b != c:
                        gcd *= 6
                    else:
                        gcd *= 3
                elif b != c:
                    gcd *= 3

                sum += gcd

    print(sum)

# else:
    # do nothing
