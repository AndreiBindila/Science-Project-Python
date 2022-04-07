from email.mime import image
import pygame
import random
from PIL import Image
from pygame.locals import(
    RLEACCEL,
    K_SPACE,
    KEYDOWN,
    K_ESCAPE,
    QUIT,
)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

bird_image_down = pygame.image.load("bird_down2.png")
bird_image_down = pygame.transform.scale(bird_image_down, (50, 50))


bird_image_up = pygame.image.load("bird_up.jpg")
bird_image_up = pygame.transform.scale(bird_image_up, (50, 50))
image = pygame.transform.rotate(image,45)


class Bird(pygame.sprite.Sprite):

    # check if we can rotate the image and do not load another
    def setBirdUp(self):
        self.surf = bird_image_up
        image()
        #self.surf.set_colorkey((255, 255, 255), RLEACCEL)
       

    def setBirdDown(self):
        self.surf = bird_image_down
        #self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        #self.rect = self.surf.get_rect()

    def __init__(self):
        super(Bird, self).__init__()
        self.setBirdDown()
        self.rect = self.surf.get_rect()
        self.rect.left = 50

    def update(self, pressed_keys):
        if pressed_keys[K_SPACE]:
            self.moveBirdUp()
        else:
            self.moveBirdDown()
 
    def moveBirdUp(self):
        self.setBirdUp()
        self.rect.move_ip(0, -5)

        if self.rect.top <= 0:
            self.rect.top = 0

    def moveBirdDown(self):
        self.setBirdDown()
        self.rect.move_ip(0, +2)
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(Cloud, self).__init__()
        self.surf = pygame.image.load("cloud.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH+100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )

    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()

# init pygame
pygame.init()
pygame.display.set_caption('SCIENCE PROJECT GAME')
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

ADDCLOUD = pygame.USEREVENT+2
pygame.time.set_timer(ADDCLOUD, 1000)

bird = Bird()
clouds = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(bird)

running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
        elif event.type == ADDCLOUD:
            new_cloud = Cloud()
            clouds.add(new_cloud)
            all_sprites.add(new_cloud)

    pressed_keys = pygame.key.get_pressed()
    clock = pygame.time.Clock()
    bird.update(pressed_keys)
    clouds.update()

    screen.fill((135, 206, 250))  
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    pygame.display.flip()
    clock.tick(30)