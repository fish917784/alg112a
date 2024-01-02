def solve_maze(maze):
    def dfs(x, y, path):
        # 若目前位置是出口，表示找到解答
        if maze[x][y] == 'E':
            print("找到解答！")
            print("路徑：", path)
            print_maze(maze)
            return True

        # 標記目前位置為走過
        maze[x][y] = 'V'

        # 定義上下左右四個方向的移動
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # 嘗試往四個方向走
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # 檢查新位置是否在迷宮範圍內且未走過
            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] != 'W' and maze[nx][ny] != 'V':
                # 遞迴往下一步走
                if dfs(nx, ny, path + [(nx, ny)]):
                    return True

        return False

    def print_maze(maze):
        for row in maze:
            print(' '.join(row))
        print()

    # 找到老鼠的起點
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'S':
                # 從起點開始 DFS 搜尋
                if dfs(i, j, [(i, j)]):
                    return
                else:
                    print("找不到解答。")
                    return

# 迷宮範例
maze_example = [
    ['S', '.', '.', '.', 'W', '.'],
    ['.', 'W', 'W', '.', 'W', '.'],
    ['.', '.', '.', '.', '.', '.'],
    ['.', 'W', 'W', 'W', 'W', '.'],
    ['.', '.', '.', '.', 'E', '.']
]

# 解決迷宮問題
solve_maze(maze_example)
