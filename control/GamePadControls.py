import socket
import time
import pygame
import sys
import array
import pygame
#import keyboard
import json
def constrain(val, min_val, max_val):
    return min(max_val, max(min_val, val))

pygame.init()
display = pygame.display.set_mode((300,300))

UDP_IP = "169.254.218.236"
UDP_PORT = 100
# Local_IP = "169.254.153.129"
# Local_Port = 4010

sock = socket.socket(socket.AF_INET, # Internet 
                      socket.SOCK_DGRAM) # UDP


#   Bits sent
#   each has an integer value (inclusively )between -128 and 127
class DATA:
    left = 0    # left motor
    right = 0   # right motor
    ch1 = 90    # servo 1
    ch2 = 0
    ch3 = 0
    ch4 = 0
    ch5 = 0
    ch6 = 0


keys = pygame.key.get_pressed()
keysPrev = None
ArrDATA = array.array('b',[DATA.left, DATA.right, DATA.ch1, DATA.ch2, DATA.ch3, DATA.ch4, DATA.ch5, DATA.ch6])
sock.sendto(ArrDATA, (UDP_IP, UDP_PORT))
lastTime = 0

# inisialising joysticks
joysticks = []
for i in range (pygame.joystick.get_count()):
    joysticks.append(pygame.joystick.Joystick(i))
for joystick in joysticks:
    joystick.init()

with open("ps4ButtonMap.json",mode="r+") as file:
    buttonMap = json.load(file)
            #left stick     #right stick    #l2     #r2
analogMap = {0:0,   1:0,    2:0,    3:0,    4:-1,   5:-1}

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:

            keysPrev = keys
            keys = pygame.key.get_pressed() #The PyGame keys function is deranged, I'm sorry about the code that follows. Why can't it just return a string!
            keyPressed = False

            if (keys != keysPrev):
                print("changed")
                DATA.left = 0
                DATA.right = 0
                keyPressed = False

            if keys[pygame.K_w]:
                DATA.left += 127
                DATA.right += 127
                keyPressed = True
                print("w")

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
            
            if keys[pygame.K_q]:
                #Add some servo stuff in empty channels
                keyPressed = True

            if keys[pygame.K_e]:
                #Add some servo stuff in empty channels
                keyPressed = True

            if not(keyPressed):
                DATA.left = 0
                DATA.right = 0

        if event.type == pygame.JOYBUTTONDOWN:
            if event.button == buttonMap['x']:
                DATA.ch1 = 127
                print("x")
            if event.button == buttonMap['circle']:
                print("circle")
            if event.button == buttonMap['triangle']:
                print("triangle")
            if event.button == buttonMap['square']:
                print("square")
            if event.button == buttonMap['l1']:
                print("l1")
            if event.button == buttonMap['r1']:
                print("r1")
            if event.button == buttonMap['l3']:
                print("l3")
            if event.button == buttonMap['r3']:
                print("r3")
            if event.button == buttonMap['down']:
                print("down")
            if event.button == buttonMap['right']:
                print("right")
            if event.button == buttonMap['up']:
                print("up")
            if event.button == buttonMap['left']:
                print("left")
            if event.button == buttonMap['options']:
                print("options")
            if event.button == buttonMap['share']:
                print("share")
            if event.button == buttonMap['home']:
                print("home")
            if event.button == buttonMap['touchpad']:
                print("touchpad")

        if event.type == pygame.JOYBUTTONUP:
            if event.button == buttonMap['x']:
                DATA.ch1 = 0
            
    DATA.left = constrain(DATA.left, -127, 127)
    DATA.right = constrain(DATA.right, -127, 127)
    print("key pressed")
        

        
    if (time.time()-lastTime>0.01):
        lastTime=time.time()
        ArrDATA = array.array('b',[DATA.left, DATA.right, DATA.ch1, DATA.ch2, DATA.ch3, DATA.ch4, DATA.ch5, DATA.ch6])
        sock.sendto(ArrDATA, (UDP_IP, UDP_PORT))



