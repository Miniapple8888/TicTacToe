import pygame


def write(surface, text, fontsize, colour, position):
    myfont = pygame.font.SysFont("None", fontsize)
    mytext = myfont.render(text, True, colour)
    mytext = mytext.convert_alpha()
    surface.blit(mytext, position)


def color(colorname):
    colors = {
        "white": (255, 255, 255),
        "black": (0, 0, 0),
        "red": (255, 0, 0),
        "yellow": (175, 175, 50),
        "green": (0, 255, 0)
    }
    return colors[colorname]


def within_boundaries(mouse_pos, x, y, width, height):
    if mouse_pos[0] >= x and mouse_pos[0] <= width + x and mouse_pos[1] >= y and mouse_pos[1] <= height + y:
        return True
    return False
