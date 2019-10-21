import game_framework
from pico2d import *
import main_state

name = "PauseState2"
image = None

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)



class Boy:
    def __init__(self):
        self.x, self.y = main_state.boy.x, main_state.boy.y
        self.frame = main_state.boy.frame
        self.image = load_image('run_animation.png')
        self.dir = 1

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir
        if self.x >= 800:
            self.dir = -1
        elif self.x <= 0:
            self.dir = 1

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

def enter():
    global image1
    image1 = load_image('pause.png')
    global boy, grass
    boy = Boy()
    grass = Grass()
    pass


def exit():
    global image1
    del(image1)
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
                game_framework.pop_state()
    pass
blink = 0
def draw():
    global blink
    clear_canvas()
    grass.draw()
    boy.draw()
    if blink <= 80:
        image1.draw(400, 300, 500, 500)
    elif blink == 160:
        blink = 0
    blink += 1
    update_canvas()
    update_canvas()
    pass



def update():
    pass


def pause():
    pass


def resume():
    pass
