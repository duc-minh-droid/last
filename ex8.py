def fibonacci(n):
    x = 0
    y = 1
    arr = [1, ]
    i = 1
    while i < n:
        z = x+y
        x = y
        y = z
        arr.append(z)
        i += 1
    return (arr)
    
inp = int(input('Input a number: '))
res = [str(x) for x in fibonacci(inp)]
print(f"First {str(inp)} Fibonacci numbers: {' '.join(res)}")