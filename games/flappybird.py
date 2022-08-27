import pygame
from sys import exit
from random import randint


class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        bird0 = pygame.image.load('./games/graphics/flappybird/bird0.png').convert_alpha()
        bird1 = pygame.image.load('./games/graphics/flappybird/bird1.png').convert_alpha()
        bird2 = pygame.image.load('./games/graphics/flappybird/bird2.png').convert_alpha()
        self.bird_animation = [bird0, bird1, bird2]
        self.bird_index = 0

        self.image = self.bird_animation[self.bird_index]
        self.rect = self.image.get_rect(center = (50, 256))
        self.gravity = 0

    
    def apply_gravity(self):
        self.gravity += 0.5
        self.rect.y += self.gravity
        if self.rect.bottom >= 400:
            self.rect.bottom = 400
        if self.rect.top <= 0:
            self.rect.top = 0


    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.gravity = -5
            self.image = pygame.transform.rotate(self.image, 20)
        elif self.rect.bottom < 400:
            self.image = pygame.transform.rotate(self.image, -20)


    def animation(self):
        self.bird_index += 0.1
        if self.bird_index >= len(self.bird_animation):
            self.bird_index = 0
        self.image = self.bird_animation[int(self.bird_index)]


    def update(self):
        self.apply_gravity()
        self.animation()
        self.player_input()
        

class Tube(pygame.sprite.Sprite):
    def __init__(self, type, y_pos):
        super().__init__()
        
        self.type = type
        self.image = pygame.image.load('./games/graphics/flappybird/tube.png').convert_alpha()

        if self.type == 'top':
            self.top = pygame.image.load('./games/graphics/flappybird/tubebottomtop.png').convert_alpha()
            self.rect = self.image.get_rect(midbottom = (300, y_pos))
        else:
            self.bottom = pygame.image.load('./games/graphics/flappybird/tubebottomdown.png').convert_alpha()
            self.rect = self.image.get_rect(midtop = (300, y_pos))


    def destroy(self):
        if self.rect.x <= -100:
            self.kill()

    
    def point(self):
        global score
        if self.rect.right == 50:
            score += 0.5
            pygame.mixer.Sound('./games/audio/flappybird/point.wav').play()


    def update(self):
        if self.type == 'top':
            screen.blit(self.top, (self.rect.bottomleft[0], self.rect.bottomleft[1] - 20))
        else:
            screen.blit(self.bottom, self.rect.topleft)
        self.rect.x -= 1
        self.destroy()
        self.point()


def collision_sprite():
    if pygame.sprite.spritecollide(bird.sprite, tube, False):
        pygame.mixer.Sound('./games/audio/flappybird/hit.wav').play()
        return False
    else:
        return True


pygame.init()
screen = pygame.display.set_mode((288, 512))
pygame.display.set_caption('Flappy Bird')
icon = pygame.image.load('./games/graphics/flappybird/bird0.png').convert_alpha()
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
game_active = True
score = 0
font = pygame.font.SysFont('Verdana', 32, True)

# Background
bg_surf = pygame.image.load('./games/graphics/flappybird/background.png').convert()
ground_surf = pygame.image.load('./games/graphics/flappybird/ground.png').convert()
ground_surf = pygame.transform.scale(ground_surf, (500, 112))
ground_rect = ground_surf.get_rect(topleft = (0, 400))

# Groups
bird = pygame.sprite.GroupSingle()
bird.add(Bird())

tube = pygame.sprite.Group()

# Timer
tube_timer = pygame.USEREVENT + 1
pygame.time.set_timer(tube_timer, 3500)

# Game over
gameover = pygame.image.load('./games/graphics/flappybird/gameover.png').convert_alpha()
gameover_rect = gameover.get_rect(center = (144, 50))
playbutton = pygame.image.load('./games/graphics/flappybird/playbutton.png').convert_alpha()
playbutton_rect = playbutton.get_rect(center = (144, 160))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
        if game_active:
            if event.type == tube_timer:
                spawn = randint(20, 220)
                tube.add(Tube('top', spawn))
                tube.add(Tube('bottom', spawn + 110))
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.Sound('./games/audio/flappybird/sfx_wing.wav').play()
        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if playbutton_rect.collidepoint(event.pos):
                    tube.empty()
                    game_active = True
                    score = 0
                    bird.sprite.rect.center = (50, 256)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    tube.empty()
                    game_active = True
                    score = 0
                    bird.sprite.rect.center = (50, 256)

    if game_active:
        screen.blit(bg_surf, (0,0))
        tube.draw(screen)
        tube.update()
        screen.blit(ground_surf, ground_rect)
        ground_rect.x -= 1

        if ground_rect.x < -105:
            ground_rect.x = 0

        score_surf = font.render(f'{int(score)}', True, 'white')
        score_rect = score_surf.get_rect(center = (144, 50))
        screen.blit(score_surf, score_rect)

        bird.draw(screen)
        bird.update()

        game_active = collision_sprite()
    else:
        final_score_surf = font.render(f'Score: {int(score)}', True, 'white')
        final_score_rect = final_score_surf.get_rect(center = (144, 100))

        screen.blit(gameover, gameover_rect)
        screen.blit(final_score_surf, final_score_rect)
        screen.blit(playbutton, playbutton_rect)

    pygame.display.update()
    clock.tick(60)