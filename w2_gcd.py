def get_gcd(a, b):
    
    if b == 0:
        return a

    return get_gcd(b, a % b)


if __name__ == '__main__':
    
    a, b = map(int, input().split())

    print(get_gcd(a, b))