from random import randint
from time import sleep

def new_apple(screen = [0,0], tam=0):
    position = (round(randint(0,screen.get_width()-20) / 20) * 20,round(randint(0,screen.get_height()-20) / 20) * 20)
    return position

def add(screen, tam, position, pixels = [], pygame=[]):
    if len(pixels) > tam:
        del pixels[0]
    for pixel in pixels:
        pygame.draw.rect(screen, 'green', [pixel[0],pixel[1],20,20], 0)
    if tam > 2:
        for pixel in pixels[:-1]:
            if pixel == [position.x,position.y]:
                faill = pygame.font.SysFont('monospace',20)
                faill = faill.render('você perdeu',False, 'red')
                screen.blit(faill, [screen.get_width()/2 - faill.get_width() / 2,screen.get_height()/2])
                pygame.display.update()
                sleep(2)
                return False
    return True 
#                        
def snake_move(pygame = [], direction = 0):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and direction.y == 0:
        direction.x = 0
        direction.y = -1
    elif keys[pygame.K_s] and direction.y == 0:
        direction.x = 0
        direction.y = 1
    elif keys[pygame.K_d] and direction.x == 0:
        direction.y = 0
        direction.x = 1
    elif keys[pygame.K_a] and direction.x == 0:
        direction.y = 0
        direction.x = -1
    return direction
#IF THE SNAKE OUTSIDE SCREEN, IT WILL TO OTHER SIDE.
def screen_effect(screen = [], position = [], direction = 0):
    if position.y >= screen.get_height() and direction.y > 0:
        position.y = 0
    if position.y < 0 and direction.y < 0:
        position.y = screen.get_height() - 20
    if position.x >= screen.get_width() and direction.x > 0:
        position.x = 0
    if position.x < 0 and direction.x < 0:
        position.x = screen.get_width() - 20
    return position