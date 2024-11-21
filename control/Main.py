#### BINDS ALL THE SCRIPTS TOGEHTER###
### USED FOR EASY TESTING ###
import Networking
import GamePadControls
import array
import time
import socket

def createUDP(): # create connection
    Networking.setup()

def sendPackets(DataArray: array): # send data to esp32
    Networking.sendData(DataArray)
def createPygame(): # initialise pygame
    pass
def Control(): # Get user inputs
    inputArray = GamePadControls.ReadInput()
    if inputArray != None:
        # UNCOMMENT THIS !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        sendPackets(inputArray)
        pass
    # set up pygame
    # while true, scan for user inputs
    # return data
    # send data
    pass
def main():
    createUDP()
    while True:
        Control()
main()
       