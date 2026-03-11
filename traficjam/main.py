import pygame
import math
from car import Car  # __init__.py のおかげで Car が直接アクセス可能
from car import CAR_NUMS
from UI import *
# import UI

# =====================
# メイン処理
# =====================
pygame.init()

# 画面設定
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("環状道路を走る車")

# 色
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)
CAR_COLORS = [(200, 0, 0), (0, 0, 200), (0, 200, 0), (200, 200, 0), (255, 165, 0)]
BREAKER_COLOR = (0, 0, 0)
# 道路パラメータ
CENTER = (WIDTH // 2, HEIGHT // 2)
ROAD_RADIUS = 250
ROAD_WIDTH = 40

# 車を作成
cars = []
NUM_CARS = CAR_NUMS
for i in range(NUM_CARS):
    angle = i * (2 * math.pi / NUM_CARS)
    speed = 0.03  # 全車同じ速度
    color = CAR_COLORS[i % len(CAR_COLORS)]
    if i == 0:
        cars.append(Car(CENTER, ROAD_RADIUS, angle, speed, BREAKER_COLOR))
    elif i != NUM_CARS-1:
        cars.append(Car(CENTER, ROAD_RADIUS, angle, speed, color))
    else:#最後尾の車
        cars.append(Car(CENTER, ROAD_RADIUS, angle, speed, color, is_last=True))


#前の車を登録
for i in range(NUM_CARS):
    cars[i].front_car = cars[(i+1)%NUM_CARS]


# ループ
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = event.pos
            # 中心からの距離で判定
            dist_sq = (mouse_pos[0] - button_center[0])**2 + (mouse_pos[1] - button_center[1])**2
            if dist_sq <= button_radius**2:
                button_on = not button_on  # 状態切り替え

    screen.fill(WHITE)

    # 道路を描く
    pygame.draw.circle(screen, GRAY, CENTER, ROAD_RADIUS + ROAD_WIDTH // 2)
    pygame.draw.circle(screen, WHITE, CENTER, ROAD_RADIUS - ROAD_WIDTH // 2)

    # 車を更新＆描画
    for car in cars:
        if car == cars[0] and button_on : car.car_break()
        else : car.update()
        car.draw(screen)

    # ボタン描画
    if button_on:
        pygame.draw.circle(screen, (0, 0, 0), button_center, button_radius)
    else:
        pygame.draw.circle(screen, (255, 255, 255), button_center, button_radius)
        pygame.draw.circle(screen, (0, 0, 0), button_center, button_radius, 2)  # 枠線

    pygame.display.flip()
    clock.tick(30)  # FPS 30

pygame.quit()
