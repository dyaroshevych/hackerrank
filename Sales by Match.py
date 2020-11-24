#!/bin/python3

import math
import os
import random
import re
import sys


def sockMerchant(num_socks, socks):
    curr_socks = set()
    num_pairs = 0

    for sock in socks:
        if sock in curr_socks:
            curr_socks.remove(sock)
            num_pairs += 1
        else:
            curr_socks.add(sock)

    return num_pairs


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
