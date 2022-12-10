import time

def checkAdjacency(H, T):
    # stessa pos
    if H == T:
        return True
    # u, r, l, d
    if [H[0]-1, H[1]] == T:
        return True
    if [H[0]+1, H[1]] == T:
        return True
    if [H[0], H[1]-1] == T:
        return True
    if [H[0], H[1]+1] == T:
        return True
    # diagonali
    if [H[0]-1, H[1]-1] == T:
        return True
    if [H[0]-1, H[1]+1] == T:
        return True
    if [H[0]+1, H[1]-1] == T:
        return True
    if [H[0]+1, H[1]+1] == T:
        return True
    return False

def part1(lines: list[str]):
    posH = [0, 0]
    posT = [0, 0]
    precH = [0, 0]
    pos = set()
    
    for line in lines:
        c, n = line.split(' ')
        for _ in range(0, int(n)):
            match c:
                case 'R':
                    posH[1] += 1
                case 'L':
                    posH[1] -= 1
                case 'U':
                    posH[0] += 1
                case 'D':
                    posH[0] -= 1
            if not checkAdjacency(posH, posT):
                posT = precH.copy()
            precH = posH.copy()
            pos.add((posT[0], posT[1]))
    return len(pos)

def part2(lines: list[str], num=10):
    lst = [0, 0]
    posK = {i: [0, 0] for i in range(num)}
    pos_tail = set()
    
    for line in lines:
        c, n = line.split(' ')
        for _ in range(0, int(n)):
            prec = posK[0].copy()
            prec2 = posK[1].copy()
            match c:
                case 'R':
                    posK[0][1] += 1
                case 'L':
                    posK[0][1] -= 1
                case 'U':
                    posK[0][0] += 1
                case 'D':
                    posK[0][0] -= 1
            for i in range(1, num):
                if i != 1:
                    prec2 = posK[i].copy()
                if not checkAdjacency(posK[i - 1], posK[i]):
                    posK[i] = prec.copy()
                prec = prec2.copy()
            print(posK[num-1])
            pos_tail.add((posK[num - 1][0], posK[num - 1][1]))
    return len(pos_tail)

def approx(seconds: float):
    if seconds <= 0:
        return str("%.3f" % seconds)+'s'

    notation = ['s', 'ms', 'µs', 'ns']
    i = 0
    while seconds < 1:
        seconds *= 1000
        i += 1
    return str("%.3f" % seconds)+notation[i]

with open('day9.txt', 'r') as file:
    lines = file.readlines()
start_time = time.time()
print(part1(lines))
end_time = time.time()
print("--- {} ---".format(approx(end_time - start_time)))

# start_time = time.time()
print(part2(lines))
# end_time = time.time()
# print("--- {} ---".format(approx(end_time - start_time)))