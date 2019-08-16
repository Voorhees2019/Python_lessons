import random, pygame, sys

window_size = [800, 600]
min_x = 0
max_x = 800
min_y = 0
max_y = 600
snowflake_size = 50
bg_color = [255, 255, 255]
snowfall = []


class Snowflake():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.img = pygame.image.load('snowflake.jpg').convert_alpha()
        self.image = pygame.transform.scale(self.img, (snowflake_size, snowflake_size))
        self.speed_y = random.randint(1, 4)
        self.speed_x = random.randint(1, 3)

    def move_snowflake(self):
        self.y += self.speed_y
        if self.y >= max_y:
            self.y = (0-snowflake_size)
        direction_x = random.choice(('left', 'right'))
        if direction_x == 'left':
            self.x -= self.speed_x
            if self.x <= min_x:
                self.x = max_x - snowflake_size
        elif direction_x == 'right':
            self.x += self.speed_x
            if self.x >= max_x:
                self.x = min_x

    def draw_snowflake(self):
        screen.blit(self.image, (self.x, self.y))


def check_for_exit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def generate_snowfall(snowfall):
    for i in range(random.randint(20, 50)):
        snowfall.append(Snowflake(random.randint(0, 800), random.randint(0, 600)))


pygame.init()
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('Snowfall')
screen.fill(bg_color)
generate_snowfall(snowfall)
while 1:
    check_for_exit()
    for i in snowfall:
        i.move_snowflake()
        i.draw_snowflake()
        pygame.display.flip()