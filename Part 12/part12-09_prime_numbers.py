def prime_numbers():
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1


if __name__ == '__main__':
    numbers = prime_numbers()
    for i in range(8):
        print(next(numbers))
