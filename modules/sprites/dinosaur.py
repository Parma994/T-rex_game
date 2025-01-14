import pygame

'''공룡'''


class Dinosaur(pygame.sprite.Sprite):
    def __init__(self, image_path, position=(40, 147)):
        pygame.sprite.Sprite.__init__(self)
        # 모든 그림 가져오기
        self.images = []
        image = pygame.image.load(image_path[0])
        for i in range(5):
            self.images.append(pygame.transform.scale(image.subsurface((i * 88, 0), (88, 95)), (44, 47)))
        image = pygame.image.load(image_path[1])
        for i in range(2):
            self.images.append(pygame.transform.scale(image.subsurface((i * 118, 0), (118, 95)), (59, 47)))
        self.image_idx = 0
        self.image = self.images[self.image_idx]
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.bottom = position
        self.mask = pygame.mask.from_surface(self.image)
        # 필요한 변수들 정의
        self.init_position = position
        self.refresh_rate = 2
        self.refresh_counter = 0
        self.speed = 13
        self.gravity = 0.7
        self.is_jumping = False
        self.is_ducking = False
        self.is_dead = False
        self.movement = [0, 0]

    '''점프동작'''

    def jump(self, sounds):
        if self.is_dead or self.is_jumping:
            return
        sounds['jump'].play()
        self.is_jumping = True
        self.movement[1] = -1 * self.speed

    '''머리 숙이기 동작'''

    def duck(self):
        if self.is_jumping or self.is_dead:
            return
        self.is_ducking = True

    '''머리 숙이지 않기 동작'''

    def unduck(self):
        self.is_ducking = False

    '''죽었다'''

    def die(self, sounds):
        if self.is_dead:
            return
        sounds['die'].play()
        self.is_dead = True
        
    '''스크린에 공룡 그리기'''

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    '''현재 상태의 그림 불러오기'''

    def load_image(self):
        self.image = self.images[self.image_idx]
        rect = self.image.get_rect()
        rect.left, rect.top = self.rect.left, self.rect.top
        self.rect = rect
        self.mask = pygame.mask.from_surface(self.image)

    '''공룡 업데이트'''

    def update(self):
        if self.is_dead:
            self.image_idx = 4
            self.load_image()
            return
        if self.is_jumping:
            self.movement[1] += self.gravity
            self.image_idx = 0
            self.load_image()
            self.rect = self.rect.move(self.movement)
            if self.rect.bottom >= self.init_position[1]:
                self.rect.bottom = self.init_position[1]
                self.is_jumping = False
        elif self.is_ducking:
            if self.refresh_counter % self.refresh_rate == 0:
                self.refresh_counter = 0
                self.image_idx = 5 if self.image_idx == 6 else 6
                self.load_image()
        else:
            if self.refresh_counter % self.refresh_rate == 0:
                self.refresh_counter = 0
                if self.image_idx == 1:
                    self.image_idx = 2
                elif self.image_idx == 2:
                    self.image_idx = 3
                else:
                    self.image_idx = 1
                self.load_image()
        self.refresh_counter += 1
