import time

def part1(lines: list[str]):
    somma = 0
    X = 1
    c = 0
    cycles = [20, 60, 100, 140, 180, 220]
    for line in lines:
        match line.rstrip().split(' '):
            case ['noop']:
                c += 1
                if c in cycles:
                    somma += c * X
            case ['addx', val]:
                c += 1
                if c in cycles:
                    somma += c * X
                c += 1
                if c in cycles:
                    somma += c * X
                X += int(val)
    return somma
    
def draw(cycle, CRT, X):
    CRT = CRT%40
    if CRT == 0:
        print('\n', end='')
    if CRT == X or CRT == X + 1 or CRT == X + 2:
        print('#', end='')
    else:
        print('.', end='')
    
def part2(lines: list[str]):
    X = 0
    c = 0
    CRT = 0
    cycles = [40, 80, 120, 160, 200, 240]
    for line in lines:
        match line.rstrip().split(' '):
            case ['noop']:
                c += 1
                draw(c, CRT, X)
                CRT += 1
            case ['addx', val]:
                c += 1
                draw(c, CRT, X)
                CRT += 1
                c += 1
                draw(c, CRT, X)
                CRT += 1
                X += int(val)
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

with open('day10.txt', 'r') as file:
    lines = file.readlines()
start_time = time.time()
print(part1(lines))
end_time = time.time()
print("--- {} ---".format(approx(end_time - start_time)))

start_time = time.time()
part2(lines)
end_time = time.time()
print("\n--- {} ---".format(approx(end_time - start_time)))