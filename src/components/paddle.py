import pygame

# font = pygame.font.Font(None, 16)

# TODO: remove this pace of shit and make it another time
# def textCard(player, points):
#     text = font.render(f"player {points}", True, (0,0,0))
#     rotated_text = pygame.transform.rotate(text, 90)
#     rotated_text_rect = rotated_text.get_rect(center=(0,0))


class Paddle:
    def __init__(self, screen, player, WIDTH, HEIGHT, initial_speed):
        self.player = player
        self.screen = screen
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.points = 0
        self.speed = initial_speed
        
        self.select_player()

    def select_player(self):
        if self.player == 1:
            # set the player color
            self.color = "red"
            # set the player position
            self.x = 0
            self.y = (self.screen.get_height()/2) - (self.HEIGHT/2)
        elif self.player == 2:
            self.color = "blue"
            self.x = 0
            self.y = (self.screen.get_height()/2) - (self.HEIGHT/2)
        elif self.player == 3:
            self.color = "green"
            self.x = self.screen.get_width() - self.WIDTH
            self.y = (self.screen.get_height()/2) - (self.HEIGHT/2)
        elif self.player == 4:
            self.color = "yellow"
            self.x = self.screen.get_width() - self.WIDTH
            self.y = (self.screen.get_height()/2) - (self.HEIGHT/2)
            
    def move(self):
        keys = pygame.key.get_pressed()
        if self.y < 0:
            self.y += self.speed 
        if self.y > self.screen.get_height() - self.HEIGHT:
            self.y -= self.speed 
        if self.player == 1 or self.player == 2:
            if keys[pygame.K_w]:
                self.y -= self.speed
            if keys[pygame.K_s]:
                self.y += self.speed
        if self.player == 3 or self.player == 4:
            if keys[pygame.K_UP]:
                self.y -= self.speed
            if keys[pygame.K_DOWN]:
                self.y += self.speed 
    

        
            
    
    def draw(self):

        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.WIDTH, self.HEIGHT))