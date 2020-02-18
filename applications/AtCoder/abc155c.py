# -*- coding: utf-8 -*-

def calc_insert_index(array, target, left, right):
    if left == right:
        if target < array[left]:
            return left
        else:
            return left + 1
    else:
        bound = (left + right) >> 1
        if target < array[bound]:
            return calc_insert_index(array, target, left, bound)
        else:
            return calc_insert_index(array, target, bound+1, right)


def abc155c(num, s):
    appearance_dict = {} # 文字列:出現回数
    array = [[] for _ in range(num)] # (出現回数-1)をindexにして文字列を配列で管理する
    max_cnt = 0

    for i in range(0, num):
        target = s[i]
        cnt = 0 # appearance count

        if target in appearance_dict :
            cnt = appearance_dict[target]
            array[cnt - 1].remove(target)
        appearance_dict[target] = cnt + 1

        # 出現回数最大のときのみ2分探索でsortしながら配列に追加する
        insert_idx = 0
        if cnt == max_cnt:
            if array[cnt]:
                insert_idx = calc_insert_index(array[cnt], target, 0, len(array[cnt])-1)
        array[cnt].insert(insert_idx, target)

        if cnt > max_cnt:
            max_cnt = cnt

    return array[max_cnt]

###
# main
if __name__ == '__main__' :
    # input
    num = int(input())
    s = [None for _ in range(num)]
    for i in range(0, num):
        s[i] = input()

    ans = abc155c(num, s)

    # output
    for name in ans :
        print(name)
# else:
# do nothing