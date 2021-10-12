import pygame


pygame.display.set_mode()  # The display must be initialized first or it might get the wrong res
u: int = {
    # cells are u lenght squares
    # u must be even or the graphics looks off and wall_stop breaks
    # * additionnal note: it doesn't work if u <= 16 BUG and the speed is all messed up
    # because full_cell_check breaks because the resulting speed jumps over full cells.
    # Trying to account for the jump is ressource intensive since the method runs every frame
    (1920, 1080): 34,
    (1080, 1920): 38,
    (2560, 1440): 44,
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


