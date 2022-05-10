from config import *

class CameraGroup(pg.sprite.Group):
    def __init__(self):
        super().__init__() 
        self.display_surface = gameDisplay
        self.ground_surf = background_img
        self.ground_rect = self.ground_surf.get_rect(topleft = (0,0))
    def draw(self):
        
        # Scenery

        self.display_surface.blit(self.ground_surf, self.ground_rect)
        
        # Active elems

        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            self.display_surface.blit(sprite.image, sprite.rect)