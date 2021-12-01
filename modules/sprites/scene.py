import pygame
import os

from pygame.surface import Surface

from .rsa import encrypt, decrypt

'''바닥'''


class Ground(pygame.sprite.Sprite):
    def __init__(self, image_path, position):
        pygame.sprite.Sprite.__init__(self)
        # 그림 가져오기
        self.image_0 = pygame.image.load(image_path)
        self.rect_0 = self.image_0.get_rect()
        self.rect_0.left, self.rect_0.bottom = position
        self.image_1 = pygame.image.load(image_path)
        self.rect_1 = self.image_1.get_rect()
        self.rect_1.left, self.rect_1.bottom = self.rect_0.right, self.rect_0.bottom
        # 필요한 인자 정의
        self.speed = -10

    '''바닥 업데이트'''

    def update(self):
        self.rect_0.left += self.speed
        self.rect_1.left += self.speed
        if self.rect_0.right < 0:
            self.rect_0.left = self.rect_1.right
        if self.rect_1.right < 0:
            self.rect_1.left = self.rect_0.right

    '''화면에 바닥 그리기'''

    def draw(self, screen):
        screen.blit(self.image_0, self.rect_0)
        screen.blit(self.image_1, self.rect_1)


'''구름'''


class Cloud(pygame.sprite.Sprite):
    def __init__(self, image_path, position):
        pygame.sprite.Sprite.__init__(self)
        # 그림 가져오기
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        # 필요한 인자 정의
        self.speed = -1

    '''화면에 그림 그리기'''

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    '''구름 업데이트'''

    def update(self):
        self.rect = self.rect.move([self.speed, 0])
        if self.rect.right < 0:
            self.kill()


'''점수판'''


class Scoreboard(pygame.sprite.Sprite):
    def __init__(self, image_path, position, size=(11, 13), is_highest=False, is_second=False, is_third=False,
                 bg_color=None):
        pygame.sprite.Sprite.__init__(self)
        # 그림 가져오기
        self.images = []
        image = pygame.image.load(image_path)
        for i in range(12):
            self.images.append(pygame.transform.scale(image.subsurface((i * 20, 0), (20, 24)), size))
        if is_highest:
            self.image = pygame.Surface((size[0] * 8, size[1]))
        else:
            self.image = pygame.Surface((size[0] * 5, size[1]))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        # 몇몇 필요한 변수
        self.is_highest = is_highest
        self.is_second = is_second
        self.is_third = is_third
        self.bg_color = bg_color
        self.score = '00000'
        self.highest_score = '00000'
        self.second_score = '00000'
        self.third_score = '00000'

    '''득점 설정'''

    def set(self, score):
        self.score = str(score).zfill(5)

    '''ranker board 득점 설정'''

    def set_ranker(self, highest_score, second_score, third_score):
        self.highest_score = str(highest_score).zfill(5)
        self.second_score = str(second_score).zfill(5)
        self.third_score = str(third_score).zfill(5)

    '''1,2,3등 점수 불러오기'''

    def get_rank_score(self):
        self.highest_score, self.second_score, self.third_score = 0, 0, 0
        if os.path.exists("T-rex.txt"):
            rank_file = open("T-rex.txt", 'r')
            rankers = rank_file.readlines()
            if len(rankers) >= 1:
                self.highest_score = decrypt(int(rankers[0].strip()))
            if len(rankers) >= 2:
                self.second_score = decrypt(int(rankers[1].strip()))
            if len(rankers) >= 3:
                self.third_score = decrypt(int(rankers[2].strip()))
            rank_file.close()
        return self.highest_score, self.second_score, self.third_score

    '''1,2,3등 점수 저장'''

    def save_rank_score(self, score):
        prev_highest_score, prev_second_score, prev_third_score = self.get_rank_score()
        if score > prev_highest_score:
            self.third_score = prev_second_score
            self.second_score = prev_highest_score
            self.highest_score = score
        elif score > prev_second_score:
            self.third_score = prev_second_score
            self.second_score = score
        elif score > prev_third_score:
            self.third_score = score
        rankers = [encrypt(self.highest_score), encrypt(self.second_score), encrypt(self.third_score)]
        rankFile = open("T-rex.txt", 'w')
        for i in range(0, 3):
            rankFile.write(f"{rankers[i]}\n")
        rankFile.close()

    '''화면에 그리기'''

    def draw(self, screen):
        self.image.fill(self.bg_color)
        if self.images:
            digital_image = self.images[0]
            for idx, digital in enumerate(list(self.score)):
                digital_image = self.images[int(digital)]
                if self.is_highest:
                    self.image.blit(digital_image, ((idx + 3) * digital_image.get_rect().width, 0))
                else:
                    self.image.blit(digital_image, (idx * digital_image.get_rect().width, 0))
            if self.is_highest and digital_image is not None:
                self.image.blit(self.images[-2], (0, 0))
                self.image.blit(self.images[-1], (digital_image.get_rect().width, 0))
            screen.blit(self.image, self.rect)
