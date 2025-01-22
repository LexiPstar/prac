import random
import pygame

# 初始化 pygame
pygame.init()

# 定义颜色
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# 定义屏幕尺寸
width = 600
height = 400

# 创建游戏窗口
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("贪吃蛇游戏")

# 定义时钟
clock = pygame.time.Clock()

# 定义蛇的大小和速度
snake_block = 10
snake_speed = 15

# 设置字体
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


# 显示分数
def display_score(score):
    value = score_font.render("分数: " + str(score), True, yellow)
    screen.blit(value, [10, 10])


# 绘制蛇
def draw_snake(snake_block, snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, green, [block[0], block[1], snake_block, snake_block])


# 显示消息
def display_message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [width / 6, height / 3])


# 游戏循环
def game_loop():
    game_over = False
    game_close = False

    # 蛇的初始位置
    x = width / 2
    y = height / 2

    # 蛇的移动方向
    x_change = 0
    y_change = 0

    # 蛇的身体
    snake_list = []
    snake_length = 1

    # 食物的位置
    food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            screen.fill(blue)
            display_message("你输了！按 Q 退出游戏，按 C 重新开始", red)
            display_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_block
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_block
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -snake_block
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = snake_block
                    x_change = 0

        # 检查是否撞墙
        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

        x += x_change
        y += y_change
        screen.fill(black)

        # 绘制食物
        pygame.draw.rect(screen, red, [food_x, food_y, snake_block, snake_block])

        # 更新蛇的身体
        snake_head = [x, y]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        # 检查是否撞到自己
        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        draw_snake(snake_block, snake_list)
        display_score(snake_length - 1)

        pygame.display.update()

        # 检查是否吃到食物
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


# 启动游戏
game_loop()


import pygame
import random

# 初始化 pygame
pygame.init()

# 定义颜色
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# 定义屏幕尺寸
width = 600
height = 400

# 创建游戏窗口
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("贪吃蛇游戏")

# 定义时钟
clock = pygame.time.Clock()

# 定义蛇的大小和速度
snake_block = 10
snake_speed = 15

# 设置字体
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


# 显示分数
def display_score(score):
    value = score_font.render("分数: " + str(score), True, yellow)
    screen.blit(value, [10, 10])


# 绘制蛇
def draw_snake(block_size, snake_body):
    for block in snake_body:
        pygame.draw.rect(screen, green, [block[0], block[1], block_size, block_size])


# 显示消息
def display_message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [width / 6, height / 3])


# 游戏循环
def game_loop():
    game_over = False
    game_close = False

    # 蛇的初始位置
    x = width / 2
    y = height / 2

    # 蛇的移动方向
    x_change = 0
    y_change = 0

    # 蛇的身体
    snake_list = []
    snake_length = 1

    # 食物的位置
    food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    try:
        while not game_over:

            while game_close:
                screen.fill(blue)
                display_message("你输了！按 Q 退出游戏，按 C 重新开始", red)
                display_score(snake_length - 1)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = True
                            game_close = False
                        if event.key == pygame.K_c:
                            game_loop()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x_change = -snake_block
                        y_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x_change = snake_block
                        y_change = 0
                    elif event.key == pygame.K_UP:
                        y_change = -snake_block
                        x_change = 0
                    elif event.key == pygame.K_DOWN:
                        y_change = snake_block
                        x_change = 0

            # 检查是否撞墙
            if x >= width or x < 0 or y >= height or y < 0:
                game_close = True

            x += x_change
            y += y_change
            screen.fill(black)

            # 绘制食物
            pygame.draw.rect(screen, red, [food_x, food_y, snake_block, snake_block])

            # 更新蛇的身体
            snake_head = [x, y]
            snake_list.append(snake_head)
            if len(snake_list) > snake_length:
                del snake_list[0]

            # 检查是否撞到自己
            for block in snake_list[:-1]:
                if block == snake_head:
                    game_close = True

            draw_snake(snake_block, snake_list)
            display_score(snake_length - 1)

            pygame.display.update()

            # 检查是否吃到食物
            if x == food_x and y == food_y:
                food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
                food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
                snake_length += 1

            clock.tick(snake_speed)

    except KeyboardInterrupt:
        print("\n游戏被用户中断！")
    finally:
        pygame.quit()
        quit()


