import random

def neighbor(p, h):
    i = len(p)
    start = 0
    p1 = p.copy()# 生成鄰近點，每個維度上的值都在原值附近加減h
    while start < i:
        p1[start] += random.uniform(-h, h)
        start += 1 
    return p1

def hillClimbing(f, p, h=0.01, max=10000):
    fail_count = 0
    for _ in range(max):
        f_now = f(p)# 生成鄰近點
        p1 = neighbor(p, h)
        f1 = f(p1)# 如果新點的函數值高於當前點，移動至新點
        if f1 >= f_now:
            p = p1
            print('p=', p, 'f(p)=', f1)
            fail_count = 0
        else:
            fail_count += 1
    return p, f(p)

def f(p):
    return -1 * (p[0]**2 + p[1]**2 + p[2]**2)

# 起始點
start_point = [2, 1, 3]

# 執行爬山演算法
final_point, max_value = hillClimbing(f,start_point)

print(f'最終座標 p = {final_point}')
print(f'最大值 f = {max_value}')
