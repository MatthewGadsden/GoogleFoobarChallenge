import math
from functools import lru_cache
import time


def solution_with_recursion(i):
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
    higher = "{0:b}".format(i+1)
    lower = "{0:b}".format(i-1)
    if len(higher) > len(lower):
        return solution(int(higher, 2)) + count + 1
    elif get_zero_count(higher) > get_zero_count(lower):
        return 1 + solution(int(higher, 2)) + count
    else:
        return 1 + solution(int(lower, 2)) + count


def get_zero_count(bin_n: str):
    return len(bin_n) - len(bin_n.rstrip('0'))


def solution(n):
    total_ops = 0
    current_n = int(n)
    while current_n > 0:
        if current_n == 1:
            current_n -= 1
        elif current_n == 2:
            total_ops += 1
            current_n -= 2
        elif current_n == 3:
            total_ops += 2
            current_n -= 3
        else:
            bin_n = "{0:b}".format(current_n)
            count = get_zero_count(bin_n)
            if count == len(bin_n) - 1:
                total_ops += count
                current_n -= current_n
            elif count > 0:
                total_ops += count
                new_bin = bin_n.rstrip('0')
                current_n = int(new_bin, 2)
            else:
                higher = "{0:b}".format(current_n + 1)
                lower = "{0:b}".format(current_n-1)
                total_ops += (count + 1)
                if len(higher) > len(lower) or get_zero_count(higher) > get_zero_count(lower):
                    current_n = int(higher, 2)
                else:
                    current_n = int(lower, 2)
    return total_ops


if __name__ == '__main__':
    n = '218632278537539213218729837213213721732183932109832091809375843757754478098084385095485492132132153121321321' \
        '8540438095535443543357430957430978890980984309485094380098654376478236462934783274932646478364982364236984326' \
        '437846862364378264237'
    print(solution(n))
