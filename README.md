# SUMOBIT Robot Wireless Control

A wireless control system for the Cytron SUMOBIT 2-Wheel Robot using BBC micro:bit radio communication and a GHBit controller.

The project allows the SUMOBIT robot to be controlled wirelessly using the GHBit joystick.

---

## Project Overview

This project uses two BBC micro:bit boards:

- One BBC micro:bit is installed on the SUMOBIT robot.
- One BBC micro:bit is installed on the GHBit controller.
- The GHBit controller sends wireless commands using the BBC micro:bit radio communication system.
- The SUMOBIT robot receives the commands and controls its motors accordingly.

The robot can perform the following movements:

- Forward
- Backward
- Left
- Right
- Stop

---

## Hardware Used

The following hardware was used in this project:

- Cytron SUMOBIT 2-Wheel Robot
- BBC micro:bit
- GHBit Controller
- DC Motors
- Robot Wheels
- SUMOBIT Motor Driver Board
- Battery
- Connecting Wires
- USB Cable

---

## Project Structure

```text
SUMOBIT-Robot-Wireless-Control/
│
├── README.md
├── LICENSE
│
├── images/
│   ├── image1.jpg
│   ├── image2.jpg
│   ├── image3.jpg
│   ├── image4.jpg
│   ├── image5.jpg
│   ├── image6.jpg
│   └── image7.jpg
│
└── code/
    ├── SUMOBIT_Robot_Code.py
    └── GHBit_Controller_Code.js
```

---

# Robot Assembly

## 1. SUMOBIT Robot and GHBit Controller

The project consists of the SUMOBIT robot and the GHBit wireless controller.

The robot uses two DC motors for movement, while the GHBit controller uses a joystick to send wireless commands to the robot.

![SUMOBIT Robot and GHBit Controller](images/image1.jpg)

**Figure 1.** SUMOBIT robot and GHBit controller.

---

## 2. Robot Assembly

The robot chassis was assembled by installing the DC motors, wheels, SUMOBIT board, and BBC micro:bit.

The mechanical and electrical components were installed before testing the wireless control system.

![SUMOBIT Robot Assembly](images/image2.jpg)

**Figure 2.** SUMOBIT robot during the assembly process.

---

## 3. Motor Driver and Power Connection

The SUMOBIT board controls the right and left DC motors.

The battery is connected to the board to provide power for the motors. The motor connections were checked carefully before testing.

![Motor Driver and Power Connection](images/image3.jpg)

**Figure 3.** SUMOBIT motor driver and battery connection.

---

# Controller Setup

The GHBit controller is used as the wireless transmitter.

It contains a joystick for directional control and additional buttons. The BBC micro:bit installed on the controller sends commands wirelessly to the robot.

![GHBit Controller Setup](images/image4.jpg)

**Figure 4.** GHBit wireless controller used to control the SUMOBIT robot.

---

# Wireless Control System

The complete system consists of the SUMOBIT robot and the GHBit controller.

The controller sends movement commands wirelessly using the BBC micro:bit radio communication system. The robot receives these commands and controls its motors.

![Complete Wireless Control System](images/image5.jpg)

**Figure 5.** Complete SUMOBIT wireless control system.

---

# Robot Components Before Assembly

Before the final assembly, the main components were arranged and prepared.

These components included the SUMOBIT board, BBC micro:bit, DC motors, wheels, robot chassis, controller, cables, and other accessories.

![Robot Components Before Assembly](images/image6.jpg)

**Figure 6.** SUMOBIT robot components before final assembly.

---

# SUMOBIT Motor Board

The SUMOBIT board contains the motor driver section used to control both DC motors.

The battery is connected to the power input, while the right and left motors are connected to their respective motor terminals.

![SUMOBIT Motor Board](images/image7.jpg)

**Figure 7.** SUMOBIT board showing the motor and battery connections.

---

# Wireless Communication

The BBC micro:bit radio communication system is used to establish wireless communication between the GHBit controller and the SUMOBIT robot.

Both BBC micro:bit boards must use the same radio group.

```python
radio.set_group(1)
radio.set_transmit_power(7)
```

The controller sends a command string, and the robot receives and processes the command.

---

# Control Commands

The following commands are used in the wireless communication system:

| Command | Function |
|---|---|
| `A` | Move Forward |
| `B` | Move Backward |
| `C` | Turn Left |
| `D` | Turn Right |
| `0` | Stop |
| `E` | GHBit Button B1 |
| `F` | GHBit Button B2 |
| `G` | GHBit Button B3 |
| `H` | GHBit Button B4 |

---

# Robot Receiver Code

The following code runs on the BBC micro:bit installed on the SUMOBIT robot.

