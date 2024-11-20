#include <Arduino.h>
#include "Actuators.h"


SimpleMotor::SimpleMotor(int _pinForward, int _pinBackward) {  //This code will automatically run when the object is created

  ledcAttach(_pinForward, frequency, resolution);  //Set up PWM on the pins selected
  ledcAttach(_pinBackward, frequency, resolution);

  pinForward = _pinForward;  //_pinForward is a temporary variable that only exists in this function- we'll copy the value to a permanent variable, since we need it later
  pinBackward = _pinBackward;
}

void SimpleMotor::setSpeed(int speed) {                         //This function sets the speed of the motor, and reverses it if it's negative. What does the commented out function do? I dunno, wrote it last week.
  speed = constrain(speed, -1 << resolution, 1 << resolution);  //Limit speed to 100% on
  if (speed < 0) {
    speed *= -1;                    //The PWM can't make a negative duty wave, set it to positive and send it to the reverse pin
    ledcWrite(pinForward, 0);       //Set the forward pin to zero- it's backward time
    ledcWrite(pinBackward, speed);  //Set the duty cycle for the backward pin to the desired speed
  } else if (speed > 0) {
    ledcWrite(pinBackward, 0);
    ledcWrite(pinForward, speed);
  } 
  //else {
  //  ledcWrite(pinForward, 0);  //If the speed is zero, turn both pins off
  //  ledcWrite(pinBackward, 0);
  //}
  else{ //You can only have one "else" statement- delete the above if you are using this one
    ledcWrite(pinForward, 1<<resolution); //"<<" means bitshift: a<<b == a*(2^b). Here, 1<<resolution (resolution being 8) means 255- or 100% duty
    ledcWrite(pinBackward, 1<<resolution);
  }
}


Servo::Servo(int _pin, int _minPulseMicros, int _maxPulseMicros) {
  int periodus = 1000000 / 50;  //1 sec = 1 000 000 micros
  minPulse = float(1 << resolution) * (float(_minPulseMicros) / float(periodus));
  maxPulse = float(1 << resolution) * (float(_maxPulseMicros) / float(periodus));
  pin = _pin;
  pinMode(_pin, OUTPUT);
  ledcAttach(_pin, frequency, resolution);
}

Servo::Servo(int _pin) {
  int periodus = 1000000 / 50;  //1 sec = 1 000 000 micros
  int minPulse = float(1 << resolution) * (float(1000) / float(periodus));
  int maxPulse = float(1 << resolution) * (float(2000) / float(periodus));
  pin = _pin;
  pinMode(_pin, OUTPUT);
  ledcAttach(_pin, frequency, resolution);
}

void Servo::writeAngle(int _angle) {
  int angleDuty = map(_angle, 0, 180, minPulse, maxPulse);  //The map function scales the input variable from the first range to the second
  ledcWrite(pin, angleDuty);
}