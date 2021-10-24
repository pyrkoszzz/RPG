import pygame, os
import pytmx

pygame.init()


display_width = 800
display_height = 800

white = (255, 255, 255)

gameScreen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('2d Game')
clock = pygame.time.Clock()

# load map data
gameMap = pytmx.load_pygame(os.path.join('Assets', 'mapa.tmx'))

def game_loop():
    player = pygame.Rect(display_width/2, display_height/2, 16,16)
    loop = True
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_w]:
            player.y -= 1
        if keys_pressed[pygame.K_s]:
            player.y += 1
        if keys_pressed[pygame.K_a]:
            player.x -= 1
        if keys_pressed[pygame.K_d]:
            player.x += 1
        
        for layer in gameMap.visible_layers:
            for x, y, gid, in layer:
                tile = gameMap.get_tile_image_by_gid(gid)
                gameScreen.blit(tile, (x * gameMap.tilewidth-player.x,
                                    y * gameMap.tileheight-player.y))
        pygame.draw.rect(gameScreen, (0,0,0), (display_width/2, display_height/2, 16,16))
        pygame.display.update()
    pygame.quit()
game_loop()