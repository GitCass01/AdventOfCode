import time
from io import TextIOWrapper
import io
import re
import queue

def part1(file: TextIOWrapper):
    queues, commands = file.read().split('\n\n')
    bufC = io.StringIO(commands)
    bufC = bufC.readlines()
    buf = io.StringIO(queues)
    buf = buf.readlines()[:-1]

    lsts = []
    commands = []

    i = 0
    while i < len(buf)+1:
        i+=1
        lsts.append([])

    for line in buf:
        res = re.split('\] \[|\[|\]', line)
        res = list(filter(lambda x: x != '\n', res))
        res.pop(0)
        for idx, i in enumerate(res):
            if i.isalpha():
                continue
            count = 0
            for c in i:
                count += 1
            if count == 5:
                res[idx:idx+1] = ' '
            if count == 21:
                res[idx:idx+1] = ' ', ' ', ' ', ' ', ' '
            if count == 17:
                res[idx:idx+1] = ' ', ' ', ' ', ' '
            if count == 9:
                res[idx:idx+1] = ' ', ' '
        i = 0
        for val in res:
            if not val.strip():
                i += 1
                continue
            lsts[i].append(val)
            i += 1

    for line in bufC:
        res = re.split('move | from | to |\n', line)
        res = list(filter(None, res))
        commands.append(list(map(int, res)))

    for c in commands:
        i = 0
        while c[0] > 0:
            c[0] -= 1
            g = lsts[c[1]-1].pop(0)
            lsts[c[2]-1].insert(0, g)
    
    str = ''
    for l in lsts:
        str += l.pop(0)
    return str

    

def part2(file: TextIOWrapper):
    queues, commands = file.read().split('\n\n')
    bufC = io.StringIO(commands)
    bufC = bufC.readlines()
    buf = io.StringIO(queues)
    buf = buf.readlines()[:-1]

    lsts = []
    commands = []

    i = 0
    while i < len(buf)+1:
        i+=1
        lsts.append([])

    for line in buf:
        res = re.split('\] \[|\[|\]', line)
        res = list(filter(lambda x: x != '\n', res))
        res.pop(0)
        for idx, i in enumerate(res):
            if i.isalpha():
                continue
            count = 0
            for c in i:
                count += 1
            if count == 5:
                res[idx:idx+1] = ' '
            if count == 21:
                res[idx:idx+1] = ' ', ' ', ' ', ' ', ' '
            if count == 17:
                res[idx:idx+1] = ' ', ' ', ' ', ' '
            if count == 9:
                res[idx:idx+1] = ' ', ' '
        i = 0
        for val in res:
            if not val.strip():
                i += 1
                continue
            lsts[i].append(val)
            i += 1

    for line in bufC:
        res = re.split('move | from | to |\n', line)
        res = list(filter(None, res))
        commands.append(list(map(int, res)))
    
    for c in commands:
        k = c[0]
        tmp = []
        tmp = lsts[c[1]-1][0:k]
        lsts[c[2]-1][:0] = tmp
        lsts[c[1]-1] = lsts[c[1]-1][k:]
    
    str = ''
    for l in lsts:
        str += l.pop(0)
    return str

def approx(seconds: float):
    if seconds <= 0:
        return str('%.3f' % seconds)+'s'

    notation = ['s', 'ms', 'µs', 'ns']
    i = 0
    while seconds < 1:
        seconds *= 1000
        i += 1
    return str("%.3f" % seconds)+notation[i]

file = open('day5.txt')
start_time = time.time()
print(part1(file))
end_time = time.time()
print("--- {} ---".format(approx(end_time - start_time)))
file.close()

file = open('day5.txt')
start_time = time.time()
print(part2(file))
end_time = time.time()
print("--- {} ---".format(approx(end_time - start_time)))
file.close()