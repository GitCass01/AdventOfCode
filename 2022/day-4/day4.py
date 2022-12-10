import time
from io import TextIOWrapper
import re

def part1(file: TextIOWrapper):
    lines = file.readlines()

    count = 0
    for line in lines:
        p11, p12, p21, p22 = map(int, re.split('-|,', line))
        if p11 <= p21 and p22 <= p12 or p21 <= p11 and p12 <= p22:
            count += 1
    return count        


def part2(file: TextIOWrapper):
    lines = file.readlines()

    count = 0
    for line in lines:
        p11, p12, p21, p22 = map(int, re.split('-|,', line))
        if p21 <= p12 and p11 <= p22:
            count += 1
    return count   

def approx(seconds: float):
    if seconds <= 0:
        return str('%.3f' % seconds)+'s'

    notation = ['s', 'ms', 'µs', 'ns']
    i = 0
    while seconds < 1:
        seconds *= 1000
        i += 1
    return str("%.3f" % seconds)+notation[i]

start_time = time.time()
file = open('day4.txt')
print(part1(file))
end_time = time.time()
print("--- {} ---".format(approx(end_time - start_time)))
file.close()

start_time = time.time()
file = open('day4.txt')
print(part2(file))
end_time = time.time()
print("--- {} ---".format(approx(end_time - start_time)))
file.close()