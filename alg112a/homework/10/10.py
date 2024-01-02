import numpy as np
from scipy.optimize import fsolve

def solve_polynomial(coefficients):
    # 定義多項式函數
    def polynomial_function(x):
        return np.polyval(coefficients, x)

    # 初始猜測值
    initial_guesses = np.linspace(-10, 10, len(coefficients))

    # 使用 fsolve 函數求解多項式的根
    roots = fsolve(polynomial_function, initial_guesses)

    return roots

# 輸入多項式的係數，例如 x^3 - 6x^2 + 11x - 6 的係數為 [1, -6, 11, -6]
coefficients = [1, 0, 0, 0, 0, 1]

# 求解多項式的根
roots = solve_polynomial(coefficients)

# 輸出結果
print(f"The roots of the polynomial are: {roots}")
