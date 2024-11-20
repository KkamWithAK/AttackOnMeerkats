import array
import socket
UDP_IP = None
UDP_PORT = None
sock = None

def setup():
    global UDP_IP
    global UDP_PORT
    global sock
    UDP_IP = "169.254.218.236"
    UDP_PORT = 100
    #Local_IP = "169.254.153.129"
    #Local_Port = 4010
    sock = socket.socket(socket.AF_INET, # Internet 
                     socket.SOCK_DGRAM) # UDP
    
def sendData(ArrDATA: array):
    #print(UDP_IP)
    sock.sendto(ArrDATA, (UDP_IP, UDP_PORT))
    pass