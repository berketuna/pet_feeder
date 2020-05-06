const int enablePin = 6;
const int stepPin = 7;
const int dirPin = 8;
const int stepsPerRevolution = 200;
int command;
int button;

void setup() {
  
  pinMode(A0,INPUT_PULLUP);
  pinMode(stepPin, OUTPUT);
  pinMode(dirPin, OUTPUT);
  pinMode(enablePin, OUTPUT);
  
  digitalWrite(dirPin,HIGH); //Clockwise direction
  digitalWrite(enablePin,HIGH); //Setting the driver off
  Serial.begin(9600); // Begin Serial communication
}

void loop() {
button = digitalRead(A0);
Serial.println(button);
  	// Step one revolution in one direction when button is pressed (to reverse, put/delete ' - ' before stepsPerRevolution:
	if (button == 0){
     digitalWrite(enablePin,LOW); //Setting the driver on
     for(int x = 0; x < 2*stepsPerRevolution; x++){
      digitalWrite(stepPin,HIGH);
      delayMicroseconds(500);
      digitalWrite(stepPin,LOW);
      delayMicroseconds(500);
     }
     digitalWrite(enablePin,HIGH); //Setting the driver off
  }
delay(200);
}
