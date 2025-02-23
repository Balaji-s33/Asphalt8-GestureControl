#include <Wire.h>
#include <MPU6050.h>
MPU6050 mpu;
const int16_t INVALID_THRESHOLD = 100;
void setup() {
  Serial.begin(115200);  
  Wire.begin(12, 14);  
  mpu.initialize();
  if (!mpu.testConnection()) {
    Serial.println("MPU-6050 connection failed.");
    while (1);
  } else {
    Serial.println("MPU-6050 connected successfully.");
  }
}
void loop() {
  int16_t ax, ay, az;
  mpu.getAcceleration(&ax, &ay, &az);
  if (abs(ax) < INVALID_THRESHOLD && abs(ay) < INVALID_THRESHOLD && abs(az) < INVALID_THRESHOLD) {
    Serial.println("Data Invalid");
  } else {
    if (ax > 5000 && ay > 9000) {
      Serial.println("Left Drift");
    } else if (ax < -5000 && ay > 10000) {
      Serial.println("Right Drift");
    } else if (az < 18000 && ax > 6000) {
      Serial.println("Left side");
    } else if (az < 18000 && ax < -6000) {
      Serial.println("Right side");
    } else if (ay < -4000) {
      Serial.println("Forward");
    } else if (ay > 5000) {
      Serial.println("Backward");
    } else {
      Serial.println("Waiting for input");
    }
  }
  delay(100);
}