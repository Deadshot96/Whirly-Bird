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
# MAN - Left= 40:40, Right= 40:40, CapMan= 35:45 (3)
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