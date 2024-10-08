from pico2d import *
import random

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

    def update(self): pass

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(0, 800), 90  # 랜덤한 x 좌표에서 시작
        self.frame = 0
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5
        if self.x > 800:
            self.x = 0  # 화면을 넘어가면 다시 왼쪽에서 시작

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

class BallSmall:
    def __init__(self):
        self.x, self.y = random.randint(0, 800), 599  # 랜덤한 x 좌표에서 상단에서 시작
        self.speed = random.randint(5, 15)  # 랜덤한 낙하 속도
        self.image = load_image('ball21x21.png')

    def update(self):
        if self.y > 70:  # 바닥에서 10px 위에 멈추기
            self.y -= self.speed

    def draw(self):
        self.image.draw(self.x, self.y)

class BallLarge:
    def __init__(self):
        self.x, self.y = random.randint(0, 800), 599  # 랜덤한 x 좌표에서 상단에서 시작
        self.speed = random.randint(5, 15)  # 랜덤한 낙하 속도
        self.image = load_image('ball41x41.png')

    def update(self):
        if self.y > 80:
            self.y -= self.speed

    def draw(self):
        self.image.draw(self.x, self.y)

def reset_world():
    global running
    global grass
    global world
    global boys
    global balls

    running = True
    world = []
    grass = Grass()
    world.append(grass)

    # 10명의 보이를 추가
    boys = [Boy() for _ in range(10)]
    world += boys

    # 랜덤하게 20개의 공을 추가 (작은 공과 큰 공)
    ball_count = 20
    small_ball_count = random.randint(5, ball_count)  # 작은 공의 개수 랜덤 설정
    large_ball_count = ball_count - small_ball_count  # 나머지는 큰 공

    balls = [BallSmall() for _ in range(small_ball_count)] + [BallLarge() for _ in range(large_ball_count)]
    world += balls

def update_world():
    for o in world:
        o.update()

def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

open_canvas()

reset_world()

while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)

close_canvas()
