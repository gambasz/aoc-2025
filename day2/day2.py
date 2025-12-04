file = 'day2_input.txt'
sample = 'day2_sample.txt'

def part1(file: str):
    invalid_ids = []

    with open(file, 'r') as f:
        ranges = f.read().split(',')
        for r in ranges:
            beginning, end = r.split('-')

            for num in range(int(beginning), int(end)+1):
                n = str(num)
                if len(n) % 2 == 0:
                    if n[:(len(n)//2)] == n[(len(n)//2):]:
                        invalid_ids.append(int(n))

        print(f'Invalid IDs: {invalid_ids}')
        print(f'Part 1: {sum(invalid_ids)}')

def part2(file: str):
    invalid_ids = []

    def split_k(s, k):
        if k == 1:
            return [s]

        res = []

        assert(len(s) % k == 0)

        num_splits = k
        len_splits = len(s) // k

        for i in range(num_splits):
            res.append(s[len_splits*i:i*len_splits+len_splits])

        return res

    def all_same(l):
        if l == []:
            return True

        l1 = l[0]

        for i in range(1, len(l)):
            if l[i] != l1:
                return False

        return True

    with open(file, 'r') as f:
        ranges = f.read().split(',')
        for r in ranges:
            beginning, end = r.split('-')

            for num in range(int(beginning), int(end)+1):
                n = str(num)
                for i in range(2, len(n)+1):
                    res = []
                    if len(n) % i == 0:
                        if all_same(split_k(n, i)):
                            invalid_ids.append(num)
                            continue
                
        print(f'Invalid IDs: {sorted(list(set(invalid_ids)))}')
        print(f'Part 2: {sum(list(set(invalid_ids)))}')