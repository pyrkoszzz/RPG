import pygame
import main


def change():
    global main.HEIGHT1

    
    main.HEIGHT1 = 100
    print(main.HEIGHT1)


"""       
def change_resolution(NEW_WIDTH, NEW_HEIGHT, WIDTH, HEIGHT):
    WIDTH = NEW_WIDTH
    HEIGHT = NEW_HEIGHT
    #WIN = pygame.display.set_mode((NEW_WIDTH, NEW_WIDTH))

    return (NEW_WIDTH, NEW_HEIGHT)
    
    
    #menu
    NEW_GAME_BUTTON = pygame.Rect(0.30*WIDTH , 0.35*HEIGHT, 0.40*WIDTH, 0.1*HEIGHT)
    LOAD_GAME_BUTTON = pygame.Rect(0.30*WIDTH , 0.50*HEIGHT, 0.40*WIDTH, 0.1*HEIGHT)
    SETTINGS_BUTTON = pygame.Rect(0.30*WIDTH , 0.65*HEIGHT, 0.175*WIDTH, 0.1*HEIGHT)
    QUIT_BUTTON = pygame.Rect(0.525*WIDTH , 0.65*HEIGHT, 0.175*WIDTH, 0.1*HEIGHT)

    #sounds
    MUSIC_SWITCH_RECT_BORDER = pygame.Rect(0.40*WIDTH-2, 0.20*HEIGHT-2, 54, 54)
    MUSIC_SWITCH_RECT = pygame.Rect(0.40*WIDTH, 0.20*HEIGHT, 50, 50)
    SFX_SWITCH_RECT_BORDER = pygame.Rect(0.40*WIDTH-2, 0.30*HEIGHT-2, 54, 54)
    SFX_SWITCH_RECT = pygame.Rect(0.40*WIDTH, 0.30*HEIGHT, 50, 50)

    DEFAULT_PLAYER_X = WIDTH/2 - PLAYER_WIDTH/2
    DEFAULT_PLAYER_Y = HEIGHT/2 - PLAYER_HEIGHT/2"""
