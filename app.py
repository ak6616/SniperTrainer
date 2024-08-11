import pygame
import sys
import requests

# zarys projektu:
# dwie postacie - cel i snajper, ich odległość oraz różnica wysokości jest pobierana
# od użytkownika z klawiatury poprzez podanie dokładnej lokalizacji
# po wybraniu wysokości oddania strzału, widok jest przełączany na doprecyzowanie wysokości
# oraz dokładnego położenia celownika

# background images:
menu_background_image = "londyn.jpg"
game_background_image = "strzelnica.jpg"

# screen parameters:
window_width, window_height = 800, 600
window = pygame.display.set_mode((window_width, window_height))  # , pygame.FULLSCREEN)
pygame.display.set_caption("Sniper Trainer")
cursor_image = pygame.image.load('celownik.jpg')
pygame.mouse.set_visible(False)

# keys:
keys = pygame.key.get_pressed()
k_right = pygame.K_RIGHT
k_left = pygame.K_LEFT
k_up = pygame.K_UP
k_down = pygame.K_DOWN

# colors:
purple = (128, 0, 128)
green = (0, 255, 0)
blue = (0, 0, 255)
grey = (160, 160, 160)

# fps
fps = 60
clock = pygame.time.Clock()


def weather_check():
    token = "f78ac47de8b6e1743864f8ff0e926814"
    city = input("Podaj miejscowość:")
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': token,
        'units': 'metric'
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return "Nie udało się wykonać kodu"

    weather_data = weather_check()
    humidity = {weather_data['main']['humidity']}
    temperature = {weather_data['main']['temp']}
    wind_speed = {weather_data['wind']['speed']}
    pressure = {weather_data['main']['pressure']}
    degrees = {weather_data['wind']['deg']}

    return humidity, temperature, wind_speed, pressure, degrees


class Button():
    def __init__(self, x, y, width, height, name=None):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.name = name

    def draw(self, window, color, rect, text):
        font = pygame.font.Font(None, 36)
        pygame.draw.rect(window, color, rect)
        text_surface = font.render(text, True, 0)
        text_rect = text_surface.get_rect(center=rect.center)
        window.blit(text_surface, text_rect)
        pygame.display.update()

    def action(self, event, button_rect, action):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                action()

class Player():
    def __init__(self, x, y, width, height, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self):
        player_image = pygame.image.load("snajper.jpg")
        resized_player_image = pygame.transform.scale(player_image, (self.width, self.height))
        window.blit(resized_player_image, (self.x, self.y))
        pygame.display.update()

class Crosshair():
    def __init__(self, x, y, width, height, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image
        self.rect = pygame.Rect(x, y, width, height)

    def move_left(self):
        self.x -= 1

    def move_right(self):
        self.x += 1

    def move_up(self):
        self.y += 1

    def move_down(self):
        self.y -= 1

    def draw(self, x=None, y=None, width=None, height=None):
        # Użycie przekazanych parametrów lub domyślnych wartości
        x = x if x is not None else self.x
        y = y if y is not None else self.y
        width = width if width is not None else self.width
        height = height if height is not None else self.height


class Target():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)
        self.hit = False

    def hit(self):
        self.hit = True


def draw_button(window, color, rect, text):
    font = pygame.font.Font(None, 36)
    pygame.draw.rect(window, color, rect)
    text_surface = font.render(text, True, 0)
    text_rect = text_surface.get_rect(center=rect.center)
    window.blit(text_surface, text_rect)

    pygame.display.update()

def draw_background(window, image):
    background_image = pygame.image.load(image)
    resized_background_image = pygame.transform.scale(background_image, (1920, 1080))
    window.blit(resized_background_image, (0, 0))

  # ------------------------------------------------------------------------------
schooting_range_image = pygame.image.load('strzelnica.jpg')
resized_schooting_range_image = pygame.transform.scale(schooting_range_image, (1920, 1080))
    # -----------------------------------------------------------------------------------------


def draw_wind_compass(window):
    arrow_image = pygame.image.load("arrow.png")
    resized_arrow_image = pygame.transform.scale(arrow_image, (400, 400))
    rotated_arrow_image = pygame.transform.rotate(resized_arrow_image, 90)

    compass_image = pygame.image.load("compass.jpg")
    resized_compass_image = pygame.transform.scale(compass_image, (400, 400))

    window.blit(resized_compass_image, (1520, 0))
    window.blit(rotated_arrow_image, (1520, 0))

    pygame.display.update()

def button_event_handler(event, button_rect, action):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if button_rect.collidepoint(event.pos):
            action()

        # button_event_handler(event, pygame.Rect(720, 540, 480, 120), start_game)
        # button_event_handler(event, pygame.Rect(720, 675, 480, 120), about_game)
        # button_event_handler(event, pygame.Rect(720, 810, 480, 120), exit_game)

def menu():
    draw_background(window, menu_background_image)

    draw_button(window, purple, pygame.Rect(720, 540, 480, 120), "Graj")
    draw_button(window, purple, pygame.Rect(720, 675, 480, 120), "O grze")
    draw_button(window, purple, pygame.Rect(720, 810, 480, 120), "Wyjście")
    # cursor()
    # Button.draw(self, window, purple, pygame.Rect(720, 540, 480, 120), "Graj")



    pygame.display.update()

def start_game():
    draw_background(window, game_background_image)
    print("Start game button clicked")

def about_game():
    print("About game button clicked!")

def exit_game():
    pygame.quit()
    sys.exit()

def cursor():

    cursor_rect = cursor_image.get_rect()
    window.blit(cursor_image, cursor_rect)
    mouse_x, mouse_y = pygame.mouse.get_pos()
    cursor_rect.topleft = (mouse_x, mouse_y)
    pygame.display.update()

def main():

    pygame.init()

    running = True
    while running:

        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        Crosshair.draw(100, 100, 300, 300, 300)






    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
