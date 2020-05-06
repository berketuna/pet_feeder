// Include the Arduino Stepper.h library:
#include <Stepper.h>

// Define number of steps per rotation:
const int enablePin = 6;
const int stepPin = 7;
const int dirPin = 8;
const int stepsPerRevolution = 2048;
int command;
int button;
// Wiring:
// Pin 9  to IN1 on the ULN2003 driver
// Pin 10 to IN2 on the ULN2003 driver
// Pin 11 to IN3 on the ULN2003 driver
// Pin 12 to IN4 on the ULN2003 driver

// Create stepper object called 'motor', note the pin order:
Stepper motor = Stepper(stepsPerRevolution, 9, 11, 10, 12);
					//  9, 11, 10, 12
void setup() {
  // Set the speed:
  motor.setSpeed(15);
  pinMode(A0,INPUT_PULLUP);
  pinMode(stepPin, OUTPUT);
  pinMode(dirPin, OUTPUT);
  pinMode(enablePin, OUTPUT);
  // Begin Serial communication at a baud rate of 9600:
  Serial.begin(9600);
}

void loop() {
digitalWrite(dirPin,HIGH);
digitalWrite(enablePin,HIGH);
button = digitalRead(A0);
Serial.println(button);
  	// Step one revolution in one direction when button is pressed (to reverse, put/delete ' - ' before stepsPerRevolution:
	if (button == 0){
     digitalWrite(enablePin,LOW);
      //motor.step(stepsPerRevolution);
     for(int x = 0; x <200; x++){
      digitalWrite(stepPin,HIGH);
      delayMicroseconds(1000);
      digitalWrite(stepPin,LOW);
      delayMicroseconds(1000);
     }
  }
delay(200);
}
