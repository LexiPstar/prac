import pygame
import random

# 初始化 pygame
pygame.init()

# 定义颜色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# 定义游戏常量
WIDTH, HEIGHT = 400, 400  # 游戏窗口大小
GRID_SIZE = 20  # 每个格子的大小
ROWS = HEIGHT // GRID_SIZE
COLS = WIDTH // GRID_SIZE
NUM_MINES = 40  # 地雷数量

# 创建游戏窗口
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("扫雷游戏")

# 加载字体
font_path = "D:/BrowserDowanload/Ma_Shan_Zheng/MaShanZheng-Regular.ttf"
font = pygame.font.SysFont("MaShanZheng-Regular", 15)
large_font = pygame.font.SysFont("MaShanZheng-Regular", 50)

# 初始化游戏数据
def initialize_game():
    # 生成地雷
    mines = set()
    while len(mines) < NUM_MINES:
        mines.add((random.randint(0, ROWS - 1), random.randint(0, COLS - 1)))

    # 计算每个格子的数字
    grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]
    for (x, y) in mines:
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if 0 <= x + dx < ROWS and 0 <= y + dy < COLS:
                    grid[x + dx][y + dy] += 1
        grid[x][y] = -1  # 地雷标记为 -1

    # 初始化状态
    revealed = [[False for _ in range(COLS)] for _ in range(ROWS)]
    flagged = [[False for _ in range(COLS)] for _ in range(ROWS)]

    return grid, revealed, flagged, mines


# 绘制游戏界面
def draw_grid(grid, revealed, flagged):
    for x in range(ROWS):
        for y in range(COLS):
            rect = pygame.Rect(y * GRID_SIZE, x * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            if revealed[x][y]:
                if grid[x][y] == -1:  # 地雷
                    pygame.draw.rect(screen, RED, rect)
                else:  # 数字
                    pygame.draw.rect(screen, GRAY, rect)
                    if grid[x][y] > 0:
                        text = font.render(str(grid[x][y]), True, BLACK)
                        screen.blit(text, (y * GRID_SIZE + 5, x * GRID_SIZE + 5))
            else:
                pygame.draw.rect(screen, BLACK, rect)
                if flagged[x][y]:  # 标记地雷
                    text = font.render("F", True, GREEN)
                    screen.blit(text, (y * GRID_SIZE + 5, x * GRID_SIZE + 5))
            pygame.draw.rect(screen, WHITE, rect, 1)  # 绘制格子边框


# 无雷展开面
def reveal_empty(grid, revealed, x, y):
    if x < 0 or x >= ROWS or y < 0 or y >= COLS or revealed[x][y]:
        return
    revealed[x][y] = True
    if grid[x][y] == 0:  # 如果是空白格子，递归展开周围格子
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                reveal_empty(grid, revealed, x + dx, y + dy)


# 检查胜利条件
def check_win(grid, revealed):
    for x in range(ROWS):
        for y in range(COLS):
            if grid[x][y] != -1 and not revealed[x][y]:
                return False
    return True


# 主游戏循环
def main():
    grid, revealed, flagged, mines = initialize_game()
    running = True
    game_over = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                x, y = event.pos[1] // GRID_SIZE, event.pos[0] // GRID_SIZE
                if event.button == 1:  # 左键点击
                    if grid[x][y] == -1:  # 踩到地雷
                        game_over = True
                        revealed[x][y] = True
                    else:
                        reveal_empty(grid, revealed, x, y)
                elif event.button == 3:  # 右键点击
                    flagged[x][y] = not flagged[x][y]

        screen.fill(BLACK)
        draw_grid(grid, revealed, flagged)

        # 检查胜利
        if check_win(grid, revealed):
            display_message("你赢了！", GREEN)
            game_over = True

        # 显示游戏结束信息
        if game_over:
            if check_win(grid, revealed):
                display_message("你赢了！", GREEN)
            else:
                display_message("你输了！", RED)

        pygame.display.flip()

    pygame.quit()


# 显示消息
def display_message(message, color):
    text = large_font.render(message, True, color)
    screen.blit(text, (WIDTH // 2 - 50, HEIGHT // 2))


# 启动游戏
if __name__ == "__main__":
    main()
