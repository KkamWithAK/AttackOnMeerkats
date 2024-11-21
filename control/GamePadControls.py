import socket
import time
import pygame
import sys
import array
import pygame
#import keyboard
import json
import os
def constrain(val, min_val, max_val):
    return min(max_val, max(min_val, val))

pygame.init()
display = pygame.display.set_mode((300,300))

#UDP_IP = "169.254.218.236"
#UDP_PORT = 100
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
    ch6 = 0     # LED
    def copy(): # So i can compare stuff, dw bout it
        return array.array('b',[DATA.left, DATA.right, DATA.ch1, DATA.ch2, DATA.ch3, DATA.ch4, DATA.ch5, DATA.ch6])


keys = pygame.key.get_pressed()
keysPrev = None
ArrDATA = array.array('b',[DATA.left, DATA.right, DATA.ch1, DATA.ch2, DATA.ch3, DATA.ch4, DATA.ch5, DATA.ch6])
#sock.sendto(ArrDATA, (UDP_IP, UDP_PORT))
lastTime = 0

# inisialising all joysticks
joysticks = [] 
for i in range (pygame.joystick.get_count()):
    joysticks.append(pygame.joystick.Joystick(i))
for joystick in joysticks:
    joystick.init()
# self explanatory
with open(os.path.join("ps4ButtonMap.json"),mode="r+") as file:
    buttonMap = json.load(file)
            #left stick     #right stick    #l2     #r2
analogMap = {0:0,   1:0,    2:0,    3:0,    4:-1,   5:-1} # all hold values between [-1,1]*
# * may go slighty over (-1.000032342230)

buttonMapState = {} # checks if a button is held down(true)
for each in buttonMap:
    buttonMapState.update({each:False}) # all false, duh


#while True:
def ReadInput():
    # initialsing varibles
    global lastTime
    global ArrDATA
    global keys
    global buttonMapState
    throttle = 0 # -127 to 127, +ve = forwards, -ve = backwards| around 50 is very slow

    prevArray = DATA.copy()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # -----------KEYBOARD-----------    
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
       
       
        # CONTROLLER
       
        # PRESSED A DIGITAL BUTTON
        if event.type == pygame.JOYBUTTONDOWN:
            if event.button == buttonMap['x']:
                DATA.ch1 = 127 # spin servo to max
                print("x")
                buttonMapState['x'] = True
            if event.button == buttonMap['circle']:
                print("circle")
                buttonMapState['circle'] = True
            if event.button == buttonMap['triangle']:
                print("triangle")
                buttonMapState['triangle'] = True
            if event.button == buttonMap['square']:
                print("square")
                buttonMapState['square'] = True
            if event.button == buttonMap['l1']:
                print("l1")
                buttonMapState['l1'] = True
            if event.button == buttonMap['r1']:
                print("r1")
                buttonMapState['r1'] = True
            if event.button == buttonMap['l3']:
                print("l3")
                buttonMapState['l3'] = True
            if event.button == buttonMap['r3']:
                print("r3")
                buttonMapState['r3'] = True
            if event.button == buttonMap['down']:
                print("down")
                buttonMapState['down'] = True
            if event.button == buttonMap['right']:
                print("right")
                buttonMapState['right'] = True
            if event.button == buttonMap['up']:
                print("up")
                buttonMapState['up'] = True
            if event.button == buttonMap['left']:
                print("left")
                buttonMapState['left'] = True
            if event.button == buttonMap['options']:
                print("options")
                buttonMapState['options'] = True
            if event.button == buttonMap['share']:
                print("share")
                buttonMapState['share'] = True
            if event.button == buttonMap['home']:
                print("home")
                buttonMapState['home'] = True
            if event.button == buttonMap['touchpad']:
                print("touchpad")
                buttonMapState['touchpad'] = True
        
        
        # RELEASED A DIGITAL BUTTON
        if event.type == pygame.JOYBUTTONUP:
            if event.button == buttonMap['x']:
                print("x released")
                buttonMapState['x'] = False
                DATA.ch1 = 0
            if event.button == buttonMap['circle']:
                print("circle released")
                buttonMapState['circle'] = False
            if event.button == buttonMap['triangle']:
                print("triangle released")
                buttonMapState['triangle'] = False
            if event.button == buttonMap['square']:
                print("square released")
                buttonMapState['square'] = False
            if event.button == buttonMap['l1']:
                print("l1 released")
                buttonMapState['l1'] = False
            if event.button == buttonMap['r1']:
                print("r1 released")
                buttonMapState['r1'] = False
            if event.button == buttonMap['l3']:
                print("l3 released")
                buttonMapState['l3'] = False
            if event.button == buttonMap['r3']:
                print("r3 released")
                buttonMapState['r3'] = False
            if event.button == buttonMap['down']:
                print("down released")
                buttonMapState['down'] = False
            if event.button == buttonMap['right']:
                print("right released")
                buttonMapState['right'] = False
            if event.button == buttonMap['up']:
                print("up released")
                buttonMapState['up'] = False
            if event.button == buttonMap['left']:
                print("left released")
                buttonMapState['left'] = False
            if event.button == buttonMap['options']:
                print("options released")
                buttonMapState['options'] = False
            if event.button == buttonMap['share']:
                print("share released")
                buttonMapState['share'] = False
            if event.button == buttonMap['home']:
                print("home released")
                buttonMapState['home'] = False
            if event.button == buttonMap['touchpad']:
                print("touchpad released")
                buttonMapState['touchpad'] = False
        
        # CHANGED AN ANALOG BUTTON
        if event.type == pygame.JOYAXISMOTION:
            analogMap[event.axis] = event.value
            # difference between the L2 & R2
            differece = (analogMap[5]+1)-(analogMap[4]+1)
            # deadzone of 0.2
            if abs(differece) < 0.2:
                throttle = 0
            else:
                throttle = int(differece* 66)
            DATA.left = throttle
            DATA.right = throttle

        #IF A BUTTON IS *STILL* HELD DOWN
        if buttonMapState['square']: # Handbrake
            throttle = throttle // 2
            if throttle < 40:
                throttle = 0
            DATA.left = throttle
            DATA.right = throttle


            
    DATA.left = constrain(DATA.left, -127, 127)
    DATA.right = constrain(DATA.right, -127, 127)
    
    
    if (time.time()-lastTime>0.4):
        #print(prevArray,"\t",ArrDATA)
        lastTime=time.time()
        ArrDATA = array.array('b',[DATA.left, DATA.right, DATA.ch1, DATA.ch2, DATA.ch3, DATA.ch4, DATA.ch5, DATA.ch6])
        print(DATA.right, analogMap[4], analogMap[5])
        #sock.sendto(ArrDATA, (UDP_IP, UDP_PORT))
        return ArrDATA
    if (prevArray != ArrDATA and time.time() - lastTime > 0.015):
        lastTime=time.time()
        ArrDATA = array.array('b',[DATA.left, DATA.right, DATA.ch1, DATA.ch2, DATA.ch3, DATA.ch4, DATA.ch5, DATA.ch6])
        print(DATA.right, analogMap[4], analogMap[5])
        #sock.sendto(ArrDATA, (UDP_IP, UDP_PORT))
        return ArrDATA
    



