# Powered Lift Wing Design for STOL Aircraft

This project presents the aerodynamic design and analysis of a powered-lift wing
developed under the **LAT Aerospace High-Preparation Problem Statement** for the
**Inter IIT Tech Meet 14.0 representing IIT Gandhinagar**.

The objective was to achieve **Short Take-Off and Landing (STOL)** capability at
low freestream velocities by integrating an **Externally Blown Flap (EBF)**
configuration with **Distributed Electric Propulsion (DEP)**.

---

## Project Objectives
- Achieve extreme lift coefficients beyond conventional passive high-lift systems  
- Enable STOL operation at low take-off speeds without VTOL mechanisms  
- Treat propulsion and aerodynamics as a tightly coupled design problem  

---

## Methodology
- **Analytical Modelling:**  
  Applied semi-empirical powered-lift theory (Kuhn’s method) for initial sizing and
  inverse design to meet target lift coefficients.

- **Airfoil Selection:**  
  Evaluated low-Reynolds-number high-lift airfoils and selected the Selig S1223
  for compatibility with blown-wing operation.

- **Wing & Propulsion Design:**  
  Designed a high-aspect-ratio wing with single-slotted flaps and distributed
  propellers positioned to maximize slipstream–flap interaction.

- **CFD Validation:**  
  Performed high-fidelity CFD simulations in ANSYS Fluent using actuator-disk
  modelling to validate lift augmentation, flow attachment, and jet deflection.
  Mesh-independence and parametric studies were conducted.

---

## Key Results
- Achieved powered lift coefficients within the target envelope (**CL ≈ 6–8**)  
- Maximum lift obtained at high angle of attack with optimized flap deflection  
- Validated slipstream attachment, circulation augmentation, and delayed stall  
- Finalized a physically realizable wing configuration meeting STOL requirements  

---

## Configuration Summary
- Wing span: ~0.96 m  
- Wing chord: ~0.096 m  
- Aspect ratio: 10  
- High-lift system: Single-slotted flap (≈30% chord)  
- Propulsion: Distributed electric propellers (externally blown flap configuration)

---

## Repository Contents
- **End-Term Report:** Detailed analytical modelling and CFD validation  
- **Mid-Term Report:** Concept development and preliminary sizing  

---

## Notes
This repository focuses on **design methodology and validation results**.
Raw CFD case files and solver data are intentionally excluded due to size and
licensing constraints.

---
