import pygame
import time
import random
# Initialize pygame
pygame.init()

display_width = 800
display_height = 600

# Define colors(rgb, because that's how pygame does it)
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
# Create window
win = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('My First py-game')

# Create a Clock
clock = pygame.time.Clock()


def game_loop():
    # Crashed variable
    game_exit = False

    # Ship variables
    x = (display_width / 2.1)
    y = (display_height * 0.8)
    ship_width = 40
    ship_height = 60
    shipspeed = 0

    # blocks variables
    block_x = random.randrange(0, display_width)
    block_y = -600
    block_width = 80
    block_height = 80

    block_speed = 8

    # Score variables
    score = 0
# Defining my functions

    def ship(ship_x, ship_y):
        pygame.draw.rect(win, black, (ship_x, ship_y, ship_width, ship_height))

    def blocks(blockx, blocky, block_width, block_height, color):
        pygame.draw.rect(win, color, (blockx, blocky, block_width, block_height))

    def text_objects(text, font):
        text_surf = font.render(text, True, black)
        return text_surf, text_surf.get_rect()

    def message_display(text):
        big_text = pygame.font.Font("freesansbold.ttf", 115)
        text_surf, text_rect = text_objects(text, big_text)
        text_rect.center = ((display_width/2), (display_height/2))
        win.blit(text_surf, text_rect)
        pygame.display.update()
        time.sleep(2)

        game_loop()

    def crash():
        message_display("You crashed")

# Game Loop:
    while not game_exit:
        # Events area
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('Game Finished')
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    shipspeed = -5
                if event.key == pygame.K_RIGHT:
                    shipspeed = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    shipspeed = 0
                if event.key == pygame.K_RIGHT:
                    shipspeed = 0

        # //-//
        win.fill(white)
        x += shipspeed
        block_y += block_speed
        ship(x, y)
        # blockx, blocky, block_width, block_height, color
        blocks(block_x, block_y, block_width, block_height, red)

        if block_y - block_width > display_height:
            block_y = -40
            block_x = random.randrange(0, display_width)
            block_speed += 0.5

        if x > display_width - ship_width or x < 0:
            crash()

        if y < block_y + block_height:
            print("y cross")
            if block_x < x < block_x + block_height or block_x < x + ship_width < block_x + block_height:
                print("x cross")
                crash()

        pygame.display.update()
        clock.tick(80)


game_loop()
pygame.quit()
