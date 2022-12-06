def part1_2():
    input = open('day1.txt')
    lines = input.readlines()

    calories = []
    current = 0
    for line in lines:
        if line == '\n':
            calories.append(current)
            current = 0
        else:
            current += int(line)

    print('Part1: ' + str(max(calories)))
    
    calories.sort()
    print('Part1: ' + str(sum(calories[len(calories)-3:])))

part1_2()