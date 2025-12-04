file = 'day1_input.txt'
sample = 'day1_sample.txt'

curr_pos = 50 # Dial starting position
password = 0
clicks_zero = 0

with open(file, 'r') as f:
    for line in f.read().splitlines():
        first = line[0]
        curr_num = 0
        assert(first == 'L' or first == 'R')
        curr_num = int(line[1:]) * (-1 if line[0] == 'L' else 1)

        for _ in range(abs(curr_num)):
            curr_pos += (1 if line[0] == 'R' else -1)
            if curr_pos % 100 == 0:
                clicks_zero += 1
            
            if curr_pos < 0 or curr_pos > 100:
                curr_pos = curr_pos % 100

        if curr_pos % 100 == 0:
            password += 1

print(f'Part 1: {password}, Part 2: {clicks_zero}')