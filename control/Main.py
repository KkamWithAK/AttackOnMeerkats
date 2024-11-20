#### BINDS ALL THE SCRIPTS TOGEHTER###
### USED FOR EASY TESTING ###
import Networking
import GamePadControls
import array

def createUDP():
    Networking.setup()

def sendPackets():
    Networking.sendData("hi")
def createPygame():
    pass
def Control():
    while True:
        inputArray = GamePadControls.ReadInputs()
        sendPackets(inputArray)

    # set up pygame
    # while true, scan for user inputs
    # return data
    # send data
    pass