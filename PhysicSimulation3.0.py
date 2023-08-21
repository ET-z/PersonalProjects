import pygame as py
import sys
import random as ran
import math

print(py.ver)

py.init()
clock = py.time.Clock()
py.display.set_caption("Orbit Simulator")

WINDOW_SIZE = (1220, 700)
screen = py.display.set_mode(WINDOW_SIZE)
screen_rect = screen.get_rect()
display = py.Surface(WINDOW_SIZE)
display_rect = display.get_rect()

G = 6.67408 * (10 ** -11)  # Gravitational Constant
MASS_AREA_RATIO = 3 * (10 ** 9)  # mass in kilograms to area in pixels

planets = []
planet_id = 0
mouse_down = False


class Planet:
    def __init__(self, x, y, radius, mass, id):
        self.x = x
        self.y = y
        self.radius = radius
        self.volume = radius ** 3
        self.mass = mass
        self.id = id
        self.rect = py.Rect(
            self.x - self.radius / 1.5,
            self.y - self.radius / 1.5,
            self.radius * 1.5,
            self.radius * 1.5,
        )
        self.last_pos = (x, y)
        self.velocityX = 0
        self.velocityY = 0
        self.velocity = (self.velocityX, self.velocityY)
        self.doneCreating = False
        self.color = (
            0, (ran.randint(100, 255)), (ran.randint(100, 255))
        )

    def update(self):
        self.getVelocity()
        self.collision()
# Creating a rectangle around the planet.
        self.rect = py.Rect(
            self.x - self.radius / 1.5,
            self.y - self.radius / 1.5,
            self.radius * 1.5,
            self.radius * 1.5,
        )
        self.x += self.velocityX
        self.y += self.velocityY
        self.mass = math.pi * (self.radius ** 2) * MASS_AREA_RATIO
        if not mouse_down:
            self.doneCreating = True
        if not self.doneCreating:
            self.create()

    def create(self):
        if self.radius <= 200:
            self.radius += 0.35
        self.mass = math.pi * (self.radius ** 2) * MASS_AREA_RATIO
        self.volume = self.radius ** 3
        self.x, self.y = mx, my

    def getVelocity(self):
        if not self.doneCreating:
            self.current_pos = [mx, my]
            self.dpos = [
                (self.current_pos[0] - self.last_pos[0]) / 5,
                (self.current_pos[1] - self.last_pos[1]) / 5,
            ]  # dividing by two to make it less sensitive
            self.last_pos = [
                mx,
                my,
            ]  # Comparing mouse pos from one frame ago to current frame to get the velocity of the mouse movement
            self.velocityX = self.dpos[0]
            self.velocityY = self.dpos[1]

        if self.doneCreating:
            for planet in planets:
                if self.id != planet.id and planet.doneCreating:
                    dx = planet.x - self.x  # Difference between the x value of planet1 and planet2
                    dy = planet.y - self.y  # Difference between the y value of planet 1 and planet 2
                    # Calculate angle between planets
                    angle = math.atan2(dy, dx)
                    # Calculate distance between planet 1 and planet 2
                    d = math.sqrt((dx ** 2) + (dy ** 2))
                    if d == 0:
                        d = 0.000001  # Prevent division by zero error
                    f = (
                        G * self.mass * planet.mass / (d ** 2)
                    )  # Calculate gravitational force

                    # Change velocity of the planet
                    self.velocityX += (math.cos(angle) * f) / \
                        self.mass  # x velocity
                    self.velocityY += (math.sin(angle) * f) / \
                        self.mass  # y velocity

    def collision(self):
        if self.doneCreating:
            for planet in planets:
                if (
                    self.id != planet.id
                    and planet.doneCreating
                    and self.rect.colliderect(planet.rect)
                    and self.mass > planet.mass
                ):
                    planets.remove(planet)
                    if self.radius <= 200:
                        self.volume += planet.volume
                        self.radius = self.volume ** (1. / 3.)

    def draw(self):
        py.draw.circle(
            display, self.color, (int(self.x), int(self.y)), int(self.radius)
        )
        # py.draw.rect(display, (255, 255, 255), self.rect)


def draw():
    display.fill((0, 0, 0))

    for planet in planets:
        planet.draw()

    display_rect.center = screen_rect.center
    screen.blit(display, (0, 0))

    py.display.update()


while True:
    clock.tick(60)
    mx, my = py.mouse.get_pos()
    for event in py.event.get():
        if event.type == py.QUIT:
            sys.exit()
            py.quit()

        if event.type == py.MOUSEBUTTONDOWN and event.button == 1:
            mouse_down = True
            planets.append(Planet(mx, my, 0, 0, planet_id))
            planet_id += 1

        if event.type == py.MOUSEBUTTONUP and event.button == 1:
            mouse_down = False

        if event.type == py.KEYDOWN and event.key == py.K_BACKSPACE:
            planets.clear()

    for planet in planets:
        if len(planets) >= 50:
            planets.remove(planet)
        if planet.x > 50000 or planet.x < -50000:
            planets.remove(planet)
        if planet.y > 50000 or planet.y < -50000:
            planets.remove(planet)
        if planet.velocity[0] > 1000 or planet.velocity[0] < -1000:
            planets.remove(planet)
        if planet.velocity[1] > 1000 or planet.velocity[1] < -1000:
            planets.remove(planet)

    for planet in planets:
        planet.update()
    draw()
