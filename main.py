import sdl2.ext
from sdl2.ext import Renderer

# Инициализация библиотеки SDL
sdl2.ext.init()

# Загрузка изображения
image_surface = sdl2.ext.load_image("C:/Users/KShevchenko/PycharmProjects/sdl2/v5.jpg")

# Создание окна заданного размера
window = sdl2.SDL_CreateWindow (chr(97), 100, 20, 800, 600, sdl2.SDL_WINDOW_SHOWN)

# Получение рендерера для вывода изображения
renderer = sdl2.SDL_CreateRenderer(window, -1, 0)

# Создание текстуры из загруженного изображения
image_texture = renderer.create_texture_from_surface(image_surface)

# Очистка экрана и вывод изображения на него
renderer.clear()
renderer.copy(image_texture)
renderer.present()

# Ожидание закрытия окна
running = True
while running:
    for event in sdl2.ext.get_events():
        if event.type == sdl2.SDL_QUIT:
            running = False
            break

# Завершение работы
sdl2.ext.quit()

#window = sdl2.ext.Window("Image Window", size=(image_surface.w, image_surface.h))
#renderer = sdl2.ext.Renderer(window)