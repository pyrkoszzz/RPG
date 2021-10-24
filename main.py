import pygame, pytmx
import os, sys
#import change_resolution

pygame.font.init()
pygame.mixer.init()


DEFAULT_FONT = pygame.font.SysFont('comicsans', 30)
AUTHOR_FONT = pygame.font.SysFont('comicsans', 10)
SETTINGS_FONT = pygame.font.SysFont('comicsans', 30)

WIDTH, HEIGHT = 1280, 720
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
BLOCK_SIZE = 40

FPS = 60
VEL = 5

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (128, 128, 128)
BLUE = (0, 0, 255)
LIGHT_BLUE = (0, 145, 255)

CAMERA_UNLOCK_X_RIGHT_EVENT = pygame.USEREVENT + 1
CAMERA_UNLOCK_X_LEFT_EVENT = pygame.USEREVENT + 2
CAMERA_UNLOCK_Y_RIGHT_EVENT = pygame.USEREVENT + 3
CAMERA_UNLOCK_Y_LEFT_EVENT = pygame.USEREVENT + 4

#menu
NEW_GAME_BUTTON = pygame.Rect(0.30*WIDTH , 0.35*HEIGHT, 0.40*WIDTH, 0.1*HEIGHT)
LOAD_GAME_BUTTON = pygame.Rect(0.30*WIDTH , 0.50*HEIGHT, 0.40*WIDTH, 0.1*HEIGHT)
SETTINGS_BUTTON = pygame.Rect(0.30*WIDTH , 0.65*HEIGHT, 0.175*WIDTH, 0.1*HEIGHT)
QUIT_BUTTON = pygame.Rect(0.525*WIDTH , 0.65*HEIGHT, 0.175*WIDTH, 0.1*HEIGHT)

#pygame.display.get_surface() #getting resolution
pygame.display.set_caption("Our Game")
gameMap = pytmx.load_pygame(os.path.join('Assets', 'mapa.tmx'))


TILE_T_SRC = pygame.image.load(os.path.join('Assets', 'grass.png')).convert()
TILE_T  = pygame.transform.scale(TILE_T_SRC, (BLOCK_SIZE,BLOCK_SIZE))
TILE_C_SRC = pygame.image.load(os.path.join('Assets', 'water.png')).convert()
TILE_C  = pygame.transform.scale(TILE_C_SRC, (BLOCK_SIZE,BLOCK_SIZE))


#settings
BUTTONS_WIDTH, BUTTONS_HEIGHT = (100, 100)

SOUND_BUTTONS = pygame.image.load(os.path.join('Assets', 'sound_buttons.png'))
MUTE_BUTTON = pygame.transform.scale(SOUND_BUTTONS.subsurface(430, 0, 375, 325), (BUTTONS_WIDTH, BUTTONS_HEIGHT))
VOLUME_3_BUTTON = pygame.transform.scale(SOUND_BUTTONS.subsurface(10, 0, 390, 320), (BUTTONS_WIDTH, BUTTONS_HEIGHT))
VOLUME_2_BUTTON = pygame.transform.scale(SOUND_BUTTONS.subsurface(10, 320, 390, 320), (BUTTONS_WIDTH, BUTTONS_HEIGHT))
VOLUME_1_BUTTON = pygame.transform.scale(SOUND_BUTTONS.subsurface(10, 650, 390, 320), (BUTTONS_WIDTH, BUTTONS_HEIGHT))
MUSIC_STOP_BUTTON = pygame.transform.scale(SOUND_BUTTONS.subsurface(684, 670, 250, 300), (BUTTONS_WIDTH, BUTTONS_HEIGHT))
MUSIC_START_BUTTON = pygame.transform.scale(SOUND_BUTTONS.subsurface(400, 670, 300, 300), (BUTTONS_WIDTH, BUTTONS_HEIGHT))

