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
