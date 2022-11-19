def get_gcd(a, b):
    
    if b == 0:
        return a

    return get_gcd(b, a % b)


def get_lcm(a, b):

    return int(a * b / get_gcd(a, b))


if __name__ == '__main__':
    
    a, b = map(int, input().split())
    print(get_lcm(a, b))

