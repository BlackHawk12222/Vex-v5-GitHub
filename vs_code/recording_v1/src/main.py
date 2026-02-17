# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       micas                                                        #
# 	Created:      2/17/2026, 3:19:46 PM                                        #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *

# Brain should be defined by default
brain=Brain()

controller_1=Controller(PRIMARY)
intake=Motor(Ports.PORT14, GearSetting.RATIO_6_1, False)
topmotor=Motor(Ports.PORT1, GearSetting.RATIO_6_1, False)
colorsorting=Motor(Ports.PORT15, GearSetting.RATIO_6_1, False)
right1=Motor(Ports.PORT11, GearSetting.RATIO_6_1, True)
right2=Motor(Ports.PORT13, GearSetting.RATIO_6_1, False)
right3=Motor(Ports.PORT12, GearSetting.RATIO_6_1, True)
left1=Motor(Ports.PORT19, GearSetting.RATIO_6_1, False)
left2=Motor(Ports.PORT20, GearSetting.RATIO_6_1, True)
left3=Motor(Ports.PORT18, GearSetting.RATIO_6_1, False)
pusher=DigitalOut(brain.three_wire_port.b)
loader=DigitalOut(brain.three_wire_port.a)

record=0
pusher_state=0
loader_state=0
controlleraxis2positionhistory=0
controlleraxis3positionhistory=0

def rightside():
    right=controller_1.axis3.position()/8.33
    right1.spin(FORWARD, right, VOLT)
    right2.spin(FORWARD, right, VOLT)
    right3.spin(FORWARD, right, VOLT)

def leftside():
    left=controller_1.axis2.position()/8.33
    left1.spin(FORWARD, left, VOLT)
    left2.spin(FORWARD, left, VOLT)
    left3.spin(FORWARD, left, VOLT)

def intakeup():
    intake.spin(FORWARD, 12, VOLT)

def intakedown():
    intake.spin(REVERSE, 12, VOLT)

def scoreup():
    topmotor.spin(FORWARD, 12, VOLT)
    intake.spin(FORWARD, 12, VOLT)

def scoredown():
    topmotor.spin(FORWARD, 12, VOLT)
    intake.spin(REVERSE, 12, VOLT)

def pushertoggle():
    global pusher_state
    if pusher_state==0:
        pusher.set(True)
        pusher_state=1
    else:
        pusher.set(False)
        pusher_state=0

def loadertoggle():
    global loader_state
    if loader_state==0:
        loader.set(True)
        loader_state=1
    else:
        loader.set(False)
        loader_state=0

def recordright():
    rightrecording()

def recordleft():
    leftrecording()

def selection():
    controller_1.buttonA.pressed(recordright)
    controller_1.buttonB.pressed(recordleft)
    while True:
        controller_1.screen.set_cursor(1, 3)
        controller_1.screen.print("Press A for right recording")
        wait(500, MSEC)
        controller_1.screen.clear_row(3)
        controller_1.screen.set_cursor(1, 3)
        controller_1.screen.print("Press B for left recording")
        wait(500, MSEC)
        controller_1.screen.clear_row(3)
        if record!=0:
            break

def rightrecording():
    global record
    record=1
    brain.sdcard.savefile("rightrecording_left.csv")
    brain.sdcard.savefile("rightrecording_right.csv")
    brain.sdcard.savefile("prerightrecording.csv")
    while record==1:
        if controller_1.axis2.position() != 0:
            left1.set_position(0, DEGREES) #left joystick/drive
            while controller_1.axis2.position() != 0:
                if controller_1.axis2.position() != controlleraxis2positionhistory:
                    controlleraxis2positionhistory=controller_1.axis2.position()
                    brain.sdcard.appendfile("rightrecording_left.csv", bytearray("Left Joystick: " + str(controller_1.axis2.position()) + "left side degrees moved: " + str(left1.position(DEGREES)) + "\n", "utf-8"))
                    left1.set_position(0, DEGREES)

        if controller_1.axis3.position() != 0:
            right1.set_position(0, DEGREES) #right joystick/drive
            while controller_1.axis3.position() != 0:
                if controller_1.axis3.position() != controlleraxis3positionhistory:
                    controlleraxis3positionhistory=controller_1.axis3.position()
                    brain.sdcard.appendfile("rightrecording_right.csv", bytearray("Right Joystick: " + str(controller_1.axis3.position()) + "right side degrees moved: " + str(right1.position(DEGREES)) + "\n", "utf-8"))
                    right1.set_position(0, DEGREES)
                

        if pusher_state==1:
            pass
        elif pusher_state==0:
            pass

        if loader_state==1:
            pass
        elif loader_state==0:
            pass

def leftrecording():
    global record
    record=2
    brain.sdcard.savefile("preleftrecording.csv")
    while record==2:
        pass

def when_started():
    while True:
        if record==0:
            selection()
        wait(20, MSEC)

controller_1.axis2.changed(rightside)
controller_1.axis3.changed(leftside)
controller_1.buttonR1.pressed(intakeup)
controller_1.buttonR2.pressed(intakedown)
controller_1.buttonL1.pressed(scoreup)
controller_1.buttonL2.pressed(scoredown)
controller_1.buttonY.pressed(pushertoggle)
controller_1.buttonB.pressed(loadertoggle)
when_started()
