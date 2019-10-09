from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 1280, 1024
def handle_events():
    global running
    global x, y
    k = 0
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass


open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
point = load_image('hand_arrow.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
i = 0
frame = 0
turn = 1

p1 = ((random.randint(0, 1200)), (random.randint(200, 800)))
p2 = ((random.randint(0, 1200)), (random.randint(200, 800)))
p3 = ((random.randint(0, 1200)), (random.randint(200, 800)))
p4 = ((random.randint(0, 1200)), (random.randint(200, 800)))
p5 = ((random.randint(0, 1200)), (random.randint(200, 800)))
p6 = ((random.randint(0, 1200)), (random.randint(200, 800)))
p7 = ((random.randint(0, 1200)), (random.randint(200, 800)))
p8 = ((random.randint(0, 1200)), (random.randint(200, 800)))
p9 = ((random.randint(0, 1200)), (random.randint(200, 800)))
p10 = ((random.randint(0, 1200)), (random.randint(200, 800)))



while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)

    frame = (frame + 1) % 8

    point.clip_draw(0, 0, 100, 100, p1[0] + 20, p1[1] - 20, 30, 30)
    point.clip_draw(0, 0, 100, 100, p2[0] + 20, p2[1] - 20, 30, 30)
    point.clip_draw(0, 0, 100, 100, p3[0] + 20, p3[1] - 20, 30, 30)
    point.clip_draw(0, 0, 100, 100, p4[0] + 20, p4[1] - 20, 30, 30)
    point.clip_draw(0, 0, 100, 100, p5[0] + 20, p5[1] - 20, 30, 30)
    point.clip_draw(0, 0, 100, 100, p6[0] + 20, p6[1] - 20, 30, 30)
    point.clip_draw(0, 0, 100, 100, p7[0] + 20, p7[1] - 20, 30, 30)
    point.clip_draw(0, 0, 100, 100, p8[0] + 20, p8[1] - 20, 30, 30)
    point.clip_draw(0, 0, 100, 100, p9[0] + 20, p9[1] - 20, 30, 30)
    point.clip_draw(0, 0, 100, 100, p10[0] + 20, p10[1] - 20, 30, 30)


    # draw p1-p2
    if i < 100 and turn == 1:
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * p10[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p1[0] + (-3 * t ** 3 + 4 * t ** 2 + t) * p2[0] + (t ** 3 - t ** 2) * p3[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p10[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p1[1] + (-3 * t ** 3 + 4 * t ** 2 + t) * p2[1] + (t ** 3 - t ** 2) * p3[1]) / 2
        if p1[0] < p2[0]:
            character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        elif p1[0] >= p2[0]:
            character.clip_draw(frame * 100, 0, 100, 100, x, y)

    # draw p2-p3
    if i < 100 and turn == 2:
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * p1[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p2[0] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p3[0] + (t ** 3 - t ** 2) * p4[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p1[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p2[1] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p3[1] + (t ** 3 - t ** 2) * p4[1]) / 2
        if p2[0] < p3[0]:
            character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        elif p2[0] >= p3[0]:
            character.clip_draw(frame * 100, 0, 100, 100, x, y)

    # draw p3-p4
    if i < 100 and turn == 3:
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * p2[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p3[0] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p4[0] + (t ** 3 - t ** 2) * p1[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p2[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p3[1] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p4[1] + (t ** 3 - t ** 2) * p1[1]) / 2
        if p3[0] < p4[0]:
            character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        elif p3[0] >= p4[0]:
            character.clip_draw(frame * 100, 0, 100, 100, x, y)
    # draw p4-p5
    if i < 100 and turn == 4:
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * p3[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p4[0] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p5[0] + (t ** 3 - t ** 2) * p6[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p3[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p4[1] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p5[1] + (t ** 3 - t ** 2) * p6[1]) / 2
        if p4[0] < p5[0]:
            character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        elif p4[0] >= p5[0]:
            character.clip_draw(frame * 100, 0, 100, 100, x, y)

    # draw p5-p6
    if i < 100 and turn == 5:
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * p4[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p5[0] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p6[0] + (t ** 3 - t ** 2) * p7[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p4[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p5[1] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p6[1] + (t ** 3 - t ** 2) * p7[1]) / 2
        if p5[0] < p6[0]:
            character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        elif p5[0] >= p6[0]:
            character.clip_draw(frame * 100, 0, 100, 100, x, y)

    # draw p6-p7
    if i < 100 and turn == 6:
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * p5[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p6[0] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p7[0] + (t ** 3 - t ** 2) * p8[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p5[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p6[1] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p7[1] + (t ** 3 - t ** 2) * p8[1]) / 2
        if p6[0] < p7[0]:
            character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        elif p6[0] >= p7[0]:
            character.clip_draw(frame * 100, 0, 100, 100, x, y)

    # draw p7-p8
    if i < 100 and turn == 7:
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * p6[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p7[0] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p8[0] + (t ** 3 - t ** 2) * p9[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p6[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p7[1] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p8[1] + (t ** 3 - t ** 2) * p9[1]) / 2
        if p7[0] < p8[0]:
            character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        elif p7[0] >= p8[0]:
            character.clip_draw(frame * 100, 0, 100, 100, x, y)
    # draw p8-p9
    if i < 100 and turn == 8:
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * p7[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p8[0] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p9[0] + (t ** 3 - t ** 2) * p10[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p7[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p8[1] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p9[1] + (t ** 3 - t ** 2) * p10[1]) / 2
        if p8[0] < p9[0]:
            character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        elif p8[0] >= p9[0]:
            character.clip_draw(frame * 100, 0, 100, 100, x, y)
    # draw p9-p10
    if i < 100 and turn == 9:
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * p8[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p9[0] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p10[0] + (t ** 3 - t ** 2) * p1[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p8[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p9[1] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p10[1] + (t ** 3 - t ** 2) * p1[1]) / 2
        if p9[0] < p10[0]:
            character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        elif p9[0] >= p10[0]:
            character.clip_draw(frame * 100, 0, 100, 100, x, y)
    # draw p10-p1
    if i < 100 and turn == 10:
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * p9[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p10[0] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p1[0] + (t ** 3 - t ** 2) * p2[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p9[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p10[1] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p1[1] + (t ** 3 - t ** 2) * p2[1]) / 2
        if p10[0] < p1[0]:
            character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        elif p10[0] >= p1[0]:
            character.clip_draw(frame * 100, 0, 100, 100, x, y)

    i += 2
    if i == 100:
        turn += 1
        i = 0
    if turn == 11:
        turn = 1

    delay(0.03)

    update_canvas()
    handle_events()

close_canvas()

