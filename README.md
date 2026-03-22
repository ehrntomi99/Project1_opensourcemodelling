# Dimensioning of an asynchronous motor
This is my first project for the course Open Source Energy System Modeling.

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

This project is released under the MIT License and linted with Ruff.

## Scope
The scope of this project is to model and visualize the characteristics of an **asynchronous motor**. With the given parameters maximum/continious speed and maximum/rated power the goal is to calculate torque values and provide a characteristic curve of the correlation of torque and speed. The graph covers than the **constant torque region** which is up to rated speed and the **field weakening region** which is above rated speed.

## Purpose of the Functions

### 1. torques
* **Purpose:** Calculates the maximum torque ($M_{max}$) and the rated torque ($M_n$) of the motor.
* **Input:** Maximum power, rated power, and rated speed ($n_n$).
* **Logic:** Uses the physical formula $M = \frac{P}{\omega}$ where $\omega$ is derived from the speed in rpm.

### 2. torques_15000
* **Purpose:** Determines the available torque at the motor's maximum speed (e.g., 15,000 rpm).
* **Scope:** It specifically models the torque drop in the field weakening region, where torque decreases as speed increases to keep power constant.

### 3. torque_curve
* **Purpose:** Generates a complete set of torque values for a list of different speeds.
* **Logic:** It uses a loop with an `if-else` condition:
    * If $n \leq n_n$: Torque remains constant ($M_{constant}$).
    * If $n > n_n$: Torque is reduced using the ratio $\frac{n_n}{n}$.
