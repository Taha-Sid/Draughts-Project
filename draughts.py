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

square_size = 5

yellow_circle = pygame.image.load("yellow_circle.png")        

class Blacksquare(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((75,75))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

class Brownsquare(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((75,75))
        self.image.fill(BROWN)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

class Piece(pygame.sprite.Sprite):
    def __init__(self,row,column):
        self.row = row
        self.column = column
        self.x = 0
        self.y = 0
        self.calculate_position()

    def calculate_position(self):
        self.x = square_size * self.column + square_size // 2
        self.y = square_size * self.row + square_size // 2
        
    def draw_white(self):
        radius = square_size // 2
        pygame.draw.circle(screen,WHITE,(self.x,self.y),radius)

class Board(pygame.sprite.Sprite):
    def __init__(self):
        self.selected_piece = None
        self.green_pieces_left = self_white_pieces_left = 12

    def draw_squares(self):
        board = [[1,0,1,0,1,0,1,0],
         [0,1,0,1,0,1,0,1],
         [1,0,1,0,1,0,1,0],
         [0,1,0,1,0,1,0,1],
         [1,0,1,0,1,0,1,0],
         [0,1,0,1,0,1,0,1],
         [1,0,1,0,1,0,1,0],
         [0,1,0,1,0,1,0,1]]
        
        for y in range(8):
            for x in range(8):
                if board[y][x] == 1:
                    brownsquare = Brownsquare(x*75,y*75)
                    all_sprites_list.add(brownsquare)
                    brownsquare_list.add(brownsquare)
                    pygame.draw.circle(screen,WHITE,(x,y),square_size)
                    #piece = Piece(x,y)
                    #piece.draw_white()
                else:
                    blacksquare = Blacksquare(x*75,y*75)
                    all_sprites_list.add(blacksquare)
                    blacksquare_list.add(blacksquare)

board = Board()
brownsquare_list = pygame.sprite.Group()
blacksquare_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            pass

    board.draw_squares()
 
    pygame.display.update()
    screen.fill(WHITE)
    all_sprites_list.update()
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)
 
pygame.quit()
