import pygame, pytmx
import os, sys
pygame.font.init()
pygame.mixer.init()


DEFAULT_FONT = pygame.font.SysFont('comicsans', 30)
AUTHOR_FONT = pygame.font.SysFont('comicsans', 10)

WIDTH, HEIGHT = 1280, 720
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

FPS = 60
VEL = 5

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (128, 128, 128)

CAMERA_UNLOCK_X_RIGHT_EVENT = pygame.USEREVENT + 1
CAMERA_UNLOCK_X_LEFT_EVENT = pygame.USEREVENT + 2
CAMERA_UNLOCK_Y_RIGHT_EVENT = pygame.USEREVENT + 3
CAMERA_UNLOCK_Y_LEFT_EVENT = pygame.USEREVENT + 4


START_GAME_BUTTON = pygame.Rect(0.05*WIDTH , 0.1*HEIGHT, 0.90*WIDTH, 0.2*HEIGHT)
START_GAME_BUTTON_BORDER = pygame.Rect(0.05*WIDTH-2 , 0.1*HEIGHT-2, 0.90*WIDTH+4, 0.2*HEIGHT+4)

#pygame.display.get_surface() #getting resolution
pygame.display.set_caption("Our Game")
gameMap = pytmx.load_pygame(os.path.join('Assets', 'mapa.tmx'))

PLAYER_SRC = pygame.image.load(os.path.join('Assets', 'player.png'))
TILE_T_SRC = pygame.image.load(os.path.join('Assets', 'grass.png')).convert()
TILE_C_SRC = pygame.image.load(os.path.join('Assets', 'water.png')).convert()
MUSIC = pygame.mixer.Sound(os.path.join('Assets', 'music.mp3'))


BLOCK_SIZE = 40
TILE_T  = pygame.transform.scale(TILE_T_SRC, (BLOCK_SIZE,BLOCK_SIZE))
TILE_C  = pygame.transform.scale(TILE_C_SRC, (BLOCK_SIZE,BLOCK_SIZE))

PLAYER_WIDTH, PLAYER_HEIGHT = 30, 60
PLAYER_L = pygame.transform.scale(PLAYER_SRC.subsurface(65, 27, 63, 163), (PLAYER_WIDTH, PLAYER_HEIGHT))
PLAYER_R = pygame.transform.scale(PLAYER_SRC.subsurface(292, 27, 63, 163), (PLAYER_WIDTH, PLAYER_HEIGHT))
PLAYER_U = pygame.transform.scale(PLAYER_SRC.subsurface(391, 27, 90, 163), (3/2*PLAYER_WIDTH, PLAYER_HEIGHT))
PLAYER_D = pygame.transform.scale(PLAYER_SRC.subsurface(161, 27, 90, 163), (3/2*PLAYER_WIDTH, PLAYER_HEIGHT))

DEFAULT_PLAYER_X = WIDTH/2 - PLAYER_WIDTH/2
DEFAULT_PLAYER_Y = HEIGHT/2 - PLAYER_HEIGHT/2


def draw_menu():
    pygame.draw.rect(WIN, BLACK, START_GAME_BUTTON_BORDER)
    pygame.draw.rect(WIN, GREY, START_GAME_BUTTON)
    start_game_text = DEFAULT_FONT.render("Let the game begin!", 1, WHITE)
    WIN.blit(start_game_text, (START_GAME_BUTTON.x + START_GAME_BUTTON.width/2 - start_game_text.get_width()/2, START_GAME_BUTTON.y + START_GAME_BUTTON.height/2 - start_game_text.get_height()/2))   

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
    

def main():  
    game_started = False
    clock = pygame.time.Clock()
    loop = True

    player = pygame.Rect(DEFAULT_PLAYER_X, DEFAULT_PLAYER_Y, PLAYER_WIDTH, PLAYER_HEIGHT)
    camera = pygame.Rect(0, 0, WIDTH, HEIGHT)    
    
    #MUSIC.play()
    #MUSIC.set_volume(0.1)
    
    while loop:
        clock.tick(FPS)
        keys_pressed = pygame.key.get_pressed()

        camera_x_right_locked = True 
        camera_x_left_locked = True
        camera_y_right_locked = True 
        camera_y_left_locked = True

        for event in pygame.event.get():
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

        if not game_started: 
            draw_menu()
            if pygame.mouse.get_pressed()[0] and START_GAME_BUTTON.collidepoint(pygame.mouse.get_pos()):
                game_started = True
        elif game_started:
            drawMap(camera)     
            movement(keys_pressed, camera, player, camera_x_right_locked, camera_x_left_locked, camera_y_right_locked, camera_y_left_locked)

        pygame.display.update()
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()