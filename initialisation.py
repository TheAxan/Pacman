import pygame

pygame.display.set_mode()  # The display must be initialized first or it might get the wrong res
u = {  # 1 unit is 30 pixels by default (840x930), 38 for 1064x1178, 34 for 952x1054
    (1920, 1080): 34,
    (1080, 1920): 38,
    (2560, 1440): 44,  # 46 messes with wall_stop and 45 with corner??
}.get((pygame.display.Info().current_w, pygame.display.Info().current_h), 30)
screen = pygame.display.set_mode((28 * u, 31 * u), flags=pygame.NOFRAME)

white = 255, 255, 255
black = 0, 0, 0
dark_grey = 15, 15, 15
yellow = 255, 255, 0
blue = 0, 0, 255
red = 255, 0, 0
orange = 255, 153, 0
cyan = 0, 230, 230
pink = 255, 179, 255