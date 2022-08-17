
#include "DHT.h"
#include <DS3231.h>

#include <SoftwareSerial.h>
SoftwareSerial HC06(10, 11); //HC06-TX Pin 10, HC06-RX to Arduino Pin 11

// DHT Sensor
#define DHTPIN 2     // Digital pin connected to the DHT sensor
#define DHTTYPE DHT11   // DHT 11
DHT dht(DHTPIN, DHTTYPE);

// RTC DS3231 sensor
// Init the DS3231 using the hardware interface
DS3231  rtc(SDA, SCL); // SDA - A4, SCL - A5

Time t;

// Defining variables
// For temperature
float temp = 0;
float conversionFactor = 0.48828;

// For humidity
float humidity = 0;

// For global time
int th = 0;
int tm = 0;
int ts = 0;

// For SW1 -> variable space.......................................
bool sw1ControlEnabled = false; // SW1 Auto control enabled
bool sw1TempControlEnabled = false; // SW1 Auto control enabled
int sw1Pin = 8; // on board pin 5

// SW1 on time
int sw1Onh = 3; // on hour
int sw1Onm = 13; // on minute
int sw1Ons = 0; // on second

// SW1 off time
int sw1Offh = 3; // off hour
int sw1Offm = 14; // off minute
int sw1Offs = 0; // off second

// SW1 on temperature
int sw1OnTemp = 0;

// SW1 off temperature
int sw1OffTemp = 0;


// For SW2 -> variable space.......................................
bool sw2ControlEnabled = false; // SW2 Auto control enabled
bool sw2TempControlEnabled = false; // SW2 Auto control enabled
int sw2Pin = 6; // on board pin 6

// SW2 on time
int sw2Onh = 0; // on hour
int sw2Onm = 0; // on minute
int sw2Ons = 0; // on second

// SW2 off time
int sw2Offh = 0; // off hour
int sw2Offm = 0; // off minute
int sw2Offs = 0; // off second

// SW2 on temperature
int sw2OnTemp = 0;

// SW2 off temperature
int sw2OffTemp = 0;


// For SW3 -> variable space.......................................
bool sw3ControlEnabled = false; // SW3 Auto control enabled
bool sw3TempControlEnabled = false; // SW3 Auto control enabled
int sw3Pin = 7; // on board pin 7

// SW3 on time
int sw3Onh = 0; // on hour
int sw3Onm = 0; // on minute
int sw3Ons = 0; // on second

// SW3 off time
int sw3Offh = 0; // off hour
int sw3Offm = 0; // off minute
int sw3Offs = 0; // off second

// SW3 on temperature
int sw3OnTemp = 0;

// SW3 off temperature
int sw3OffTemp = 0;



void setup() {
  Serial.begin(9600);
//  Serial.println(F("DHTxx test!"));
//  Timer1.initialize(2000000);
//  Timer1.attachInterrupt(updateSensorReadings);
  
  HC06.begin(9600); //Baudrate 9600  
  HC06.println(F("DHTxx test!"));

  // Initialize DHT sensor
  dht.begin();
   // Initialize the rtc object
  rtc.begin();

  // The following lines can be uncommented to set the date and time
    rtc.setDOW(TUESDAY);     // Set Day-of-Week to SUNDAY
    rtc.setTime(17, 27, 55);     // Set the time to 12:00:00 (24hr format)
    rtc.setDate(9, 8, 2022);   // Set the date to January 1st, 2014

  pinMode(sw1Pin, OUTPUT);
  pinMode(sw2Pin, OUTPUT);
  pinMode(sw3Pin, OUTPUT);
}



void loop() {
  // reading the serial input
  // extract the opcode
  /*
    available operations

    // First phase......................................................
    1. GET temperature and humidity -> OPCODE = (%a%)
    2. SET ON Switches 1, 2, 3 -> OPCODE = (%bsw11%)
    3. SET OFF Switches 1, 2, 3 -> OPCODE = (%bsw10%)

    // Second phase......................................................
    2. SET events -
      a. SET temperature threshold to on/off for switches 1, 2, 3 -> OPCODE = (%csw1tmp30#tmp20%)
      
      b. SET time to turn on the switches 1, 2, 3 -> OPCODE = (%esw1h02m30#h02m30%)
  */  
  while (HC06.available() > 0) {
    String msg = HC06.readString();
//    Serial.print("Message received: ");
    Serial.println(msg);
    int l = msg.length();
//    Serial.println(l);
    if (msg == "%a%\n") {
      //Serial.println("GET temperature and humidity");
      printSensor();
    }else if(msg[0] == '%' && msg[1] == 'b' && msg[l-2] == '%'){
      // Switch ON/OFF manual handle
      // Serial.println("SET ON/OFF Switches 1 or 2 or 3");
      swOnOffHandler(msg);
    }else if(msg[0] == '%' && msg[1] == 'e' && msg[l-2] == '%'){
      setTimerForSw(msg); // if it is for sw timer setting       
    }
    else if(msg[0] == '%' && msg[1] == 'c' && msg[l-2] == '%'){
      setTempForSw(msg);
    }
  }
  // handing events if time matches
  if(sw1ControlEnabled || sw2ControlEnabled || sw3ControlEnabled){
    handleTimerEvents();
  }
  if(sw1TempControlEnabled || sw2TempControlEnabled || sw3TempControlEnabled){
    handleTempEvents();
  }
  printStatus();
}

