#ifndef Actuators_h
#define Actuators_h 

#include <Arduino.h>

class SimpleMotor {     //This class can be used to drive a motor
private:                //Methods and variables placed here can't be accessed outside this class
  int resolution = 8;  //This is how many bits should be used for the duty cycle- 10 bits means (1<<10) = 2^10 = 1024 is full speed
  int frequency = 500;  //Frequency of the PWM- this number has a big effect on how your robot moves! I won't fully explain it here, but it's due to how the coils in your motor resist changes in current. Try adjusting this, and see how it reacts.
  int speed;            //The speed the motor is currently set to
  int pinForward;      //The PWM generator to use for the forward signal- which one you use doesn't matter, since they're all the same, however make sure to use a different one for each channel
  int pinBackward;      //The PWM generator to use for the backward signal

public:  //Methods and variables here can be called/accessed from the main loop
  SimpleMotor(int _pinForward, int _pinBackward);
  void setSpeed(int speed);
};

class Servo{
  const int frequency = 50;
  const int resolution = 14;
  int minPulse;
  int maxPulse;
  int pin;
  public:
  Servo(int _pin, int _minPulseMicros, int _maxPulseMicros);
  Servo(int _pin);
  void writeAngle(int _angle);
};

#endif