import pygame
import sys
from functions import *
from CONSTANCE import *

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

#Snake variables

#Note WIDTH and HEIGHT have been hard coded such that WIDTH//2 and HEIGHT//2 divide 20 evenly.
x = WIDTH // 2
y = HEIGHT // 2

snake_body = [[x, y]]
snake_body.append([x, y + GRID_SIZE])
snake_body.append([x, y + GRID_SIZE * 2])
snake_body.append([x, y + GRID_SIZE * 3])

grow = [0, 0]

is_over = [False]

#Arrow keys right, left, up and down will contol the snakes movement
#movement variable will be changed in the snake function
right = False
left = False
up = False
down = False
movement = [right, left, up, down,]

#If borders is set to True the game will end if the snake hits the edge of the screen
#If borders is set to False the snake will come out the other side screen
borders = False

#Switch grid_on to true to draw a grid
grid_on = False

#Food variables
food_x = (random.randint(0, WIDTH - GRID_SIZE) // GRID_SIZE) * GRID_SIZE 
food_y = (random.randint(SCORE_DISPLAY, HEIGHT - GRID_SIZE) // GRID_SIZE) * GRID_SIZE 
food = [food_x, food_y]

#Score variables
score_font = pygame.font.SysFont(None, 40)
score = [0]

def main(snake_body):
    
    active = True
    while active:

        snake_body = snake_body[-1:] + snake_body[:-1]

        screen.fill((BLACK))
        
        grid(screen, grid_on)

        draw_food(screen, snake_body, movement, grow, food)
        snake(screen, snake_body, movement, is_over, borders)

        game_score(screen, snake_body, movement, grow, food, score, score_font, is_over)

        game_over(screen, snake_body, is_over, borders)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main(snake_body)



