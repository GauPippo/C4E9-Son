import pygame

pygame.init()

# Change title game console => Sokobannnnn
pygame.display.set_caption("Sokobannnn")
# Creat screen console 600x400
screen = pygame.display.set_mode((600, 400))
loop = True
clock = pygame.time.Clock()

# Add image object
mario_image = pygame.image.load("sokoban_images/mario.png")
square_image = pygame.image.load("sokoban_images/square.png")
box_image = pygame.image.load("sokoban_images/box.png")

#Set variable
mario_col = 0
mario_row = 0
mario_next_x = 0
mario_next_y = 0

square_width = square_image.get_width()
square_height = square_image.get_height()

col_count = 8
row_count = 8

box_next_x = 0
box_next_y = 0

box_col = 2
box_row = 2

box_width = box_image.get_width()
box_height = box_image.get_height()

right_pressed = False
left_pressed = False
up_pressed = False
down_press = False

def maps(next_col, next_row):
    if next_col >= 0 and next_col < col_count and next_row >= 0 and next_row < row_count:
        return True
    return False

while loop:
    x_step = 0
    y_step = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                    y_step = 1
            elif event.key == pygame.K_LEFT:
                    y_step = -1
            elif event.key == pygame.K_UP:
                    x_step = -1
            elif event.key == pygame.K_DOWN:
                    x_step = 1
            else:
                pass

            mario_next_x = mario_col + x_step
            mario_next_y = mario_row + y_step

            if maps(mario_next_x, mario_next_y):
                if (mario_next_x, mario_next_y) != (box_col, box_row):
                    mario_row = mario_next_y
                    mario_col = mario_next_x
    screen.fill((0, 255, 0))

    # row, col, display map

    for col in range(col_count):
        for row in range(row_count):
            x = row * square_width - square_width / 2 + 16
            y = col * square_height - square_height / 2 + 16

            screen.blit(square_image, (x, y))

    mario_x = (mario_row * square_width) - square_width / 2 + 16
    mario_y = (mario_col * square_height) - square_height / 2 + 16

    box_x = (box_row * square_width) - square_width / 2 + 50
    box_y = (box_col * square_height) - square_height / 2 + 50

    # Blit : Ve hinh mario o vi tri x , y
    screen.blit(mario_image,(mario_x, mario_y))

    # Show box in map
    screen.blit(box_image, (box_x, box_y))

    # Show in mario 50, 100 in console
    pygame.display.flip()

    # Speed of mario_image
    clock.tick(60)