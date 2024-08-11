def draw_wind_compass(screen):
    arrow_image = pygame.image.load("arrow.png")
    resized_arrow_image = pygame.transform.scale(arrow_image, (400, 400))
    rotated_arrow_image = pygame.transform.rotate(resized_arrow_image, 90)

    compass_image = pygame.image.load("compass.jpg")
    resized_compass_image = pygame.transform.scale(compass_image, (400, 400))

    screen.blit(resized_compass_image, (1520, 0))
    screen.blit(rotated_arrow_image, (1520, 0))
    pygame.display.flip()