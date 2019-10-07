from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

destination_x, destination_y, character_x, character_y, temp_x, temp_y = 0, 0, 0, 0, 0, 0

def handle_events():
    global running
    global x, y
    global destination_x, destination_y, temp_x, temp_y, character_x, character_y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, KPU_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_MOUSEBUTTONDOWN:
            destination_x, destination_y = event.x, KPU_HEIGHT - 1 - event.y
            temp_x, temp_y = character_x, character_y
            draw_line((temp_x, temp_y), (destination_x, destination_y))
    pass

def draw_line(p1, p2):
    global character_x, character_y, frame
    for i in range(0, 100 + 1, 2):
        t = i / 100
        character_x = (1 - t) * p1[0] + t * p2[0]
        character_y = (1 - t) * p1[1] + t * p2[1]
        frame = (frame + 1) % 8
    pass

open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
cursor = load_image('hand_arrow.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
direction = 0
frame = 0
hide_cursor()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    cursor.clip_draw(0, 0, 100, 100, x, y)
    if temp_x < destination_x:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, character_x, character_y)
    elif temp_x >= destination_x:
        character.clip_draw(frame * 100, 0, 100, 100, character_x, character_y)
    update_canvas()

    handle_events()

close_canvas()




