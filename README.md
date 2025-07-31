# 🚌 3-in-1 Smart Bus Safety System

A combined project with **3 key safety features** designed for public transport (especially free government buses):

---

## 🚦 1. Drowsiness Detection System (Driver Safety)
- Uses a computer camera to monitor the driver's eyes.
- If the driver closes eyes for 3–4 seconds → triggers **buzzer alert** and **stops the motor**.
- Prevents accidents caused by sleepy driving.

---

## 🔥 2. Smoke Detection System (Fire Safety)
- Uses an **MQ-2 gas sensor** to detect smoke or gas leaks inside the bus.
- Alerts through a buzzer and optionally sends a warning.

---

## 📊 3. Passenger Counter System
- Uses **IR sensors** to count how many passengers enter and exit.
- Displays real-time count on an LCD screen.
- Helps in data collection and avoiding overloading.

---

## 📢 Bonus: In-Bus Advertisement Display
- Uses LCD to show ads for **local businesses**.
- Useful for recovering bus costs in **free transport services**.
- Promotes local entrepreneurship and makes public transport smarter.

---

## 🧠 Tech Used
- Arduino Uno
- MQ-2 Gas Sensor
- IR Sensors
- LCD Display
- Camera for Drowsiness Detection
- Buzzer
- Wires & Breadboard

---

## 🤖 Code Files
- `smoke_detection.ino` – Fire & gas alert
- `passenger_counter.ino` – IR-based people counting
- `advertisement_system.ino` – Display for ads
- `drowsiness.py` – Python code for fatigue detection

---

## 👨‍🔧 Made By
Vikas Nayak, 2nd year Mechanical Engineering  
GitHub: [your GitHub profile link]

---

## 🌟 Future Improvements
- Add GPS + GSM module for location & message alerts
- Solar backup for rural areas
- Central data collection for smart city integration
