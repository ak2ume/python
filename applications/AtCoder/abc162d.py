# -*- coding: utf-8 -*-

def abc162d(n, s):

    r_arr = []
    g_arr = []
    b_arr = []

    for i in range(n):
        if s[i] == 'R':
            r_arr.append(i)
        elif s[i] == 'G':
            g_arr.append(i)
        else: # 'B'
            b_arr.append(i)

    min1_arr = r_arr
    min2_arr = g_arr
    max_arr = b_arr
    if len(r_arr) < len(g_arr) and len(b_arr) < len(g_arr):
        min1_arr = r_arr
        min2_arr = b_arr
        max_arr = g_arr
    elif len(g_arr) < len(r_arr) and len(b_arr) < len(r_arr):
        min1_arr = g_arr
        min2_arr = b_arr
        max_arr = r_arr

    max_dict = dict()
    for elem in max_arr:
        max_dict[elem] = 1

    except_num = 0
    for r_i in min1_arr:
        for g_i in min2_arr:
            min_i = r_i
            max_i = g_i
            if g_i < r_i:
                min_i = g_i
                max_i = r_i
            diff = max_i - min_i
            minmin = min_i - diff
            maxmax = max_i + diff
            exists_central = (max_i + min_i) % 2

            if minmin in max_dict:
                except_num += 1
            if maxmax in max_dict:
                except_num += 1
            if exists_central == 0:
                central = (max_i + min_i) / 2
                if central in max_dict:
                    except_num += 1

    ans = len(r_arr) * len(g_arr) * len(b_arr) - except_num
    return ans

###
# main
if(__name__ == '__main__'):
    # input
    n = int(input())
    s = input()
    
    ans = abc162d(n, s)
    
    # output
    print(ans)
# else:
    # do nothing
