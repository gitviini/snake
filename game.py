import pygame
from utils import new_apple
#SET
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True
dt = 0
direction = pygame.Vector2(0,0)
click = 0
apples = 0
position = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
position_apple = 0
tam = 1
pixels = []

def add(pixels = []):
    if len(pixels) > tam:
        del pixels[0]
    for pixel in pixels:
        pygame.draw.rect(screen, 'green', [pixel[0],pixel[1],20,20], 0)
    if tam > 2:
        for pixel in pixels[:-1]:
            if pixel == [position.x,position.y]:
                pygame.QUIT()

#RUN
if __name__ == '__main__':
    pygame.init()
    
    while running:
        #QUIT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        #COLOR SCREEN
        screen.fill((22,33,44))
        
        if(apples == 0):
            position_apple = new_apple((screen.get_width(),screen.get_height()))
            apples = 1
        #PLAYER SET
        pygame.draw.rect(screen, 'red', [position_apple[0],position_apple[1],20,20])

        screen.blit(pygame.font.SysFont('monospace', 18).render(f'pontos: {tam-1}', False, 'red'), [10,10])

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
        if keys[pygame.K_o]:
            running = False

        if position_apple[0] == position.x and position_apple[1] == position.y:
            tam+=1
            position_apple = new_apple((screen.get_width(),screen.get_height()))
        position.x += round(direction.x * 20) 
        position.y += round(direction.y * 20)
        
        pixels.append([position.x,position.y])
        add(pixels)
        
        if position.y >= screen.get_height() and direction.y > 0:
            position.y = 0
        if position.y < 0 and direction.y < 0:
            position.y = screen.get_height()
        if position.x >= screen.get_width() and direction.x > 0:
            position.x = 0
        if position.x < 0 and direction.x < 0:
            position.x = screen.get_width()
            
        pygame.display.set_caption('flap')
        pygame.display.flip()
        pygame.display.update()
        dt = clock.tick(12) /100
        
    pygame.quit()