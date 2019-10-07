from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

destination_x, destination_y, character_x, character_y, temp_x, temp_y = 0, 0, 0, 0, 0, 0


def handle_events():
    global running
    global x, y
    global destination_x, destination_y, temp_x, temp_y, character_x, character_y, i
    k = 0
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
            i = 0

    pass


open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
cursor = load_image('hand_arrow.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
direction = 0
frame = 0
i = 0
hide_cursor()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    cursor.clip_draw(0, 0, 100, 100, x, y)

    if i < 100:
        t = i / 100
        character_x = (1 - t) * temp_x + t * destination_x
        character_y = (1 - t) * temp_y + t * destination_y
        frame = (frame + 1) % 8
        i = i + 2
        delay(0.01)




    if temp_x < destination_x:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, character_x - 30, character_y + 45)
    elif temp_x >= destination_x:
        character.clip_draw(frame * 100, 0, 100, 100, character_x - 30, character_y + 45)

    update_canvas()
    handle_events()

close_canvas()




