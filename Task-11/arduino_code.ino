#include<Servo.h>
Servo servomotor;
void setup() {
  servomotor.attach(3); //servomotor connect to arduino ~ PWM pin 3
}

void loop() {
  // Analog input from LDR to A1 pin:
  int ldr_input_val= analogRead(A1);
  
  //servmotor rotate 180
  if(ldr_input_val<300){
    servomotor.write(180);
  }
  
   //servmotor rotate 0
  else{
    servomotor.write(0);
  } 
}