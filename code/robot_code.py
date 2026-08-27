def on_received_string_deprecated(receivedString):
    global item
    item = receivedString
    if item.compare("A") == 0:
        sumobit.run_motor(SumobitMotorChannel.BOTH, SumobitMotorDirection.FORWARD, 255)
    elif item.compare("B") == 0:
        sumobit.run_motor(SumobitMotorChannel.BOTH,
            SumobitMotorDirection.BACKWARD,
            255)
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