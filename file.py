import sys
import pygame
 
white = (255,255,255)
red = (255, 0, 0)
 
class Things:
    def __init__(self):
 
        pygame.init()
        self.screen = pygame.display.set_mode((700, 700))
        self.screen.fill(white)
        pygame.display.set_caption('Things')
        
    def run_game(self):
        while True:
            self._check_events()
 
            self._update_screen()
        
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                pygame.draw.circle(self.screen, red, pos, 30)
                pygame.display.update()
            if event.type == pygame.QUIT:
                sys.exit()
    
    def _update_screen(self):
        pygame.display.flip()
 
if __name__ == '__main__':
    th = Things()
    th.run_game()