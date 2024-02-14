import pygame
from components.paddle import Paddle
from components.ball import Ball

# global constants

WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 512

PADDLE_WIDTH = 30
PADDLE_HEIGHT = 120

# initial variables

PADDLE_SPEED = 5
BALL_SPEED = 6

# game status

game_status = "in_game"

# controllers

    # text controller 

def text_score(screen, paddle):
        font = pygame.font.Font(None, 100)
        text = font.render(f"{paddle.points}", True,(36,36,36))
        if paddle.player == 1 or paddle.player == 2:
            text_rect = text.get_rect(center=(WINDOW_WIDTH//4, WINDOW_HEIGHT//2))
        if paddle.player == 3 or paddle.player == 4:
            text_rect = text.get_rect(center=((WINDOW_WIDTH*3)//4, WINDOW_HEIGHT//2))
        screen.blit(text, text_rect)
        
    # game over controller
    
def game_over(paddle, ball, screen):
    if paddle.points == 5:
        global game_status
        game_status = "game_over"
        ball.color = (0,0,0,0)
        if game_status == "game_over":
            ball.speed_x, ball.speed_y = 0, 0
            font = pygame.font.Font(None, 36)
            text = font.render(f"player {paddle.player} win's; please pulse SPACE", True,(255,255,255))
            text_rect = text.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//2-30))
            screen.blit(text, text_rect)

def main():
    global game_status
    # game config 

    pygame.init()

    screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
    pygame.display.set_caption("Pong Game")

    clock = pygame.time.Clock()
    running = True

    # init components

    paddle1 = Paddle(screen=screen, player=2, HEIGHT=PADDLE_HEIGHT, WIDTH=PADDLE_WIDTH, initial_speed=PADDLE_SPEED)
    paddle2 = Paddle(screen=screen, player=4, HEIGHT=PADDLE_HEIGHT, WIDTH=PADDLE_WIDTH, initial_speed=PADDLE_SPEED)
    
    ball = Ball(screen=screen, radius=10, initial_speed=BALL_SPEED)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        
        screen.fill("black")
        # collisions

            # collision with paddles
        
        if (paddle1.WIDTH > ball.x and paddle1.y + paddle1.HEIGHT > ball.y and paddle1.y < ball.y) or (WINDOW_WIDTH-paddle2.WIDTH < ball.x and paddle2.y + paddle2.HEIGHT > ball.y and paddle2.y < ball.y):
            ball.speed_x *= -1
            
            # games points collisions
        
        if WINDOW_WIDTH < ball.x:
            paddle1.points += 1 
            ball.init_movement()
        if 0 > ball.x:
            paddle2.points +=1
            ball.init_movement()
            
        # text and data
        text_score(screen, paddle1)
        text_score(screen, paddle2)

        # moving and drawing

        paddle1.draw()
        paddle1.move()
        
        paddle2.draw()
        paddle2.move()
        
        ball.draw()
        ball.move()
        
        # divisory line
        
        pygame.draw.line(screen,(255,255,255),(WINDOW_WIDTH//2,0), (WINDOW_WIDTH//2,WINDOW_HEIGHT))
        
        # game over checker
        game_over(paddle1, ball, screen)
        game_over(paddle2, ball, screen)
        
        # restart game
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and game_status == "game_over":
            ball.speed_x, ball.speed_y = BALL_SPEED, BALL_SPEED
            paddle1.points, paddle2.points = 0, 0
            paddle1.y, paddle2.y = (WINDOW_HEIGHT//2-paddle1.HEIGHT//2), (WINDOW_HEIGHT//2-paddle2.HEIGHT//2)
            game_status = "in_game"
            ball.color = (255,255,255)

        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    main()