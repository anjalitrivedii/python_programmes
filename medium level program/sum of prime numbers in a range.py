def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True  # Move this outside the for loop

def sum_of_primes(start, end):
    return sum(num for num in range(start, end + 1) if is_prime(num))

print(sum_of_primes(10, 30))
