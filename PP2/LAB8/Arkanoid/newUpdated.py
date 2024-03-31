import pygame
import random

pygame.init()

W, H = 1200, 800
FPS = 60

screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
clock = pygame.time.Clock()
done = False
bg = (0, 0, 0)

# Paddle
paddleW = 150
paddleH = 25
paddleSpeed = 20
paddle = pygame.Rect(W // 2 - paddleW // 2, H - paddleH - 30, paddleW, paddleH)

# Ball
ballRadius = 20
ballSpeed = 6
ball_rect = int(ballRadius * 2 ** 0.5)
ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)
dx, dy = 1, -1

# Game score
game_score = 0
game_score_fonts = pygame.font.SysFont('comicsansms', 40)
game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (0, 0, 0))
game_score_rect = game_score_text.get_rect()
game_score_rect.center = (210, 20)

# Catching sound
collision_sound = pygame.mixer.Sound('catch.mp3')


def detect_collision(dx, dy, ball, rect, is_unbreakable=False):
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top

    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    if delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx

    if is_unbreakable:
        dx = -dx
        dy = -dy

    return dx, dy


#Block settings
block_list = [pygame.Rect(10 + 120 * i, 50 + 70 * j, 100, 50) for i in range(10) for j in range(4)]
color_list = [(random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)) for _ in range(10 * 4)]

#Unbreakable bricks
unbreakable_block_list = [pygame.Rect(10 + 120 * i, 50 + 70 * j, 100, 50) for i in range(5) for j in range(2)]
unbreakable_color_list = [(100, 100, 100) for _ in range(len(unbreakable_block_list))]

#Bonus bricks
bonus_block_list = [pygame.Rect(10 + 120 * i, H - 100, 100, 50) for i in range(2)]  #Two bonus bricks at the bottom
bonus_color_list = [(0, 255, 0) for _ in range(len(bonus_block_list))]

#Game over Screen
losefont = pygame.font.SysFont('comicsansms', 40)
losetext = losefont.render('Game Over', True, (255, 255, 255))
losetextRect = losetext.get_rect()
losetextRect.center = (W // 2, H // 2)

#Win Screen
winfont = pygame.font.SysFont('comicsansms', 40)
wintext = losefont.render('You win yay', True, (0, 0, 0))
wintextRect = wintext.get_rect()
wintextRect.center = (W // 2, H // 2)

#Restart Button
restartfont = pygame.font.SysFont('comicsansms', 40)
restarttext = restartfont.render('Restart', True, (255, 255, 255))
restarttextRect = restarttext.get_rect()
restarttextRect.center = (W // 2, H // 2 + 50)


def restart_game():
    global paddle, ball, dx, dy, game_score, paddleW, block_list, color_list, unbreakable_block_list, unbreakable_color_list, bonus_block_list, bonus_color_list, ballSpeed
    paddle = pygame.Rect(W // 2 - paddleW // 2, H - paddleH - 30, paddleW, paddleH)
    ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)
    dx, dy = 1, -1
    game_score = 0
    ballSpeed = 6
    block_list = [pygame.Rect(10 + 120 * i, 50 + 70 * j, 100, 50) for i in range(10) for j in range(4)]
    color_list = [(random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)) for _ in range(10 * 4)]
    unbreakable_block_list = [pygame.Rect(10 + 120 * i, 50 + 70 * j, 100, 50) for i in range(5) for j in range(2)]
    unbreakable_color_list = [(100, 100, 100) for _ in range(len(unbreakable_block_list))]
    bonus_block_list = [pygame.Rect(10 + 120 * i, H - 100, 100, 50) for i in range(2)]  #Two bonus bricks at the bottom
    bonus_color_list = [(0, 255, 0) for _ in range(len(bonus_block_list))]


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if restarttextRect.collidepoint(event.pos):
                restart_game()

    screen.fill(bg)

    [pygame.draw.rect(screen, color_list[color], block) for color, block in enumerate(block_list)]  #drawing blocks
    [pygame.draw.rect(screen, unbreakable_color_list[color], block) for color, block in
     enumerate(unbreakable_block_list)]  #unbreakable blocks
    [pygame.draw.rect(screen, bonus_color_list[color], block) for color, block in
     enumerate(bonus_block_list)]  #bonus blocks

    pygame.draw.rect(screen, pygame.Color(255, 255, 255), paddle)
    pygame.draw.circle(screen, pygame.Color(255, 0, 0), ball.center, ballRadius)

    #Ball movement
    ball.x += ballSpeed * dx
    ball.y += ballSpeed * dy

    if ball.centerx < ballRadius or ball.centerx > W - ballRadius:
        dx = -dx
    if ball.centery < ballRadius + 50:
        dy = -dy
    if ball.colliderect(paddle) and dy > 0:
        dx, dy = detect_collision(dx, dy, ball, paddle)

    hitIndex = ball.collidelist(block_list + unbreakable_block_list + bonus_block_list)

    if hitIndex != -1:
        if hitIndex < len(block_list):
            hitRect = block_list.pop(hitIndex)
            hitColor = color_list.pop(hitIndex)
            dx, dy = detect_collision(dx, dy, ball, hitRect)
            game_score += 1
            collision_sound.play()
        elif hitIndex < len(block_list) + len(unbreakable_block_list):
            hitRect = unbreakable_block_list[hitIndex - len(block_list)]
            dx, dy = detect_collision(dx, dy, ball, hitRect, is_unbreakable=True)
        else:
            hitRect = bonus_block_list.pop(hitIndex - len(block_list) - len(unbreakable_block_list))
            hitColor = bonus_color_list.pop(hitIndex - len(block_list) - len(unbreakable_block_list))
            dx, dy = detect_collision(dx, dy, ball, hitRect)
            game_score += 5  #Increase score as a bonus
            paddleW += 10  #Increase paddle size as a bonus
            collision_sound.play()

    #Game score
    game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (255, 255, 255))
    screen.blit(game_score_text, game_score_rect)

    if ball.bottom > H:
        screen.fill((0, 0, 0))
        screen.blit(losetext, losetextRect)
        screen.blit(restarttext, restarttextRect)
    elif not len(block_list) and not len(bonus_block_list):
        screen.fill((255, 255, 255))
        screen.blit(wintext, wintextRect)
        screen.blit(restarttext, restarttextRect)

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddleSpeed
    if key[pygame.K_RIGHT] and paddle.right < W:
        paddle.right += paddleSpeed

    pygame.display.flip()
    clock.tick(FPS)

    #increase ball speed gradually
    ballSpeed += 0.01

    #shrink paddle gradually
    if paddleW > 50:
        paddleW -= 0.01
        paddle.width = paddleW

pygame.quit()
