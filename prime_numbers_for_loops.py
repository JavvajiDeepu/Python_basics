for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} equal {x} * {n//x}")
            break
    else:
        print(f"{n} is a prime number")