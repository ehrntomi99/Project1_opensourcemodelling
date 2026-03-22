# Dimensioning of an asynchronous motor
This is my first project for the course Open Source Energy System Modeling.

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

This project is released under the MIT License and linted with Ruff.

## Scope
The scope of this project is to model and visualize the characteristics of an **asynchronous motor**. With the given parameters maximum/continious speed and maximum/rated power the goal is to calculate torque values and provide a characteristic curve of the correlation of torque and speed. The graph covers than the **constant torque region** which is up to rated speed and the **field weakening region** which is above rated speed.

## Purpose of the Functions

### 1. torques
* **Purpose:** Calculate the maximum torque ($M_{max}$) and the rated torque ($M_n$) of the motor
* **Input:** Maximum power, rated power, and rated speed ($n_n$)
* **Logic:** Uses the physical formula $M = \frac{P}{\omega}$ 

### 2. torques_15000
* **Purpose:** Define the available torque at the motor's defined maximum speed
* **Input:** Rated torque ($M_n$), maximum torque ($M_{max}$), rated speed ($n_n$), and maximum speed ($n_{max}$)
* **Logic:** Field weakening formula $M_{Lowest} = M \cdot (n_n / n_{max})$

### 3. torque_curve
* **Purpose:** Generates a dataset of torque values for a range of different speeds
* **Input:** List of speed values ($n\_list$), constant torque ($M_{constant}$), rated speed ($n_n$)
* **Logic:** Uses a loop with an if-else condition:
    * If $n \le n_n$: Torque remains at $M_{constant}$ (Constant Torque Region)
    * If $n > n_n$: Torque is reduced by the factor $(n_n / n)$ (Field Weakening Region)

## AI Disclosure
This project was developed with the assistance of artificial intelligence of Gemini 3 Flash for the following steps:
* **Code Optimization:** I tried to implement the functions by myself, because my programming skills are a bit rusty because my last implemented project was a while ago. For the 





