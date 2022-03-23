import pygame
import random
from CONSTANCE import *


def grid(screen, grid_on):
    
    draw_grid = 0
    
    if grid_on == True:

        for i in range(0, WIDTH // GRID_SIZE):
            draw_grid += GRID_SIZE
            
            pygame.draw.line(screen, GRAY, (draw_grid, 0), (draw_grid, HEIGHT), 1)
            pygame.draw.line(screen, GRAY, (0, draw_grid), (WIDTH, draw_grid), 1)
    else:
        pass

def game_score(screen, snake_body, movement, grow, food, score, game_font, is_over):
    
    score_board = pygame.Rect(0, 0, WIDTH, SCORE_DISPLAY)
    score_rect = pygame.Rect(WIDTH - 200, 12, 200, 30)
    game_over_rect = pygame.Rect(50, 12, 100, 30)

    show_score = game_font.render("Score: " + str(score[0]), True, BLACK)
    game_is_over = game_font.render("GAME OVER!", True, BLACK)

    screen.set_clip(score_board)

    pygame.draw.rect(screen, GRAY, score_board)

    screen.blit(show_score, score_rect)

    if is_over[0] == True:
        screen.blit(game_is_over, game_over_rect)
        
        keys = pygame.key.get_pressed()
        
        #Resetting the game        
        if keys[pygame.K_RETURN]:
            
            is_over[0] = False

            score[0] = 0

            grow[0] = 0
            grow[1] = 0

            movement[0] = False
            movement[1] = False
            movement[2] = False
            movement[3] = False

            x = WIDTH // 2
            y = HEIGHT // 2

            snake_body.clear() 
            snake_body.append([x, y]) 
            snake_body.append([x, y + GRID_SIZE])
            snake_body.append([x, y + GRID_SIZE * 2])
            snake_body.append([x, y + GRID_SIZE * 3])

    screen.set_clip(None)
    
    if snake_body[0] == food:
        score[0] += 1


def game_over(screen, snake_body, is_over, borders):

    for segment in snake_body[1:]:
        if snake_body[0] == segment:
            is_over[0] = True
    
    #If borders == True the game will stop if the snake runs into the edge
    if borders == True:

        if snake_body[0][0] + GRID_SIZE > WIDTH:
            is_over[0] = True

        if snake_body[0][0] < 0:
            is_over[0] = True

        if snake_body[0][1] < SCORE_DISPLAY:
            is_over[0] = True

        if snake_body[0][1] + GRID_SIZE > HEIGHT:
            is_over[0] = True
         

def draw_food(screen, snake_body, movement, grow, food):

    pygame.draw.rect(screen, RED, [food[0], food[1], GRID_SIZE, GRID_SIZE])

    if snake_body[0] == food:

        while True:
            food[0] = (random.randint(0, WIDTH - GRID_SIZE) // GRID_SIZE) * GRID_SIZE
            food[1] = (random.randint(SCORE_DISPLAY, HEIGHT - GRID_SIZE) // GRID_SIZE) * GRID_SIZE

            food_tpl = (food[0], food[1])

            if food_tpl in snake_body:
                continue

            else:
                pygame.draw.rect(screen, RED, [food[0], food[1], GRID_SIZE, GRID_SIZE])
                break

        grow = list(snake_body[-1])

        if movement[0] == True:
            grow[0] += GRID_SIZE

        if movement[1] == True:
            grow[0] -= GRID_SIZE

        if movement[2] == True:
            grow[1] += GRID_SIZE

        if movement[3] == True:
            grow[1] -= GRID_SIZE

        snake_body.append(grow)


def snake(screen, snake_body, movement, is_over, borders):
    
    #Drawing the snake
    for (i, j) in snake_body:
        
        pygame.draw.rect(screen, WHITE, [i, j, GRID_SIZE, GRID_SIZE])    
    
    if is_over[0] == False:

        #Moving the snake
        keys = pygame.key.get_pressed()

        #Right
        if keys[pygame.K_RIGHT] and movement[1] != True:

            movement[0] = True

            #movement[2] = False
            #movement[3] = False


        #Left
        elif keys[pygame.K_LEFT] and movement[0] != True:
            
            movement[1] = True

            movement[2] = False
            movement[3] = False

        #Up
        elif keys[pygame.K_UP] and movement[3] != True:
            
            movement[2] = True

            movement[0] = False
            movement[1] = False

        #Down
        elif keys[pygame.K_DOWN] and movement[2] != True:

            movement[3] = True

            movement[0] = False
            movement[1] = False
        
        #changing direction

        #Right
        if movement[0] == True:
            snake_body[0][0] = snake_body[1][0] + GRID_SIZE
            snake_body[0][1] = snake_body[1][1] 
 
            movement[2] = False
            movement[3] = False

       
        #Left 
        if movement[1] == True:
            snake_body[0][0] = snake_body[1][0] - GRID_SIZE
            snake_body[0][1] = snake_body[1][1] 
         
        #Up 
        if movement[2] == True:
            snake_body[0][0] = snake_body[1][0]
            snake_body[0][1] = snake_body[1][1] - GRID_SIZE
        
        #Down
        if movement[3] == True:
            snake_body[0][0] = snake_body[1][0]
            snake_body[0][1] = snake_body[1][1] + GRID_SIZE
        
        #Handling if the snake collides with the edge of the screen
        #If borders == False the snake will pass through the walls and come out the other side
        if borders == False:

            if snake_body[0][0] + GRID_SIZE > WIDTH:
                snake_body[0][0] = 0
            
            if snake_body[0][0] < 0:
                snake_body[0][0] = WIDTH
            
            if snake_body[0][1] + GRID_SIZE > HEIGHT:
                snake_body[0][1] = SCORE_DISPLAY

            if snake_body[0][1] < SCORE_DISPLAY:
                snake_body[0][1] = HEIGHT 



