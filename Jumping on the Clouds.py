#!/bin/python3

import math
import os
import random
import re
import sys


def jumpingOnClouds(clouds):
    num_jumps = 0
    idx = 0

    while idx < len(clouds) - 1:
        if idx < len(clouds) - 2 and clouds[idx + 2] == 0:
            idx += 2
        else:
            idx += 1

        num_jumps += 1

    return num_jumps


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
