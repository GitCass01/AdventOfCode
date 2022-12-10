import time


def parse(lines):
    grid = []
    for line in lines:
        row = []
        for c in line.rstrip():
            row.append(int(c))
        grid.append(row)
    return grid

# brutta ma più efficiente
def checkVisibility(value, row, col, grid):  
    check = True
    tmp = row - 1
    while tmp >= 0:
        if value <= grid[tmp][col]:
            check = False
            break
        tmp -= 1
    if check:
        return True
    tmp = row + 1
    while tmp < len(grid):
        if value <= grid[tmp][col]:
            check = False
            break
        else:
            check = True
        tmp += 1
    if check:
        return True
    tmp = col - 1
    while tmp >= 0:
        if value <= grid[row][tmp]:
            check = False
            break
        else:
            check = True
        tmp -= 1
    if check:
        return True
    tmp = col + 1
    while tmp < len(grid[0]):
        if value <= grid[row][tmp]:
            check = False
            break
        else:
            check = True
        tmp += 1
    if check:
        return True
    return False

# versione più pulita
def checkVisibility_v2(value, row, col, grid):
    check = [True, True, True, True]
    for i in range(row - 1, -1, -1):
        if grid[i][col] >= value:
            check[0] = False
            break
    for i in range(row + 1, len(grid)):
        if grid[i][col] >= value:
            check[1] = False
            break
    for l in reversed(grid[row][:col]):
        if l >= value:
            check[2] = False
            break
    for r in grid[row][col + 1:]:
        if r >= value:
            check[3] = False
            break
    return any(check)


def scenicScore(grid, row, col):
    val = grid[row][col]
    top = bottom = left = right = 0

    if row == 0 or row == len(grid) or col == 0 or col == len(grid[0]):
        return 0
    for i in range(row - 1, -1, -1):
        top += 1
        if grid[i][col] >= val:
            break
    for i in range(row + 1, len(grid)):
        bottom += 1
        if grid[i][col] >= val:
            break
    for l in reversed(grid[row][:col]):
        left += 1
        if l >= val:
            break
    for r in grid[row][col + 1:]:
        right += 1
        if r >= val:
            break	
	
    return top * bottom * right * left

def part1(lines: list[str]):
    grid = parse(lines)
    count = 0
    for row, i in enumerate(grid):
        for col, j in enumerate(i):
            if row == 0 or col == 0 or row == len(grid)-1 or col == len(grid)-1:
                count += 1
                continue
            if checkVisibility_v2(j, row, col, grid):
                count += 1
    return count


def part2(lines: list[str]):
    grid = parse(lines)  
    
    score = 0
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[0]) - 1):
            s = scenicScore(grid, i, j)
            if s > score:
                score = s
    return score


def approx(seconds: float):
    if seconds <= 0:
        return str("%.3f" % seconds)+'s'

    notation = ['s', 'ms', 'µs', 'ns']
    i = 0
    while seconds < 1:
        seconds *= 1000
        i += 1
    return str("%.3f" % seconds)+notation[i]


with open('day8.txt', 'r') as file:
    lines = file.readlines()
start_time = time.time()
print(part1(lines))
end_time = time.time()
print("--- {} ---".format(approx(end_time - start_time)))

start_time = time.time()
print(part2(lines))
end_time = time.time()
print("--- {} ---".format(approx(end_time - start_time)))
