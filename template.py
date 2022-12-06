import time
from io import TextIOWrapper

def part1(lines: list[str]):
    return None

def part2(lines: list[str]):
    return None

def approx(seconds: float):
    if seconds <= 0:
        return str("%.3f" % seconds)+'s'

    notation = ['s', 'ms', 'µs', 'ns']
    i = 0
    while seconds < 1:
        seconds *= 1000
        i += 1
    return str("%.3f" % seconds)+notation[i]

with open('day.txt', 'r') as file:
    lines = file.readlines()
# start_time = time.time()
print(part1(lines))
# end_time = time.time()
# print("--- {} ---".format(approx(end_time - start_time)))

file = open('day.txt')
# start_time = time.time()
print(part2(lines))
# end_time = time.time()
# print("--- {} ---".format(approx(end_time - start_time)))