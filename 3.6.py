def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

def fibonacci_sum(n):
    total = 0
    for i in range(1, n + 1):
        fib_num = fibonacci(i)
        print(f"Fibonacci({i}) = {fib_num}")
        total += fib_num
    print(f"Tổng các số Fibonacci từ F(1) đến F({n}) là: {total}")

n = int(input())
fibonacci_sum(n)
