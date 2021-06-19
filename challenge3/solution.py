def solution(x, y):
    v = x+y-2
    return str(int(v * (v+1) / 2 + x))


if __name__ == '__main__':
    print(solution(5, 10))
