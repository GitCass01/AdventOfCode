import time

def compareLst(a, b):
    if type(a) == type(b) == int:
        return a - b
    if type(a) == int and type(b) == list:
        a = [a]
    elif type(a) == list and type(b) == int:
        b = [b]
    if type(a) == type(b) == list:
        for i in range(len(a)):
            if i == len(b):
                return 1
            l,r = a[i], b[i]
            res = compareLst(l, r)
            if res != 0:
                return res
        return len(a) - len(b)
        

def part1(lines: list[str]):
    count = 0
    for i in range(0, len(lines), 2):
        lst1 = eval(lines[i])
        lst2 = eval(lines[i + 1])
        count += (i//2+1) if compareLst(lst1, lst2) < 0 else 0
    return count

def part2(lines: list[str]):
    lines.append('[[2]]')
    lines.append('[[6]]')
    lists = []
    for l in lines:
        lists.append(eval(l))
    # bubble sort perchè mi piace
    swapped = False
    for i in range(len(lists)-1):
        for j in range(0, len(lists)-i-1):
            if compareLst(lists[j + 1], lists[j]) < 0:
                swapped = True
                lists[j], lists[j + 1] = lists[j +1], lists[j]
        if not swapped:
            break
    divider1 = lists.index([[2]]) + 1
    divider2 = lists.index([[6]]) + 1
    return divider1 * divider2

def approx(seconds: float):
    if seconds <= 0:
        return str("%.3f" % seconds)+'s'

    notation = ['s', 'ms', 'µs', 'ns']
    i = 0
    while seconds < 1:
        seconds *= 1000
        i += 1
    return str("%.3f" % seconds)+notation[i]

with open('day13.txt', 'r') as file:
    lines = file.readlines()
    lines = [l.rstrip() for l in lines]
    lines = list(filter(None, lines))
start_time = time.time()
print(part1(lines))
end_time = time.time()
print("--- {} ---".format(approx(end_time - start_time)))

start_time = time.time()
print(part2(lines))
end_time = time.time()
print("--- {} ---".format(approx(end_time - start_time)))