CLOSE_BUTTON_IMAGE_SRC = pygame.image.load(os.path.join('Assets', 'close_button.png'))
CLOSE_BUTTON_IMAGE = pygame.transform.scale(CLOSE_BUTTON_IMAGE_SRC, (BUTTONS_WIDTH, BUTTONS_HEIGHT))
CLOSE_BUTTON = pygame.Rect(0.80*WIDTH, 0.10*HEIGHT, BUTTONS_WIDTH, BUTTONS_HEIGHT)
MUSIC_VOLUME_TEXT = SETTINGS_FONT.render("Music Volume: ", 1, BLACK)
MUSIC_VOLUME_RECT = pygame.Rect(0.60*WIDTH - BUTTONS_HEIGHT/8, 0.4*HEIGHT + MUSIC_VOLUME_TEXT.get_height()/2 - BUTTONS_HEIGHT/8, BUTTONS_WIDTH/4, BUTTONS_HEIGHT/4)

SFX_VOLUME_TEXT = SETTINGS_FONT.render("SFX Volume: ", 1, BLACK)
SFX_VOLUME_RECT = pygame.Rect(0.60*WIDTH - BUTTONS_HEIGHT/8, 0.5*HEIGHT + SFX_VOLUME_TEXT.get_height()/2 - BUTTONS_HEIGHT/8, BUTTONS_WIDTH/4, BUTTONS_HEIGHT/4)


#sounds 
MUSIC = pygame.mixer.Sound(os.path.join('Assets', 'music.mp3'))

MUSIC_SWITCH_RECT_BORDER = pygame.Rect(0.40*WIDTH-2, 0.20*HEIGHT-2, 54, 54)
MUSIC_SWITCH_RECT = pygame.Rect(0.40*WIDTH, 0.20*HEIGHT, 50, 50)
SFX_SWITCH_RECT_BORDER = pygame.Rect(0.40*WIDTH-2, 0.30*HEIGHT-2, 54, 54)
SFX_SWITCH_RECT = pygame.Rect(0.40*WIDTH, 0.30*HEIGHT, 50, 50)


#player
PLAYER_SRC = pygame.image.load(os.path.join('Assets', 'player.png'))
PLAYER_WIDTH, PLAYER_HEIGHT = 30, 60
PLAYER_L = pygame.transform.scale(PLAYER_SRC.subsurface(65, 27, 63, 163), (PLAYER_WIDTH, PLAYER_HEIGHT))
PLAYER_R = pygame.transform.scale(PLAYER_SRC.subsurface(292, 27, 63, 163), (PLAYER_WIDTH, PLAYER_HEIGHT))
PLAYER_U = pygame.transform.scale(PLAYER_SRC.subsurface(391, 27, 90, 163), (3/2*PLAYER_WIDTH, PLAYER_HEIGHT))
PLAYER_D = pygame.transform.scale(PLAYER_SRC.subsurface(161, 27, 90, 163), (3/2*PLAYER_WIDTH, PLAYER_HEIGHT))

DEFAULT_PLAYER_X = WIDTH/2 - PLAYER_WIDTH/2
DEFAULT_PLAYER_Y = HEIGHT/2 - PLAYER_HEIGHT/2


def draw_menu():
    WIN.fill(WHITE)
    pygame.draw.rect(WIN, BLACK, NEW_GAME_BUTTON)
    pygame.draw.rect(WIN, BLACK, LOAD_GAME_BUTTON)
    pygame.draw.rect(WIN, BLACK, SETTINGS_BUTTON)
    pygame.draw.rect(WIN, BLACK, QUIT_BUTTON)
    new_game_text = DEFAULT_FONT.render("New Game!", 1, WHITE)
    WIN.blit(new_game_text, (NEW_GAME_BUTTON.x + NEW_GAME_BUTTON.width/2 - new_game_text.get_width()/2, NEW_GAME_BUTTON.y + NEW_GAME_BUTTON.height/2 - new_game_text.get_height()/2))   
    load_game_text = DEFAULT_FONT.render("Load Game!", 1, WHITE)
    WIN.blit(load_game_text, (NEW_GAME_BUTTON.x + LOAD_GAME_BUTTON.width/2 - load_game_text.get_width()/2, LOAD_GAME_BUTTON.y + LOAD_GAME_BUTTON.height/2 - load_game_text.get_height()/2))   
    settings_text = DEFAULT_FONT.render("Settings", 1, WHITE)
    WIN.blit(settings_text, (SETTINGS_BUTTON.x + SETTINGS_BUTTON.width/2 - settings_text.get_width()/2, SETTINGS_BUTTON.y + SETTINGS_BUTTON.height/2 - settings_text.get_height()/2))    
    quit_text = DEFAULT_FONT.render("Quit", 1, WHITE)
    WIN.blit(quit_text, (QUIT_BUTTON.x + QUIT_BUTTON.width/2 - quit_text.get_width()/2, QUIT_BUTTON.y + QUIT_BUTTON.height/2 - quit_text.get_height()/2))        

