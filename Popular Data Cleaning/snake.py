import pygame
import random

# Inicializar pygame
pygame.init()

# Establecer el tamaño de la pantalla
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))

# Establecer el título de la ventana
pygame.display.set_caption("Snake")

# Establecer la velocidad de la serpiente
snake_speed = 5

# Definir los colores
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Definir la clase Snake
class Snake:
    def __init__(self):
        self.size = 1
        self.elements = [[100, 100]]
        self.radius = 10
        self.dx = 5  # desplazamiento en x
        self.dy = 0  # desplazamiento en y
        self.is_add_new = False

    def draw(self):
        for element in self.elements:
            pygame.draw.circle(screen, green, element, self.radius)

    def move(self):
        # Mover la serpiente
        for i in range(self.size - 1, 0, -1):
            self.elements[i] = self.elements[i - 1][:]

        # Añadir un nuevo elemento a la serpiente
        if self.is_add_new:
            self.elements.append(self.elements[-1][:])
            self.size += 1
            self.is_add_new = False

        # Actualizar la posición de la cabeza de la serpiente
        self.elements[0][0] += self.dx
        self.elements[0][1] += self.dy

# Definir la clase Comida
class Food:
    def __init__(self):
        self.x = random.randint(50, screen_width - 50)
        self.y = random.randint(50, screen_height - 50)
        self.radius = 5

    def draw(self):
        pygame.draw.circle(screen, white, (self.x, self.y), self.radius)

# Crear una serpiente y una comida
snake = Snake()
food = Food()

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Obtener las teclas pulsadas
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.dx = 0
                snake.dy = -sn