void handleTempEvents(){
  if(sw1TempControlEnabled){
    if(temp >= sw1OnTemp){
      digitalWrite(sw1Pin, HIGH);
    }else if(temp < sw1OffTemp){
      digitalWrite(sw1Pin, LOW);
    }
  }
  if(sw2TempControlEnabled){
    if(temp >= sw2OnTemp){
      digitalWrite(sw2Pin, HIGH);
    }else if(temp < sw2OffTemp){
      digitalWrite(sw2Pin, LOW);
    }
  }
  if(sw3TempControlEnabled){
    if(temp >= sw3OnTemp){
      digitalWrite(sw3Pin, HIGH);
    }else if(temp < sw3OffTemp){
      digitalWrite(sw3Pin, LOW);
    }
  }
}

void setTempForSw(String msg){
  //%csw1tmp30#tmp20%
//  int tempOn = String(msg[8]) + String(msg[9]).toInt();
//  int tempOff = String(msg[14]) + String(msg[15]).toInt();
  
  int tempOn = msg.substring(8, 10).toInt();
  int tempOff = msg.substring(14, 16).toInt();
  
  if(msg[4] == '1'){ // for SW 1 //bool sw1TempControlEnabled = false; 
    sw1TempControlEnabled = true;
    sw1OnTemp = tempOn;
    sw1OffTemp = tempOff;
  }
  else if(msg[4] == '2'){ // for SW 2 //bool sw2TempControlEnabled = false; 
    sw2TempControlEnabled = true;
    sw2OnTemp = tempOn;
    sw2OffTemp = tempOff;
  }
  else if(msg[4] == '3'){ // for SW 3 //bool sw3TempControlEnabled = false; 
    sw3TempControlEnabled = true;
    sw3OnTemp = tempOn;
    sw3OffTemp = tempOff;
  }
}

void handleTimerEvents(){
  
  t = rtc.getTime();
  
  int temp_h = t.hour;
  int temp_m = t.min;
  
  // if controlEnabled for sw1 then
  if(sw1ControlEnabled){
    // if time matches with on_time and currently sw1 is off
    if(temp_h == sw1Onh && temp_m == sw1Onm && (digitalRead(sw1Pin) == LOW)){
      // turn on sw1
      digitalWrite(sw1Pin, HIGH);
    }
    // if time matches with off_time and currently sw1 is on
    if(temp_h == sw1Offh && temp_m == sw1Offm &&  (digitalRead(sw1Pin) == HIGH)){
      // turn off sw1
      digitalWrite(sw1Pin, LOW);
    }
    
  }

  // if controlEnabled for sw2 then
  if(sw2ControlEnabled){
    // if time matches with on_time and currently sw2 is off
    if(temp_h == sw2Onh && temp_m == sw2Onm && (digitalRead(sw2Pin) == LOW)){
      // turn on sw2
      digitalWrite(sw2Pin, HIGH);
    }
    // if time matches with off_time and currently sw2 is on
    if(temp_h == sw2Offh && temp_m == sw2Offm &&  (digitalRead(sw2Pin) == HIGH)){
      // turn off sw2
      digitalWrite(sw2Pin, LOW);
    }    
  }

  // if controlEnabled for sw3 then
  if(sw3ControlEnabled){
    // if time matches with on_time and currently sw3 is off
    if(temp_h == sw3Onh && temp_m == sw3Onm && (digitalRead(sw3Pin) == LOW)){
      // turn on sw3
      digitalWrite(sw3Pin, HIGH);
    }
    // if time matches with off_time and currently sw3 is on
    if(temp_h == sw3Offh && temp_m == sw3Offm &&  (digitalRead(sw3Pin) == HIGH)){
      // turn off sw3
      digitalWrite(sw3Pin, LOW);
    }    
  }  
}

void setTimerForSw(String msg){
  //%esw1h02m30#h02m30%
  //0123456789
  
  int tempOn_h = msg.substring(6, 8).toInt();
  int tempOn_m = msg.substring(9, 11).toInt();
  int tempOff_h = msg.substring(13, 15).toInt();
  int tempOff_m = msg.substring(16, 18).toInt();
  
  if(msg[4] == '1'){ // for SW 1 //bool sw1ControlEnabled = false; 
    sw1ControlEnabled = true;
    if(msg[1] == 'e'){// sw1 ontime set
      sw1Onh = tempOn_h;
      sw1Onm = tempOn_m;
     // sw1 off time set
      sw1Offh = tempOff_h;
      sw1Offm = tempOff_m;
      }    
  }
  else if(msg[4] == '2'){
    sw2ControlEnabled = true;
    if(msg[1] == 'e'){// sw2 ontime set
      sw2Onh = tempOn_h;
      sw2Onm = tempOn_m;
     // sw2 off time set
      sw2Offh = tempOff_h;
      sw2Offm = tempOff_m;
    }
    
  }
  else if(msg[4] == '3'){
    sw3ControlEnabled = true;
    if(msg[1] == 'e'){// sw3 ontime set
      sw3Onh = tempOn_h;
      sw3Onm = tempOn_m;
     // sw3 off time set
      sw3Offh = tempOff_h;
      sw3Offm = tempOff_m;
    }
  }
}

