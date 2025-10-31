import pygame
from constants import *
from circleshape import *
from shot import Shot, SHOT_RADIUS

class Player(CircleShape):
    def __init__ (self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pts = [(int(p.x), int(p.y)) for p in self.triangle()]
        pygame.draw.polygon(screen, (255, 255, 255), pts, 2)

    def rotate(self, dt):
        self.rotation = (self.rotation + PLAYER_TURN_SPEED * dt) % 360

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def shoot(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        spawn_pos = self.position + forward * (PLAYER_RADIUS + SHOT_RADIUS)
        shot = Shot(spawn_pos.x, spawn_pos.y, SHOT_RADIUS)
        shot.velocity = forward * PLAYER_SHOOT_SPEED

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)

        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_s]:
            self.move(-dt)
        
        if keys[pygame.K_SPACE]:
            self.shoot()

   

