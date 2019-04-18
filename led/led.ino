/*
Created on Apr 16, 2019

@author: Venkat Prasad Krishnamurthy
@author: Jaydeep Shah
*/

#include <LiquidCrystal.h>

// initialize the library by associating any needed LCD interface pin
// with the arduino pin number it is connected to
const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

String substring(char s[], int p, int l) {
  String ret = "";
   int c = 0;
   
   while (c < l) {
      ret[c] = s[p+c-1];
      c++;
   }
   ret[c] = '\0';
   return ret;
}



void setup() {
  // set up the LCD's number of columns and rows:
  lcd.begin(16, 2);
  // Print a message to the LCD.
  Serial.begin(9600);
}

void loop() {
  
  while (Serial.available() > 0) {
    
    String text = Serial.readString();
    lcd.setCursor(0,0);
    lcd.print("Time:"+text.substring(0,5));
    lcd.setCursor(0,1);
    lcd.print("Weather:"+text.substring(6,11)+"F");
  // print the number of seconds since reset:
        }
}
