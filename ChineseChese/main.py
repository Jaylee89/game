import pygame
import sys

# 初始化pygame
pygame.init()

# 设置屏幕大小
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("中国象棋")

# 加载棋盘图片
board_img = pygame.image.load("chess_board.png")
board_img = pygame.transform.scale(board_img, (800, 800))

# 加载棋子图片
pieces = {
    "r_king": pygame.image.load("r_king.png"),
    "r_advisor": pygame.image.load("r_advisor.png"),
    "r_elephant": pygame.image.load("r_elephant.png"),
    "r_horse": pygame.image.load("r_horse.png"),
    "r_chariot": pygame.image.load("r_chariot.png"),
    "r_cannon": pygame.image.load("r_cannon.png"),
    "r_soldier": pygame.image.load("r_soldier.png"),
    "b_king": pygame.image.load("b_king.png"),
    "b_advisor": pygame.image.load("b_advisor.png"),
    "b_elephant": pygame.image.load("b_elephant.png"),
    "b_horse": pygame.image.load("b_horse.png"),
    "b_chariot": pygame.image.load("b_chariot.png"),
    "b_cannon": pygame.image.load("b_cannon.png"),
    "b_soldier": pygame.image.load("b_soldier.png")
}

# 缩放棋子图片
for key in pieces:
    pieces[key] = pygame.transform.scale(pieces[key], (80, 80))

# 定义棋盘初始布局
initial_board = [
    ["b_chariot", "b_horse", "b_elephant", "b_advisor", "b_king", "b_advisor", "b_elephant", "b_horse", "b_chariot"],
    ["", "", "", "", "", "", "", "", ""],
    ["", "b_cannon", "", "", "", "", "", "b_cannon", ""],
    ["b_soldier", "", "b_soldier", "", "b_soldier", "", "b_soldier", "", "b_soldier"],
    ["", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", ""],
    ["r_soldier", "", "r_soldier", "", "r_soldier", "", "r_soldier", "", "r_soldier"],
    ["", "r_cannon", "", "", "", "", "", "r_cannon", ""],
    ["", "", "", "", "", "", "", "", ""],
    ["r_chariot", "r_horse", "r_elephant", "r_advisor", "r_king", "r_advisor", "r_elephant", "r_horse", "r_chariot"]
]

# 定义一个函数来绘制棋盘和棋子
def draw_board(screen, board):
    screen.blit(board_img, (0, 0))
    for y in range(10):
        for x in range(9):
            piece = board[y][x]
            if piece != "":
                screen.blit(pieces[piece], (x * 80, y * 80))

# 主循环
board = initial_board
selected_piece = None
selected_pos = None

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            x //= 80
            y //= 80
            if selected_piece:
                board[selected_pos[1]][selected_pos[0]] = ""
                board[y][x] = selected_piece
                selected_piece = None
            else:
                selected_piece = board[y][x]
                selected_pos = (x, y)

    screen.fill((255, 255, 255))
    draw_board(screen, board)
    pygame.display.flip()