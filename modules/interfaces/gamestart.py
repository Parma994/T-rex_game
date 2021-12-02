import sys
import pygame
import os

from ..sprites import Dinosaur
from ..sprites import encrypt, decrypt

'''게임시작 인터페이스'''


def show_game_start_interface(screen, sounds, cfg):
    dino = Dinosaur(cfg.IMAGE_PATHS['dino'])
    ground = pygame.image.load(cfg.IMAGE_PATHS['ground']).subsurface((0, 0), (83, 19))
    rect = ground.get_rect()
    rect.left, rect.bottom = cfg.SCREENSIZE[0] / 20, cfg.SCREENSIZE[1]
    clock = pygame.time.Clock()
    press_flag = False

    text_font = pygame.font.SysFont(['imprintshadow'], 20, True, False)
    highest_score, second_score, third_score = 0, 0, 0
    if os.path.exists("T-rex.txt"):
        rank_file = open("T-rex.txt", 'r')
        rankers = rank_file.readlines()
        if len(rankers) >= 1:
            highest_score = int(rankers[0].strip())
        if len(rankers) >= 2:
            second_score = int(rankers[1].strip())
        if len(rankers) >= 3:
            third_score = int(rankers[2].strip())
        rank_file.close()
    text1_title = text_font.render(f"1st  {decrypt(highest_score)}", True, (83, 83, 83))
    text1_rect = text1_title.get_rect()
    text1_rect.left, text1_rect.top = cfg.SCREENSIZE[0] * 0.8, cfg.SCREENSIZE[1] * 0.1
    text2_title = text_font.render(f"2nd {decrypt(second_score)}", True, (83, 83, 83))
    text2_rect = text2_title.get_rect()
    text2_rect.left, text2_rect.top = cfg.SCREENSIZE[0] * 0.8, cfg.SCREENSIZE[1] * 0.3
    text3_title = text_font.render(f"3rd {decrypt(third_score)}", True, (83, 83, 83))
    text3_rect = text1_title.get_rect()
    text3_rect.left, text3_rect.top = cfg.SCREENSIZE[0] * 0.8, cfg.SCREENSIZE[1] * 0.5

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    press_flag = True
                    dino.jump(sounds)
        dino.update()
        screen.fill(cfg.BACKGROUND_COLOR)
        screen.blit(ground, rect)
        dino.draw(screen)
        screen.blit(text1_title, text1_rect)
        screen.blit(text2_title, text2_rect)
        screen.blit(text3_title, text3_rect)
        pygame.display.update()
        clock.tick(cfg.FPS)
        if (not dino.is_jumping) and press_flag:
            return True
