import pygame
from datetime import datetime

# Инициализация Pygame
pygame.init()

# Создание экрана с указанными размерами
screen = pygame.display.set_mode((1000, 650))
pygame.display.set_caption("Clock")

# Загрузка изображений и их масштабирование
mick = pygame.transform.scale(pygame.image.load("mainclock.png"), (1000, 650))
min = pygame.transform.scale(pygame.image.load("rightarm.png"), (1000, 650))
sec = pygame.transform.scale(pygame.image.load("leftarm.png"), (63, 650))

# Функция для вращения изображения вокруг своего центра
def rot_center(surf, image, angle, x, y):
    image = pygame.transform.rotate(image, angle)
    rect = image.get_rect(center=image.get_rect(center=(x, y)).center)
    surf.blit(image, rect)

# Основной цикл программы
while True:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Отображение фонового изображения часов
    screen.blit(mick, (0, 0))

    # Получение текущего времени
    t = datetime.now()

    # Вращение часовой стрелки
    rot_center(screen, min, -t.second * 6, 500, 325)

    # Вращение минутной стрелки
    rot_center(screen, sec, -t.minute * 6, 500, 325)

    # Обновление экрана
    pygame.display.flip()

    # Установка частоты обновления экрана
    pygame.time.Clock().tick(30)
