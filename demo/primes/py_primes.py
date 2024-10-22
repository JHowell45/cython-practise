def primes(n: int) -> list[int]:
    prime_list: list[int] = []
    if n > 1000:
        n = 1000
    prime_count = 0
    number = 2
    while len(prime_list) < n:
        for i in prime_list[:prime_count]:
            if number % i == 0:
                break
        else:
            prime_list.append(number)
            prime_count += 1
        number += 1
    return prime_list
