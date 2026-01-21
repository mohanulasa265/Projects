# Drona Aviation – Flight Control & Sensor Integration  
## Inter-IIT Tech Meet | Aerial Robotics Problem Statement

---

## Overview

This repository contains the flight-control firmware development and validation work carried out as part of the **Drona Aviation Inter-IIT Tech Meet Problem Statement**.  
The project focuses on low-level control logic, sensor integration, and structured testing methodologies for nano-UAV platforms based on the **Pluto ecosystem**.

The work is built on **MagisV2**, Drona Aviation’s open-source flight controller firmware, and extends it through modular APIs, sensor-driven stabilization logic, and safe flight-testing practices suitable for GPS-denied indoor environments.

---

## Problem Statement Objective

The core objectives of this problem statement were:

- Development of stable and extensible **flight control firmware**
- Integration of multiple onboard sensors for **state estimation**
- Implementation of **safe, incremental testing strategies**
- Adherence to **Inter-IIT Tech Meet rules and Drona Aviation safety guidelines**

---

## System Architecture

### Firmware Base
- MagisV2 (C++ port of Cleanflight)
- Object-oriented, API-driven design
- Compatible with PlutoX2 / Primus X2 flight controllers

### Sensors Integrated
- **Optical Flow Sensor (PAW3903E1)**  
  Used for horizontal motion estimation in GPS-denied conditions
- **Time-of-Flight Sensor (VL53L1X)**  
  Used for precise altitude measurement and height-hold control
- **IMU (ICM-20948)**  
  9-axis inertial sensing for attitude estimation and stabilization

### Control Framework
- PID-based attitude and stabilization control
- Sensor data abstraction via Magis APIs
- Incremental enablement of flight modes (hover, position hold, etc.)

---

## Testing and Validation Strategy

All testing was performed in progressive and controlled stages to ensure safety and repeatability:

1. **Sensor-only dry runs**  
   Validation of IMU, optical flow, and ToF sensor data without motor actuation

2. **Hand-held motor response testing**  
   Verification of PID response and motor mapping without free flight

3. **Ground-based tethered tests**  
   Initial tuning of control gains and detection of oscillations or drift

4. **Low-throttle hover attempts**  
   Controlled lift-off to identify instability early

5. **Incremental feature activation**  
   Flight modes enabled one at a time to isolate faults

This staged approach minimizes risk and allows deterministic debugging.

---

Repository Structure

.
├── src
│ └── main
│ └── API
│ ├── FC-Control # Control logic
│ ├── FC-Data # Sensor and state data
│ ├── Motor # Motor control interface
│ ├── RC-Interface # Receiver input handling
│ └── Scheduler-Timer # Loop timing and scheduling
│
├── docs
│ └── testing # Safety and testing methodology
│
├── PlutoPilot.cpp # User control loop
├── PlutoPilot.h # Core firmware interface
├── Makefile
└── README.md

---

## Usage Instructions

1. Clone the repository
2. Open the project in **Pluto IDE**
3. Select the target board (Primus X2 / PlutoX2)
4. Implement control logic inside `plutoLoop()`
5. Flash firmware and follow the defined testing stages

> **Note:** Do not attempt free flight without completing sensor validation and tethered tests.

---

## Compliance and Safety

- Fully compliant with **Inter-IIT Tech Meet Rule Book**
- Follows **Drona Aviation Flight Control Testing & Safety Guidelines**
- Designed for indoor, GPS-denied testing environments
- Emphasis on reproducibility, safety, and fault isolation

---

## Results and Learnings

- Reliable sensor data acquisition under varying lighting conditions
- Stable altitude estimation using Time-of-Flight sensing
- Predictable motor response after incremental PID tuning
- Clear separation between hardware abstraction and control logic

---

## Acknowledgements

- Drona Aviation Pvt. Ltd. for the problem statement and platform
- Inter-IIT Tech Meet Organizing Committee
- Open-source contributors to MultiWii, Baseflight, and Cleanflight
- MagisV2 development team

---

## License

This project follows the licensing terms of **MagisV2 (GPL-3.0-or-later)**.  
Refer to the `LICENSE` file for detailed information.
