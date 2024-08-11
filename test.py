import pygame
import requests

pygame.init()
width_height = (1200, 800)
window = pygame.display.set_mode(width_height)
menu_background_image = pygame.transform.scale(pygame.image.load("menu_background.jpg"), width_height)
game_background_image = pygame.transform.scale(pygame.image.load("shooting_range.jpg"), width_height)
crosshair = pygame.transform.scale(pygame.image.load("crosshair.jpg"), (100, 100))
mouse = pygame.transform.scale(pygame.image.load("mouse.png"), (100, 100))
targets = ["target_1.jpg", "target_2.jpg", "target_3.jpg", "target_4.jpg", "target_5.jpg"]
keys = pygame.key.get_pressed()

purple = (128, 0, 128)
green = (0, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
grey = (160, 160, 160)




# keys = pygame.key.get_pressed()

# def tick(self, keys):
#     if keys[pygame.K_UP]:
#         self.y -= self.velocity
#     if keys[pygame.K_DOWN]:
#         self.y += self.velocity
#     if keys[pygame.K_LEFT]:
#         self.x -= self.velocity
#     if keys[pygame.K_RIGHT]:
#         self.x += self.velocity

class Player:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.image = pygame.image.load("player.jpg")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.score = 0


    def tick(self):
        pass

    def draw(self):
        window.blit(self.image, (self.x, self.y))
        pass


class Crosshair:

    def __init__(self, crosshair_image):
        self.x, self.y = pygame.mouse.get_pos()
        self.crosshair_image = pygame.transform.scale(pygame.image.load(crosshair_image), (100, 100))
        self.width = self.crosshair_image.get_width()
        self.height = self.crosshair_image.get_height()
        self.hitbox = pygame.Rect(self.width/2, self.height/2, 1, 1)

    def draw(self, mouse_x, mouse_y):
        window.blit(self.crosshair_image, (mouse_x - (self.width / 2), mouse_y - (self.height / 2)))

    def tick(self):
        if keys[pygame.MOUSEBUTTONDOWN]:


        pass

class Target:
    def __init__(self, target_image):
        self.x = 0
        self.y = 0
        self.image = pygame.image.load(target_image)
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.hit = False
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def tick(self):
        pass

    def draw(self, x, y):
        window.blit(self.image, (x, y))
        pass

def draw_wind_compass(screen):
    arrow_image = pygame.image.load("arrow.png")
    resized_arrow_image = pygame.transform.scale(arrow_image, (400, 400))
    rotated_arrow_image = pygame.transform.rotate(resized_arrow_image, 90)

    compass_image = pygame.image.load("compass.jpg")
    resized_compass_image = pygame.transform.scale(compass_image, (400, 400))

    screen.blit(resized_compass_image, (1520, 0))
    screen.blit(rotated_arrow_image, (1520, 0))
    pygame.display.flip()

def menu(mouse_x, mouse_y):
    mouse = Crosshair("mouse.png")


    draw_button(window, purple, pygame.Rect(720, 540, 480, 135), "Graj")
    draw_button(window, purple, pygame.Rect(720, 675, 480, 135), "O grze")
    draw_button(window, purple, pygame.Rect(720, 810, 480, 135), "Wyjście")
    mouse.draw(mouse_x, mouse_y)

def draw_button(window, color, rect, text):
    font = pygame.font.Font(None, 36)
    pygame.draw.rect(window, color, rect)
    text_surface = font.render(text, True, 0)
    text_rect = text_surface.get_rect(center=rect.center)
    window.blit(text_surface, text_rect)

    pygame.display.update()

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

def choosing_target(mouse_x, mouse_y):
    target = Target("target.jpg")


    target.draw(240, 135)
    pygame.draw.circle(window, blue, (mouse_x, mouse_y), 100)




def game(mouse_x, mouse_y):
    crosshair = Crosshair("crosshair.jpg")
    window.blit(game_background_image, (0, 0))

    choosing_target()

    #target_choice_space = pygame.draw.rect(window, red, pygame.Rect(100, 100, 800, 500))


    crosshair.draw(mouse_x, mouse_y)
    pass


def main():


    pygame.mouse.set_visible(False)


    run = True




    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.time.Clock().tick(60)

        mouse_x, mouse_y = pygame.mouse.get_pos()

        game(mouse_x, mouse_y)



        pygame.display.update()

if __name__ == "__main__":
    main()
