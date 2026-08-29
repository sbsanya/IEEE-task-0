def is_prime(n):
    if n == 0 or n == 1:
        return False
    if n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            break
    else:
        # The else block executes when the for loop finishes without a break .aka. the number is not perfectly divisible by any of its possible factors and therefore it is a prime number.
        # If the loop did break somewhere before finishing, it would return false.
        return True
    return False
N = int(input("Enter N: "))
for num in range(2, N + 1):
    if is_prime(num):
        print(num)
