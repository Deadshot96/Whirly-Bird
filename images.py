import pygame
import os

asset_path = os.path.join(os.getcwd(), 'assets')

# Types:
# man, capman, step_f, step_h, step_i
# step_c, step_s, step_t, block
# SIZES & INSTANCES
# CAP - 35:25
# MAN - Left= 40:40, Right= 40:40, CapMan= 35:45 (3)
# step_h - 40:20
# step_f - 40:25
# step_i - 40:20 - (3)
# block - 30:30, 35:35 (2)
# step_c - 40:20 - (1) - crunch - 40:30
# step_s - 35:25 - (1) - up - 35:15 and 35:30
# throne - 40:30
img_dir = dict()
img = pygame.image.load(os.path.join(asset_path, 'cap1.jpg'))