# 启动游戏
game_loop()


import pygame
import random

# 初始化 pygame
pygame.init()

# 定义颜色
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# 定义屏幕尺寸
width = 600
height = 400

# 创建游戏窗口
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("贪吃蛇游戏")

# 定义时钟
clock = pygame.time.Clock()

# 定义蛇的大小和速度
snake_block = 10
snake_speed = 10

# 设置字体
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
font_path = "D:/BrowserDowanload/Ma_Shan_Zheng/MaShanZheng-Regular.ttf"

try:
    font_style = pygame.font.Font(font_path, 30)
except Exception as e:
    print(f"字体加载失败: {e}")


# 显示分数
def display_score(score):
    value = score_font.render("分数: " + str(score), True, yellow)
    screen.blit(value, [10, 10])


# 显示暴击
def display_crit_status(is_crit):
    if is_crit:
        crit_text = font_style.render('暴击激活', True, red)
    else:
        crit_text = font_style.render('暴击未激活', False, white)
    screen.blit(crit_text, [width - 200, 10])


# 绘制蛇
def draw_snake(block_size, snake_body):
    for block in snake_body:
        pygame.draw.rect(screen, green, [block[0], block[1], block_size, block_size])


# 显示消息
def display_message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [width / 6, height / 3])


# 游戏循环
def game_loop():
    game_over = False
    game_close = False

    # 蛇的初始位置
    x = width / 2
    y = height / 2

    # 蛇的移动方向
    x_change = 0
    y_change = 0

    # 蛇的身体
    snake_list = []
    snake_length = 1

    # 食物的位置
    food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    # 暴击变量
    crit_counter = 0
    is_crit = False

    try:
        while not game_over:

            while game_close:
                screen.fill(blue)
                display_message(f"你输了！按 Q 退出游戏，按 C 重新开始", red)
                display_score(snake_length - 1)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = True
                            game_close = False
                        if event.key == pygame.K_c:
                            game_loop()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and x_change == 0:  # 防止反向移动
                        x_change = -snake_block
                        y_change = 0
                    elif event.key == pygame.K_RIGHT and x_change == 0:
                        x_change = snake_block
                        y_change = 0
                    elif event.key == pygame.K_UP and y_change == 0:
                        y_change = -snake_block
                        x_change = 0
                    elif event.key == pygame.K_DOWN and y_change == 0:
                        y_change = snake_block
                        x_change = 0

            # 检查是否撞墙
            if x >= width or x < 0 or y >= height or y < 0:
                game_close = True

            # 更新蛇的位置
            x += x_change
            y += y_change
            screen.fill(black)

            # 绘制食物
            pygame.draw.rect(screen, red, [food_x, food_y, snake_block, snake_block])

            # 更新蛇的身体
            snake_head = [x, y]
            snake_list.append(snake_head)
            if len(snake_list) > snake_length:
                del snake_list[0]

            # 检查是否撞到自己
            for block in snake_list[:-1]:
                if block == snake_head:
                    game_close = True

            draw_snake(snake_block, snake_list)
            display_score(snake_length - 1)

            pygame.display.update()

            # 检查是否吃到食物
            if x == food_x and y == food_y:
                crit_counter += 1
                if crit_counter >= 5:
                    is_crit = True
                    crit_counter = 0
                if is_crit:
                    snake_length += 2
                    is_crit = False
                else:
                    snake_length += 1

                food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
                food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
                snake_length += 1

            clock.tick(snake_speed)

    except KeyboardInterrupt:
        print("\n游戏被用户中断！")
    finally:
        pygame.quit()
        quit()


# 启动游戏
game_loop()
