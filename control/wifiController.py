import socket
import time
import pygame
import sys
import array
import keyboard

def myVersion():
    print("Press a key")
    while True:
        try:
            if keyboard.is_pressed('q'):
                print('Pressed a Key!')
                break
        except:
            break

def constrain(val, min_val, max_val):
    return min(max_val, max(min_val, val))

pygame.init()
display = pygame.display.set_mode((300,300))

UDP_IP = "172.20.10.3"
UDP_PORT = 100

class DATA:
    left = 0
    right = 0
    ch1 = 90
    ch2 = 0
    ch3 = 0
    ch4 = 0
    ch5 = 0
    ch6 = 0


sock = socket.socket(socket.AF_INET, # Internet 
                     socket.SOCK_DGRAM) # UDP
keys = pygame.key.get_pressed()

ArrDATA = array.array('b',[DATA.left, DATA.right, DATA.ch1, DATA.ch2, DATA.ch3, DATA.ch4, DATA.ch5, DATA.ch6])        
sock.sendto(ArrDATA, (UDP_IP, UDP_PORT))
lastTime = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    keysPrev = keys
    keys = pygame.key.get_pressed() #The PyGame keys function is deranged, I'm sorry about the code that follows. Why can't it just return a string!

    if (keys != keysPrev):
        print("changed")
        DATA.left = 0
        DATA.right = 0
        keyPressed = False

        if keys[pygame.K_w]:
            DATA.left += 127
            DATA.right += 127
            keyPressed = True

        if keys[pygame.K_s]:
            DATA.left -= 127
            DATA.right -= 127
            keyPressed = True

        if keys[pygame.K_d]:
            DATA.left += 100
            DATA.right -= 100
            keyPressed = True

        if keys[pygame.K_a]:
            DATA.left -= 100
            DATA.right += 100
            keyPressed = True

        if keys[pygame.K_q]:
            DATA.ch1 = 70
            keyPressed = True

        if keys[pygame.K_e]:
            DATA.ch1 = 110
            keyPressed = True

        if keys[pygame.K_RETURN]:
            myVersion()
        
        

        if keys[pygame.K_q]:
            #Add some servo stuff in empty channels
            keyPressed = True

        if keys[pygame.K_e]:
            #Add some servo stuff in empty channels
            keyPressed = True

        if not(keyPressed):
            DATA.left = 0
            DATA.right = 0
        DATA.left = constrain(DATA.left, -127, 127)
        DATA.right = constrain(DATA.right, -127, 127)
        

        
    if (time.time()-lastTime>0.01):
        lastTime=time.time()
        ArrDATA = array.array('b',[DATA.left, DATA.right, DATA.ch1, DATA.ch2, DATA.ch3, DATA.ch4, DATA.ch5, DATA.ch6])
        sock.sendto(ArrDATA, (UDP_IP, UDP_PORT))



