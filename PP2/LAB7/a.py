import pygame
import datetime

pygame.init()
screen = pygame.display.set_mode((500, 400))
running = True
is_blue = True


clock = pygame.time.Clock()
main_clock = pygame.image.load("images/clock/mainclock.png")
minute = pygame.image.load(("images/clock/rightarm.png"))
second = pygame.image.load(("images/clock/leftarm.png"))
main_clock = pygame.transform.scale(main_clock, (500, 400))

while running:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        exit()
        
        screen.fill((255, 255, 255))
        current_time = datetime.datetime.now()
        intmin = int(current_time.strftime("%M"))

        intsec = int(current_time.strftime("%S"))


        minute_angle = intmin * 6 * -1
        second_angle = intsec * 6 * -1

        minute = pygame.transform.rotate(minute, minute_angle)
        second = pygame.transform.rotate(second, second_angle)

        screen.blit(main_clock, main_clock.get_rect(center = screen.get_rect().center))
        screen.blit(minute, minute.get_rect(center = screen.get_rect().center))
        screen.blit(second, second.get_rect(center = screen.get_rect().center))
        pygame.display.flip()
        clock.tick(120)
pygame.quit()

    

