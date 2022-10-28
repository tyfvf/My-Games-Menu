import pygame
from random import randint

class Plataforma(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface((70, 20))
        self.rect = self.image.get_rect(center = (randint(70, 530), randint(-100, 0)))
        self.count = 0

    
    def grab(self):
        global score
        if self.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            jones_rect.bottom = self.rect[1]
            jones_rect.x = self.rect[0]
            if self.count == 0:
                score += y_velocity
            self.count += 1


    def destroy(self):
        if self.rect.y > 700:
            self.kill()


    def update(self):
        self.rect.y += y_velocity
        self.grab()
        self.destroy()


pygame.init()
display = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Whip Game?')
running = True
clock = pygame.time.Clock()
font = pygame.font.SysFont('Comic Sans', 32, True)

jones = pygame.image.load('./games/graphics/arte.png').convert_alpha()
jones_rect = jones.get_rect(center = (30, 570))

plataforma_group = pygame.sprite.Group()

plataforma_group.add(Plataforma())

y_velocity = 1
x_velocity = 0

score = 0

plataforma_timer = pygame.USEREVENT + 1
pygame.time.set_timer(plataforma_timer, 1500)

difficulty_timer = pygame.USEREVENT + 2
pygame.time.set_timer(difficulty_timer, 10000)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == plataforma_timer:
            plataforma_group.add(Plataforma())

        if event.type == difficulty_timer:
            y_velocity += 1


    display.fill('white')
    display.blit(jones, jones_rect)
    render = font.render(f'{score}', True, 'black')
    score_rect = render.get_rect(center = (300, 50))
    display.blit(render, score_rect)
    plataforma_group.draw(display)
    plataforma_group.update()
    jones_rect.y += y_velocity

    if jones_rect.y > 700:
        pygame.quit()

    pygame.draw.line(display, 'brown', (jones_rect.midright[0] - 3, jones_rect.midright[1] + 7), (pygame.mouse.get_pos()), 3)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
