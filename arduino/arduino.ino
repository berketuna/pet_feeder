// Include the Arduino Stepper.h library:
#include <Stepper.h>

// Define number of steps per rotation:
const int stepsPerRevolution = 2048;
int command;

// Wiring:
// Pin 9  to IN1 on the ULN2003 driver
// Pin 10 to IN2 on the ULN2003 driver
// Pin 11 to IN3 on the ULN2003 driver
// Pin 12 to IN4 on the ULN2003 driver

// Create stepper object called 'motor', note the pin order:
Stepper motor = Stepper(stepsPerRevolution, 9, 11, 10, 12);

void setup() {
  // Set the speed:
  motor.setSpeed(15);
  
  // Begin Serial communication at a baud rate of 9600:
  Serial.begin(9600);
}

void loop() {
  // Step one revolution in one direction:
  if (Serial.available()){
    command = Serial.parseInt();
    if (command == 1){
      Serial.println("Turning clockwise");
      motor.step(stepsPerRevolution);
    }
    if (command == -1){
      Serial.println("Turning counterclockwise");
      motor.step(-stepsPerRevolution);
    }
  }
}
