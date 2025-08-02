1.def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
2.def digit_sum(k):
    total = 0
    while k > 0:
        total += k % 10
        k = k // 10
    return total
3.def power_of_two(N):
    x = 1
    while x * 2 <= N:
        x *= 2
        print(x)

