import time
from io import TextIOWrapper

def get_commons_char(str1, str2):
    return set(str1).intersection(str2)

def part1(file: TextIOWrapper):
    lines = file.readlines()

    sum_priorities = 0
    for line in lines:
        half1 = line[:len(line)//2]
        half2 = line[len(line)//2:]
        common = ''.join(get_commons_char(half1, half2))
        sum_priorities += (ord(common) - 96) if common.islower() else (ord(common) - 38)

    return sum_priorities

def part2(file: TextIOWrapper):
    lines = file.readlines()

    sum_priorities = 0
    count = 3
    group = []
    for line in lines:
        group.append(line)
        count -= 1
        if count == 0:
            common = ''.join(get_commons_char(group[0], group[1]))
            common = ''.join(get_commons_char(common, group[2]))
            group = []
            count = 3
            common = common.replace(chr(10), '')
            sum_priorities += (ord(common) - 96) if common.islower() else (ord(common) - 38)
    return sum_priorities

def approx(seconds: float):
    if seconds <= 0:
        return str('%.3f' % seconds)+'s'

    notation = ['s', 'ms', 'µs', 'ns']
    i = 0
    while seconds < 1:
        seconds *= 1000
        i += 1
    return str("%.3f" % seconds)+notation[i]

file = open('day3.txt')
start_time = time.time()
print(part1(file))
end_time = time.time()
print("--- {} ---".format(approx(end_time - start_time)))
file.close()

file = open('day3.txt')
start_time = time.time()
print(part2(file))
end_time = time.time()
print("--- {} ---".format(approx(end_time - start_time)))
file.close()