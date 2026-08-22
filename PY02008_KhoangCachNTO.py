# SangSoNguyenTo
def SangSoNTo(n):

    is_prime = [True] * (10001)
    primes = []

    is_prime[0] = is_prime[1] = False

    for i in range(2, int(10000 ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, 10001, i):
                is_prime[j] = False

    for i in range(len(is_prime)):
        if is_prime[i]:
            primes.append(i)

    return is_prime, primes


# Main
n, x = map(int, input().split())

is_prime, primes = SangSoNTo(n)
print(x, end=" ")

for i in range(1, n+1):
    x += primes[i-1]
    print(x, end=" ")

print()