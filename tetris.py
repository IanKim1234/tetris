import pygame
import random

pygame.font.init()

s_width = 800
s_height = 700
play_width = 300
play_height = 600
top_left_x = (s_width - play_width)//2
top_left_y = (s_height - play_height)

shapeO_1 = [[1, 1, 0, 0],
            [1, 1, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]]

shapeO_2 = [[1, 1, 0, 0],
            [1, 1, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]]

shapeO_3 = [[1, 1, 0, 0],
            [1, 1, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]]

shapeO_4 = [[1, 1, 0, 0],
            [1, 1, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]]
shapeO = [
    shapeO_1,
    shapeO_2,
    shapeO_3,
    shapeO_4
]
"----------------------------"
shapeI_1 = [[2, 0, 0, 0],
            [2, 0, 0, 0],
            [2, 0, 0, 0],
            [2, 0, 0, 0]]

shapeI_2 = [[2, 2, 2, 2],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]]

shapeI_3 = [[2, 0, 0, 0],
            [2, 0, 0, 0],
            [2, 0, 0, 0],
            [2, 0, 0, 0]]

shapeI_4 = [[2, 2, 2, 2],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]]
shapeI = [
    shapeI_1,
    shapeI_2,
    shapeI_3,
    shapeI_4
]
"----------------------------"

shapeS_1 = [[0, 3, 3],
            [3, 3, 0],
            [0, 0, 0]]

shapeS_2 = [[3, 0, 0],
            [3, 3, 0],
            [0, 3, 0]]

shapeS_3 = [[0, 3, 3],
            [3, 3, 0],
            [0, 0, 0]]

shapeS_4 = [[3, 0, 0],
            [3, 3, 0],
            [0, 3, 0]]
shapeS = [
    shapeS_1,
    shapeS_2,
    shapeS_3,
    shapeS_4
]
"----------------------------"
shapeZ_1 = [[4, 4, 0],
            [0, 4, 4],
            [0, 0, 0]]

shapeZ_2 = [[0, 4, 0],
            [4, 4, 0],
            [4, 0, 0]]

shapeZ_3 = [[4, 4, 0],
            [0, 4, 4],
            [0, 0, 0]]

shapeZ_4 = [[0, 4, 0],
            [4, 4, 0],
            [4, 0, 0]]
shapeZ = [
    shapeZ_1,
    shapeZ_2,
    shapeZ_3,
    shapeZ_4
]
"----------------------------"
shapeL_1 = [[5,0, 0],
            [5,0, 0],
            [5,5, 0]]

shapeL_2 = [[5, 5, 5],
            [5, 0, 0],
            [0, 0, 0]]

shapeL_3 = [[5, 5, 0],
            [0, 5, 0],
            [0, 5, 0]]

shapeL_4 = [[0, 0, 5],
            [5, 5, 5],
            [0, 0, 0]]
shapeL = [
    shapeL_1,
    shapeL_2,
    shapeL_3,
    shapeL_4
]
"----------------------------"
shapeJ_1 = [[0, 6, 0],
            [0, 6, 0],
            [6, 6, 0]]

shapeJ_2 = [[6, 0, 0],
            [6, 6, 6],
            [0, 0, 0]]

shapeJ_3 = [[6, 6, 0],
            [6, 0, 0],
            [6, 0, 0]]

shapeJ_4 = [[6, 6, 6],
            [0, 0, 6],
            [0, 0, 0]]
shapeJ = [
    shapeJ_1,
    shapeJ_2,
    shapeJ_3,
    shapeJ_4
]
"----------------------------"
shapeT_1 = [[7, 7, 7],
            [0, 7, 0],
            [0, 0, 0]]

shapeT_2 = [[7, 0, 0],
            [7, 7, 0],
            [7, 0, 0]]

shapeT_3 = [[0, 7, 0],
            [7, 7, 7],
            [0, 0, 0]]

shapeT_4 = [[0, 7, 0],
            [7, 7, 0],
            [0, 7, 0]]
shapeT = [
    shapeT_1,
    shapeT_2,
    shapeT_3,
    shapeT_4
]
"----------------------------"

SHAPES = [shapeO, shapeI, shapeS, shapeZ, shapeL, shapeJ, shapeT]
shape_colors = [
    (255, 0, 0),
    (255,165,0),
    (255,215,0),
    (0,0,205),
    (176,224,230),
    (124,252,0),
    (75,0,130)
]

class Piece(object):
    def __init__(self, x, y, shape):
        self.shape = shape
        self.rotation = 0
        self.color = shape_colors[SHAPES.index(shape)]
        self.x = x
        self.y = y

def create_grid(locked_positions={}):
    print("yes")
    grid = [[0 for column in range(10)] for row in range(20)]
    for x in grid:
        print(x)

def convert_shape_format(shape):
    pass

def valid_space(shape, grid):
    pass

def check_lost(positions):
    pass

def get_shape():
    return Piece(5, 0, random.choice(SHAPES))

def draw_text_middle(text, size, color, surface):
    font = pygame.font.SysFont("comicsans", size, bold=True)
    label = font.render(text , 1, color)
    surface.blit(label,(
        (top_left_x + play_width/2) - (label.get_width()/2),
        (top_left_y + play_width / 2) - (label.get_height() / 2)))

def draw_grid(surface, row, col):
    pass

def clear_rows(grid, locked):
    pass

def draw_next_shape(shape, surface):
    font = pygame.font.SysFont("comicsans", 60)
    label = font.render("Next shape", 1, (255, 255, 255))
    surface.blit(label,
             (top_left_x + play_width / 2 - (label.get_width() / 2), 30))

def draw_window(win, grid):
    win.fill((0, 0, 0))
    font = pygame.font.SysFont("comicsans", 60)
    label = font.render("Tetris", 1, (255,255,255))
    win.blit(label,
             (top_left_x+play_width/2 - (label.get_width()/2), 30))
    pygame.draw.rect(win,
                     (255,0,0),
                     (top_left_x, top_left_y, play_width, play_height),
                     5)
def main(win):
    locked_positions = {}
    grid = create_grid(locked_positions)
    current_shape = get_shape()
    next_shape = get_shape()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window(win, grid)
        draw_next_shape(next_shape, win)
        pygame.display.update()

def main_menu(win):
    run = True
    while run:
        win.fill((0, 0, 0))

        draw_text_middle("Press any key to start!", 60, (255, 255, 255), win)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                main(win)


window = pygame.display.set_mode((s_width, s_height))


main_menu(window)