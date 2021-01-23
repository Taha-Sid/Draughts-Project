import pygame
 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BROWN = (170,50,10)
 
pygame.init()
 
size = (600, 600) # x, y
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Draughts")
 
done = False
 
clock = pygame.time.Clock()

box_y = 5
box_x = 5

board = [[1,0,1,0,1,0,1,0],
         [0,1,0,1,0,1,0,1],
         [1,0,1,0,1,0,1,0],
         [0,1,0,1,0,1,0,1],
         [1,0,1,0,1,0,1,0],
         [0,1,0,1,0,1,0,1],
         [1,0,1,0,1,0,1,0],
         [0,1,0,1,0,1,0,1]]
        

class BlackBox(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('yellow_circle.png')
        self.rect = self.image.get_rect()
        #self.image = pygame.Surface((75,75))
        #self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

class BrownBox(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('blue_circle.png')
        self.rect = self.image.get_rect()
        #self.image = pygame.Surface((75,75))
        #self.image.fill(BROWN)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


brownbox_list = pygame.sprite.Group()
blackbox_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()


for y in range(8):
    for x in range(8):
        if board[y][x] == 1:
            brownbox = BrownBox(x*75,y*75)
            all_sprites_list.add(brownbox)
            brownbox_list.add(brownbox)
        else:
            blackbox = BlackBox(x*75,y*75)
            all_sprites_list.add(blackbox)
            blackbox_list.add(blackbox)
            

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    pygame.display.update()
    screen.fill(WHITE)
    all_sprites_list.update()
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)
 
pygame.quit()