def draw_settings(MUSIC_BOOL, SFX_BOOL):
    WIN.fill(WHITE)
    pygame.draw.rect(WIN, WHITE, CLOSE_BUTTON)
    WIN.blit(CLOSE_BUTTON_IMAGE, (CLOSE_BUTTON.x, CLOSE_BUTTON.y))
    music_text = SETTINGS_FONT.render("Music: ", 1, BLACK)
    WIN.blit(music_text, (0.3*WIDTH, 0.2*HEIGHT))
    pygame.draw.rect(WIN, BLACK, MUSIC_SWITCH_RECT_BORDER)
    if not MUSIC_BOOL:
        pygame.draw.rect(WIN, WHITE, MUSIC_SWITCH_RECT)
    sfx_text = SETTINGS_FONT.render("SFX: ", 1, BLACK)
    WIN.blit(sfx_text, (0.3*WIDTH, 0.3*HEIGHT))
    pygame.draw.rect(WIN, BLACK, SFX_SWITCH_RECT_BORDER)
    if not SFX_BOOL:
        pygame.draw.rect(WIN, WHITE, SFX_SWITCH_RECT)
    
    WIN.blit(MUSIC_VOLUME_TEXT, (0.3*WIDTH, 0.4*HEIGHT))
    pygame.draw.line(WIN, LIGHT_BLUE, (0.5*WIDTH, 0.4*HEIGHT + MUSIC_VOLUME_TEXT.get_height()/2), (0.70*WIDTH, 0.4*HEIGHT + MUSIC_VOLUME_TEXT.get_height()/2), width = 5)
    pygame.draw.line(WIN, BLUE, (0.5*WIDTH, 0.4*HEIGHT + MUSIC_VOLUME_TEXT.get_height()/2), (MUSIC_VOLUME_RECT.x + MUSIC_VOLUME_RECT.width/2, 0.4*HEIGHT + MUSIC_VOLUME_TEXT.get_height()/2), width = 5)
    pygame.draw.rect(WIN, BLUE, MUSIC_VOLUME_RECT)

    WIN.blit(SFX_VOLUME_TEXT, (0.3*WIDTH, 0.5*HEIGHT))
    pygame.draw.line(WIN, LIGHT_BLUE, (0.5*WIDTH, 0.5*HEIGHT + SFX_VOLUME_TEXT.get_height()/2), (0.70*WIDTH, 0.5*HEIGHT + SFX_VOLUME_TEXT.get_height()/2), width = 5)
    pygame.draw.line(WIN, BLUE, (0.5*WIDTH, 0.5*HEIGHT + SFX_VOLUME_TEXT.get_height()/2), (SFX_VOLUME_RECT.x + SFX_VOLUME_RECT.width/2, 0.5*HEIGHT + SFX_VOLUME_TEXT.get_height()/2), width = 5)
    pygame.draw.rect(WIN, BLUE, SFX_VOLUME_RECT)
    
    #WIN.blit(VOLUME_3_BUTTON, (400, 500))
    #WIN.blit(VOLUME_2_BUTTON, (500, 500))
    #WIN.blit(VOLUME_1_BUTTON, (600, 500))
    #WIN.blit(MUSIC_START_BUTTON, (700, 500))
    #WIN.blit(MUSIC_STOP_BUTTON, (800, 500))

