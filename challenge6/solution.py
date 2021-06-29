def solution(i):
    i = int(i)
    bin = "{0:b}".format(i)
    if i == 1:
        return 0
    if i % 2 != 0:
        return 1 + min(solution(i-1), solution(i+1))
    c = len(bin) - len(bin.rstrip('0'))
    return c + solution(int(bin.rstrip('0'), 2))

def solution2(i):
    i = int(i)
    bin = "{0:b}".format(i)
    count = 0
    if i == 1:
        return 0
    for i in bin[1:]:
        if i == '1':
            count += 2
        if i == '0':
            count += 1
    return count - 1

if __name__ == '__main__':
    [print(i, ': ', solution(i), solution2(i), ',', "{0:b}".format(i)) for i in range(10,21)]
    print(solution('30001923020901'))