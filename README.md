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
* **Code Optimization:** To reactivate my programming skills I tried to implement the functions by myself. For the the function **torque_curve** I implemented the basic physical formulas for the two regions constant torque and field weakening with a conditional "for" loop, but I always got a "ZeroDivisionError" and didn't get a solution for it, so I asked Gemini how to solve the error. The solution was an additional if/elif clause, it suggested adding the if n == 0 and the function worked. Because I am used to using Jupyther notebook I did the code as an .ipynb file but the following coding like the tests didn't work for that, so I changed to the .py format.
* **Ruff Linter** I have to say I never worked with a linter so I started to ask Gemini for which reason a linter is useful, why there are different ones, which is the most used one and what are the details of a ruff linter. With that information I understand now the concept of a linter, but to implement it I needed Gemini from the beginning on. It showed me how to create the pyproject.toml, the .github/workflows folder with the lint.yml file and explained me how it works step by step. It worked from the beginning on but later I tried to adjust it to the workflow of the pytest of professor Huppmann, which was made during the lesson, like changing the python version fromm 3.10 to 3.12, I also changed .yml to .yaml because it is the official ending.
* **Pytest** Because I just tried to test the functions itself if they are working and didn't know some standard tests, I asked Gemini what is a really simple test, it would always recommend to implement. The answer was a test to test that a function returns exactly two torque values like the **test_torques_values** and the  **test_torques_15000_values**. I tried to test the **torque_curve** function but, didn't come to a solution which makes sense, so I also had to ask Gemini how to test the function and it gave me the **test_torque_curve** with an exülanation how it works.
* **README** For the Readme I asked Gemini how to structurize the file, like how to do bullet points, subheading, bold text and it also did for me the formula style, so I didn't have to write every dollar sign. I explained the functions to Gemini how I understand them and told it to structurize my explanation in a Purpose, Input, Logic style. I also did a grammar and vocabulary check with Gemini.
  
  





