import time

modulo = 1 # Usato per il teorema cinese dei resti
def parse(lines):
    global modulo
    monkeys = []
                   
    for i in range(0, len(lines), 6):
        monkey = {}
        monkey['si'] = list(map(lambda x: x.strip(), lines[i+1].split(':')[1].lstrip().split(',')))
        monkey['si'] = list(map(lambda x: int(x), monkey['si']))
        match lines[i+2].split()[4:]:
            case ['+', 'old']:
                op = lambda x: x + x
            case ['+', val]:
                op = lambda x, y=int(val): x + y
            case ['*', 'old']:
                op = lambda x: x * x
            case ['*', val]:
                op = lambda x, y=int(val): x * y
        monkey['op'] = op
        divisible = int(lines[i+3].split()[3])
        modulo *= divisible
        monkeyT = int(lines[i+4][len(lines[i+4])-1])
        monkeyF = int(lines[i+5][len(lines[i+5])-1])
        monkey['test'] = (lambda x, mT=monkeyT, d=divisible, mF=monkeyF: mT if x%d == 0 else mF)
        monkey['inspected'] = 0
        monkeys.append(monkey)
    return monkeys

def rounds(monkeys, n=20, divided=True):
    for i in range(0, n):
        for m in monkeys:
            for item in m['si']:
                m['inspected'] += 1
                new = m['op'](item)
                if divided:
                    new = new//3
                monkeys[m['test'](new)]['si'].append(new%modulo)
            m['si'] = []
    return monkeys

def getTopTwo(monkeys):
    inspected = []
    for m in monkeys:
        inspected.append(m['inspected'])
    inspected.sort(reverse=True)
    return inspected[0], inspected[1]
    
def part1(lines: list[str]):
    monkeys = parse(lines)
    monkeys = rounds(monkeys)
    m1, m2 = getTopTwo(monkeys)
    return m1 * m2

def part2(lines: list[str]):
    monkeys = parse(lines)
    monkeys = rounds(monkeys, 10000, False)
    m1, m2 = getTopTwo(monkeys)
    return m1 * m2

def approx(seconds: float):
    if seconds <= 0:
        return str("%.3f" % seconds)+'s'

    notation = ['s', 'ms', 'µs', 'ns']
    i = 0
    while seconds < 1:
        seconds *= 1000
        i += 1
    return str("%.3f" % seconds)+notation[i]

with open('day11.txt', 'r') as file:
    lines = file.readlines()
    lines = list(map(lambda l: l.strip(), lines))
    lines = list(filter(None, lines))
    
start_time = time.time()
print(part1(lines))
end_time = time.time()
print("--- {} ---".format(approx(end_time - start_time)))

start_time = time.time()
print(part2(lines))
end_time = time.time()
print("--- {} ---".format(approx(end_time - start_time)))