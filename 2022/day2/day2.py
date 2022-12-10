import time
from io import TextIOWrapper

win = {'A':'Y', 'B':'Z', 'C':'X'}
draw = {'A':'X', 'B':'Y', 'C':'Z'}
lose = {'A':'Z', 'B':'X', 'C':'Y'}
points = {'X':1, 'Y':2, 'Z':3}

def calculate_points(player1, player2):
    score = points[player2]
        
    if draw[player1] == player2:
        score += 3
    elif win[player1] == player2:
        score += 6

    return score

def part1(file: TextIOWrapper):
    lines = file.readlines()

    score = 0
    for line in lines:
        score += calculate_points(line[0], line[2])
    return score

def part2(file: TextIOWrapper):
    lines = file.readlines()

    score = 0
    for line in lines:
        player1 = line[0]
        player2 = line[2]

        if player2 == 'X':
            score += calculate_points(player1, lose[player1])
        elif player2 == 'Y':
            score += calculate_points(player1, draw[player1])
        else:
            score += calculate_points(player1, win[player1])
    return score


def approx(seconds: float):
    if seconds <= 0:
        return str('%.3f' % seconds)+'s'

    notation = ['s', 'ms', 'µs', 'ns']
    i = 0
    while seconds < 1:
        seconds *= 1000
        i += 1
    return str("%.3f" % seconds)+notation[i]


file = open('day2.txt')
start_time = time.time()
print(part1(file))
end_time = time.time()
print("--- {} ---".format(approx(end_time - start_time)))
file.close()

file = open('day2.txt')
start_time = time.time()
print(part2(file))
end_time = time.time()
print("--- {} ---".format(approx(end_time - start_time)))
file.close()