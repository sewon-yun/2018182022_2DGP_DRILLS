import game_framework
from pico2d import *

import game_world

PIXEL_PER_METER = (10.0 / 0.1)  # 10 pixel 10 cm
RUN_SPEED_KMPH = 50.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# fill expressions correctly
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14

(FIRST, SECOND, THIRD, FOURTH, FIFTH, SIXTH, SEVENTH, EIGHTTH,
 NINTH, TENTH, ELEVENTH, TWELFTH, THIRTEENTH, FOURTEENTH) = range(14)

frameX, frameY = 0, 0

frameX_location_table = {
    FIRST: 0, SECOND: 183, THIRD: 366, FOURTH: 549, FIFTH: 732,
    SIXTH: 0, SEVENTH: 183, EIGHTTH: 366, NINTH: 549, TENTH: 732,
    ELEVENTH: 0, TWELFTH: 183, THIRTEENTH: 366, FOURTEENTH: 549
}
frameY_location_table = {
    FIRST: 336, SECOND: 336, THIRD: 336, FOURTH: 336, FIFTH: 336,
    SIXTH: 168, SEVENTH: 168, EIGHTTH: 168, NINTH: 168, TENTH: 168,
    ELEVENTH: 0, TWELFTH: 0, THIRTEENTH: 0, FOURTEENTH: 0
}

class Bird:
    def __init__(self):
        self.x, self.y = 0, 300
        self.frameX, self.frameY = 0, 0
        self.image = load_image('bird_animation.png')
        self.dir = 1
        self.velocity = RUN_SPEED_PPS
        self.frame = 0

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14
        self.frameX = frameX_location_table[int(self.frame)]
        self.frameY = frameY_location_table[int(self.frame)]

        self.x += self.velocity * game_framework.frame_time

        if self.dir == 1:
            self.velocity = RUN_SPEED_PPS
            if self.x > 1500:
                self.dir = -1
        else:
            self.velocity = -RUN_SPEED_PPS
            if self.x < 100:
                self.dir = 1
        pass
    def draw(self):
        if self.dir == -1:
            self.image.clip_composite_draw(self.frameX, self.frameY, 183, 168,
                                           0.0, 'h', self.x, self.y, 100, 100)
        else:
            self.image.clip_draw(self.frameX, self.frameY, 183, 168, self.x, self.y, 100, 100)



