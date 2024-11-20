import pygame
import time
import sys
pygame.init()
display = pygame.display.set_mode((300,300))
while True:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        key = pygame.key.get_pressed()
        #print(key)
        if key[pygame.K_l]:
            break
        if key[pygame.K_w]:
            print("w")
        time.sleep(0.1)