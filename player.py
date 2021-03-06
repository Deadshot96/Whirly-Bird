from images import man_dir
from settings import GW_WIDTH, GW_HEIGHT

class Player:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 35
        self.h = 45
        self.isCapped = False
        self.cap_animation_count = 0
        self.current_img = man_dir['left']
        self.vx = 0
        self.vy = 0
        self.ay = 1

    
    def draw(self, win):
        # if self.vx >= 0:
        #     img = man_dir['right']
        # else:
        #     img = man_dir['left']
        rect = self.current_img.get_rect()
        rect.center = self.x, self.y
        win.blit(self.current_img, rect)

    def move(self):
        self.x += self.vx
        self.y += self.vy

        if self.x + self.w // 2 < 0:
            self.x = GW_WIDTH - self.w // 2
        elif self.x - self.w // 2 > GW_WIDTH:
            self.x = -self.w // 2

        if self.y + self.h // 2 >= GW_HEIGHT:
            self.jump()

        self.vy = min(4, self.vy + self.ay)

    def push_right(self):
        self.vx = 3
        self.current_img = man_dir['right']

    def push_left(self):
        self.vx = -3
        self.current_img = man_dir['left']

    def stop_push(self):
        self.vx = 0

    def jump(self):
        self.vy = -16

    def update_velocity(self, vel):
        pass

