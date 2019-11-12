import pygame

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1000

GREEN = (34, 139, 34)
WHITE = (255, 255, 255)

FPS = 60

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

rects = []
images = []

grande_carta = (175, 250)

for palo in range(0, 4):
    for numero in range(0, 13):
        numero_real = numero + 1
        if palo == 0:
            if numero_real < 10:
                images.append(pygame.image.load('cartas/C0{}.png'.format(numero_real)).convert_alpha())
                numero = len(images) - 1
                images[numero] = pygame.transform.scale(images[numero], grande_carta)
                rects.append(images[numero].get_rect())
            else:
                images.append(pygame.image.load('cartas/C{}.png'.format(numero_real)).convert_alpha())
                numero = len(images) - 1
                images[numero] = pygame.transform.scale(images[numero], grande_carta)
                rects.append(images[numero].get_rect())
        elif palo == 1:
            if numero_real < 10:
                images.append(pygame.image.load('cartas/R0{}.png'.format(numero_real)).convert_alpha())
                numero = len(images) - 1
                images[numero] = pygame.transform.scale(images[numero], grande_carta)
                rects.append(images[numero].get_rect())
            else:
                images.append(pygame.image.load('cartas/R{}.png'.format(numero_real)).convert_alpha())
                numero = len(images) - 1
                images[numero] = pygame.transform.scale(images[numero], grande_carta)
                rects.append(images[numero].get_rect())
        elif palo == 2:
            if numero_real < 10:
                images.append(pygame.image.load('cartas/P0{}.png'.format(numero_real)).convert_alpha())
                numero = len(images) - 1
                images[numero] = pygame.transform.scale(images[numero], grande_carta)
                rects.append(images[numero].get_rect())
            else:
                images.append(pygame.image.load('cartas/P{}.png'.format(numero_real)).convert_alpha())
                numero = len(images) - 1
                images[numero] = pygame.transform.scale(images[numero], grande_carta)
                rects.append(images[numero].get_rect())
        elif palo == 3:
            if numero_real < 10:
                images.append(pygame.image.load('cartas/T0{}.png'.format(numero_real)).convert_alpha())
                numero = len(images) - 1
                images[numero] = pygame.transform.scale(images[numero], grande_carta)
                rects.append(images[numero].get_rect())
            else:
                images.append(pygame.image.load('cartas/T{}.png'.format(numero_real)).convert_alpha())
                numero = len(images) - 1
                images[numero] = pygame.transform.scale(images[numero], grande_carta)
                rects.append(images[numero].get_rect())


pygame.mixer.music.load('bensound-thejazzpiano.mp3')
pygame.mixer.music.play()

selected = None

clock = pygame.time.Clock()

running = True
offset_x = 0
offset_y = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for i, r in enumerate(rects):
                    if r.collidepoint(event.pos):
                        selected = i
                        selected_offset_x = r.x - event.pos[0]
                        selected_offset_y = r.y - event.pos[1]

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                selected = None

        elif event.type == pygame.MOUSEMOTION:
            if selected is not None:
                rects[selected].x = event.pos[0] + selected_offset_x
                rects[selected].y = event.pos[1] + selected_offset_y

    screen.fill(GREEN)
    for r in range(0, len(rects)):
        screen.blit(images[r], rects[r])

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
