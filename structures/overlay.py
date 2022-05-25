from config import *
from structures.label import DynLabel

class Resources:
    def __init__(self, count, types):
        self.render = []
        self.count = count
        self.type = types

    def draw(self):

        # menu = pg.sprite.Group([])
        
        if(self.type == 'ELI'):
            # gameDisplay.blit(resource_bar_img, (1000, 10))
            self.get_percent()
            DynLabel(1120, 48, (0, 0, 0), True, f"{self.count}")
            gameDisplay.blit(elixir_img, (1180, 35))
        else:
            # gameDisplay.blit(resource_bar_img, (1000, 60))
            self.get_percent()
            DynLabel(1120, 98, (0, 0, 0), True, f"{self.count}")
            gameDisplay.blit(coin_img, (1180, 80))

    def get_percent(self):

        percent = int(100 * (self.count / 10000))
        # print(percent)

        if(self.type == 'ELI'):
            if(percent < 50):
                gameDisplay.blit(resource_e_low_img, (900, 10))
            elif(percent >= 50 and percent < 80):
                gameDisplay.blit(resource_e_mid_img, (900, 10))
            else:
                gameDisplay.blit(resource_e_full_img, (900, 10))
        else:
            if(percent < 50):
                gameDisplay.blit(resource_g_low_img, (900, 60))
            elif(percent >= 50 and percent < 80):
                gameDisplay.blit(resource_g_mid_img, (900, 60))
            else:
                gameDisplay.blit(resource_g_full_img, (900, 60))

    def remove_monez(self, count):
        self.count -= count
    def get_credits(self):
        return self.count
    
    def __repr__(self):
        return self.count
    
    def __str__(self):
        return str(self.count)


        # I'm gonna do it brute force sorry
        # if(self.type == 'ELI'):
        #     progress_rect = Rectangle(100, 28, (54, 10, 74))
        #     progress_rect.set_rounded(8)
        #     progress_rect.rect.center = (1135, 45)
        #     return progress_rect
        # else:
        #     progress_rect = Rectangle(220, 28, (235, 235, 12))
        #     progress_rect.set_rounded(8)
        #     progress_rect.rect.center = (1135, 95)
        #     return progress_rect


            