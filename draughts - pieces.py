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
font_name = pygame.font.match_font('calibri')

done = True
 
clock = pygame.time.Clock() 
    
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
    def __init__(self,row,column,colour):
        self.row = row
        self.column = column
        self.colour = colour
        self.radius = 25
        self.x = 0
        self.y = 0
        self.position()

    def position(self):
        self.y = 75 * self.column + 75 // 2
        self.x = 75 * self.row + 75 // 2

    def draw(self):
        pygame.draw.circle(screen,self.colour,(self.y,self.x),self.radius)

    
class Board(pygame.sprite.Sprite):
    def __init__(self):
        self.green_pieces_left = 12
        self_white_pieces_left = 12
        self.board = []
        self.occupied_spaces = []
        
    def draw_squares(self):
        arrangement = [[1,0,1,0,1,0,1,0],
         [0,1,0,1,0,1,0,1],
         [1,0,1,0,1,0,1,0],
         [0,1,0,1,0,1,0,1],
         [1,0,1,0,1,0,1,0],
         [0,1,0,1,0,1,0,1],
         [1,0,1,0,1,0,1,0],
         [0,1,0,1,0,1,0,1]]
        
        for y in range(8):
            for x in range(8):
                if arrangement[y][x] == 1:
                    brownsquare = Brownsquare(x*75,y*75)
                    all_sprites_list.add(brownsquare)
                    brownsquare_list.add(brownsquare)
                elif arrangement[y][x] == 0:
                    blacksquare = Blacksquare(x*75,y*75)
                    all_sprites_list.add(blacksquare)
                    blacksquare_list.add(blacksquare)


    def pieces_on_board(self):
        for x in range(8):
            self.board.append([])
            for y in range(8):
                if y % 2 == ((x+1)%2):
                    if x < 3:
                        self.board[x].append(Piece(x,y,GREEN))
                    elif x > 4:
                        self.board[x].append(Piece(x,y,WHITE))
                    else:
                        self.board[x].append(0)
                else:
                    self.board[x].append(0)
                
                        
    def draw_pieces(self):
        for x in range(8):
            for y in range(8):
                piece = self.board[x][y]
                if piece != 0:
                    piece.draw()

board = Board()
all_sprites_list = pygame.sprite.Group()
brownsquare_list = pygame.sprite.Group()
blacksquare_list = pygame.sprite.Group()

def mouse_movement(position):
    x,y = position
    row = y // 75
    column = x // 75
    return row, column


done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass
                        

    board.draw_squares()
    board.pieces_on_board()
    board.draw_pieces()
 
    pygame.display.update()
    screen.fill(WHITE)
    all_sprites_list.update()
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
