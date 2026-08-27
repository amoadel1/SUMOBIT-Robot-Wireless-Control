# SUMOBIT Robot Wireless Control

![Platform](https://img.shields.io/badge/Platform-BBC%20micro%3Abit-blue)
![Robot](https://img.shields.io/badge/Robot-Cytron%20SUMOBIT-red)
![Controller](https://img.shields.io/badge/Controller-GHBit-orange)
![Communication](https://img.shields.io/badge/Communication-Micro%3Abit%20Radio-green)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

---

## Overview

This project presents the design and implementation of a wireless control system for the Cytron SUMOBIT robot using BBC micro:bit radio communication.

The system consists of two main units:

- A **SUMOBIT Robot** that receives wireless commands and controls the left and right motors.
- A **GHBit Controller** that uses a joystick to send movement commands through micro:bit radio communication.

The joystick allows the user to move the robot forward, backward, left, and right. When the joystick is released or pressed, a stop command is sent to the robot.

---

## Features

- Wireless robot control using BBC micro:bit radio communication
- Forward movement
- Backward movement
- Left turning
- Right turning
- Stop function
- Joystick-based control using the GHBit controller
- Dual motor speed control
- Configured radio communication group
- Configured radio transmit power
- Visual direction indication on the micro:bit LED display

---

## Hardware Components

### Robot Unit

- Cytron SUMOBIT Robot
- BBC micro:bit
- SUMOBIT Motor Driver Board
- Two DC Motors
- Two Wheels
- Robot Chassis
- Battery Connection

### Controller Unit

- BBC micro:bit
- Cytron GHBit Controller
- Joystick
- Control Buttons

---

## Wireless Communication

The robot and the controller communicate using the built-in BBC micro:bit radio communication.

Both devices use:

- **Radio Group:** `1`
- **Transmit Power:** `7`

The controller sends a character through the radio, and the robot receives the character and performs the corresponding movement.

---

## Control Commands

| Command | Action |
|--------|--------|
| `A` | Move Forward |
| `B` | Move Backward |
| `C` | Turn Left |
| `D` | Turn Right |
| `0` | Stop |

The GHBit controller also contains additional buttons that send the commands:

| Button | Command Sent |
|--------|--------------|
| B1 | `E` |
| B2 | `F` |
| B3 | `G` |
| B4 | `H` |

> **Note:** In the current robot receiver code, the implemented motor commands are `A`, `B`, `C`, `D`, and `0`. The additional commands `E`, `F`, `G`, and `H` are sent by the controller and can be used for future functions.

---

## System Concept

The overall operation of the system is shown below:

```text
GHBit Controller
      │
      │  Joystick Input
      ▼
BBC micro:bit Controller
      │
      │  Radio Command
      │
      ▼
BBC micro:bit on SUMOBIT
      │
      │  Motor Control
      ▼
SUMOBIT Motor Driver
      │
      ├───────────────┐
      ▼               ▼
 Left Motor       Right Motor
      │               │
      └───────┬───────┘
              ▼
        Robot Movement
```

---

## Robot Components

<p align="center">
  <img src="./Images/components.jpg" width="750">
</p>

<p align="center">
<b>Figure 1.</b> SUMOBIT robot components before assembly.
</p>

The main components include the SUMOBIT chassis, motor driver board, BBC micro:bit, DC motors, wheels, battery cables, and mounting parts.

---

## Robot Assembly

<p align="center">
  <img src="./Images/robot_assembly.jpg" width="750">
</p>

<p align="center">
<b>Figure 2.</b> SUMOBIT robot during the assembly process.
</p>

The robot chassis was assembled by installing the motors, wheels, motor driver board, and BBC micro:bit.

---

## Motor Driver and Power Connection

<p align="center">
  <img src="./Images/motor_driver.jpg" width="750">
</p>

<p align="center">
<b>Figure 3.</b> SUMOBIT motor driver board and battery connection.
</p>

The battery is connected to the motor driver board, which controls the right and left motors according to the wireless commands received by the robot.

---

## Controller Setup

<p align="center">
  <img src="./Images/controller_setup.jpg" width="750">
</p>

<p align="center">
<b>Figure 4.</b> GHBit wireless controller used to control the SUMOBIT robot.
</p>

The GHBit controller contains a joystick for directional control and additional buttons for sending extra wireless commands.

---

## Wireless Control System

<p align="center">
  <img src="./Images/wireless_setup.jpg" width="750">
</p>

<p align="center">
<b>Figure 5.</b> Complete wireless control system with the SUMOBIT robot and GHBit controller.
</p>

The controller sends movement commands wirelessly to the SUMOBIT robot using the BBC micro:bit radio communication system.

---

## Final Setup

<p align="center">
  <img src="./Images/final_setup.jpg" width="750">
</p>

<p align="center">
<b>Figure 6.</b> Final assembled SUMOBIT robot and GHBit wireless controller.
</p>

---

# System Operation

1. Power on the SUMOBIT robot.
2. Power on the GHBit controller.
3. Both micro:bits communicate using radio group `1`.
4. Move the joystick **Up** to send command `A`.
5. Move the joystick **Down** to send command `B`.
6. Move the joystick **Left** to send command `C`.
7. Move the joystick **Right** to send command `D`.
8. Release or press the joystick to send command `0`.
9. The robot receives the command and controls its motors accordingly.

---

# Source Code

The project uses two separate programs:

- **Robot Code**: Receives wireless commands and controls the SUMOBIT motors.
- **Controller Code**: Reads the GHBit joystick and sends wireless commands.

---

## Robot Code

The following program receives wireless commands and controls the SUMOBIT robot motors.

```python
def on_received_string_deprecated(receivedString):
    global item

    item = receivedString

    if item.compare("A") == 0:
        sumobit.run_motor(
            SumobitMotorChannel.BOTH,
            SumobitMotorDirection.FORWARD,
            255
        )

    elif item.compare("B") == 0:
        sumobit.run_motor(
            SumobitMotorChannel.BOTH,
            SumobitMotorDirection.BACKWARD,
            255
        )

    elif item.compare("C") == 0:
        sumobit.set_motors_speed(-255, 255)

    elif item.compare("D") == 0:
        sumobit.set_motors_speed(255, -255)

    elif item.compare("0") == 0:
        sumobit.set_motors_speed(0, 0)


radio.on_received_string_deprecated(on_received_string_deprecated)

item = ""

radio.set_group(1)
radio.set_transmit_power(7)

basic.show_icon(IconNames.HEART)
```

### Robot Movement Logic

- Command `A` runs both motors forward at speed `255`.
- Command `B` runs both motors backward at speed `255`.
- Command `C` sets the motor speeds to `-255` and `255` to turn the robot.
- Command `D` sets the motor speeds to `255` and `-255` to turn the robot in the opposite direction.
- Command `0` stops both motors.

The complete robot code is also available in:

```text
Code/robot_code.py
```

---

## Controller Code

The following program reads the GHBit joystick and sends wireless commands to the SUMOBIT robot.

```python
def my_function():
    radio.send_string("G")

GHBit.on_key(GHBit.enButton.B3, my_function)


def my_function2():
    radio.send_string("E")

GHBit.on_key(GHBit.enButton.B1, my_function2)


def my_function3():
    radio.send_string("H")

GHBit.on_key(GHBit.enButton.B4, my_function3)


def my_function4():
    radio.send_string("F")

GHBit.on_key(GHBit.enButton.B2, my_function4)


basic.show_icon(IconNames.HEART)

radio.set_group(1)
radio.set_transmit_power(7)


def on_forever():

    if GHBit.rocker(GHBit.enRocker.UP):
        radio.send_string("A")
        basic.show_arrow(ArrowNames.NORTH)

    elif GHBit.rocker(GHBit.enRocker.DOWN):
        radio.send_string("B")
        basic.show_arrow(ArrowNames.SOUTH)

    elif GHBit.rocker(GHBit.enRocker.LEFT):
        radio.send_string("C")
        basic.show_arrow(ArrowNames.WEST)

    elif GHBit.rocker(GHBit.enRocker.RIGHT):
        radio.send_string("D")
        basic.show_arrow(ArrowNames.EAST)

    elif GHBit.rocker(GHBit.enRocker.PRESS):
        radio.send_string("0")
        basic.show_icon(IconNames.NO)

    elif GHBit.rocker(GHBit.enRocker.NOSTATE):
        radio.send_string("0")
        basic.show_icon(IconNames.NO)


basic.forever(on_forever)
```

### Controller Logic

The controller continuously checks the position of the GHBit joystick.

| Joystick Direction | Command Sent | Display |
|-------------------|--------------|---------|
| Up | `A` | North Arrow |
| Down | `B` | South Arrow |
| Left | `C` | West Arrow |
| Right | `D` | East Arrow |
| Press | `0` | Stop Icon |
| No State | `0` | Stop Icon |

The complete controller code is also available in:

```text
Code/controller_code.py
```

---

## Repository Structure

```text
SUMOBIT-Robot-Wireless-Control/
│
├── README.md
├── LICENSE
│
├── Code/
│   ├── robot_code.py
│   └── controller_code.py
│
└── Images/
    ├── components.jpg
    ├── robot_assembly.jpg
    ├── motor_driver.jpg
    ├── controller_setup.jpg
    ├── wireless_setup.jpg
    └── final_setup.jpg
```

---

## Software and Tools

- Microsoft MakeCode
- BBC micro:bit
- BBC micro:bit Radio Communication
- Cytron SUMOBIT Library
- Cytron GHBit Library

---

## How to Run the Project

### Robot

1. Open the robot program in Microsoft MakeCode.
2. Make sure the required SUMOBIT extension is added.
3. Download the program to the micro:bit installed on the SUMOBIT robot.
4. Connect the battery and power on the robot.

### Controller

1. Open the controller program in Microsoft MakeCode.
2. Make sure the required GHBit extension is added.
3. Download the program to the micro:bit installed on the GHBit controller.
4. Power on the controller.

Both devices must use the same radio group.

---

## Future Improvements

Possible future improvements include:

- Implementing functions for the additional commands `E`, `F`, `G`, and `H`
- Adding different robot movement modes
- Adding speed control
- Adding obstacle detection
- Adding autonomous movement
- Adding sensors for line following
- Adding additional wireless control features

---

## Author

**Adel Husham Mohamedain Yousuf**

Electrical Engineering Student  
Universiti Malaysia Perlis (UniMAP)

---

## License

This project is licensed under the MIT License.
