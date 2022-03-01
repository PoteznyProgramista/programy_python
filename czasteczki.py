
import pygame as pg
import sys
import math
import random

WHITE = (255, 255, 255)
BLUE = (0,   0, 255)
GREEN = (0, 255,   0)
RED = (255,   0,   0)
BLACK = (0,     0,   0)


def wektor_znormalizowany(x, y):
    dlugosc = math.sqrt(x**2 + y**2)
    return (x/dlugosc, y/dlugosc)


class Particle:

    def __init__(self, x, y, vx=0, vy=0, mass=1, r=5, color=WHITE):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.mass = mass
        self.r = r
        self.color = color

    def odleglosc_do_kwadratu(self, particle2):
        return (self.x - particle2.x)**2 + (self.y - particle2.y)**2

    def move(self, delta_time):
        self.x += self.vx * delta_time
        self.y += self.vy * delta_time

    def sila_grawitacji(self, particle2):
        sila = (self.mass * particle2.mass) / \
            self.odleglosc_do_kwadratu(particle2)
        kierunek_x, kierunek_y = self.kierunek_do(particle2)
        return (kierunek_x * sila, kierunek_y * sila)

    def apply_gravity(self, force_x, force_y, delta_time):
        self.vx += force_x * delta_time
        self.vy += force_y * delta_time

    def kierunek_do(self, particle2):
        dx = particle2.x - self.x
        dy = particle2.y - self.y
        return wektor_znormalizowany(dx, dy)
    
    def odleglosc_do(self,particle2):
        return math.sqrt(self.odleglosc_do_kwadratu(particle2))
    


def generator_czasteczek(n, r, cx, cy, prawdopodobienstwo_duza_kulka=0.1):
    particles = []
    current_angle = 0
    for i in range(n):
        current_angle += (2*math.pi/n)
        x = math.cos(current_angle)*r + cx
        y = math.sin(current_angle)*r + cy
        if random.random() <= prawdopodobienstwo_duza_kulka:
            particle = Particle(x, y, mass=10, r=8, color=RED)
        else:
            particle = Particle(x, y, color=WHITE)
        particles.append(particle)
    return particles


def gravity_effect(particles, delta_time):
    for particle in particles:
        akumulator_x = 0
        akumulator_y = 0
        for particle2 in particles:
            if particle is particle2 or particle.odleglosc_do(particle2) <= particle.r + particle2.r:
                continue
            
            (sila_x, sila_y) = particle.sila_grawitacji(particle2)
            akumulator_x += sila_x
            akumulator_y += sila_y
        particle.apply_gravity(akumulator_x, akumulator_y, delta_time)

def grawitacja_myszy(mysz_x, mysz_y,delta_time,mass):
    for particle in particles:
        wirtualna_czasteczka = Particle(mysz_x,mysz_y,mass = mass, r = 0)
        if particle.odleglosc_do(wirtualna_czasteczka) <= particle.r + wirtualna_czasteczka.r:
                continue
        (sila_x, sila_y) = particle.sila_grawitacji(wirtualna_czasteczka)
        particle.apply_gravity(sila_x, sila_y, delta_time)


def drawCircle(particle, screen):
    position = particle.x, particle.y
    pg.draw.circle(screen, particle.color, position, particle.r)
    
def odbij_czasteczke(particle, screen_width, screen_height):
    if particle.x - particle.r < 0:
        particle.vx *= -1 
        particle.x = particle.r
    if particle.x + particle.r > screen_width:
        particle.vx *= -1
        particle.x = screen_width - particle.r
    if particle.y - particle.r < 0:
        particle.vy *= -1
        particle.y = particle.r
    if particle.y + particle.r > screen_height:
        particle.vy *= -1
        particle.y = screen_height - particle.r

screen_width = 800
screen_height = 800
cx = screen_width // 2
cy = screen_height // 2
clock = pg.time.Clock()
screen_width, screen_height = 1200, 1000
screen = pg.display.set_mode((screen_width, screen_height))

prawdopodobienstwo_duza_kulka = 0.1
delta_time = 1
masa_myszki = -100

particles = generator_czasteczek(50, 500, cx, cy, prawdopodobienstwo_duza_kulka)
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    screen.fill(BLACK)

    # TU KOD

    gravity_effect(particles, delta_time)
    pozycja_myszy = pg.mouse.get_pos()
    grawitacja_myszy(pozycja_myszy[0],pozycja_myszy[1],delta_time, masa_myszki)
    for particle in particles:
        particle.move(delta_time)
        odbij_czasteczke(particle,screen_width,screen_height)
        drawCircle(particle, screen)

    ###

    pg.display.flip()
    clock.tick(60)
