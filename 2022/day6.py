import time

def getIdx(line, i):
    idx = 0
    for idx in range(0, len(line)):
        q = line[idx:idx+i]
        check = True
        for c in q:
            if q.count(c) > 1:
                check = False
                break
        if check:
           return idx+i

def part1(lines: list[str]):
    return getIdx(lines[0], 4)

def part2(lines: list[str]):
    return getIdx(lines[0], 14)

def approx(seconds: float):
    if seconds <= 0:
        return str('%.3f' % seconds)+'s'

    notation = ['s', 'ms', 'µs', 'ns']
    i = 0
    while seconds < 1:
        seconds *= 1000
        i += 1
    return str("%.3f" % seconds)+notation[i]

with open('day6.txt', 'r') as file:
    lines = file.readlines()
start_time = time.time()
print(part1(lines))
end_time = time.time()
print("--- {} ---".format(approx(end_time - start_time)))

start_time = time.time()
print(part2(lines))
end_time = time.time()
print("--- {} ---".format(approx(end_time - start_time)))