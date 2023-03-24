from logics import *
import pygame
import sys


def draw_interface():
    # draw header block
    pygame.draw.rect(screen, WHITE, TITLE_REC)

    # draw field in console
    pretty_print(mas)

    # draw blocks
    for row in range(BLOCKS):
        for col in range(BLOCKS):
            # get block`s value
            block_value = mas[row][col]
            block_text = block_font.render(f'{block_value}', True, BLACK)

            # draw 1 block
            w = SIZE_BLOCK * col + MARGIN * (col + 1)
            h = HEADER_HEIGHT + SIZE_BLOCK * row + MARGIN * (row + 1)
            pygame.draw.rect(screen, COLORS[block_value], (w, h, SIZE_BLOCK, SIZE_BLOCK))

            if block_value != 0:
                text_width, text_height = block_text.get_size()
                text_w = w + (SIZE_BLOCK - text_width) / 2
                text_h = h + (SIZE_BLOCK - text_height) / 2
                screen.blit(block_text, (text_w, text_h))


# define colors
WHITE = (255, 255, 255)
GRAY = (130, 130, 130)
BLACK = (0, 0, 0)


# set screen size
BLOCKS = 4
SIZE_BLOCK = 110
HEADER_HEIGHT = 110
MARGIN = 10
WIDTH = SIZE_BLOCK * BLOCKS + MARGIN * (BLOCKS + 1)
HEIGHT = WIDTH + HEADER_HEIGHT
TITLE_REC = pygame.Rect(0, 0, WIDTH, HEADER_HEIGHT)

mas = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

COLORS = {
    0: (130, 130, 130),
    2: (255, 255, 255),
    4: (255, 255, 128),
    8: (255, 255, 0)
}

mas[1][2] = 2
mas[3][0] = 4

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048")

# font for numbers in blocks
block_font = pygame.font.SysFont("stxingkai",70)

draw_interface()

while is_zero_in_mas(mas):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            # get empty cells
            empty_list = get_empty_list(mas)

            # get random empty cell
            random.shuffle(empty_list)
            random_num = empty_list.pop()

            # insert a number in the empty cell
            x, y = get_index_from_number(random_num)
            mas = insert_2_or_4(mas, x, y)
            print(f'We filled elem {random_num}')

            draw_interface()

    pygame.display.update()


