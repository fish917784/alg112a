import numpy as np

def df(f, p, k, step=1e-5):
    p1 = p.copy()
    p1[k] = p[k] + step
    return (f(p1) - f(p)) / step
def grad(f, p):
    gp = np.zeros_like(p)
    for k in range(len(p)):
        gp[k] = df(f, p, k)
    return gp
def gradient_descent(f, initial_point, learning_rate=0.1, iterations=1000, tolerance=1e-6):
    p = initial_point
    for i in range(iterations):
        gradient = grad(f, p)
        p_new = p - learning_rate * gradient
        if np.linalg.norm(p_new - p) < tolerance:
            break
        p = p_new
    return p
def target_function(p):
    x, y, z = p[0], p[1], p[2]
    return (x-1)*2 + (y-1)**2 + (z-1)**2
initial_point = np.array([1.0, 1.0, 1.0])
result = gradient_descent(target_function, initial_point)
print("最優解:", result)
print("目標函數在最優解處的值:", target_function(result))