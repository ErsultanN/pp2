import pygame
from pygame import mixer

pygame.init()
mixer.init()
clock = pygame.time.Clock()
FPS = 60

screen = pygame.display.set_mode((424, 780))


play_images = [pygame.image.load("images/music1/song4.png"), pygame.image.load("images/music1/song5.png"), pygame.image.load("images/music1/song6.png")]
pause_images = [pygame.image.load("images/music1/song1.png"), pygame.image.load("images/music1/song2.png"), pygame.image.load("images/music1/song3.png")]

running = True
i = 0
music = ['basta.mp3', 'bum.mp3', 'inna.mp3']

def start(i):
    mixer.music.load(music[i])
    mixer.music.set_volume(0.3)
    mixer.music.play()

start(i)
space = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if space == False:
                mixer.music.pause()
                space = True
            else:
                mixer.music.unpause()
                space = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            if i == 2:
                i = 0
            else:
                i = i + 1
                start(i)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            if i == 0:
                i = 2
            else:
                i = i - 1
                start(i)

    screen.fill((255, 255, 255))
    # screen.blit(background_image, background_image.get_rect(center=screen.get_rect().center))

    if space:
        screen.blit(pause_images[i], (0, 0))
    else:
        screen.blit(play_images[i], (0, 0))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