void swOnOffHandler(String msg){
  if (msg[4] == '1') {
    // Switch 1
    if (msg[5] == '1') {
      // ON
      //Serial.println("Switch 1 ON");
      digitalWrite(sw1Pin, HIGH);
    }else if (msg[5] == '0') {
      // OFF
      //Serial.println("Switch 1 OFF");
      digitalWrite(sw1Pin, LOW);
    }
    sw1ControlEnabled = false;
    sw1TempControlEnabled = false;
  }else if (msg[4] == '2') {
    // Switch 2
    if (msg[5] == '1') {
      // ON
      //Serial.println("Switch 2 ON");
      digitalWrite(sw2Pin, HIGH);
    }else if (msg[5] == '0') {
      // OFF
      //Serial.println("Switch 2 OFF");
      digitalWrite(sw2Pin, LOW);
    }
    sw2ControlEnabled = false;
    sw2TempControlEnabled = false;
  }else if (msg[4] == '3') {
    // Switch 3
    if (msg[5] == '1') {
      // ON
      //Serial.println("Switch 3 ON");
      digitalWrite(sw3Pin, HIGH);
    }else if (msg[5] == '0') {
      // OFF
      //Serial.println("Switch 3 OFF");
      digitalWrite(sw3Pin, LOW);
    }
    sw3ControlEnabled = false;
    sw3TempControlEnabled = false;
  }  
}

void printStatus(){
//  Serial.print("SW1 Enabled: ");
//  Serial.print(sw1ControlEnabled);
//  Serial.print(", SW1 On Time: ");
//  Serial.print(String(sw1Onh) + "." + String(sw1Onm));
//  Serial.print(", SW1 Off Time: ");
//  Serial.print(String(sw1Offh) + "." + String(sw1Offm));
//  Serial.print(", SW1 status: ");
//  Serial.println(String(digitalRead(sw1Pin)));
//
//  Serial.print("SW2 Enabled: ");
//  Serial.print(sw2ControlEnabled);
//  Serial.print(", SW2 On Time: ");
//  Serial.print(String(sw2Onh) + "." + String(sw2Onm));
//  Serial.print(", SW2 Off Time: ");
//  Serial.print(String(sw2Offh) + "." + String(sw2Offm));
//  Serial.print(", SW2 status: ");
//  Serial.println(String(digitalRead(sw2Pin)));
//
//  Serial.print("SW3 Enabled: ");
//  Serial.print(sw3ControlEnabled);
//  Serial.print(", SW3 On Time: ");
//  Serial.print(String(sw3Onh) + "." + String(sw3Onm));
//  Serial.print(", SW3 Off Time: ");
//  Serial.print(String(sw3Offh) + "." + String(sw3Offm));
//  Serial.print(", SW3 status: ");
//  Serial.println(String(digitalRead(sw3Pin)));
  Serial.print("SW1 onTemp: ");
  Serial.print(sw1OnTemp);
  Serial.print(" /offTemp: ");
  Serial.println(sw1OffTemp);
}

void printSensor() {
  
  // Wait a few seconds between measurements.
  delay(2000);

  // Reading temperature or humidity takes about 250 milliseconds!
  // Sensor readings may also be up to 2 seconds 'old' (its a very slow sensor)
  float h = dht.readHumidity();
  // Read temperature as Celsius (the default)
//  float t = dht.readTemperature();
  float t = analogRead(A0) * conversionFactor;
  temp = t;
  
  // Read temperature as Fahrenheit (isFahrenheit = true)
  float f = dht.readTemperature(true);

  // Check if any reads failed and exit early (to try again).
  if (isnan(h) || isnan(t) || isnan(f)) {
    HC06.println(F("Failed to read from DHT sensor!"));
    return;
  }

  // Compute heat index in Fahrenheit (the default)
  float hif = dht.computeHeatIndex(f, h);
  // Compute heat index in Celsius (isFahreheit = false)
  float hic = dht.computeHeatIndex(t, h, false);

  HC06.print(F(" Humidity: "));
  HC06.print(h);
  HC06.print(F("%  Temperature: "));
  HC06.print(t);
  HC06.print(F("C "));
  HC06.print(f);
  HC06.print(F("F  Heat index: "));
  HC06.print(hic);
  HC06.print(F("C "));
  HC06.print(hif);
  HC06.print(F("F"));
  HC06.println(rtc.getTimeStr());
}
