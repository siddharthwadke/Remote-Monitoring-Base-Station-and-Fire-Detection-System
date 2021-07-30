# Remote-Monitoring-Base-Station-and-Fire-Detection-System
ECE692 Embedded Computing Systems - Embedded System Project

## Contents
* Introduction
* Componants

## <ins>**Introduction:**</ins>
### _Remote Monitoring Base Station_
• Monitor environmental parameters like Temperature and Relative Humidity, Air Quality parameters like CO 2 and CO Level, Methane and Butane Gas Level, LPG Level remotely to keep a track of environmental pollution
• Rather than having a monitoring station at every city / county, we can have a remotely monitoring base station which can monitor multiple cities from a single base station.

### _Fire Detection System_
• Monitor parameters like temperature and smoke to detect / prevent Fire.
• In case of emergencies, the system will notify the residents and neighbors for Fire Alert through SMS.
• In this way, the residents can be alerted even when they are not at home which will prevent any major loss of life or property.
• Also, the neighbors are notified which can in return help those who are in need and can even take precautionary actions.

## <ins>**Componants:**</ins>
*	Transmitter
	1. FRDM KL25Z
	2. nRF24L01+
	3. DHT11 Temperature Humidity Sensor
	4. MQ135 Air Quality Sensor
	5. MQ4 Gas (CH4, LPG) Sensor


*	Receiver
	1. FRDM KL25Z
	2. nRF24L01+

*	Alert System
	1. Arduino Mega 2560
	2. SIM800L Module
	3. Buzzer Alarm Module


## <ins>**Programming Language:**</ins>
C++
## <ins>**IDE:**</ins>
CLion, MBED

