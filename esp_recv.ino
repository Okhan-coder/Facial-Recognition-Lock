#Modified from source code provided at:
#https://siytek.com/esp8266-udp-send-receive/

#include <ESP8266WiFi.h>
#include <WiFiUdp.h>

#define WIFI_SSID "esp8266"
#define WIFI_PASSWORD "lock"
#define UDP_PORT 4210

//UDP instance
WiFiUDP udp;
char recv_packet[255];

void setup()
{
	//Set up serial port
	Serial.begin(115200);
	Serial.println();
	
	//Start WiFi
	WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
	
	//Connecting to WiFi
	Serial.print("Connecting to ");
	Serial.print(WIFI_SSID);

	//While WiFi is NOT connected, continue looping
	while (WiFi.status() != WL_CONNECTED)
	{
		delay(100);
		Serial.print(".");
	}
	
	//Connected to WiFi
	Serial.println();
	Serial.print("Connected. IP address: ");
	Serial.println(WiFi.localIP());

	//Listen to UDP port for incoming packet
	UDP.begin(UDP_PORT);
	Serial.print("Listening on UDP port ");
	Serial.println(UDP_PORT);
}

void loop()
{
	//Store size if packet received
	int packetSize = UDP.parsePacket();

	if (packetSize)
	{
		Serial.print("Received packet. Unlocking!");
	}
}