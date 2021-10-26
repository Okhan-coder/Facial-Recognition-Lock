//Modified from source code provided at:
//https://siytek.com/esp8266-udp-send-receive/

#include <ESP8266WiFi.h>
#include <WiFiUdp.h>

#define WIFI_SSID "SSJCPL Guest"
#define WIFI_PASSWORD ""
#define UDP_PORT 4210

//UDP instance
WiFiUDP udp;
char recv_packet[255];
int pin = 2;

void setup()
{
	//Initialize GPIO 2 as an output
	pinMode(pin, OUTPUT);

  //TESTING
  //Initialize LED ON
  digitalWrite(pin, LOW);
  
	//Set up serial port
	Serial.begin(115200);
	Serial.println();
	
	//Start WiFi
	WiFi.begin(WIFI_SSID);
	
	/*
	//Connecting to WiFi
	Serial.print("Connecting to ");
	Serial.print(WIFI_SSID);
  */

	//While WiFi is NOT connected, continue looping
	while (WiFi.status() != WL_CONNECTED)
	{
		delay(100);
		Serial.print(".");
	}
  digitalWrite(pin, HIGH);
  delay(1000);
  digitalWrite(pin,LOW);
	
	//Connected to WiFi
	Serial.println();
	Serial.print("Connected. IP address: ");
	Serial.println(WiFi.localIP());
 
  digitalWrite(pin, HIGH);
  delay(1000);
  digitalWrite(pin,LOW);

	//Listen to UDP port for incoming packet
	udp.begin(UDP_PORT);
	Serial.print("Listening on UDP port ");
	Serial.println(UDP_PORT);
}

void loop()
{
	//Store size if packet received
	int packetSize = udp.parsePacket();
  
	if (packetSize)
	{    
		Serial.print("Received packet. Unlocking!");
		digitalWrite(pin, HIGH);	//turn the LED on (HIGH is the voltage level)	    
    delay(3000);
    digitalWrite(pin, LOW);
	}
}
