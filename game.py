import pygame
from utils import new_apple, add, snake_move, screen_effect

#SET
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
running = True
direction = pygame.Vector2(0,0)
apples = 0
position = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
position_apple = []
tam = 1
pixels = []
color = {'background':(22,33,44),'snake':'green','apple':'red','text':'white'}

#RUN
if __name__ == '__main__':
    pygame.init()
    
    while running:
        #COLOR SCREEN
        screen.fill(color['background'])           
        
        #QUIT
        for event in pygame.event.get():
            pygame.quit() if event.type == pygame.QUIT else {}
        
        #IF APPLE ARE AT PLACE OF SNAKE
        if apples == 0:
            position_apple = new_apple(screen, tam)
            apples = 1
        if position_apple[0] == position.x and position_apple[1] == position.y:
            tam+=1
            apples=0
        #DRAWING APPLES
        pygame.draw.rect(screen, color['apple'], [position_apple[0],position_apple[1],20,20]) 
            
        #PLAYER SET
        pixels.append([position.x,position.y])
        running = add(screen,tam,position,pixels,pygame)
        
        #SNAKE'S DIRECTION    
        direction = snake_move(pygame, direction)
        
        #ROUNDING POSITION
        position.x += round(direction.x * 20) 
        position.y += round(direction.y * 20)
        
        #EFFEITO DISPLAY INFINITE
        position = screen_effect(screen, position, direction)
        
        #STATES
        screen.blit(pygame.font.SysFont('monospace', 18).render(f'pontos: {tam-1}', False, color['text']), [10,10])
        
        #NAME WINDOW
        pygame.display.set_caption('flap')
        
        #UPDATE DISPLAY
        pygame.display.flip()
        pygame.display.update()
        
        #FRAMES
        clock.tick(10)
    
    pygame.quit()