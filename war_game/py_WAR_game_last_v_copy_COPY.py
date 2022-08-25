import pygame
import random
from os import path
from pygame.locals import *
#константы
WIDTH = 900
HEIGHT = 1000
FPS = 30
#цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

a = 0

#создаем класс с функциями и создаем квадрат 50 на 50 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        
        self.image = pygame.transform.scale(player2_img, (140, 110))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT - 50)
        pygame.sprite.Sprite.__init__(self)   #спрайты

    #перемещение вправо/лево
    def update(self):
        global hits
        global hits1
        global hits2

        global shot_speed
        global player_speed
        
        if self.rect.right > WIDTH-10:
            self.rect.right = WIDTH-10
        elif self.rect.left < 10:
            self.rect.left = 10
        if self.rect.top < HEIGHT/2:
            self.rect.top = HEIGHT/2
        elif self.rect.bottom > HEIGHT-10:
            self.rect.bottom = HEIGHT-10
        pressed_keys = pygame.key.get_pressed()
        
                
        if pressed_keys[K_SPACE] and counter % shot_speed == 0:
            global bullet
            bullet = Bullet()
            all_sprites.add(bullet)
            bullets.add(bullet)
            shot.play()
        
        if pressed_keys[K_RIGHT]:  
            self.rect.x += player_speed
        elif pressed_keys[K_LEFT]: 
            self.rect.x -= player_speed
        elif pressed_keys[K_UP]:
            self.rect.y -= player_speed
        elif pressed_keys[K_DOWN]:
            self.rect.y += player_speed

        hits_shoot = pygame.sprite.spritecollide(player, bullets, False)
        
        for hit in hits_shoot:
            shoot = Shoot(hit.rect.center, 'lg')
            all_sprites.add(shoot)

        # Столкновение:
        
class Enemy1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)   #спрайты
        c1 = random.randrange(1, 6)
        if c1 == 1:
            self.image = pygame.transform.scale(enemy1_img, (140, 110))
        elif c1 == 2:
            self.image = pygame.transform.scale(enemy2_img, (140, 110))
        elif c1 == 3:
            self.image = pygame.transform.scale(enemy3_img, (140, 110))
        elif c1 == 4:
            self.image = pygame.transform.scale(enemy4_img, (140, 110))
        elif c1 == 5:
            self.image = pygame.transform.scale(enemy5_img, (140, 110))
        elif c1 == 6:
            self.image = pygame.transform.scale(enemy6_img, (140, 110))

        self.rect = self.image.get_rect()    #из объекта создаем порямоугольник(существенный объект для его изменения)
        self.rect.center = (random.randrange(60, 540), random.randrange(-500, -50)) #задаем положение центра уже имеющего возможность ихменяться объекта

        hits_shoot = pygame.sprite.spritecollide(player, bullets, False)
        
        for hit in hits_shoot:
            shoot = Shoot(hit.rect.center, 'lg')
            all_sprites.add(shoot)
    
    def update(self):
        global score
        global score_record
        self.rect.y += 10
        if self.rect.top > HEIGHT:
            self.rect.y = random.randrange(-500, -50)
            self.rect.x = random.randrange(60, 540)

        hits1 = pygame.sprite.spritecollide(       #столкновени пули и врага, при столкновении пуля иничтожается, враш возвращается
            self, bullets, True
        )
        if hits1:
            #expl.play()
            self.rect.center = (random.randrange(60, 840), random.randrange(-500, -50))
            score += 1
            if score_record < score:
                score_record += 1

        for hit in hits1:
            explosion = Explosion(hit.rect.center, 'lg')
            all_sprites.add(explosion)
            random.choice(expl_sounds).play()

class Bullet(pygame.sprite.Sprite):  # класс пуль!!!!
    def __init__(self):
        global player
        pygame.sprite.Sprite.__init__(self)   # спрайты
        self.image = pygame.transform.scale(bullet_img, (20, 40))
        self.rect = self.image.get_rect()    #из объекта создаем порямоугольник(существенный объект для его изменения)
        self.rect.center = (player.rect.x + 70, player.rect.y)

    def update(self):     # движение пуль
        self.rect.y -= 20

        if self.rect.top > HEIGHT:
            self.rect.y = random.randrange(-500, -50)
            self.rect.x = random.randrange(60, 540)
class Background(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(bg_image, (900, 1080))
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, -80)

    def update(self):     # движение фона
        self.rect.y += 3

        if self.rect.top > HEIGHT:
            self.rect.y = -1080
            self.rect.x = 0
class Background2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(bg2_image, (900, 1080))
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, -1160)

    def update(self):     # движение фона
        self.rect.y += 3

        if self.rect.top > HEIGHT:
            self.rect.y = -1080
            self.rect.x = 0
class Mainmenu(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(bg_main, (900, 1080))
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)
class Control_img(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(main_control, (500, 400))
        self.rect = self.image.get_rect()
        self.rect.topleft = (50, 500)
class Button_player_choose1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img, (120, 100))
        self.rect = self.image.get_rect()
        self.rect.topleft = (700, 500)
class Button_player_choose2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player1_img, (120, 100))
        self.rect = self.image.get_rect()
        self.rect.topleft = (700, 600)
class Button_player_choose3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player2_img, (120, 100))
        self.rect = self.image.get_rect()
        self.rect.topleft = (700, 700)

class Mouseclick(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player2_img, (20, 20))
        self.rect = self.image.get_rect()
        self.rect.center = (0, 0)

