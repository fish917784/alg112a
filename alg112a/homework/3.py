
def permutation(n, p=None):
    #先把p用為空陣列
    if p is None:
        p = []
    #假如陣列長度＝n 就是完整的排列
    if len(p) == n:
        print(p)
        return
    #重複生成
    for i in range(n):
        if i not in p:
            permutation(n, p + [i])

permutation(5)
#有用ChatGPT
