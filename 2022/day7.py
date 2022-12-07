import time

def set_nested(tree, key, value):
    if len(key) == 1:
        tree[key[0]] = value
        return
    set_nested(tree.get(key[0])[0], key[1:], value)

def update_nested(tree, key, value):
    if len(key) == 0:
        tree[value[1]] = value[0]
        return
    update_nested(tree.get(key[0])[0], key[1:], value)
    tree.get(key[0])[1] += int(value[0])

def createTree(lines):
    tree = {}

    l = len(lines)
    idx = 0
    currentDir = ''

    while idx < l:
        match lines[idx].rstrip()[2:].split(' '):
            case ['cd', '/']:
                currentDir = '/'
                tree[currentDir] = [{}, 0]
                idx += 1
            case ['cd', '..']:
                idxs = [i for i, d in enumerate(currentDir) if d == '/']
                currentDir = currentDir[:idxs[len(idxs)-2]+1]
                idx += 1
            case ['cd', directory]:
                currentDir += directory + '/'
                idx += 1
            case ['ls']:
                idx += 1
                while True:
                    if idx >= len(lines) or lines[idx].startswith('$'):
                        break
                    i, j = lines[idx].rstrip().split(' ')
                    dirs = currentDir.split('/')
                    dirs = list(filter(None, dirs))
                    dirs.insert(0, '/')
                    if i == 'dir':
                        dirs.append(j)
                        if len(dirs) > 1:
                            set_nested(tree, dirs, [{}, 0])
                    else: # file
                        update_nested(tree, dirs, [i, j])
                    idx += 1
    return tree

def sizes(tree, atMost):
    if len(tree) == 0:
        return size
    size = 0
    for k in tree.keys():
        value = tree.get(k)
        if isinstance(value, list):
            if value[1] <= atMost:
                size += value[1]
            size += sizes(value[0], atMost)
    return size

def getEligibleDirs(tree, atMost):
    if len(tree) == 0:
        return []
    dirs = []
    for k in tree.keys():
        value = tree.get(k)
        if isinstance(value, list):
            if value[1] >= atMost:
                dirs.append(value[1])
            dirs += getEligibleDirs(value[0], atMost)
    return dirs


def part1(lines: list[str]):
    tree = createTree(lines)
    return sizes(tree, 100000)

def part2(lines: list[str]):
    tree = createTree(lines)
    unused = 70000000 - tree.get('/')[1]
    needed = 30000000 - unused
    dirs = getEligibleDirs(tree, needed)

    return min(dirs)

def approx(seconds: float):
    if seconds <= 0:
        return str("%.3f" % seconds)+'s'

    notation = ['s', 'ms', 'µs', 'ns']
    i = 0
    while seconds < 1:
        seconds *= 1000
        i += 1
    return str("%.3f" % seconds)+notation[i]

with open('day7.txt', 'r') as file:
    lines = file.readlines()
start_time = time.time()
print(part1(lines))
end_time = time.time()
print("--- {} ---".format(approx(end_time - start_time)))

file = open('day7.txt')
start_time = time.time()
print(part2(lines))
end_time = time.time()
print("--- {} ---".format(approx(end_time - start_time)))