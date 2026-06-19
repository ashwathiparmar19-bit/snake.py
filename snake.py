import pygame 
import random
import time

# Initialize pygame
pygame.init()

# Set up display
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# FPS (speed)
clock = pygame.time.Clock()
snake_speed = 15

# Snake properties
snake_block = 10
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
snake_direction = 'RIGHT'
change_to = snake_direction

# Food position
food_pos = [
    random.randrange(1, (width // 10)) * 10,
    random.randrange(1, (height // 10)) * 10
]
food_spawn = True

# Score
score = 0


def show_score(color, font, size):
    """Display score on screen"""
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    score_rect.topleft = (10, 10)
    screen.blit(score_surface, score_rect)


# Game loop
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != 'DOWN':
                change_to = 'UP'
            elif event.key == pygame.K_DOWN and snake_direction != 'UP':
                change_to = 'DOWN'
            elif event.key == pygame.K_LEFT and snake_direction != 'RIGHT':
                change_to = 'LEFT'
            elif event.key == pygame.K_RIGHT and snake_direction != 'LEFT':
                change_to = 'RIGHT'

    # Change direction
    snake_direction = change_to

    # Move the snake
    
    if snake_direction == 'UP':
        snake_pos[1] -= 10
    elif snake_direction == 'DOWN':
        snake_pos[1] += 10
    elif snake_direction == 'LEFT':
        snake_pos[0] -= 10
    elif snake_direction == 'RIGHT':
        snake_pos[0] += 10

    # Snake body growing mechanism
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()

    # Spawn new food
    if not food_spawn:
        food_pos = [
            random.randrange(1, (width // 10)) * 10,
            random.randrange(1, (height // 10)) * 10
        ]
    food_spawn = True

    # Fill background
    screen.fill(black)

    # Draw snake
    for pos in snake_body:
        pygame.draw.rect(screen, green, pygame.Rect(pos[0], pos[1], snake_block, snake_block))

    # Draw food
    pygame.draw.rect(screen, red, pygame.Rect(food_pos[0], food_pos[1], snake_block, snake_block))

    # Check game over conditions
    if (snake_pos[0] < 0 or snake_pos[0] >= width or
            snake_pos[1] < 0 or snake_pos[1] >= height):
        game_over = True

    # Check if snake collides with itself
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over = True

    # Show score
    show_score(white, 'times new roman', 20)

    # Refresh game screen
    pygame.display.update()

    # Control speed
    clock.tick(snake_speed)

# End screen
screen.fill(black)
font = pygame.font.SysFont('times new roman', 35)
game_over_surface = font.render('Game Over! Your Score: ' + str(score), True, red)
game_over_rect = game_over_surface.get_rect(center=(width / 2, height / 2))
screen.blit(game_over_surface, game_over_rect)
pygame.display.flip()
time.sleep()

pygame.quit()
