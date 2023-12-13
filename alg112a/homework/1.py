n = int(input("請輸入數字: "))
#如果小於陣列長度就進行計算再加入陣列
def fibonacci(n):
    fib= [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib
result = fibonacci(n)
print(result)