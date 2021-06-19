import math

def get_col_row_pair(pos_n):
    col = (pos_n % 8)
    row = int((pos_n / 8))
    return col, row

def get_min_moves(x, y):
    if (x == 0 and y == 1) or (x == 1 and y == 0):
        return 3
    elif x == 2 and y == 2:
        return 4
    delta = x - y
    if y > delta:
  	    return delta - 2*math.floor((delta-y)/3);
    else:
  	    return delta - 2*math.floor((delta-y)/4);


def solution(src, dest):
    src_pair = get_col_row_pair(src)
    dest_pair = get_col_row_pair(dest)
    diff_pair = (abs(dest_pair[0] - src_pair[0]), abs(dest_pair[1] - src_pair[1]))
    print(diff_pair)
    return get_min_moves(diff_pair[0], diff_pair[1])


if __name__ == '__main__':
    print(solution(36, 19))
