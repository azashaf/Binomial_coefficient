def factorial(num):
    if num == 0:
        return 1
    else:
        a = 1
        for i in range(1, num + 1):
            a *= i
        return a
    
def compute_binom(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))

n = int(input("Введите первое число: "))
k = int(input("Введите второе число: "))
print(compute_binom(n, k))