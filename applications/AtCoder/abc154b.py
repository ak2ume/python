# -*- coding: utf-8 -*-

import re

def abc154b(s):
    t = re.sub('[a-z]', 'x', s)
    return(t)

###
# main
if(__name__ == '__main__'):
    # input
    s = input()

    t = abc154b(s)

    # output
    print(t)
# else:
    # do nothing
