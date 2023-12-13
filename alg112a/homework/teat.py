import random

def neighbor(p, h):
    p1 = p.copy()
    p1[0] += random.uniform(-h, h)
    p1[1] += random.uniform(-h, h)
    return p1

def hillClimbing(f, p, h=0.01, max_iter=10000):
    fail_count = 0
    for _ in range(max_iter):
        f_now = f(*p)
        p1 = neighbor(p, h)
        f1 = f(*p1)
        if f1 >= f_now:
            p = p1
            print('p=', p, 'f(p)=', f1)
            fail_count = 0
        else:
            fail_count += 1
    return p, f(*p)

def f(x, y):
    return -x**2 - y**2

# 起始點
initial_point = [1, 1]

# 執行爬山演算法
final_point, max_value = hillClimbing(f, initial_point)

print(f'最終座標 p = {final_point}')
print(f'最大值 f = {max_value}')
