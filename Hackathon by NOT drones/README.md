# Drone Firmware Development Project
## SkyFrontier Hackathon – IIT Gandhinagar

### Overview
This repository contains the firmware development work carried out during the **SkyFrontier Drone Firmware Hackathon** conducted at **IIT Gandhinagar**, in collaboration with **NOT Drones Innovations Pvt. Ltd.**

The project focuses on developing and testing firmware for a **custom ESP32-based quadrotor drone**, with emphasis on real-world embedded control challenges such as sensor noise, thrust dead-band, actuator nonlinearity, and manual PID tuning.  
The goal was to achieve **stable and predictable manual flight** using onboard sensors and embedded control logic.

---

### Repository Contents

#### **1. Technical Documentation**
**File:** `NOT_drones.pdf`

This PDF contains the complete technical report of the project. It explains:
- Drone physical parameters and experimental thrust testing  
- Identification of thrust dead-band and its effect on flight behavior  
- Dynamic modeling of translational and rotational motion  
- Open-loop stability analysis  
- Cascaded control architecture for attitude and altitude control  
- PID controller design and manual tuning methodology  
- Sensor fusion using complementary and Kalman filtering  
- Final control results, limitations, and future scope  

This document should be referred to for **theoretical background, control design decisions, and validation results**.

---

#### **2. Drone Firmware (Receiver Code)**
**File:** `hackathon.zip`

This zip file contains the firmware that runs on the **drone (receiver unit)**.  
It includes:
- IMU and barometer initialization and validation  
- Sensor data processing and state estimation  
- Complementary filter for attitude estimation  
- Kalman filter for altitude estimation  
- PWM-based motor control  
- Arming and disarming safety logic  
- PID control for roll, pitch, yaw, and altitude  
- Thrust bias compensation to overcome dead-band  
- Navigation and status LED control  

This code is responsible for **all onboard control, stabilization, and safety functions** of the drone.

---

#### **3. Controller Firmware (Transmitter Code)**
**File:** `hackathon_controller.zip`

This zip file contains the firmware for the **remote controller (transmitter unit)**.  
It includes:
- Joystick and switch input reading  
- Mapping of user inputs to roll, pitch, yaw, and throttle  
- Wireless communication with the drone  
- Arming and disarming commands  
- Emergency motor stop functionality  
- User feedback through LEDs  

This code serves as the **human–machine interface** for manual flight control.

---

### How to Navigate the Project
1. Start with the **technical documentation PDF** to understand the control strategy and results.  
2. Review the **controller firmware** to see how pilot commands are generated and transmitted.  
3. Study the **drone firmware** to understand sensor fusion, control loops, and motor actuation.

---

### Current Status
- Manual flight control implemented  
- Sensor fusion and filtering validated  
- PID gains manually tuned and tested  
- Stable and predictable response achieved under controlled conditions  
- Some limitations remain due to sensor noise, hardware asymmetry, and thrust nonlinearity  

---

### Disclaimer
This project was developed strictly for **educational and research purposes** as part of the IIT Gandhinagar workshop and hackathon.  
The hardware platform and reference materials are provided by **NOT Drones Innovations Pvt. Ltd.**  
Commercial use of this code or documentation is not permitted without prior authorization.

---

### Acknowledgements
We thank **NOT Drones Innovations Pvt. Ltd.** for providing the drone kits, documentation, and mentorship, and **IIT Gandhinagar** for hosting the workshop and hackathon.

---

End of README
