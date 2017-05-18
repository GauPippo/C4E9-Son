import pygame

# Create screen 600, 400
pygame.init()
# Change title game console => Sokobannnnn
pygame.display.set_caption("Sokobannnn")
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

square_width = square_image.get_width()
square_height = square_image.get_height()

col_count = 5
row_count = 5

box_x = 100
box_y = 150

box_col = 2
box_row = 2

box_width = box_image.get_width()
box_height = box_image.get_height()

right_pressed = False
left_pressed = False
up_pressed = False
down_pressed = False
step = 1

while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                mario_row += step
            elif event.key == pygame.K_LEFT:
                mario_row -= step
            elif event.key == pygame.K_UP:
                mario_col -= step
            elif event.key == pygame.K_DOWN:
                mario_col += step

    screen.fill((0, 255, 0))

    # row, col
    for col in range(col_count):
        for row in range(row_count):
            x = row * square_width - square_width / 2 + 16
            y = col * square_height - square_height / 2 + 16

            screen.blit(square_image, (x, y))

    mario_x = (mario_row * square_width) - square_width / 2 + 16
    mario_y = (mario_col * square_height) - square_height / 2 + 16

    box_x = (box_row * square_width) - square_width / 2 + 50
    box_y = (box_col * square_height) - square_height / 2 + 50


    if mario_x > x or mario_x < 0 or mario_y > y or mario_y < 0:
        mario_row = 0
        mario_col = 0
        print("Ko duoc di chuyen ra khoi ban do")

    # Blit : Ve hinh mario o vi tri x , y
    screen.blit(mario_image,(mario_x, mario_y))

    # Show box in map
    screen.blit(box_image, (box_x, box_y))

    # Show in mario 50, 100 in console
    pygame.display.flip()
    # Speed of mario_image
    clock.tick(60)