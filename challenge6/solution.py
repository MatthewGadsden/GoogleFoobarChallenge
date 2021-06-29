import math


def get_zero_count(bin_n: str):
    return len(bin_n) - len(bin_n.rstrip('0'))


def solution(i):
    i = int(i)
    if i == 1:
        return 0
    if i == 2:
        return 1
    if i == 3:
        return 2
    bin = "{0:b}".format(i)
    count = get_zero_count(bin)
    if count == len(bin) - 1:
        return count
    if count > 0:
        new_bin = bin.rstrip('0')
        new_n = int(new_bin, 2)
        return count + solution(new_n)
    else:
        higher = "{0:b}".format(i+1)
        lower = "{0:b}".format(i-1)
    if len(higher) > len(lower):
        return solution(int(higher, 2)) + count + 1
    elif get_zero_count(higher) > get_zero_count(lower):
        return 1 + solution(int(higher, 2)) + count
    else:
        return 1 + solution(int(lower, 2)) + count


if __name__ == '__main__':
    n = '3298623563104621673217321730217310732639856102810983219332130921730921723021703212758174298384649835084374874132809309875868356749387504850935840392367213021631936276231908217382613062032109387594376239837219730219732163021163218362362103621063210732630212109372097321097321021313121363026103621063265921321'
    print(len(n))
    print(solution(n))
