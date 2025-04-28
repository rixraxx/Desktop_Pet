import pygame
from pygame.locals import *
import win32api # type: ignore
import win32con # type: ignore
import win32gui # type: ignore

# Settings
HEIGHT, WIDTH = 450, 700
FPS = 30
BG_COLOR = (255, 0, 128)

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, scale_factor=2):
        super().__init__()
        self.attack_animation = False
        self.sprites = []
        
        # Load and scale sprite images (use valid image paths here)
        for i in range(1, 11):
            sprite = pygame.image.load(f'sprites\\attack_{i}.png')  # Assuming you have attack_1.png, attack_2.png, ...
            scaled_sprite = pygame.transform.scale(sprite, (sprite.get_width() * scale_factor, sprite.get_height() * scale_factor))
            self.sprites.append(scaled_sprite)
        
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def attack(self):
        self.attack_animation = True

    def update(self, speed):
        # Continuous animation, looping through sprites
        self.current_sprite += speed
        if int(self.current_sprite) >= len(self.sprites):
            self.current_sprite = 0  # Reset to first sprite for continuous loop
        self.image = self.sprites[int(self.current_sprite)]


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.isrunning = True
        self.clock = pygame.time.Clock()

        # Make window transparent
        self.hwnd = pygame.display.get_wm_info()["window"]
        
        # Set the window to be transparent
        win32gui.SetWindowLong(self.hwnd, win32con.GWL_EXSTYLE, 
                               win32gui.GetWindowLong(self.hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
        win32gui.SetLayeredWindowAttributes(self.hwnd, win32api.RGB(255, 0, 128), 0, win32con.LWA_COLORKEY)

        # Set the window always on top
        win32gui.SetWindowPos(self.hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

        # Create player sprite (scaled)
        self.player = Player(100, 100, scale_factor=3)  # Increase scale_factor for larger sprite
        self.moving_sprites = pygame.sprite.Group()
        self.moving_sprites.add(self.player)

    def run(self):
        while self.isrunning:
            dt = self.clock.tick(FPS)

            # Handle events
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.isrunning = False
                if event.type == KEYDOWN and event.key == K_ESCAPE:
                    self.isrunning = False

            # Fill background with transparent color
            self.screen.fill(BG_COLOR)

            # Update and draw sprites (continuous animation)
            self.moving_sprites.update(0.25)  # Speed of sprite animation
            self.moving_sprites.draw(self.screen)

            # Update the display
            pygame.display.update()

        pygame.quit()

def Main():
    if __name__ == "__main__":
        game = Game()
        game.run()

Main()
 