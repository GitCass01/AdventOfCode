import re
import time

def parse(lines):
    positions = {}
    minX, maxX = 2**16, 0
    for line in lines:
        line = [int(x) for x in re.split('Sensor at x=|, y=|: closest beacon is at x=', line)[1:]]
        sensor, beacon = (line[0], line[1]), (line[2], line[3])
        positions[sensor] = beacon
        minX = min(minX, line[0]-manhattan_distance(sensor, beacon), line[2])
        maxX = max(maxX, line[0]+manhattan_distance(sensor, beacon), line[2])
    return positions, minX, maxX

def manhattan_distance(sensor, beacon):
    return abs(sensor[0]-beacon[0]) + abs(sensor[1]-beacon[1])

def part1(lines: list[str]):
    positions, minX, maxX = parse(lines)
    count, y = 0, 2000000
    distance = {}
    for s in positions.keys():
        distance[s] = manhattan_distance(s, positions[s])
    for x in range(minX, maxX+1):
        if (x, y) == positions[s] or (x, y) in positions.keys():
            continue
        for s in positions.keys():
            if manhattan_distance((x, y), s) <= distance[s]:
                count += 1
                break
    return count

def part2(lines: list[str]):
    positions, minX, maxX = parse(lines)
    count, y = 0, 2000000
    distance = {}
    for s in positions.keys():
        distance[s] = manhattan_distance(s, positions[s])
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

with open('day15.txt', 'r') as file:
    lines = [x.rstrip('\n') for x in file]
start_time = time.time()
print(part1(lines))
end_time = time.time()
print("--- {} ---".format(approx(end_time - start_time)))

start_time = time.time()
print(part2(lines))
end_time = time.time()
print("--- {} ---".format(approx(end_time - start_time)))