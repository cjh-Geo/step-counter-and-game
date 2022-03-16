def on_gesture_shake():
    global step
    step += 1
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

drop5x = 0
drop4x = 0
drop3x = 0
drop2x = 0
drop1x = 0
scrn3 = 3
scrn1 = 1
scrn2 = 2
screen = scrn1
newstep = 0
step = 0
token = 0
laststep = 0
game2 = 1
intervaltime = 300

def on_forever():
    global game2, drop1x, drop2x, drop3x, drop4x, drop5x
    if screen == scrn3 and input.button_is_pressed(Button.A):
        game2 = 0
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
                        . . # . .
        """)
        basic.pause(500)
        drop1x = randint(0, 4)
        led.plot(drop1x, 0)
        basic.pause(intervaltime)
        led.unplot(drop1x, 0)
        led.plot(drop1x, 1)
        drop2x = randint(0, 4)
        led.plot(drop2x, 0)
        basic.pause(intervaltime)
        led.unplot(drop1x, 1)
        led.plot(drop1x, 2)
        led.unplot(drop2x, 0)
        led.plot(drop2x, 1)
        drop3x = randint(0, 4)
        led.plot(drop3x, 0)
        basic.pause(intervaltime)
        led.unplot(drop1x, 2)
        led.plot(drop1x, 3)
        led.unplot(drop2x, 1)
        led.plot(drop2x, 2)
        led.unplot(drop3x, 0)
        led.plot(drop3x, 1)
        drop4x = randint(0, 4)
        led.plot(drop4x, 0)
        basic.pause(intervaltime)
        led.unplot(drop1x, 3)
        led.plot(drop1x, 4)
        led.unplot(drop2x, 2)
        led.plot(drop2x, 3)
        led.unplot(drop3x, 1)
        led.plot(drop3x, 2)
        led.unplot(drop4x, 0)
        led.plot(drop4x, 1)
        drop5x = randint(0, 4)
        led.plot(drop5x, 0)
        basic.pause(intervaltime)
        while game2 == 0:
            if game2 == 0 + 1:
                break
            led.unplot(drop1x, 4)
            led.unplot(drop2x, 2)
            led.plot(drop2x, 3)
            led.unplot(drop3x, 1)
            led.plot(drop3x, 2)
            led.unplot(drop4x, 0)
            led.plot(drop4x, 1)
            led.unplot(drop5x, 3)
            led.plot(drop5x, 4)
            drop1x = randint(0, 4)
            led.plot(drop1x, 0)
            if game2 == 0 + 1:
                break
            basic.pause(intervaltime)
            if game2 == 0 + 1:
                break
            led.unplot(drop2x, 4)
            led.unplot(drop1x, 0)
            led.plot(drop1x, 1)
            led.unplot(drop3x, 3)
            led.plot(drop3x, 4)
            led.unplot(drop4x, 2)
            led.plot(drop4x, 3)
            led.unplot(drop4x, 1)
            led.plot(drop5x, 2)
            drop2x = randint(0, 4)
            led.plot(drop2x, 0)
            if game2 == 0 + 1:
                break
            basic.pause(intervaltime)
            if game2 == 0 + 1:
                break
            led.unplot(drop3x, 4)
            led.unplot(drop1x, 1)
            led.plot(drop1x, 2)
            led.unplot(drop2x, 0)
            led.plot(drop2x, 1)
            led.unplot(drop4x, 3)
            led.plot(drop4x, 4)
            led.unplot(drop5x, 2)
            led.plot(drop5x, 3)
            drop3x = randint(0, 4)
            led.plot(drop3x, 0)
            if game2 == 0 + 1:
                break
            basic.pause(intervaltime)
            if game2 == 0 + 1:
                break
            led.unplot(drop4x, 4)
            led.unplot(drop1x, 2)
            led.plot(drop1x, 3)
            led.unplot(drop2x, 1)
            led.plot(drop2x, 2)
            led.unplot(drop3x, 0)
            led.plot(drop3x, 1)
            led.unplot(drop5x, 3)
            led.plot(drop5x, 4)
            drop4x = randint(0, 4)
            led.plot(drop4x, 0)
            if game2 == 0 + 1:
                break
            basic.pause(intervaltime)
            if game2 == 0 + 1:
                break
            led.unplot(drop5x, 4)
            led.unplot(drop1x, 3)
            led.plot(drop1x, 4)
            led.unplot(drop2x, 2)
            led.plot(drop2x, 3)
            led.unplot(drop3x, 1)
            led.plot(drop3x, 2)
            led.unplot(drop4x, 0)
            led.plot(drop4x, 1)
            drop5x = randint(0, 4)
            led.plot(drop5x, 0)
            if game2 == 0 + 1:
                break
            basic.pause(intervaltime)
            if game2 == 0 + 1:
                break
basic.forever(on_forever)

def on_forever2():
    global laststep, token
    if step - laststep == 10:
        laststep = step
        token += 1
basic.forever(on_forever2)

def on_forever3():
    global screen
    if input.button_is_pressed(Button.B):
        if screen == scrn1:
            screen = scrn2
        elif screen == scrn2:
            screen = scrn3
        elif screen == scrn3:
            screen = scrn1
        else:
            basic.show_leds("""
                . . # . .
                                . # . # .
                                . . . # .
                                . . # . .
                                . . # . .
            """)
        basic.pause(200)
basic.forever(on_forever3)

def on_forever4():
    if screen == scrn1:
        basic.show_number(step)
    elif screen == scrn2:
        basic.show_number(token)
    elif screen == scrn3:
        if game2 != 0:
            basic.show_leds("""
                # . # . #
                                . # . # .
                                # . # . #
                                . # . # .
                                # . # . #
            """)
basic.forever(on_forever4)

def on_forever5():
    global game2
    if screen == scrn3 and input.button_is_pressed(Button.A):
        basic.pause(12500)
        game2 = 1
basic.forever(on_forever5)
