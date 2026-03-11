import pygame
import math
# =====================
# 車クラス
# =====================
CAR_NUMS = 30
THRESHOLD = 30

class Car:
    def __init__(self, center, road_radius, angle, speed, color, size=10,is_last=False):
        self.center = center
        self.road_radius = road_radius
        self.angle = angle
        self.speed = speed
        self.color = color
        self.size = size
        self.front_car = None#前の車
        self.last = is_last#最後尾の車か
        self.speed_up_dradually = 1

    def update(self):
        """車を移動 or 停止"""
        if self.last and (self.front_car.angle + 2*math.pi) - self.angle > 2*math.pi / (CAR_NUMS * 2)\
            or\
            (not self.last) and self.front_car.angle - self.angle > 2*math.pi / (CAR_NUMS * 2) :
            if self.speed_up_dradually < THRESHOLD:
                self.angle += self.speed * (self.speed_up_dradually)/THRESHOLD
                self.speed_up_dradually += 1
            else:
                self.angle += self.speed
            
        else:
            self.speed_up_dradually = 1
            # self.car_break()

    def draw(self, surface):
        """車を描画"""
        x = self.center[0] + self.road_radius * math.cos(self.angle)
        y = self.center[1] + self.road_radius * math.sin(self.angle)
        pygame.draw.circle(surface, self.color, (int(x), int(y)), self.size)

    
    def car_break(self):
        pass
