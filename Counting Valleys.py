#!/bin/python3

import math
import os
import random
import re
import sys


def countingValleys(num_steps, path):
    num_valleys = 0
    curr_level = 0
    is_valley = False

    for step in path:
        if step == 'D':
            curr_level -= 1
        else:
            curr_level += 1

        if curr_level >= 0 and is_valley:
            num_valleys += 1
            is_valley = False

        if curr_level < 0:
            is_valley = True

    return num_valleys


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
