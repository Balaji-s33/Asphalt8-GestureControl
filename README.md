# Asphalt8-GestureControl
A gesture controlled gaming system using an MPU6050 gyroscope and ESP8266, converting gesture inputs into keyboard controls for PC games like asphalt, forza horizon and etc.

---
## Features
- **Compact & Wireless Communication** – Uses ESP8266 with WiFi/Bluetooth for a seamless, wire-free gaming experience.
- **Customizable Controls** – Allows users to assign keys for drift, spin, nitro, and other in-game actions.
- **Real-time gesture-based game control** using an MPU6050 sensor.

---
## Hardware Requirements
- **ESP8266 (NodeMCU)**
- **MPU6050 Gyroscope & Accelerometer**
- **Breadboard**

---
## Software Requirements
- **Arduino IDE** (for programming ESP8266)
- **Python 3** (for running the control script)
- **pydirectinput** (for simulating keyboard inputs)

---
## Connections 

| ESP8266 | MPU6050 |
|---------|---------|
| GPIO 12 (D6) | SDA |
| GPIO 14 (D5) | SCL |
| 3.3V | VCC |
| GND | GND |

---
## Arduino Code
The ESP8266 reads data from the MPU6050 and sends movement commands via Serial. Upload the [Arduino Code](arduino_code.ino) to the ESP8266.

---
## Python Code
Run the [Python script](python_code.py) to the ESP8266.
 on your PC to process serial data and simulate keyboard input.

---
# Video Demonstration
Play this [video](https://youtu.be/oYzMg8GiY-M) for a demonstration of this project.
