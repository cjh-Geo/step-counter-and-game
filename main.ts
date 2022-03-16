input.onButtonPressed(Button.A, function () {
    if (screen == scrn3 && (game2 == 1 && token >= 1)) {
        game2 = 0
        token += -1
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
        curry = 0
        while (game2 < 1) {
            drop1x = randint(0, 4)
            for (let index = 0; index < 5; index++) {
                led.plot(drop1x, dropy)
                basic.pause(intervaltime)
                led.unplot(drop1x, dropy)
                if (dropy < 4) {
                    dropy += 1
                } else {
                    dropy = 0
                }
                if (drop1x == basketx && dropy == 4) {
                    game2 = 2
                    totalcurry += -1
                    basic.showNumber(curry)
                    basic.pause(3000)
                    game2 = 1
                }
            }
            totalcurry += 1
            curry += 1
        }
    }
})
input.onGesture(Gesture.Shake, function () {
    if (true) {
        step += 1
    }
})
let basketx = 0
let drop1x = 0
let dropy = 0
let intervaltime = 0
let curry = 0
let game2 = 0
let token = 0
let screen = 0
let scrn3 = 0
scrn3 = 3
let scrn1 = 1
let scrn2 = 2
let scrn4 = 4
screen = scrn1
let step = 0
token = 0
let laststep = 0
game2 = 1
let totalcurry = 0
curry = 0
intervaltime = 100
dropy = 0
basic.forever(function () {
    if (screen == scrn1) {
        basic.showNumber(step)
    } else if (screen == scrn2) {
        basic.showNumber(token)
    } else if (screen == scrn3) {
        if (game2 == 1) {
            basic.showLeds(`
                # . # . #
                . # . # .
                # . # . #
                . # . # .
                # . # . #
                `)
        }
    } else if (screen == scrn4) {
        basic.showNumber(totalcurry)
    }
})
basic.forever(function () {
    if (game2 == 0) {
        if (screen == scrn3 && input.buttonIsPressed(Button.A)) {
            led.unplot(basketx, 4)
            if (basketx > 0) {
                basketx += -1
            } else if (basketx == 0) {
                basketx = 4
            }
        } else if (screen == scrn3 && input.buttonIsPressed(Button.B)) {
            led.unplot(basketx, 4)
            if (basketx < 4) {
                basketx += 1
            } else if (basketx == 4) {
                basketx = 0
            }
        }
        led.plot(basketx, 4)
        basic.pause(100)
    }
})
basic.forever(function () {
    if (game2 == 1) {
        if (input.buttonIsPressed(Button.B)) {
            if (screen == scrn1) {
                screen = scrn2
            } else if (screen == scrn2) {
                screen = scrn3
            } else if (screen == scrn3) {
                screen = scrn4
            } else if (screen == scrn4) {
                screen = scrn1
            }
            basic.pause(200)
        }
    }
})
basic.forever(function () {
    if (step - laststep == 10) {
        laststep = step
        token += 1
    }
})
