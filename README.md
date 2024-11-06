# 🚨 Distance Detection and Alert System Using Raspberry Pi

This project demonstrates a **distance detection and alert system** using a Raspberry Pi with an ultrasonic distance sensor, RGB LED, buzzer, and button for user control. The system continuously monitors the distance of objects within its range and provides both visual and auditory feedback based on the detected distance.

🌟 **Ideal for**: Obstacle detection or proximity alert systems, with applications in robotics, security, and accessibility devices.

---

## 🔑 Key Features

- **Distance Measurement**: Uses an ultrasonic sensor to measure distance and convert it to centimeters.
  
- **Visual Alerts**: An RGB LED changes color based on the distance:
  - 🟢 **Green**: Object is far (more than 20 cm away).
  - 🔵 **Blue**: Object is at a moderate distance (10 to 20 cm).
  - 🔴 **Red**: Object is near (less than 10 cm).
  
- **Auditory Alerts**:
  - 🔇 **No sound** when the object is far.
  - 🔔 **Beeps intermittently** at a moderate distance.
  - 🔊 **Continuous tone** when the object is very close.

- **Button Control**: 🛑 A button toggles the buzzer sound on or off, allowing the user to mute alerts if necessary.

---

## 🛠 Hardware Components

- **Raspberry Pi** 🖥️
- **Ultrasonic Distance Sensor** 📏
- **RGB LED** (to indicate distance range visually)
- **Buzzer** 🔊 (for auditory feedback)
- **Button** 🛑 (to enable/disable buzzer sound)

---

## ⚙️ How It Works

1. **Distance Sensing**: The ultrasonic sensor continuously measures the distance from an object.
2. **Feedback Control**: Based on the measured distance, the system changes the RGB LED color and activates or deactivates the buzzer.
3. **User Control**: The button allows the user to toggle the buzzer on or off, providing flexibility in alert management.

---

## 💻 Project Code

The Python code uses the `gpiozero` library for easy access to GPIO pins and threading for running the distance reading loop in a separate thread.
