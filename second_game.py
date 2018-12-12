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
red = (200, 10, 20)
red_2 = (255, 0, 0)
green = (0, 220, 0)
green_2 = (10, 255, 10)
# Create window
win = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('My First py-game')

# Create a Clock
clock = pygame.time.Clock()

# Counter variable
counter = 0
high_score = 0

# Intro variable
intro = True


def button(msg, x, y, w, h, inact, act, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(win, act, (x, y, w, h))
        if click[0] == 1 and action == "play":
            game_loop()
        elif click[0] == 1 and action == "quit":
            pygame.quit()
            quit()
    else:
        pygame.draw.rect(win, inact, (x, y, w, h))

    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    win.blit(textSurf, textRect)


def text_objects(text, font):
    text_surf = font.render(text, True, black)
    return text_surf, text_surf.get_rect()


def message_display(text):

    big_text = pygame.font.Font("freesansbold.ttf", 115)
    text_surf, text_rect = text_objects(text, big_text)
    text_rect.center = ((display_width / 2), (display_height / 2))
    win.blit(text_surf, text_rect)

    pygame.display.update()
    time.sleep(2)


def crash():
    message_display("You crashed")
    game_intro()


# Start screen
def game_intro():

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        win.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects("Race-Game", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        win.blit(TextSurf, TextRect)

        # button(msg, x, y, width, height, actColor, color)
        button("Go!", 150, 450, 100, 50, green, green_2, "play")
        button("Quit", 550, 450, 100, 50, red, red_2, "quit")

        pygame.display.update()
        clock.tick(15)


def game_loop():
    global counter
    counter = 0
    global high_score
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

    block_speed = 6

    # Defining my functions

    def score(count):
        font = pygame.font.SysFont(None, 25)
        text = font.render("Score: " + str(count) + " High Score: " + str(high_score), True, black)
        win.blit(text, (0, 0))

    def ship(ship_x, ship_y):
        pygame.draw.rect(win, black, (ship_x, ship_y, ship_width, ship_height))

    def blocks(blockx, blocky, block_width, block_height, color):
        pygame.draw.rect(win, color, (blockx, blocky, block_width, block_height))

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
        score(counter)
        # blockx, blocky, block_width, block_height, color
        blocks(block_x, block_y, block_width, block_height, red)

        if block_y - block_width > display_height:
            block_y = -40
            block_x = random.randrange(0, display_width)
            block_speed += 0.5
            block_width += 2
            counter += 1
            # high score
            if counter > high_score:
                high_score = counter

        if x > display_width - ship_width or x < 0:
            crash()

        if y < block_y + block_height:
            if block_x < x < block_x + block_height or block_x < x + ship_width < block_x + block_height:
                crash()

        pygame.display.update()
        clock.tick(80)


game_intro()

game_loop()

pygame.quit()
