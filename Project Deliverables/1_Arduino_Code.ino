#include<LiquidCrystal.h>
int gasReading = 0;
int LED = 9;
int Buzzer = 8;
int gasSensor = A0;
int flag = 1;
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);
void setup()
{
 lcd.begin(16, 2);
  pinMode(LED, OUTPUT);
  pinMode(Buzzer, OUTPUT);
  pinMode(gasSensor, INPUT);
}

void loop()
{
  gasReading = analogRead(gasSensor);
  String p = "Gas"+gasReading;
  lcd.setCursor(0,0);
  lcd.print(String("Sensor value:")+String(gasReading));
  if(gasReading>400){
    if(flag == 0) {
      lcd.setCursor(0,1);
      lcd.print("                    ");
    }
    flag=1;
    lcd.setCursor(0,1);
    lcd.print("Gas Detected");
    digitalWrite(LED, HIGH);
    digitalWrite(Buzzer, HIGH);
  }else {
    if(flag == 1) {
      lcd.setCursor(0,1);
      lcd.print("                    ");
    }
    flag=0;
    lcd.setCursor(0,1);
    lcd.print("No Gas Detected");
    digitalWrite(LED, LOW);
    digitalWrite(Buzzer, LOW);
  }
  delay(500);
}