from text import TextBox
import pygame
from utils import get_assets_path

class Tooltip(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.position = pygame.math.Vector2(0,0)
        self.bg_container = pygame.image.load(get_assets_path("UI/Tooltip.png")).convert_alpha()
        self.bg_container = pygame.transform.smoothscale_by(self.bg_container,0.25)
        
        self.image = pygame.Surface((self.bg_container.get_width(), self.bg_container.get_height()), pygame.SRCALPHA)
        self.rect = self.image.get_rect()

        self.title_rect = pygame.Rect(11.38, 0, 113, 30)
        self.title_box = TextBox(
            self.title_rect, 
            "", 
            font_size=16, 
            text_color=(255, 255, 255), 
            font_url=get_assets_path("Jersey_10/Jersey10-Regular.ttf"),
            align="center",
    
        )
        
        self.desc_rect = pygame.Rect(11, 38, 113, 84) 
        self.description_box = TextBox(
            self.desc_rect, 
            "", 
            font_size=16, 
            text_color=(255, 255, 255), 
            font_url=get_assets_path("Jersey_10/Jersey10-Regular.ttf"),
            align="center",
        )
        
    def set_position(self,position):
        self.rect.topleft = position

    def displayTooltip(self,position : pygame.math.Vector2,title,description, group):
        self.set_position(position)
        self.title_box.set_text(title)
        self.description_box.set_text(description)

        self.image.fill((0,0,0,0))
        self.image.blit(self.bg_container, (0,0))
        self.image.blit(self.title_box.image, self.title_box.rect)
        self.image.blit(self.description_box.image, self.description_box.rect)
        self.add(group)

    def hideTooltip(self):
        self.kill()