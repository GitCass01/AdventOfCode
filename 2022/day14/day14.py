import time

def parse(lines):
    rocks = set()
    maxRow = 0
    for line in lines:
        path = list(map(lambda x: x.strip(), line.split('->')))
        for i, rck in enumerate(path):
            if i+1 == len(path):
                break
            a = [int(x) for x in rck.split(',')]
            b = [int(x) for x in path[i+1].split(',')]
            if a[1] > maxRow:
                maxRow = a[1]
            if b[1] > maxRow:
                maxRow = b[1]
            for c in range(0, abs(a[0]-b[0])):
                minCol = min(a[0], b[0])
                rocks.add((minCol+c+1, a[1]))
            for r in range(0, abs(a[1]-b[1])):
                minRow = min(a[1], b[1])
                rocks.add((a[0], minRow+r+1))
            rocks.add((a[0], a[1]))
            rocks.add((b[0], b[1]))
    return rocks, maxRow

def sandFalls(rocks, maxRow):
    sands = set()
    sand = (500, 0)
    while True:
        if (sand[0], sand[1]+1) not in rocks:
            sand = (sand[0], sand[1]+1)
        elif (sand[0]-1, sand[1]+1) not in rocks:
            sand = (sand[0]-1, sand[1]+1)
        elif (sand[0]+1, sand[1]+1) not in rocks:
            sand = (sand[0]+1, sand[1]+1)
        else:
            rocks.add(sand)
            sands.add(sand)
            sand = (500, 0)
        if sand[1] > maxRow:
            break
    return sands

def sandFalls_part2(rocks, maxRow):
    sands = set()
    sand = (500, 0)
    while True:
        if sand in rocks:
            break
        if (sand[0], sand[1]+1) not in rocks and sand[1]+1 != maxRow:
            sand = (sand[0], sand[1]+1)
        elif (sand[0]-1, sand[1]+1) not in rocks and sand[1]+1 != maxRow:
            sand = (sand[0]-1, sand[1]+1)
        elif (sand[0]+1, sand[1]+1) not in rocks and sand[1]+1 != maxRow:
            sand = (sand[0]+1, sand[1]+1)
        else:
            rocks.add(sand)
            sands.add(sand)
            sand = (500, 0)
    return sands

def part1(lines: list[str]):
    rocks, maxRow = parse(lines)
    sands = sandFalls(rocks, maxRow)
    return len(sands)

def part2(lines: list[str]):
    rocks, maxRow = parse(lines)
    sands = sandFalls_part2(rocks, maxRow+2)
    return len(sands)

def approx(seconds: float):
    if seconds <= 0:
        return str("%.3f" % seconds)+'s'

    notation = ['s', 'ms', 'µs', 'ns']
    i = 0
    while seconds < 1:
        seconds *= 1000
        i += 1
    return str("%.3f" % seconds)+notation[i]

with open('day14.txt', 'r') as file:
    lines = file.readlines()
start_time = time.time()
print(part1(lines))
end_time = time.time()
print("--- {} ---".format(approx(end_time - start_time)))

start_time = time.time()
print(part2(lines))
end_time = time.time()
print("--- {} ---".format(approx(end_time - start_time)))