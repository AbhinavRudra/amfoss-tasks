# Servo Motor In Arduino

 Here I have used an  _arduino uno r3_ , _breadboard_ , a _photoresistor_ ,an _lcd screen 16x2_ , a _micro server_ , 2 _resistors_ , a _photoresistor_ , a _potentiometer_ and 27 _wires_ to perform this task .
 
 In this circuit I have connected the lcd ports to the breadboard as well as the arduino , when the intensity of the light reaches a value greater than 300 ( which indicates a tiny level of brightness ) the servo motor moves to 180 degree angle (  if (val > 300){ myServo.write(180); }  ) and when the servo motor rotates the lcd display shows CLOSE ( lcd.print("CLOSE"); ) and if the process does not happens i.e the light intensty does not crossess 300 then the lcd display shows OPEN . All these events are done inside a loop , thus it will be running until the user provide any initiative to break the loop . 

I also faced some issues regarding making the project public, as when I sent the project, it showed a "forbidden error" message. Now, I have solved the issue and tried it again, and it's working. 


Link for the tinkercad project :
https://www.tinkercad.com/things/92WGZ6D4LsW-arduino-roof-?sharecode=-5DAXBdTzy_yJdZDDF2ef3DZVM1TxReDrGgKVE7ky3U