def drawMap(camera):
    for layer in gameMap.visible_layers:
            for x, y, gid, in layer:
                tile = gameMap.get_tile_image_by_gid(gid)
                WIN.blit(tile, (x * gameMap.tilewidth-camera.x, y * gameMap.tileheight-camera.y))

            index_x = camera.x
            index_y = camera.y

            if index_x <= PLAYER_WIDTH:
                pygame.event.post(pygame.event.Event(CAMERA_UNLOCK_X_LEFT_EVENT))
            elif index_x >= gameMap.tilewidth*gameMap.width-WIDTH-PLAYER_WIDTH:
                pygame.event.post(pygame.event.Event(CAMERA_UNLOCK_X_RIGHT_EVENT))
            if index_y <= PLAYER_HEIGHT:
                pygame.event.post(pygame.event.Event(CAMERA_UNLOCK_Y_LEFT_EVENT))
            elif index_y >= gameMap.tileheight*gameMap.height-HEIGHT-PLAYER_HEIGHT:
                pygame.event.post(pygame.event.Event(CAMERA_UNLOCK_Y_RIGHT_EVENT))

def handlePlayer(player, direction):
    if direction == 'L':
        WIN.blit(PLAYER_L, (player.x, player.y))
    elif direction == 'R':
        WIN.blit(PLAYER_R, (player.x, player.y))
    elif direction == 'U':
        WIN.blit(PLAYER_U, (player.x, player.y))
    else:
        WIN.blit(PLAYER_D, (player.x, player.y))    


def movement(keys_pressed, camera, player, camera_x_right_locked, camera_x_left_locked, camera_y_right_locked, camera_y_left_locked):
    direction = '' 
    x, y = 0, 0
    if keys_pressed[pygame.K_w]:
        y -= VEL
        direction = 'U'
    if keys_pressed[pygame.K_s]:
        y += VEL
        direction = 'D'
    if keys_pressed[pygame.K_a]:
        x -= VEL
        direction = 'R'
    if keys_pressed[pygame.K_d]:
        x += VEL
        direction = 'L'
    handlePlayer(player, direction)

    if player.x + PLAYER_WIDTH/2 == WIDTH/2:
        camera_x_locked = True
    else: 
        camera_x_locked = False
    if   player.y + PLAYER_HEIGHT/2 == HEIGHT/2:
        camera_y_locked = True   
    else: 
        camera_y_locked = False

    if camera_x_locked: 
        if x<0 and not camera_x_left_locked:
            player.x += x
        elif x>0 and not camera_x_right_locked:
            player.x += x
        else:
            camera.x += x
    elif not camera_x_locked: 
        player.x += x
    if camera_y_locked: 
        if y<0 and not camera_y_left_locked:
            player.y += y
        elif y>0 and not camera_y_right_locked:
            player.y += y
        else:
            camera.y += y
    elif not camera_y_locked: 
        player.y += y    
    
def move_volume(VOLUME_RECT, SOUND):
    x = pygame.mouse.get_pos()[0]
    if  x < 0.50*WIDTH:
        VOLUME_RECT.x = 0.50*WIDTH - VOLUME_RECT.width/2 
    elif x > 0.70*WIDTH:  
        VOLUME_RECT.x = 0.70*WIDTH - VOLUME_RECT.width/2           
    else:
        VOLUME_RECT.x = x
    volume = (x/WIDTH-0.5)/0.2
    if volume < 0:
        volume = 0
    elif volume > 1:                        
        volume = 1
    SOUND.set_volume(volume) 

