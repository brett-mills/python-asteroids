import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def update(self, dt):
        # sub-classes must override
        pass

    def collides_with_player(self, player):
        distance = self.position.distance_to(player.position)
        if distance <= (self.radius + player.radius):
            return True
        return False
    
    def collides_with_shot(self, shot):
        distance = self.position.distance_to(shot.position)
        if distance <= (self.radius + shot.radius):
            return True
        return False