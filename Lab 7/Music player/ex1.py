import pygame

# Инициализация Pygame
pygame.init()

# Создание окна с указанными размерами
screen = pygame.display.set_mode((400, 200))
pygame.display.set_caption('Bad - Media - Player')

# Список музыкальных файлов
music_list = ['song1.mp3', 'song2.mp3', 'song3.mp3', 'song4.mp3', 'song5.mp3', 'song6.mp3']

# Пользовательское событие для завершения воспроизведения музыки
SONG_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(SONG_END)

# Индекс текущего трека в списке
current_track_index = 0

# Флаг паузы
paused = False  

# Основной цикл программы
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                current_track_index += 1
                if current_track_index > len(music_list) - 1:
                    current_track_index = 0
                pygame.mixer.music.stop()
                pygame.mixer.music.load(music_list[current_track_index])
                pygame.mixer.music.play(-1)
            
            if event.key == pygame.K_LEFT:
                current_track_index -= 1
                if current_track_index < 0:
                    current_track_index = len(music_list) - 1
                pygame.mixer.music.stop()
                pygame.mixer.music.load(music_list[current_track_index])
                pygame.mixer.music.play(-1)
            
            if event.key == pygame.K_SPACE:
                if paused:
                    pygame.mixer.music.unpause()  
                    paused = False
                else:
                    pygame.mixer.music.pause()  
                    paused = True

    # Отображение белого фона
    screen.fill((0, 2, 7))
    # Обновление экрана
    pygame.display.flip()