class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image = explosion_anim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosion_anim[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = explosion_anim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

class Shoot(pygame.sprite.Sprite):
    def __init__(self, center, size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image = shoot_anim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(shoot_anim[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = shoot_anim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

class Back_to_main_p(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(back_to_main_img_plane, (400, 100))
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 800)


##########################################################################################
##########################################################################################
###КЛАССЫ ТАНКОВ!!!!


class Tank_player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(t2, (90, 160))
        #self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT -10)
        
           #спрайты

    #перемещение вправо/лево
    def update(self):
        global hits_t
        global hits1_t
        global hits2_t
        global hits3_t
        global hp_player
        global shot_speed
        global player_speed
        global ct1
        global ct2
        global ct3
        global ct4
        global hp_tank_player
        global hp_player_t

        if self.rect.right > WIDTH-10:
            self.rect.right = WIDTH-10
        elif self.rect.left < 10:
            self.rect.left = 10
        if self.rect.top < HEIGHT/2:
            self.rect.top = HEIGHT/2
        elif self.rect.bottom > HEIGHT-10:
            self.rect.bottom = HEIGHT-10
        pressed_keys = pygame.key.get_pressed()
        pressed_keys = pygame.key.get_pressed()
        
        
        if pressed_keys[K_SPACE] and counter % shot_speed == 0:
            global bullet_tank
            bullet_tank = Bullet_tank()
            all_sprites_tank.add(bullet_tank)
            bullets_tank.add(bullet_tank)


             
        
        if pressed_keys[K_RIGHT]:  
            self.rect.x += player_speed
        elif pressed_keys[K_LEFT]: 
            self.rect.x -= player_speed
        elif pressed_keys[K_UP]:
            self.rect.y -= player_speed
        elif pressed_keys[K_DOWN]:
            self.rect.y += player_speed

        
        hits_shoot_tank = pygame.sprite.spritecollide(self, bullets_tank, False)
        
        for hit in hits_shoot_tank:
            shoot_t = Shoot_t(hit.rect.center, 'lg')
            all_sprites_tank.add(shoot_t)
            random.choice(shot_t_sounds).play()

class Enemy1_tank(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)   #спрайты
        c1 = random.randrange(1, 6)
        self.image = pygame.transform.scale(t7, (90, 180))    
        self.rect = self.image.get_rect()    
            #из объекта создаем порямоугольник(существенный объект для его изменения)
        self.rect.center = (random.randrange(60, 540), random.randrange(-500, -50)) #задаем положение центра уже имеющего возможность ихменяться объекта
    
    def update(self):
        global score
        global score_record
        self.rect.y += 5
        if self.rect.top > HEIGHT:
            self.rect.y = random.randrange(-500, -50)
            self.rect.x = random.randrange(60, 540)
        
        hits1 = pygame.sprite.spritecollide(self, bullets_tank, True)
        if hits1:
            score += 1
            if score_record < score:
                score_record += 1
            self.rect.center = (random.randrange(60, 840), random.randrange(-500, -50))
        if bullet_enemy1.rect.y> 2000:
            bullet_enemy1.rect.center = (enemy1_tank.rect.x + 45, enemy1_tank.rect.y + 170)
            random.choice(shot_t_sounds).play()
        for hit in hits1:
            explosion = Explosion(hit.rect.center, 'lg')
            all_sprites_tank.add(explosion)
            random.choice(expl_sounds).play()
        hits_e = pygame.sprite.spritecollide(self, mob_bullets_group, False)
        for hit_e in hits_e:
            shoot_t_e_name = Shoot_t_e(hit_e.rect.center, 'lg')
            all_sprites_tank.add(shoot_t_e_name)
        

class Enemy2_tank(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)   #спрайты
        c1 = random.randrange(1, 6)
        self.image = pygame.transform.scale(t3, (90, 180))
        self.rect = self.image.get_rect()    #из объекта создаем порямоугольник(существенный объект для его изменения)
        self.rect.center = (random.randrange(60, 540), random.randrange(-500, -50)) #задаем положение центра уже имеющего возможность ихменяться объекта
    
    def update(self):
        global score
        global score_record
        self.rect.y += 5
        if self.rect.top > HEIGHT:
            self.rect.y = random.randrange(-500, -50)
            self.rect.x = random.randrange(60, 540)
        
        hits1 = pygame.sprite.spritecollide(self, bullets_tank, True)
        if hits1:
            score += 1
            if score_record < score:
                score_record += 1
            self.rect.center = (random.randrange(60, 840), random.randrange(-500, -50))
        if bullet_enemy2.rect.y> 1900:
            bullet_enemy2.rect.center = (enemy2_tank.rect.x + 45, enemy2_tank.rect.y + 170)
            random.choice(shot_t_sounds).play()
        for hit in hits1:
            explosion_t = Explosion_t(hit.rect.center, 'lg')
            all_sprites_tank.add(explosion_t)
            random.choice(expl_sounds).play() 
        hits_e = pygame.sprite.spritecollide(self, mob_bullets_group, False)
        for hit_e in hits_e:
            shoot_t_e_name = Shoot_t_e(hit_e.rect.center, 'lg')
            all_sprites_tank.add(shoot_t_e_name)
         

class Enemy3_tank(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)   #спрайты
        c1 = random.randrange(1, 6)
        self.image = pygame.transform.scale(t5, (90, 180))
        self.rect = self.image.get_rect()    #из объекта создаем порямоугольник(существенный объект для его изменения)
        self.rect.center = (random.randrange(60, 540), random.randrange(-500, -50)) #задаем положение центра уже имеющего возможность ихменяться объекта
    
    def update(self):
        global score
        global score_record
        self.rect.y += 5
        if self.rect.top > HEIGHT:
            self.rect.y = random.randrange(-500, -50)
            self.rect.x = random.randrange(60, 540)
        
        hits1 = pygame.sprite.spritecollide(self, bullets_tank, True)
        if hits1:
            score += 1
            if score_record < score:
                score_record += 1
            self.rect.center = (random.randrange(60, 840), random.randrange(-500, -50))
        if bullet_enemy3.rect.y > 2100:
            bullet_enemy3.rect.center = (enemy3_tank.rect.x + 45, enemy3_tank.rect.y + 170)
            random.choice(shot_t_sounds).play()
        for hit in hits1:
            explosion = Explosion(hit.rect.center, 'lg')
            all_sprites_tank.add(explosion)
            random.choice(expl_sounds).play()  
        hits_e = pygame.sprite.spritecollide(self, mob_bullets_group, False)
        for hit_e in hits_e:
            shoot_t_e_name = Shoot_t_e(hit_e.rect.center, 'lg')
            all_sprites_tank.add(shoot_t_e_name)
        
class Enemy4_tank(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)   #спрайты
        c1 = random.randrange(1, 6)
        self.image = pygame.transform.scale(t1, (90, 180))
        self.rect = self.image.get_rect()    #из объекта создаем порямоугольник(существенный объект для его изменения)
        self.rect.center = (random.randrange(60, 540), random.randrange(-500, -50)) #задаем положение центра уже имеющего возможность ихменяться объекта
    
    def update(self):
        global score
        global score_record
        self.rect.y += 5
        if self.rect.top > HEIGHT:
            self.rect.y = random.randrange(-500, -50)
            self.rect.x = random.randrange(60, 540)
        
        hits1 = pygame.sprite.spritecollide(self, bullets_tank, True)
        if hits1:
            score += 1
            if score_record < score:
                score_record += 1
            self.rect.center = (random.randrange(60, 840), random.randrange(-500, -50))
        if bullet_enemy4.rect.y > 2000:
            bullet_enemy4.rect.center = (enemy4_tank.rect.x + 45, enemy4_tank.rect.y + 170)
            random.choice(shot_t_sounds).play()
        for hit in hits1:
            explosion = Explosion(hit.rect.center, 'lg')
            all_sprites_tank.add(explosion)
            random.choice(expl_sounds).play()  
        hits_e = pygame.sprite.spritecollide(self, mob_bullets_group, False)
        for hit_e in hits_e:
            shoot_t_e_name = Shoot_t_e(hit_e.rect.center, 'lg')
            all_sprites_tank.add(shoot_t_e_name)
        
 

class Bullet_tank(pygame.sprite.Sprite):  # класс пуль!!!!
    def __init__(self):
        global player
        pygame.sprite.Sprite.__init__(self)   # спрайты
        self.image = pygame.transform.scale(bullet_tank_image, (20, 40))
        self.rect = self.image.get_rect()    #из объекта создаем порямоугольник(существенный объект для его изменения)
        self.rect.center = (tank.rect.x + 40, tank.rect.y)

    def update(self):     # движение пуль
        self.rect.y -= 20

        if self.rect.top > HEIGHT:
            self.rect.y = random.randrange(-500, -50)
            self.rect.x = random.randrange(60, 540)
        
        


class Bullet_tank_enemy1(pygame.sprite.Sprite):  # класс пуль!!!!
    def __init__(self):
        global player
        pygame.sprite.Sprite.__init__(self)   # спрайты
        self.image = pygame.transform.scale(bullet_tank_en_image, (20, 40))
        self.rect = self.image.get_rect()    #из объекта создаем порямоугольник(существенный объект для его изменения)
        self.rect.center = (enemy1_tank.rect.x + 40, enemy1_tank.rect.y + 50)

    def update(self):     # движение пуль
        self.rect.y += 20
        


class Bullet_tank_enemy2(pygame.sprite.Sprite):  # класс пуль!!!!
    def __init__(self):
        global player
        pygame.sprite.Sprite.__init__(self)   # спрайты
        self.image = pygame.transform.scale(bullet_tank_en_image, (20, 40))
        self.rect = self.image.get_rect()    #из объекта создаем порямоугольник(существенный объект для его изменения)
        self.rect.center = (enemy2_tank.rect.x + 40, enemy2_tank.rect.y + 50)

    def update(self):     # движение пуль
        self.rect.y += 20
        
class Bullet_tank_enemy3(pygame.sprite.Sprite):  # класс пуль!!!!
    def __init__(self):
        global player
        pygame.sprite.Sprite.__init__(self)   # спрайты
        self.image = pygame.transform.scale(bullet_tank_en_image, (20, 40))

        self.rect = self.image.get_rect()    #из объекта создаем порямоугольник(существенный объект для его изменения)
        self.rect.center = (enemy3_tank.rect.x + 40, enemy3_tank.rect.y + 50)

    def update(self):     # движение пуль
        self.rect.y += 20
      

class Bullet_tank_enemy4(pygame.sprite.Sprite):  # класс пуль!!!!
    def __init__(self):
        global player
        pygame.sprite.Sprite.__init__(self)   # спрайты
        self.image = pygame.transform.scale(bullet_tank_en_image, (20, 40))

        self.rect = self.image.get_rect()    #из объекта создаем порямоугольник(существенный объект для его изменения)
        self.rect.center = (enemy4_tank.rect.x + 40, enemy4_tank.rect.y + 50)

    def update(self):     # движение пуль
        self.rect.y += 20
        

#КЛАССЫ КНОПОК
class Button_tank_choose1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(t2, (80, 140))
        
        self.rect = self.image.get_rect()
        self.rect.topleft = (700, 350)
class Button_tank_choose2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(t6, (80, 140))
        
        self.rect = self.image.get_rect()
        self.rect.topleft = (700, 500)
class Button_tank_choose3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(t4, (80, 140))
        
        self.rect = self.image.get_rect()
        self.rect.topleft = (700, 650)
class Button_tank_choose4(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(t8, (80, 140))
        
        self.rect = self.image.get_rect()
        self.rect.topleft = (700, 800)
class Mouseclick2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((3,3))
        self.rect = self.image.get_rect()
        self.rect.center = (0, 0)


#ПОКАЗЫВАНИЕ КОЛВА ХП ИГРОКА И ЕГО УСЛОВИЯ И ПЕРЕДВИЖЕНИЕ
class Hp_table(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.Surface((100, 10))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT -140)
        
    def update(self):
        
        if hp_player > ct1:
            self.image = pygame.transform.scale(hp100, (100, 10))
        elif hp_player > ct2:
            self.image = pygame.transform.scale(hp75, (100, 10))
        elif hp_player > ct3:
            self.image = pygame.transform.scale(hp50, (100, 10))
        elif hp_player > ct4:
            self.image = pygame.transform.scale(hp25, (100, 10))
        elif hp_player <=5:
            self.image = pygame.transform.scale(hp0, (100, 10))


        if pressed_keys[K_RIGHT]:  
            self.rect.x += player_speed
        elif pressed_keys[K_LEFT]: 
            self.rect.x -= player_speed
        elif pressed_keys[K_UP]:
            self.rect.y -= player_speed
        elif pressed_keys[K_DOWN]:
            self.rect.y += player_speed

        if self.rect.right > WIDTH :
            self.rect.right = WIDTH
        elif self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < HEIGHT/2 -20:
            self.rect.top = HEIGHT/2 -20
        elif self.rect.bottom > HEIGHT-140:
            self.rect.bottom = HEIGHT-140

class Background_tank(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(road, (900, 1080))
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, -80)

    def update(self):     # движение фона
        self.rect.y += 3

        if self.rect.top > HEIGHT:
            self.rect.y = -1080
            self.rect.x = 0
class Background2_tank(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(road2, (900, 1080))
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, -1160)

    def update(self):     # движение фона
        self.rect.y += 3

        if self.rect.top > HEIGHT:
            self.rect.y = -1080
            self.rect.x = 0

class Mainmenu_tank(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(bg_image_tank, (900, 1080))
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)



#########################################################
#########################################################
###ПЕРВЫЙ ЭКРАН ГЛАВНОЕ МЕНЮ


class MainMainmenu_tank(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(t6, (100, 180))
        self.rect = self.image.get_rect()
        self.rect.topleft = (200, 480)

class MainMainmenu_plane(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img, (160, 110))
        self.rect = self.image.get_rect()
        self.rect.topleft = (520, 500)
        
class Mouseclick3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10,10))
        self.rect = self.image.get_rect()
        self.rect.center = (0, 0)

class Mouseclick4_color(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10,10))
        self.rect = self.image.get_rect()
        self.rect.center = (0, 0)

class Mouseclick3_plate_color_p(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((180,130))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (0, 0)

class Mouseclick3_plate_color_t(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((120,200))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (0, 0)

##################
###ЭФФЕКТЫ ТАНКОВ

class Explosion_t(pygame.sprite.Sprite):
    def __init__(self, center, size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image = explosion_anim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosion_anim[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = explosion_anim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

class Shoot_t(pygame.sprite.Sprite):
    def __init__(self, center, size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image = shoot_anim_t[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(shoot_anim_t[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = shoot_anim_t[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

class Shoot_t_e(pygame.sprite.Sprite):
    def __init__(self, center, size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image = shoot_anim_t_e[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(shoot_anim_t_e[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = shoot_anim_t_e[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center


class Back_to_main_t(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(back_to_main_img_tank, (400, 100))
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 800)


#################################ПАПКИ

pygame.init()

print( pygame.image.get_extended() )
# Указание пути к ассетам:
game_folder = path.dirname(__file__)

img_dir = path.join(game_folder, 'img')

snd_dir = path.join(game_folder, 'snd')

fnt_dir = path.join(game_folder, 'fnt')

img_shoot_dir = path.join(game_folder, 'img_shoot')

img_shoot_dir_t = path.join(game_folder, 'img_shoot_tank')


######################################################
############ЭФФЕКТЫ ТАНКИ/САМОЛЕТЫ

shoot_anim = {}
shoot_anim['lg'] = []

for i in range(4):
    filename = 'regularShoot0{}.png'.format(i)
    img = pygame.image.load(path.join(img_shoot_dir, filename))
    img.set_colorkey(BLACK)
    img_lg = pygame.transform.scale(img, (60, 60))
    shoot_anim['lg'].append(img_lg)


explosion_anim = {}
explosion_anim['lg'] = []

for i in range(9):
    filename = 'regularExplosion0{}.png'.format(i)
    img = pygame.image.load(path.join(img_dir, filename))
    img.set_colorkey(BLACK)
    img_lg = pygame.transform.scale(img, (100, 100))
    explosion_anim['lg'].append(img_lg)

           
shoot_anim_t = {}
shoot_anim_t['lg'] = []

for i in range(6):
    filename = 'TankregularShoot0{}.png'.format(i)
    img = pygame.image.load(path.join(img_shoot_dir_t, filename))
    img.set_colorkey(BLACK)
    img_lg = pygame.transform.scale(img, (90, 90))
    shoot_anim_t['lg'].append(img_lg)

shoot_anim_t_e = {}
shoot_anim_t_e['lg'] = []

for i in range(6):
    filename = 'TankregularShoot_enemy0{}.png'.format(i)
    img = pygame.image.load(path.join(img_shoot_dir_t, filename))
    img.set_colorkey(BLACK)
    img_lg = pygame.transform.scale(img, (90, 90))
    shoot_anim_t_e['lg'].append(img_lg)

# explosion_anim_t = {}
# explosion_anim_t['lg'] = []

# for i in range(9):
#     filename = 'regularExplosion0{}.png'.format(i)
#     img = pygame.image.load(path.join(img_dir, filename))
#     img.set_colorkey(BLACK)
#     img_lg = pygame.transform.scale(img, (100, 100))
#     explosion_anim['lg'].append(img_lg)



score = 0
score_record = 0

fpsClock = pygame.time.Clock()  #что-то типа счетчика

# Загрузка аудио
#pygame.mixer.music.load(path.join(snd_dir, 'gul.mp3'))
#pygame.mixer.music.play(-1)
pygame.mixer.music.load(path.join(snd_dir, 'engine.mp3'))
pygame.mixer.music.play(-1)

shot = pygame.mixer.Sound(path.join(snd_dir, 'shot (2).wav'))
shot_t1 = pygame.mixer.Sound(path.join(snd_dir, 'shot_t1.wav'))
shot_t2 = pygame.mixer.Sound(path.join(snd_dir, 'shot_t2.wav'))
shot_t3 = pygame.mixer.Sound(path.join(snd_dir, 'shot_t3.wav'))
expl = pygame.mixer.Sound(path.join(snd_dir, 'expl.wav'))
expl1 = pygame.mixer.Sound(path.join(snd_dir, 'expl1.wav'))
lesgo = pygame.mixer.Sound(path.join(snd_dir, 'lesgo.wav'))

expl_sounds = []
expl_sounds.append(expl)
expl_sounds.append(expl1)
shot_t_sounds = []
shot_t_sounds.append(shot_t1)
shot_t_sounds.append(shot_t2)
shot_t_sounds.append(shot_t3)

##########################################
##########################################
##########################################
###САМОЛЕТЫ


# Загрузка изображений:
bg_main = pygame.image.load(path.join(img_dir, 'bg_main.jpg'))
main_control = pygame.image.load(path.join(img_dir, 'control.png'))

bg_image = pygame.image.load(path.join(img_dir, 'bg1(1).png'))
bg2_image = pygame.image.load(path.join(img_dir, 'bg1(2).png'))

player_img = pygame.image.load(path.join(img_dir, 'plane.png'))
player1_img = pygame.image.load(path.join(img_dir, 'plane1.png'))
player2_img = pygame.image.load(path.join(img_dir, 'plane2.png'))

enemy1_img = pygame.image.load(path.join(img_dir, 'en1.png'))
enemy2_img = pygame.image.load(path.join(img_dir, 'en2.png'))
enemy3_img = pygame.image.load(path.join(img_dir, 'en3.png'))
enemy4_img = pygame.image.load(path.join(img_dir, 'en4.png'))
enemy5_img = pygame.image.load(path.join(img_dir, 'en5.png'))
enemy6_img = pygame.image.load(path.join(img_dir, 'en6.png'))

bullet_img = pygame.image.load(path.join(img_dir, 'bullet.png'))

back_to_main_img_plane = pygame.image.load(path.join(img_dir, 'back_to_main.png'))

#текст
pygame.font.init()
game_score = pygame.font.Font(path.join(fnt_dir, '19255.ttf'), 20)
game_over = pygame.font.Font(path.join(fnt_dir, '19255.ttf'), 40)

################################################
###ГЛАВНОЕ МЕНЮ САМОЛЕТОВ
main_menu = pygame.sprite.Group()
main_img = Mainmenu()
control = Control_img()
main_menu.add(main_img)
main_menu.add(control)

###КНОПКИ

btp1 = Button_player_choose1()
btp2 = Button_player_choose2()
btp3 = Button_player_choose3()
main_menu.add(btp1)
main_menu.add(btp2)
main_menu.add(btp3)

###КЛИК

click_group = pygame.sprite.Group()
click = Mouseclick()
main_menu.add(click)
click_group.add(click)

###ВСЕ СПРАЙТЫ САМОЛЕТЫ

all_sprites = pygame.sprite.Group() #создание группы спрайтов
bg = Background()
bg2 = Background2()

all_sprites.add(bg)
all_sprites.add(bg2)

mobs = pygame.sprite.Group() #добавление мобов в группу
bullet = None
bullets = pygame.sprite.Group()
player = Player()   #назначаем имя класса

all_sprites.add(player)  #добавляем в группу спрайтов класс спрайтов игрока
  #вызов функции класса
enemy1 = Enemy1()

back_p = pygame.sprite.Group()
back_to_main_plane = Back_to_main_p()
back_p.add(back_to_main_plane)

#СОЗДАНИЕ МОБОВ##################

mob_list = []
for cnt in range(12): 
    enemy1 = Enemy1()
    all_sprites.add(enemy1)
    mobs.add(enemy1)
    mob_list.append(enemy1)
screen = pygame.display.set_mode((WIDTH, HEIGHT))  #создание главного окна
pygame.display.set_caption('WAR Game')  #имя окна

###############################
###############################
###############################
###############################
###ТАНКИ

counter = 0
start = True
start0 = True 
start2 = False
start_plane_main = False

#########СПРАЙТЫ ТАНКОВ И ПРИЛАГАЮЩИЕСЯ К НИМ ЭЛЕМЕНТЫ

t1 = pygame.image.load(path.join(img_dir, 't1.png'))
t2 = pygame.image.load(path.join(img_dir, 't2.png'))
t3 = pygame.image.load(path.join(img_dir, 't3.png'))
t4 = pygame.image.load(path.join(img_dir, 't4.png'))
t5 = pygame.image.load(path.join(img_dir, 't5.png'))
t6 = pygame.image.load(path.join(img_dir, 't6.png'))
t7 = pygame.image.load(path.join(img_dir, 't7.png'))
t8 = pygame.image.load(path.join(img_dir, 't8.png'))

bg_image_tank = pygame.image.load(path.join(img_dir, 'image.jpg'))

bullet_tank_image = pygame.image.load(path.join(img_dir, 'bullet_tank.png'))
bullet_tank_en_image = pygame.image.load(path.join(img_dir, 'bullet_tank_en.png'))

hp100 = pygame.image.load(path.join(img_dir, 'hp100.png'))
hp75 = pygame.image.load(path.join(img_dir, 'hp75.png'))
hp50 = pygame.image.load(path.join(img_dir, 'hp50.png'))
hp25 = pygame.image.load(path.join(img_dir, 'hp25.png'))
hp0 = pygame.image.load(path.join(img_dir, 'hp0.png'))

road = pygame.image.load(path.join(img_dir, 'road.jpg'))
road2 = pygame.image.load(path.join(img_dir, 'road2.jpg'))

back_to_main_img_tank = pygame.image.load(path.join(img_dir, 'back_to_main.png'))

####################################ШРИФТЫ

pygame.font.init()
game_score = pygame.font.Font(path.join(fnt_dir, '19255.ttf'), 20)
game_over = pygame.font.Font(path.join(fnt_dir, '19255.ttf'), 40)

#############################################СТАНДАРТНЫЕ ХАРАКТРЕИСТИКИ ТАНКА

shot_speed = 60
player_speed = 5

##################ЗАГРУЗКА СПРАЙТОВ

main_menu2 = pygame.sprite.Group()  ###ГРУППА ГЛАВНОГО МЕНЮ ТАКНОВ
main_image = Mainmenu_tank()
main_menu2.add(main_image)
bttp1 = Button_tank_choose1()
bttp2 = Button_tank_choose2()
bttp3 = Button_tank_choose3()
bttp4 = Button_tank_choose4()
main_menu2.add(bttp1)
main_menu2.add(bttp2)
main_menu2.add(bttp3)
main_menu2.add(bttp4)
click2_group = pygame.sprite.Group()
click2 = Mouseclick2()
main_menu2.add(click2)
click2_group.add(click2)

all_sprites_tank = pygame.sprite.Group()

bg_road = Background_tank()
all_sprites_tank.add(bg_road)
bg_road2 = Background2_tank()
all_sprites_tank.add(bg_road2)
tank = Tank_player()
all_sprites_tank.add(tank)

hp_tank = Hp_table()
all_sprites_tank.add(hp_tank)

back_t = pygame.sprite.Group()
back_to_main_t = Back_to_main_t()
back_t.add(back_to_main_t)




####################################
####################################
###МОБЫ ТАНКОВ!!!!!!
mobs_tank = pygame.sprite.Group()

mob_list_tank = []
mob_bullet = []

for en1 in range(2):
    enemy1_tank = Enemy1_tank()
    all_sprites_tank.add(enemy1_tank)
    mobs_tank.add(enemy1_tank)
    mob_list_tank.append(enemy1_tank)

for en2 in range(2):
    enemy2_tank = Enemy2_tank()
    all_sprites_tank.add(enemy2_tank)
    mobs_tank.add(enemy2_tank)
    mob_list_tank.append(enemy2_tank)

for en3 in range(2):
    enemy3_tank = Enemy3_tank()
    all_sprites_tank.add(enemy3_tank)
    mobs_tank.add(enemy3_tank)
    mob_list_tank.append(enemy3_tank)

for en4 in range(1):
    enemy4_tank = Enemy4_tank()
    all_sprites_tank.add(enemy4_tank)
    mobs_tank.add(enemy4_tank)
    mob_list_tank.append(enemy4_tank)

####################################
###ПУЛИ МОБОВ ТАНКОВ

mob_bullets_group = pygame.sprite.Group()

bullet_enemy1 = Bullet_tank_enemy1()
all_sprites_tank.add(bullet_enemy1)
mob_bullet.append(bullet_enemy1)
mob_bullets_group.add(bullet_enemy1)

bullet_enemy2 = Bullet_tank_enemy2()
all_sprites_tank.add(bullet_enemy2)
mob_bullet.append(bullet_enemy2)
mob_bullets_group.add(bullet_enemy2)

bullet_enemy3 = Bullet_tank_enemy3()
all_sprites_tank.add(bullet_enemy3)
mob_bullet.append(bullet_enemy3)
mob_bullets_group.add(bullet_enemy3)

bullet_enemy4 = Bullet_tank_enemy4()
all_sprites_tank.add(bullet_enemy4)
mob_bullet.append(bullet_enemy4)
mob_bullets_group.add(bullet_enemy4)


main_menu3 = pygame.sprite.Group()
main_but_in_main_t = MainMainmenu_tank()

main_but_in_main_p = MainMainmenu_plane()

#################################
#################################
###КУРСОРЫ/КЛИКИ


click_plate_p = Mouseclick3_plate_color_p()
click_plate_t = Mouseclick3_plate_color_t()


click_mainmain = pygame.sprite.Group()
click3 = Mouseclick3()
click_mainmain.add(click3)
click_mainmain_for4 = pygame.sprite.Group()
click4 = Mouseclick4_color()
click_mainmain_for4.add(click4)

main_menu3.add(click_plate_p)
main_menu3.add(click_plate_t)

main_menu3.add(main_but_in_main_t)

main_menu3.add(main_but_in_main_p)

###ПЕРЕМЕННЫЕ ЦИКЛОВ

bullet_tank = None
bullets_tank = pygame.sprite.Group()

start_tank_main = False
start2_tank = False
start_tank = False

counter = 0
fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

while True:
    for event in pygame.event.get():  # для события происходящего в окне
        if event.type == pygame.QUIT:  # если событие выход, то
            pygame.quit()  # остановка главного цикла программы
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                click3.rect.center = event.pos 

        if event.type == pygame.MOUSEMOTION:
                click4.rect.center = event.pos
    #pressed_keys = pygame.key.get_pressed()
    screen.fill((0, 0, 0))
    
    click_mainmain.update()
    click_mainmain.draw(screen)
    click_mainmain_for4.update()
    click_mainmain_for4.draw(screen)
    main_menu3.update()
    main_menu3.draw(screen)
    
    hits_main1 = pygame.sprite.spritecollide(main_but_in_main_t, click_mainmain, False)
    if hits_main1:
        start_tank_main = True


    hits_main2 = pygame.sprite.spritecollide(main_but_in_main_p, click_mainmain, False)
    if hits_main2:
        start_plane_main = True
    
    

    hits_main3 = pygame.sprite.spritecollide(main_but_in_main_t, click_mainmain_for4, False)
    if hits_main3:
        click_plate_t.rect.topleft = (190, 480)
    else:
        click_plate_t.rect.topleft = (-500, 0)
    
    hits_main4 = pygame.sprite.spritecollide(main_but_in_main_p, click_mainmain_for4, False)

    if hits_main4:
        click_plate_p.rect.topleft = (510, 490)
    else:
        click_plate_p.rect.topleft = (-500, 0)
    
    pygame.display.flip()

################################################
###САМОЛЕТ

    while start_plane_main:
        
                
        global choosing_font
        global choosing_font1
        global choosing_font2
        pressed_keys = pygame.key.get_pressed()
        
        hits = pygame.sprite.spritecollide(btp1, click_group, False)
        
        if hits:
            player.image = pygame.transform.scale(player_img, (140, 110))
            shot_speed = 5
            player_speed = 5
            a = 1
            start2 = True
            start = True
            player.rect.center = (WIDTH / 2, HEIGHT - 50)

        hits1 = pygame.sprite.spritecollide(btp2, click_group, False)
        if hits1:
            player.image = pygame.transform.scale(player1_img, (140, 110)) 
            shot_speed = 10
            player_speed = 10 
            a = 2
            start2 = True
            start = True
            player.rect.center = (WIDTH / 2, HEIGHT - 50)

        hits2 = pygame.sprite.spritecollide(btp3, click_group, False)
        if hits2:
            player.image = pygame.transform.scale(player2_img, (140, 110))
            shot_speed = 15
            player_speed = 15
            a = 3    
            start2 = True
            start = True
            player.rect.center = (WIDTH / 2, HEIGHT - 50) 
        
        # if pressed_keys[K_s]:
        #     start2 = True
        #     start = True
        #     player.rect.center = (WIDTH / 2, HEIGHT - 50)
        for enemy1 in mob_list:
            enemy1.rect.center = (random.randrange(60, 840), random.randrange(-500, -50))
        if pressed_keys[K_ESCAPE]:
            pygame.quit()
        if pressed_keys[K_RSHIFT]:
            start_plane_main = False
            click3.rect.topleft = (0, 0)
        main_menu.update()
        main_menu.draw(screen)
        click_group.update()
        click_group.draw(screen)
        for event in pygame.event.get():  # для события происходящего в окне

            if event.type == pygame.QUIT:  # если событие выход, то
                pygame.quit()  # остановка главного цикла программы
                
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                click.rect.center = event.pos  
        
        text_surface1 = game_over.render(
                'PLANE GAME', True, RED 
            )
        text_surface3 = game_score.render(
                'to start choose your plane and press "s"', True, RED 
            )
        choosing_font_speed =  game_score.render('speed: low', True, BLACK, WHITE )
        choosing_font_shot =  game_score.render('shot: high', True, BLACK, WHITE )
        choosing_font1_speed = game_score.render('speed: mid', True, BLACK, WHITE )
        choosing_font1_shot = game_score.render('shot: mid', True, BLACK, WHITE)
        choosing_font2_speed = game_score.render('speed: high', True, BLACK, WHITE)  
        choosing_font2_shot = game_score.render('shot: low', True, BLACK, WHITE) 


        screen.blit(text_surface1, (50, 300))
        screen.blit(text_surface3, (50, 350))
        screen.blit(choosing_font_speed, (500, 500))
        screen.blit(choosing_font_shot, (500, 530))
        screen.blit(choosing_font1_speed, (500, 600))
        screen.blit(choosing_font1_shot, (500, 630))
        screen.blit(choosing_font2_speed, (500, 700))
        screen.blit(choosing_font2_shot, (500, 730))
        pygame.display.flip()

        while start2:
            back_p.update()
            click_group.update()
            # Текст при проигрыше
            text_surface = game_over.render(
                'Game Over! Continue?', True, RED 
            )
            text_surface2 = game_over.render(
                'to continue press "y"', True, RED 
            )
            text_surface3 = game_score.render(
                'to change plane press LSHIFT', True, RED 
            )
            # Вывод текста на экран
            screen.blit(text_surface, (50, 300))
            screen.blit(text_surface2, (50, 350))
            screen.blit(text_surface3, (50, 400))
            for event in pygame.event.get():  # для события происходящего в окне

                if event.type == pygame.QUIT:  # если событие выход, то
                    pygame.quit()  # остановка главного цикла программы
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    click.rect.center = event.pos
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[K_ESCAPE]:
                pygame.quit()
            elif pressed_keys[K_y]:  # перезапуск при столкновении
                start = True
                player.rect.center = (WIDTH / 2, HEIGHT - 50)  # вовращение игрока
                for mob in mob_list:                  # возвращение мобов
                    mob.rect.center = (random.randrange(60, 540), random.randrange(-500, -50))
            hits_to_back = pygame.sprite.spritecollide(back_to_main_plane, click_group, False)
            if hits_to_back:
                start2 = False
                click.rect.center = (0, 0)
            score = 0
            back_p.draw(screen)
            click_group.draw(screen)
            pygame.display.flip()  # переворот экрана (очень важно)
            
            while start:            #постоянная программа игровой цикл
                
                counter = counter + 1
                fpsClock.tick(FPS)     #счетчик кадров (без него программа не запуститься)
                for event in pygame.event.get():        #для события происходящего в окне

                    if event.type == pygame.QUIT:           #если событие выход, то
                        start = False               # остановка главного цикла программы
                

                all_sprites.update()         #постоянное обновление спрайтов в каждом кадре

                hits = pygame.sprite.spritecollide(
                    player, mobs, False
                )
                if hits:
                    start2 = True
                    #lesgo.play()
                    expl.play()
                    start = False  #при столкновении происходит остановка цикла
                if pressed_keys[K_ESCAPE]:
                    pygame.quit()
                
                all_sprites.draw(screen)  #рендеринг, отрисовка спрайтов на экране

                score_surface = game_score.render(f'Score: {score}', True, BLACK, WHITE)
                score_surface_record = game_score.render(f'Score record: {score_record}', True, BLACK, WHITE)
                screen.blit(score_surface, (500, 0))
                screen.blit(score_surface_record, (150, 0))

                pygame.display.flip()   #переворот экрана (очень важно)

##############################ТАНК
    while start_tank_main:
        
                
        text_surface1_t = game_over.render(
            'TANK GAME', True, RED 
        )
        text_surface3_t = game_score.render(
            'to start choose your tank and press "s"', True, RED 
        )
        pressed_keys = pygame.key.get_pressed()

        choosing_font_speed =  game_score.render('speed: high', True, BLACK, WHITE )
        choosing_font_shot =  game_score.render('shot: high', True, BLACK, WHITE )
        choosing_font_hp = game_score.render('hp: 75', True, BLACK, WHITE )
        choosing_font1_speed = game_score.render('speed: mid', True, BLACK, WHITE )
        choosing_font1_shot = game_score.render('shot: high', True, BLACK, WHITE)
        choosing_font1_hp = game_score.render('shot: 125', True, BLACK, WHITE )
        choosing_font2_speed = game_score.render('speed: low', True, BLACK, WHITE)  
        choosing_font2_shot = game_score.render('shot: so low', True, BLACK, WHITE) 
        choosing_font2_hp = game_score.render('hp: 500', True, BLACK, WHITE )
        choosing_font3_speed = game_score.render('speed: low', True, BLACK, WHITE)  
        choosing_font3_shot = game_score.render('shot: mid', True, BLACK, WHITE) 
        choosing_font3_hp = game_score.render('hp: 200', True, BLACK, WHITE )

        
        if pressed_keys[K_ESCAPE]:
            pygame.quit()
        if pressed_keys[K_RSHIFT]:
            start_tank_main = False
            click3.rect.topleft = (0, 0)

        #ПРОВЕРКА КНОПКИ НАЖАТОЙ ВГЛАВНОМ МЕНЮ И ПРИСВОЕНИЕ ТАНКУ КАРТИКНИ/ХАРАКТЕРИСТИК

#t3485
        hits_t = pygame.sprite.spritecollide(bttp1, click2_group, False)
        if hits_t:
            tank.image = pygame.transform.scale(t2, (90, 160))
            shot_speed = 30
            player_speed = 8
            a = 1
            hp_player = 75
            ct1 = 60
            ct2 = 40
            ct3 = 20
            ct4 = 5
            hp_counter = hp_player
            start2_tank = True
            start_tank = True
            tank.rect.center = (WIDTH / 2, HEIGHT -10)
            hp_tank.rect.center = (WIDTH / 2, HEIGHT -140)
            for mob_tank in mob_list_tank:                  # возвращение мобов
                    mob_tank.rect.center = (random.randrange(60, 540), random.randrange(-500, -50))
#tiger1
        hits1_t = pygame.sprite.spritecollide(bttp2, click2_group, False)
        if hits1_t:
            tank.image = pygame.transform.scale(t6, (90, 160)) 
            shot_speed = 30
            a = 2
            hp_player = 125
            ct1 = 100
            ct2 = 60
            ct3 = 30
            ct4 = 5
            hp_counter = hp_player
            start2_tank = True
            start_tank = True
            tank.rect.center = (WIDTH / 2, HEIGHT -10)
            hp_tank.rect.center = (WIDTH / 2, HEIGHT -140)
            for mob_tank in mob_list_tank:                  # возвращение мобов
                    mob_tank.rect.center = (random.randrange(60, 540), random.randrange(-500, -50))
#maus
        hits2_t = pygame.sprite.spritecollide(bttp3, click2_group, False)
        if hits2_t:
            tank.image = pygame.transform.scale(t4, (90, 160))
            shot_speed = 120
            player_speed = 5
            a = 3     
            hp_player = 500
            ct1 = 350
            ct2 = 225
            ct3 = 100
            ct4 = 20
            hp_counter = hp_player
            start2_tank = True
            start_tank = True
            tank.rect.center = (WIDTH / 2, HEIGHT -10)
            hp_tank.rect.center = (WIDTH / 2, HEIGHT -140)
            for mob_tank in mob_list_tank:                  # возвращение мобов
                    mob_tank.rect.center = (random.randrange(60, 540), random.randrange(-500, -50))
#tiger2
        hits3_t = pygame.sprite.spritecollide(bttp4, click2_group, False)
        if hits3_t:
            tank.image = pygame.transform.scale(t8, (90, 160))
            shot_speed = 45
            player_speed = 5
            a = 3     
            hp_player = 200
            ct1 = 150
            ct2 = 100
            ct3 = 50
            ct4 = 10
            hp_counter = hp_player
            start2_tank = True
            start_tank = True
            tank.rect.center = (WIDTH / 2, HEIGHT -10)
            hp_tank.rect.center = (WIDTH / 2, HEIGHT -140)
            for mob_tank in mob_list_tank:                  # возвращение мобов
                    mob_tank.rect.center = (random.randrange(60, 540), random.randrange(-500, -50))

        for event in pygame.event.get():  # для события происходящего в окне
            
            if event.type == pygame.QUIT:  # если событие выход, то
                pygame.quit()  # остановка главного цикла программы
                
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                click2.rect.center = event.pos  
        screen.fill(GREEN)
        
        main_menu2.update()
        main_menu2.draw(screen)
        click2_group.update()
        screen.blit(text_surface1_t, (50, 300))
        screen.blit(text_surface3_t, (50, 350))
        screen.blit(choosing_font_speed, (500, 400))
        screen.blit(choosing_font_shot, (500, 425))
        screen.blit(choosing_font_hp, (500, 450))
        screen.blit(choosing_font1_speed, (500, 525))
        screen.blit(choosing_font1_shot, (500, 550))
        screen.blit(choosing_font1_hp, (500, 575))
        screen.blit(choosing_font2_speed, (500, 675))
        screen.blit(choosing_font2_shot, (500, 700))
        screen.blit(choosing_font2_hp, (500, 725))
        screen.blit(choosing_font3_speed, (500, 825))
        screen.blit(choosing_font3_shot, (500, 850))
        screen.blit(choosing_font3_hp, (500, 875))
        pygame.display.flip()
        
        while start2_tank:
            back_t.update()
            click2_group.update()
            for event in pygame.event.get():  # для события происходящего в окне

                if event.type == pygame.QUIT:  # если событие выход, то
                    pygame.quit()  # остановка главного цикла программы
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    click2.rect.center = event.pos         
            pressed_keys = pygame.key.get_pressed()
            
            text_surface_t = game_over.render('Game Over! Continue?', True, RED )
            text_surface2_t = game_over.render('to continue press "y"', True, RED )
            text_surface3_t = game_score.render('to change tank press LSHIFT', True, RED )

            # Вывод текста на экран
            screen.blit(text_surface_t, (50, 300))
            screen.blit(text_surface2_t, (50, 350))
            screen.blit(text_surface3_t, (50, 400))
            score = 0
            if pressed_keys[K_ESCAPE]:
                pygame.quit()
            elif pressed_keys[K_y]:
                hp_player = hp_counter
                # перезапуск при столкновении
                start_tank = True
                tank.rect.center = (WIDTH / 2, HEIGHT - 30)
                hp_tank.rect.center = (WIDTH / 2, HEIGHT -140) # вовращение игрока
                for mob_tank in mob_list_tank:                  # возвращение мобов
                    mob_tank.rect.center = (random.randrange(60, 540), random.randrange(-500, -50))
            
            hits_to_main_t = pygame.sprite.spritecollide(back_to_main_t, click2_group, False)
            if hits_to_main_t:
                start2_tank = False
                click2.rect.center = (0, 0)
                
            back_t.draw(screen)
            click2_group.draw(screen)
            pygame.display.flip()  # переворот экрана (очень важно)
                
            while start_tank:
                col_hp = BLACK
                counter += 1
                fpsClock.tick(FPS)
                
                for event in pygame.event.get():  # для события происходящего в окне

                            if event.type == pygame.QUIT:  # если событие выход, то
                                pygame.quit()  # остановка главного цикла программы
                pressed_keys = pygame.key.get_pressed()
                all_sprites_tank.update()
                
                hits = pygame.sprite.spritecollide(tank, mobs_tank, False)
                if hits and counter % 15:
                    hp_player = hp_player - 1

                hits1 = pygame.sprite.spritecollide(tank, mob_bullets_group, False)
                if hits1:
                    hp_player = hp_player - 5
                
                if hp_player > ct3:
                    col_hp = BLACK
                else:
                    col_hp = RED
                
                if hp_player <= 0:
                    hp_player = 0
                    start_tank = False
                    start2_tank = True
                
                screen.fill(BLACK)
                if pressed_keys[K_ESCAPE]:
                    pygame.quit()
                
                all_sprites_tank.draw(screen)
                hp_surface_tank = game_score.render(f'Hp: {hp_player}', True, col_hp, WHITE)
                score_surface_tank = game_score.render(f'Score: {score}', True, BLACK, WHITE)
                score_surface_record_tank = game_score.render(f'Score record: {score_record}', True, BLACK, WHITE)
                screen.blit(score_surface_tank, (500, 0))
                screen.blit(score_surface_record_tank, (150, 0))
                screen.blit(hp_surface_tank, (700, 975))

                pygame.display.flip()


pygame.quit()