The robot receives the wireless commands and controls both motors according to the received command.

The complete code is available in:

```text
code/SUMOBIT_Robot_Code.py
```

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


radio.on_received_string_deprecated(
    on_received_string_deprecated
)

item = ""

radio.set_group(1)

radio.set_transmit_power(7)

basic.show_icon(IconNames.HEART)
```

---

# GHBit Controller Code

The following code runs on the BBC micro:bit installed on the GHBit controller.

The joystick sends different wireless commands according to its direction.

The complete code is available in:

```text
code/GHBit_Controller_Code.js
```

```javascript
GHBit.onKey(GHBit.enButton.B3, function () {

    radio.sendString("G")

})

GHBit.onKey(GHBit.enButton.B1, function () {

    radio.sendString("E")

})

GHBit.onKey(GHBit.enButton.B4, function () {

    radio.sendString("H")

})

GHBit.onKey(GHBit.enButton.B2, function () {

    radio.sendString("F")

})

basic.showIcon(IconNames.Heart)

radio.setGroup(1)

radio.setTransmitPower(7)

basic.forever(function () {

    if (GHBit.Rocker(GHBit.enRocker.Up)) {

        radio.sendString("A")

        basic.showArrow(ArrowNames.North)

    } else if (GHBit.Rocker(GHBit.enRocker.Down)) {

        radio.sendString("B")

        basic.showArrow(ArrowNames.South)

    } else if (GHBit.Rocker(GHBit.enRocker.Left)) {

        radio.sendString("C")

        basic.showArrow(ArrowNames.West)

    } else if (GHBit.Rocker(GHBit.enRocker.Right)) {

        radio.sendString("D")

        basic.showArrow(ArrowNames.East)

    } else if (GHBit.Rocker(GHBit.enRocker.Press)) {

        radio.sendString("0")

        basic.showIcon(IconNames.No)

    } else if (GHBit.Rocker(GHBit.enRocker.Nostate)) {

        radio.sendString("0")

        basic.showIcon(IconNames.No)

    }

})
```

---

# Control Logic

The wireless control system operates as follows:

```text
GHBit Controller
       ↓
Joystick Input
       ↓
BBC micro:bit Radio
       ↓
Wireless Command
       ↓
SUMOBIT BBC micro:bit
       ↓
Motor Driver
       ↓
Right and Left Motors
       ↓
Robot Movement
```

---

# Movement Logic

## Forward

When the joystick is moved upward, the controller sends:

```text
A
```

The robot receives the command and both motors move forward.

---

## Backward

When the joystick is moved downward, the controller sends:

```text
B
```

The robot receives the command and both motors move backward.

---

## Left

When the joystick is moved to the left, the controller sends:

```text
C
```

The motors rotate in opposite directions, causing the robot to turn left.

---

## Right

When the joystick is moved to the right, the controller sends:

```text
D
```

The motors rotate in opposite directions, causing the robot to turn right.

---

## Stop

When the joystick is pressed or is in the neutral position, the controller sends:

```text
0
```

The robot stops both motors.

---

# Testing and Troubleshooting

During the initial testing, some motor movements were not working as expected.

The following steps were performed:

1. Checked the motor wire connections.
2. Verified the right and left motor outputs.
3. Tested the motors individually.
4. Checked the battery and power connections.
5. Used a multimeter to check the connections.
6. Adjusted the motor wiring where required.
7. Repeated the Forward, Backward, Left, Right, and Stop tests.

After correcting the required connections, the robot successfully responded to the wireless commands.

---

# Final Result

The SUMOBIT robot was successfully assembled, programmed, and tested.

The GHBit controller successfully communicates with the robot using BBC micro:bit radio communication.

The final system can perform the following movements:

- Forward
- Backward
- Left
- Right
- Stop

The wireless communication between the GHBit controller and the SUMOBIT robot was successfully tested.

---

# How to Run the Project

1. Assemble the SUMOBIT robot.
2. Connect the DC motors to the SUMOBIT board.
3. Connect the battery to the robot.
4. Install the BBC micro:bit on the SUMOBIT robot.
5. Upload the robot receiver code.
6. Install another BBC micro:bit on the GHBit controller.
7. Upload the GHBit controller code.
8. Make sure both BBC micro:bit boards use the same radio group:

```text
Radio Group = 1
```

9. Turn on the robot and the controller.
10. Use the GHBit joystick to control the SUMOBIT robot.

---

# Project Status

**Status: Completed and Tested**

The SUMOBIT robot wireless control system was successfully assembled, programmed, and tested.

---

# Author

**Adel Husham Mohamedain**

Electrical Engineering Student  
Universiti Malaysia Perlis (UniMAP)

---

# License

This project is licensed under the MIT License.
