import math

def solution(i):
    i = int(i)
    bin = "{0:b}".format(i)
    if i == 1:
        return 0
    if i % 2 != 0:
        return 1 + min(solution(i-1), solution(i+1))
    c = len(bin) - len(bin.rstrip('0'))
    return c + solution(int(bin.rstrip('0'), 2))

def get_zero_count(bin_n: str):
    return len(bin_n) - len(bin_n.rstrip('0'))

def solution2(i):
    i = int(i)
    if i == 1:
        return 0
    if i == 2:
        return 1
    bin = "{0:b}".format(i)
    count = get_zero_count(bin)
    if count == len(bin) - 1:
        return count
    new_bin = bin.rstrip('0')
    new_n = int(new_bin, 2)
    higher = "{0:b}".format(new_n+1)
    lower = "{0:b}".format(new_n-1)
    if len(higher) > len(lower):
        return 1 + solution2(int(lower, 2)) + count
    elif get_zero_count(higher) > get_zero_count(lower):
        return 1 + solution2(int(higher, 2)) + count
    else:
        return 1 + solution2(int(lower, 2)) + count

if __name__ == '__main__':
    for i in range(1,129):
        s1, s2 = solution2(i), solution(i)
        print(i, ': ', s1, s2) if s1 != s2 else 'pass'
    # print(solution2(15))
