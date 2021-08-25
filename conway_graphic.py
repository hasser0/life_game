import pygame
from time import sleep
from life_algo import conway_iter

WIDTH, HEIGHT = 600,600
BLOCK_SIZE = 20
BLACK = (0,0,0)
WHITE = (255,255,255)
PINK = (255,182,193)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Conway game")

def main():
    run = True
    matrix = [[0 for _ in range(30)] for _ in range(30)]
    #Heart
    matrix[3][4] = 1
    matrix[2][5] = 1
    matrix[3][6] = 1
    matrix[4][5] = 1
    matrix[8][11] = 1
    matrix[10][11] = 1
    matrix[9][10] = 1
    matrix[9][12] = 1
    matrix[12][7] = 1
    matrix[6][3] = 1
    matrix[6][4] = 1
    matrix[6][5] = 1
    matrix[6][6] = 1
    matrix[6][7] = 1
    matrix[7][8] = 1
    matrix[8][8] = 1
    matrix[9][8] = 1
    matrix[10][8] = 1
    matrix[11][8] = 1
    matrix[7][2] = 1
    matrix[8][2] = 1
    matrix[8][2] = 1
    matrix[8][3] = 1
    matrix[8][4] = 1
    matrix[8][4] = 1
    matrix[9][4] = 1
    matrix[10][5] = 1
    matrix[10][6] = 1
    matrix[10][6] = 1
    matrix[11][6] = 1
    matrix[12][6] = 1

    for x in range(0, WIDTH, BLOCK_SIZE):
        for y in range(0, HEIGHT, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(WIN, WHITE, rect, 1)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        for row in range(30):
            for col in range(30):
                rect = pygame.Rect(row*BLOCK_SIZE+1, col*BLOCK_SIZE+1, BLOCK_SIZE-2, BLOCK_SIZE-2)
                if matrix[row][col] == 0:
                    pygame.draw.rect(WIN, BLACK, rect, 0)
                if matrix[row][col] == 1:
                    pygame.draw.rect(WIN, PINK, rect, 0)
        matrix = conway_iter(matrix)
        sleep(0.5)
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()