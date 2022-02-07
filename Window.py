import pygame

pygame.init()
screen = pygame.display.set_mode((500, 700))
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(0, 100, 600, 60)) ## first numebrs refer to color, second refer to colored box size

    #load fonts
    font = pygame.font.SysFont("Comic Sans", 40)
    # Render text
    text = font.render("6 Letter Word Game!", True, (255, 255, 255))
    screen.blit(text, (270 - text.get_width() // 2, 150 - text.get_height())) ## Placement of intro text
    pygame.display.flip() ## Make all changes available for screen

