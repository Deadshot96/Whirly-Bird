from images import man_dir

class Player:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 35
        self.h = 45
        self.isCapped = False
        self.cap_animation_count = 0
        self.vx = 0
        self.vy = 0
        self.ay = 0

    
    def draw(self, win):
        if self.vx >= 0:
            img = man_dir['right']
        else:
            img = man_dir['left']
        rect = img.get_rect()
        rect.center = self.x, self.y
        win.blit(img, rect)

    def move(self):
        pass

    def update_velocity(self, vel):
        pass

