#include <WiFi.h>       //A collection of objects and functions for using WiFi on the ESP32
#include "Actuators.h"  //This code is in the other tabs at the top of the IDE. Putting it here will de-clutter our code.

const char *ssid = "Kaamil";    //The SSID of your hotspot, or network name
const char *password = "password"; //The password of your network

WiFiUDP Udp;  //Set up an object that handles UDP

//Here we'll define variables for setting a static IP address. This way, there's no risk of your robot suddenly changing addresses.
//IPAddress local_ip(192, 168,137, 104);  //This is the static IP address that the ESP32 will try to use **** MAX'S IP ADRESS
//IPAddress gateway(172,22,157,201); //This is the gateway address that will be used by a laptop ****** MAX'S LAPTOP ADRESS
//IPAddress gateway(192, 168, 43, 1); //This is the gateway for most android phones

IPAddress local_ip(172,20,10,3); // Kaamil's IPHONE
IPAddress gateway(172,20,10,2); // Kaamil's LAPTOP

IPAddress subnet(255, 255, 0, 0);

byte packetBuffer[255];  //We'll store the bytes from the UDP packet here. It can have up to 255 elements, although we'll only use a few

unsigned int localPort = 100;  //Port number- make sure this is the same in both the python script and here

SimpleMotor left(8,9);  //Make a motor object, to represent the left motor
//SimpleMotor left2(14,13);  //Make a motor object, to represent the left motor
//SimpleMotor right2(16,15);
SimpleMotor right(10,11);
Servo rightServo(6, 500, 2500);
Servo leftServo(7, 500, 2500);
int len;        //number of bytes recieved

void setup() {
  Serial.begin(115200);
  startWiFi();
}

void loop() {
  while (WiFi.status() != WL_CONNECTED) {  //If we're disconnected
    rgbLedWrite(48,0,0,30);
    WiFi.begin(ssid, password);
    Serial.println("reconnecting");
    delay(100);
  }

  rgbLedWrite(48, 0, 55, 0);
  int packetSize = Udp.parsePacket();  //Grab the packet data. The actual data is stored inside the Udp object, but the function returns a number stored in packetSize that is bigger than zero if there is data

  if (packetSize) {                     //If packet size isn't zero, ie if there is data
    len = Udp.read(packetBuffer, 8);  //Take everything out of the packet, and put it in our buffe
    for (int i = 0; i < packetSize; i++) {
      Serial.print((int8_t)packetBuffer[i]);
      Serial.print(" ");
    }
    Serial.println();
  }


  int speedLeft = (int8_t)packetBuffer[0]; //The packet is of datatype byte- this goes from 0-255. We want -127 to 128, so we'll use (int8_t) to convert it
  int speedRight = (int8_t)packetBuffer[1];
  int servoPos = packetBuffer[2];
  int servoPos2 = packetBuffer[3];
  left.setSpeed(speedLeft);
  right.setSpeed(speedRight);
  rightServo.writeAngle(servoPos);
  //left2.setSpeed(speedLeft);
  //right2.setSpeed(speedRight);
  leftServo.writeAngle(servoPos2);



  delay(5);
}

void startWiFi(){
  Serial.println("Start");
  rgbLedWrite(48, 55, 0, 0);
    if (!WiFi.config(local_ip, gateway, subnet)) {                      //Try to configure a static IP address. If it doesn't work, print a helpful and informative error message
    Serial.println("Horrible turn of events, no static IP for you");  //TODO: replace with helpful and informative error message
  }

  WiFi.mode(WIFI_STA);         //Set WiFi mode. Station mode (WIFI_STA) means connected to a outside network, instead of broadcasting your own.
  WiFi.begin(ssid, password);  //Start WiFi, using the network name and password we set earlier

  while (WiFi.status() != WL_CONNECTED) {  //Run this code as long as WiFi isn't connected
    Serial.println("connecting");
    delay(100);
  }
  

  Udp.begin(localPort);            //Start listening on port "localPort", a port number we set earlier
  delay(50);                      //Wait a bit
  Serial.println(WiFi.localIP());  //Print out the IP address we're using
  rgbLedWrite(48, 0, 55, 0);
}
