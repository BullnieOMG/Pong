from pygame import *
from random import *

class GameSprite(sprite.Sprite):
    # constructor de clase
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed_x, player_speed_y):
        # llamamos al constructor de la clase (Sprite):
        sprite.Sprite.__init__(self)

        # cada objeto debe almacenar una propiedad image
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed_x = player_speed_x
        self.speed_y = player_speed_y
        self.size_x = size_x
        self.size_y = size_y

        # cada objeto debe almacenar la propiedad rect en la cual está inscrito
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    # método que dibuja al personaje en la ventana
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player1(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
    
        if keys_pressed[K_s] and self.rect.y < win_height - 100:
            self.rect.y += self.speed_y
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed_y

class Player2(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
    
        if keys_pressed[K_DOWN] and self.rect.y < win_height - 100:
            self.rect.y += self.speed_y
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed_y
            
class Ball(GameSprite):
    global finish
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.x > 670:
            Game_over = font2.render('P1 win',1,(0,255,0))
            window.blit(Game_over, (200,200))
            finish = True
        if self.rect.x < -10:
            Game_over = font2.render('P2 win',1,(0,255,0))
            window.blit(Game_over, (200,200))
            finish = True
            
        if self.rect.y > 450:
            self.speed_y *= -1
        if self.rect.y < 0:
            self.speed_y *= -1
            
        collision_ball_player1 = sprite.collide_rect(jugador1, self)
        collision_ball_player2 = sprite.collide_rect(jugador2, self)
        if collision_ball_player1:
            print('Colision 1')
            self.speed_x *= -1
        if collision_ball_player2:
            print('Colision 2')
            self.speed_x *= -1

font.init()
font1 = font.SysFont('Arial',36)
font2 = font.SysFont('Arial',70)
win_height = 500
win_width = 700
window = display.set_mode((win_width,win_height))
display.set_caption('Pong')
background = transform.scale(image.load('Fondo_pong.png'), (win_width,win_height))
clock = time.Clock()
jugador1 = Player1('Pong.png', 10, 200, 15, 105, 0, 15)
jugador2 = Player2('Pong.png', 675, 200, 15, 105, 0, 15)
pelota = Ball('bola_pong.png', 322, 200, 40, 40, 8, 8)

FPS = 40

game = True
finish = False

while game:
    clock.tick(FPS)
    for e in event.get():
        if e.type == QUIT:
            game = False
            
    if finish == False:
            
        window.blit(background,(0, 0))
        
        jugador1.update()
        jugador2.update()
        pelota.update()
        
        jugador1.reset()
        jugador2.reset()
        pelota.reset()
        
        
        display.update()
    elif finish == True:
        display.update()