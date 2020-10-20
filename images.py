import pygame
import os
from functools import reduce
from colors import MINT_CREAM

asset_path = os.path.join(os.getcwd(), 'assets')
# paste_path = os.path.join(os.getcwd(), 'saved')

# if not os.path.exists(paste_path):
#     os.mkdir(paste_path)

# Types:
# man, capman, step_f, step_h, step_i
# step_c, step_s, step_t, block
# SIZES & INSTANCES
# CAP - 35:25
# MAN - Left= 35:45, Right= 35:45, CapMan= 35:45 (3)
# step_h - 40:20
# step_f - 40:25
# step_i - 40:20 - (3)
# block - 30:30, 35:35 (2)
# step_c - 40:20 - (1) - crunch - 40:30
# step_s - 35:25 - (1) - up - 35:15 and 35:30
# throne - 40:30
# img_dir = dict()
# img = pygame.image.load(os.path.join(asset_path, 'cap1.jpg'))


# for file in os.listdir(asset_path):
#     print(file)
#     if os.path.splitext(file)[1] == '.jpg':
#         img = pygame.image.load(os.path.join(asset_path, file))
#         for x in range(img.get_width()):
#             for y in range(img.get_height()):
#                 T = img.get_at((x, y))
#                 L = [i > 240 for i in T]
#                 if reduce(lambda x, y : x and y, L):
#                     img.set_at((x, y), MINT_CREAM)

#     pygame.image.save(img, os.path.join(paste_path, file))

man_dir = dict()
man_left = pygame.image.load(os.path.join(asset_path, 'left.jpg'))
man_right = pygame.image.load(os.path.join(asset_path, 'right.jpg'))

man_dir['left'] = pygame.transform.scale(man_left, (35, 45))
man_dir['right'] = pygame.transform.scale(man_right, (35, 45))

# Man Caps:
cap1 = pygame.transform.scale(pygame.image.load(os.path.join(asset_path, 'capman1.jpg')), (35, 45))
cap2 = pygame.transform.scale(pygame.image.load(os.path.join(asset_path, 'capman2.jpg')), (35, 45))
cap3 = pygame.transform.scale(pygame.image.load(os.path.join(asset_path, 'capman3.jpg')), (35, 45))

man_caps = [cap3, cap2, cap1, cap2]
man_dir['caps'] = man_caps