def main(): 
    game_started = False
    settings = False
    MUSIC_BOOL = True
    SFX_BOOL = True 
    clock = pygame.time.Clock()
    loop = True
    music_volume_hold = False
    sfx_volume_hold = False
    player = pygame.Rect(DEFAULT_PLAYER_X, DEFAULT_PLAYER_Y, PLAYER_WIDTH, PLAYER_HEIGHT)
    camera = pygame.Rect(0, 0, WIDTH, HEIGHT)
    if MUSIC_BOOL:
        #MUSIC.play()
        pass
    #MUSIC.set_volume(0.1)
    
    while loop:
        clock.tick(FPS)
        keys_pressed = pygame.key.get_pressed()

        camera_x_right_locked = True 
        camera_x_left_locked = True
        camera_y_right_locked = True
        camera_y_left_locked = True 
        
        for event in pygame.event.get():
            if  pygame.mouse.get_pressed()[0] and LOAD_GAME_BUTTON.collidepoint(pygame.mouse.get_pos()):
                    #change_resolution.change_resolution(600, 600)
                    pass
            if event.type == pygame.QUIT:
                loop = False
            if event.type == CAMERA_UNLOCK_X_RIGHT_EVENT:
                camera_x_right_locked = False  
            if event.type == CAMERA_UNLOCK_X_LEFT_EVENT:
                camera_x_left_locked = False    
            if event.type == CAMERA_UNLOCK_Y_RIGHT_EVENT:
                camera_y_right_locked = False   
            if event.type == CAMERA_UNLOCK_Y_LEFT_EVENT:
                camera_y_left_locked = False
            if settings:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if  pygame.mouse.get_pressed()[0] and MUSIC_SWITCH_RECT.collidepoint(pygame.mouse.get_pos()):
                        if MUSIC_BOOL: 
                            MUSIC_BOOL = False
                            MUSIC.stop()
                        else:
                            MUSIC_BOOL = True 
                            MUSIC.play()
                    if  pygame.mouse.get_pressed()[0] and SFX_SWITCH_RECT.collidepoint(pygame.mouse.get_pos()):
                        if SFX_BOOL:
                            SFX_BOOL = False
                        else:
                            SFX_BOOL = True
            
                if  pygame.mouse.get_pressed()[0] and MUSIC_VOLUME_RECT.collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN:
                    music_volume_hold = True
                if music_volume_hold and event.type == pygame.MOUSEBUTTONUP: 
                    move_volume(MUSIC_VOLUME_RECT, MUSIC)
                    music_volume_hold = False   
                
                if  pygame.mouse.get_pressed()[0] and SFX_VOLUME_RECT.collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN:
                    sfx_volume_hold = True
                if sfx_volume_hold and event.type == pygame.MOUSEBUTTONUP: 
                    move_volume(SFX_VOLUME_RECT, MUSIC)
                    sfx_volume_hold = False
                                   
                
            """if event.type == pygame.MOUSEBUTTONDOWN:
                if  pygame.mouse.get_pressed()[0] and SFX_SWITCH_RECT.collidepoint(pygame.mouse.get_pos()):
                    if SFX_BOOL:
                        SFX_BOOL = False
                        SFX.stop()                        
                    else:
                        SFX_BOOL = True
                        SFX.play()"""
        if not game_started and not settings: 
            draw_menu()
            if pygame.mouse.get_pressed()[0]:
                if QUIT_BUTTON.collidepoint(pygame.mouse.get_pos()):
                    loop = False 
                if  SETTINGS_BUTTON.collidepoint(pygame.mouse.get_pos()):
                    settings = True            
                if NEW_GAME_BUTTON.collidepoint(pygame.mouse.get_pos()):
                    game_started = True
        elif game_started:
            drawMap(camera)     
            movement(keys_pressed, camera, player, camera_x_right_locked, camera_x_left_locked, camera_y_right_locked, camera_y_left_locked)
        if settings:
            if  pygame.mouse.get_pressed()[0] and CLOSE_BUTTON.collidepoint(pygame.mouse.get_pos()):
                    settings = False
            
            draw_settings(MUSIC_BOOL, SFX_BOOL)
        pygame.display.update()
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()