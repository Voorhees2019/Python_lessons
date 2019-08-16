# моя первая игра пинг-понг на пайгейм(есть баг с ударом кубика о верх ракеток)
import pygame
import random


window_size = [800, 600]
min_x = 0
max_x = 800
min_y = 0
max_y = 600
bg_color = [0, 0, 0]
left_score = 0
right_score = 0
pos_left_paddle = [0, 250]
pos_right_paddle = [780, 250]
moving_paddle_step = 1
pos_center = [window_size[0]/2-2, 0]
pos_ball = [window_size[0]/2-10, window_size[1]/2-10]
game_over = True
ball_serving = True
ball_direction_x = 1
ball_direction_y = 1
ball_speed = 0.2
direction = random.choice(('left', 'right'))
#direction = 'right'
start_flag = 1
while start_flag == 1:
    pygame.init()
    screen = pygame.display.set_mode(window_size, pygame.FULLSCREEN)
    pygame.display.set_caption('My first PyGame PONG GAME')
    screen.fill(bg_color)
    paddle = pygame.image.load('paddle.jpg').convert()
    #scaled_paddle = pygame.transform.scale(paddle, (20, 100))
    ball = pygame.image.load('ball.jpg').convert()
    center = pygame.image.load('center.jpg').convert()


    while game_over == True:

        # management of the game
        font = pygame.font.SysFont('arial', 28)
        """by using the render method that belongs to our font object, supplying three arguments: the text to be rendered,
         whether or not it should be anti-aliased/должен ли он быть сглаженным (1=yes, 0=no), and the color of the text 
         (again in RGB format)"""
        text_surface = font.render('This is my first PyGame PONG game.', 1, [255, 0, 0])
        screen.blit(text_surface, (50, 50))
        text_surface = font.render('Use "W" and "S" to move left paddle.', 1, [255, 0, 0])
        screen.blit(text_surface, (50, 100))
        text_surface = font.render('Use "K_UP" and "K_DOWN" to move right paddle.', 1, [255, 0, 0])
        screen.blit(text_surface, (50, 150))
        text_surface = font.render('Use "SPACE" to start the new game and to serve the ball.', 1, [255, 0, 0])
        screen.blit(text_surface, (50, 200))
        text_surface = font.render('Use "Q" to end the new game and exit the program.', 1, [255, 0, 0])
        screen.blit(text_surface, (50, 250))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_SPACE]:
            game_over = False
            screen.fill(bg_color)
        elif pressed_keys[pygame.K_q]:
            start_flag = 0
            exit()

    a = 0
# ---------------------- main game --------------------
    while not game_over:
        # printing score
        font = pygame.font.SysFont('arial', 50)
        text_surface = font.render(str(left_score), 1, (255, 255, 255))
        text_left = screen.blit(text_surface, (window_size[0]/2-50, 20))
        text_surface = font.render(str(right_score), 1, (255, 255, 255))
        text_right = screen.blit(text_surface, (window_size[0]/2+30, 20))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        # q - exit the game
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_q]:
            start_flag = 0
            exit()

        # moving paddles
        if pressed_keys[pygame.K_w]:
            if pos_left_paddle[1] > min_y:
                pos_left_paddle[1] -= moving_paddle_step

        if pressed_keys[pygame.K_s]:
            if pos_left_paddle[1] < max_y - 100:
                pos_left_paddle[1] += moving_paddle_step

        if pressed_keys[pygame.K_UP]:
            if pos_right_paddle[1] > min_y:
                pos_right_paddle[1] -= moving_paddle_step

        if pressed_keys[pygame.K_DOWN]:
            if pos_right_paddle[1] < max_y - 100:
                pos_right_paddle[1] += moving_paddle_step

        # serving the ball
        if pressed_keys[pygame.K_SPACE] and ball_serving is True:
            ball_serving = False
            if direction == 'right':
                # make random ball direction
                ball_direction_x = random.randrange(2, 3)
                ball_direction_y = random.randrange(-3, 3)
                direction = 'left'
            elif direction == 'left':
                ball_direction_x = random.randrange(-2, -1)
                ball_direction_y = random.randrange(-3, 3)
                direction = 'right'

        # ball moving
        if ball_serving is not True:
            # hit the left paddle
            if pos_ball[0] <= (pos_left_paddle[0] + 20) and (pos_left_paddle[1] - 19) < pos_ball[1] < (
                    pos_left_paddle[1] + 99):
                ball_direction_x = -ball_direction_x
                if pressed_keys[pygame.K_w] or pressed_keys[pygame.K_s]:
                    ball_direction_y = random.randrange(2, 4)
                else:
                    ball_direction_y = random.randrange(0, 3)

            # hit the right paddle
            elif pos_ball[0] > (pos_right_paddle[0]-20) and (pos_right_paddle[1] - 19) < pos_ball[1] < (
                    pos_right_paddle[1] + 99):
                ball_direction_x = -ball_direction_x
                if pressed_keys[pygame.K_UP] or pressed_keys[pygame.K_DOWN]:
                    ball_direction_y = random. randrange(2, 4)
                else:
                    ball_direction_y = random.randrange(0, 3)

            # hit the top of screen
            elif pos_ball[1] <= min_y:
                ball_direction_y = -ball_direction_y

            # hit the bottom of screen
            elif pos_ball[1] >= max_y - 20:
                ball_direction_y = -ball_direction_y

            # ball crossed left field
            elif pos_ball[0] <= min_x:
                ball_serving = True
                direction = 'right'
                right_score += 1
                pygame.draw.rect(screen, (0, 0, 0), text_right)
            # ball crossed right field
            elif pos_ball[0] >= max_x:
                ball_serving = True
                left_score += 1
                direction = 'left'
                pygame.draw.rect(screen, (0, 0, 0), text_left)

            # move the ball
            pos_ball[0] = pos_ball[0] + ball_speed * ball_direction_x
            pos_ball[1] = pos_ball[1] + ball_speed * ball_direction_y
        else:
            if direction == 'right':
                pos_ball[0] = pos_left_paddle[0]+25
                pos_ball[1] = pos_left_paddle[1]+40
            elif direction == 'left':
                pos_ball[0] = pos_right_paddle[0]-25
                pos_ball[1] = pos_right_paddle[1]+40


        screen.fill(bg_color)
        screen.blit(center, pos_center)
        screen.blit(ball, pos_ball)
        screen.blit(paddle, pos_left_paddle)
        screen.blit(paddle, pos_right_paddle)
        #pygame.display.update()


# if __name__ == '__main__':
#     main()