# Imports
from car import Car
import random

# Constants
SPAWN_Y_LIMIT = 240
COLOURS = ["red", "blue", "purple", "yellow", "green", "orange", "pink", "brown"]
LENGTHS = [2, 3, 4, 5, 6]
VELOCITIES = [5, 10, 15]


# Class declaration
class Spawnmanager:
    def __init__(self):
        self.velocities_modifier = 0
        self.spawn_delay = 1
        self.current_cars = []
        self.car_pool = []
        for i in range(20):
            self.car_pool.append(self.spawn_car())


    def spawn_car(self):
        colour = random.choice(COLOURS)
        start_y = (random.randint(-240, 240) // 40) * 40    # Round to nearest 40
        length = random.choice(LENGTHS)
        velocity = random.choice(VELOCITIES) + self.velocities_modifier
        return Car(y=start_y, length=length, colour=colour, speed=velocity)

    def send_car(self):
        c = random.choice(self.car_pool)
        c.move_car()
        self.car_pool.remove(c)
        self.current_cars.append(c)
        if len(self.car_pool) == 0:
            d = self.current_cars.pop(0)
            self.car_pool.append(d)
            d.reset_car()

    def level_up(self):
        self.car_pool.clear()
        for car in self.current_cars:
            car.hideturtle()
        self.current_cars.clear()
        self.velocities_modifier += 4
        self.spawn_delay *= 0.75
        for i in range(20):
            self.car_pool.append(self.spawn_car())






