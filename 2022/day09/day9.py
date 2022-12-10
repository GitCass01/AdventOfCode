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

# parte 2 rifatta da zero
def mov_t(dist):
    if dist[0] in [-1,0,1] and dist[1] in [-1,0,1]: return (0,0)
    if dist[0] > 1 and dist[1]==0: return (1,0)
    if dist[0] < -1 and dist[1]==0: return (-1,0)
    if dist[1] > 1 and dist[0]==0: return (0,1)
    if dist[1] <-1 and dist[0]==0: return (0,-1)
    if dist[0] > 0 and dist[1] > 0: return (1,1)
    if dist[0] < 0 and dist[1] > 0: return (-1,1)
    if dist[0] > 0 and dist[1] < 0: return (1,-1)
    if dist[0] < 0 and dist[1] < 0: return (-1,-1)

def add_mov(pos, mov):
    pos[0] += mov[0]
    pos[1] += mov[1]
    return pos

def part2(lines: list[str]):
    pos = [[0,0] for x in range (10)]
    pos_tail = set([(0,0)])
    mov_dict = { 'L':(-1,0), 'R':(1,0), 'D':(0,-1), 'U':(0,1)}   
    
    for l in lines:
        l = l.split(' ')
        for n in range (int(l[1])):
            pos[0] = add_mov(pos[0], mov_dict[l[0]])
            for i in range (1, len(pos)):
                dist = (pos[i-1][0] - pos[i][0], pos[i-1][1] - pos[i][1])
                pos[i] = add_mov(pos[i], mov_t(dist))
            pos_tail.add((pos[9][0],pos[9][1]))
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

start_time = time.time()
print(part2(lines))
end_time = time.time()
print("--- {} ---".format(approx(end_time - start_time)))