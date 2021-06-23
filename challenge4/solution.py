def solution(x, y):
    # Your code here
    x = int(x)
    y = int(y)
    count = 0
    while x != 1 or y != 1:
        if x == 1:
            return str(count + y - 1)
        elif y == 1:
            return str(count + x - 1)
        div = 1
        if y % x == 0 or x % y == 0:
            return "impossible"
        if y > x:
            div = int(y / x)
            y -= div * x
        else:
            div = int(x / y)
            x -= div * y
        count += div
    return str(count)


if __name__ == '__main__':
    print(solution('4', '7'))
    print(solution('999', '1000'))
    print(solution('27', '8'))
