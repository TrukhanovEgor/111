numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for numbers in numbers:
    if number == 1:
        continue
    if numbers < 2:
        not_primes.append(numbers)
        continue
    is_prime = True
    for i in range(2,numbers):
        if numbers % i == 0:
            is_prime = False
            not_primes.append(numbers)
            break
    if is_prime:
        primes.append(numbers)
print("Primes:", primes)
print("Not Primes:", not_primes)
