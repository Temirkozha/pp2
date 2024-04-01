#библиотеку Pygame для создания простой игровой сцены,
#где пользователь может перемещать красный эллипс по экрану с помощью клавиатуры.

import pygame

# Инициализация Pygame
pygame.init()

# Определение цветов
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Определение размеров экрана
size = width, height = (600, 600)

# Создание окна с указанными размерами
screen = pygame.display.set_mode(size)

# Создание объекта Clock для управления скоростью обновления экрана
clock = pygame.time.Clock()

# Начальные координаты, скорость и скорость перемещения
x, y, dx, dy, velocity = 0, 0, 0, 0, 20

# Основной цикл программы
while True:
    # Обработка событий
    for event in pygame.event.get():
        # Обработка события закрытия окна
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # Обработка нажатий клавиш
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_LEFT, pygame.K_a):
                dy, dx = 0, -velocity
            elif event.key in (pygame.K_RIGHT, pygame.K_d):
                dy, dx = 0, velocity
            elif event.key in (pygame.K_UP, pygame.K_w):
                dx, dy = 0, -velocity
            elif event.key in (pygame.K_DOWN, pygame.K_s):
                dx, dy = 0, velocity

    # Очистка экрана и заполнение его белым цветом
    screen.fill(WHITE)

    # Изменение координат
    y += dy
    x += dx

    # Ограничение координат, чтобы эллипс оставался видимым на экране
    x, y = max(0, min(x, width - 50)), max(0, min(y, height - 50))

    # Отрисовка эллипса
    pygame.draw.ellipse(screen, RED, (x, y, 50, 50))

    # Ожидание до следующего кадра с частотой 60 Гц
    clock.tick(60)

    # Обновление экрана для отображения изменений
    pygame.display.update()
