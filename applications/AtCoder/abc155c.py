# -*- coding: utf-8 -*-

def abc155c(num, s):
    array = [[] for _ in range(2*(10**5))]
    max_cnt = 0

    for i in range(0, num):
        target = s[i]
        cnt = 0 # appearance count
        iter_num = 0
        # array内で一致する文字列を見つける
        for iter in array:
            iter_num += 1
            for string in iter:
                if( target == string ):
                    cnt = iter_num
                    break
            if( cnt != 0 ): break

        if( cnt != 0 ):
            array[cnt-1].remove(target)
        # sortしながらリスト追加する
        insert_idx = 0
        target_array = array[cnt]
        if( target_array != [] ):
            for sort_idx in range(0, len(target_array)):
                if( target < target_array[sort_idx] ): 
                    insert_idx = sort_idx
                    break
        array[cnt].insert(insert_idx, target)

        if( cnt > max_cnt ) : max_cnt = cnt

    return(array[max_cnt])

###
# main
if(__name__ == '__main__'):
    # input
    s = [None for _ in range(2*(10**5))]
    num = int(input())
    for i in range(0, num):
        s[i] = input()

    ans = abc155c(num, s)

    # output
    for name in ans :
        print(name)
# else:
# do nothing
