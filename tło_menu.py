def draw_background(screen):
    background_image = pygame.image.load('londyn.jpg')
    resized_background_image = pygame.transform.scale(background_image, (1920, 1080))
    screen.blit(resized_background_image, (0, 0))
    pygame.display.flip()