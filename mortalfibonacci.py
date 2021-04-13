def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def mfibo(n):
    if n < 2:
        return n
    elif n >= 2 and n <= 3:
        return mfibo(n-1) + mfibo(n-2)
    else:
        return mfibo(n-2) + mfibo(n-3)

for i in range(30):
    print(str(fibonacci(i) - mfibo(i)))

