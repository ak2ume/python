# -*- coding: utf-8 -*-

def abc157b(bingo, b):
    ans = False

    # check row
    for i in range(0, 3):
        bCnt = 0
        for j in range(0, 3):
            if bingo[i][j] in b:
                bCnt += 1
#                print("bingo!" + str(i) + str(j))
        if bCnt == 3:
            ans = True

    # check column
    for j in range(0, 3):
        bCnt = 0
        for i in range(0, 3):
            if bingo[i][j] in b:
                bCnt += 1
#                print("bingo!" + str(i) + str(j))
        if bCnt == 3:
            ans = True

    # check slope
    bCnt = 0
    for i in range(0, 3):
        if bingo[i][i] in b:
            bCnt += 1
#            print("bingo!" + str(i) + str(i))
    if bCnt == 3:
        ans = True

    bCnt = 0
    for i in range(0, 3):
        if bingo[i][2-i] in b:
            bCnt += 1
#            print("bingo!" + str(i) + str(2-i))
    if bCnt == 3:
        ans = True
    
    if ans:
        return("Yes")
    else:
        return("No")

###
# main
if(__name__ == '__main__'):
    # input
    bingoArray = [[] for _ in range(3)]
    for i in range(0, 3):
        bingoArray[i] = list(map(int, input().split(" ")))
    n = int(input())
    b = [[] for _ in range(n)]
    for j in range(0, n):
        b[j] = int(input())
    
    accomplishment = abc157b(bingoArray, b)
    
    # output
    print(accomplishment)
# else:
    # do nothing
