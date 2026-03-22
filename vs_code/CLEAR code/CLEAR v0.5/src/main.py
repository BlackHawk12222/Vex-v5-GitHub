#region VEXcode Generated Robot Configuration
from vex import *

# Brain should be defined by default
brain=Brain()

def none():
    pass

# Robot configuration code
controller_1 = Controller(PRIMARY)
Right1 = Motor(Ports.PORT11, GearSetting.RATIO_6_1, False)
Right2 = Motor(Ports.PORT13, GearSetting.RATIO_6_1, False)
Right3 = Motor(Ports.PORT12, GearSetting.RATIO_6_1, True)
left1 = Motor(Ports.PORT20, GearSetting.RATIO_6_1, True)
left3 = Motor(Ports.PORT18, GearSetting.RATIO_6_1, False)
optical_9 = Optical(Ports.PORT9)
colorsorting = Motor(Ports.PORT15, GearSetting.RATIO_18_1, True)
left2 = Motor(Ports.PORT19, GearSetting.RATIO_6_1, True)
TopMotor = Motor(Ports.PORT1, GearSetting.RATIO_18_1, True)
frontPiston = DigitalOut(brain.three_wire_port.a)
inertial_for_auton = Inertial(Ports.PORT6)
DeScorer = DigitalOut(brain.three_wire_port.b)
Intake = Motor(Ports.PORT14, GearSetting.RATIO_6_1, True)
Left= MotorGroup(left1, left2)
Right= MotorGroup(Right1, Right2)
analog_input=PotentiometerV2(brain.three_wire_port.c)
limitswitch=Limit(brain.three_wire_port.b)
bumperswitch=Bumper(brain.three_wire_port.a)
optical2=Optical(Ports.PORT2)
rotation=Rotation(Ports.PORT3)

# wait for rotation sensor to fully initialize
wait(30, MSEC)

def play_vexcode_sound(sound_name):
    print("VEXPlaySound:" + sound_name)
    wait(5, MSEC)

# add a small delay to make sure we don't print in the middle of the REPL header
wait(200, MSEC)
# clear the console to make sure we don't have the REPL in the console
print("\033[2J")

#endregion VEXcode Generated Robot Configuration
screen_precision = 0
console_precision = 0
pusher_state = False
loader_state = False
record = 0
recording_state=0

# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       CLEAR.py                                                     #
# 	Author:       Micah Bow                                                    #
# 	Created:      1/27/2026, 12:42 PM                                          #
#   Last Edited:  2/23/2026, 10:00 PM                                          #
# 	Description:  Capture, logging, Encoding, Archiving, Recording.            #
#                                                                              #
# ---------------------------------------------------------------------------- #

Right1.set_stopping(HOLD)
Right2.set_stopping(HOLD)
Right3.set_stopping(HOLD)
left1.set_stopping(HOLD)
left2.set_stopping(HOLD)
left3.set_stopping(HOLD)

# Driver Control Functions

def rightside():
    rightspeed = controller_1.axis2.position() / 8.33
    Right1.spin(FORWARD, rightspeed, VOLT)
    Right2.spin(FORWARD, rightspeed, VOLT)
    Right3.spin(FORWARD, rightspeed, VOLT)

def leftside():
    leftspeed = controller_1.axis3.position() / 8.33
    left1.spin(FORWARD, leftspeed, VOLT)
    left2.spin(FORWARD, leftspeed, VOLT)
    left3.spin(FORWARD, leftspeed, VOLT)

def intakeup():
    Intake.spin(FORWARD, 12, VOLT)
    while controller_1.buttonR1.pressing():
        wait(5, MSEC)
    Intake.stop()

def intakedown():
    Intake.spin(REVERSE, 12, VOLT)
    while controller_1.buttonR2.pressing():
        wait(5, MSEC)
    Intake.stop()

def scoreup():
    TopMotor.spin(FORWARD, 12, VOLT)
    Intake.spin(FORWARD, 12, VOLT)
    while controller_1.buttonL1.pressing():
        wait(5,MSEC)
    TopMotor.stop()
    Intake.stop()

def scoredown():
    TopMotor.spin(FORWARD, 12, VOLT)
    Intake.spin(REVERSE, 12, VOLT)
    while controller_1.buttonL2.pressing():
        wait(5, MSEC)
    TopMotor.stop()
    Intake.stop()

# Mixed functions

def pushertoggle():
    global pusher_state, Pusher
    if not pusher_state:
        DeScorer.set(True)
        pusher_state=1
        Pusher=True
    else:
        DeScorer.set(False)
        pusher_state=0
        Pusher=False

def loadertoggle():
    global loader_state
    if not loader_state:
        frontPiston.set(True)
        loader_state=True
    else:
        frontPiston.set(False)
        loader_state=False

# Aton Functions

def leftmove(leftspeed):
    print("left: ", leftspeed)
    if leftspeed != 0:
        leftspeed=leftspeed/8.33
    left1.spin(FORWARD, leftspeed, VOLT)
    left2.spin(FORWARD, leftspeed, VOLT)
    left3.spin(FORWARD, leftspeed, VOLT)

def rightmove(rightspeed):
    print("Right: ", rightspeed)
    if rightspeed != 0:
        rightspeed=rightspeed/8.33
    Right1.spin(FORWARD, rightspeed, VOLT)
    Right2.spin(FORWARD, rightspeed, VOLT)
    Right3.spin(FORWARD, rightspeed, VOLT)

def intakeupstart():
    print("Intake up")
    Intake.spin(FORWARD)

def intakedownstart():
    print("Intake down")
    Intake.spin(REVERSE)

def intakestop():
    print("Intake stop")
    Intake.stop()

def scoreupstart():
    print("Score up")
    Intake.spin(FORWARD)
    TopMotor.spin(FORWARD)

def scoredownstart():
    print("Score down")
    Intake.spin(REVERSE)
    TopMotor.spin(FORWARD)

def scorestop():
    print("Score stop")
    Intake.stop()
    TopMotor.stop()

# Recording Functions
if brain.sdcard.is_inserted() and brain.sdcard.exists("CLEAR.py"):
    import CLEAR
    logging=Thread(lambda: CLEAR.log.auto_start(True))

    def recordright():
        global recording_state
        if recording_state == 0:
            CLEAR.log.recording.start("Right")
            controller_1.screen.clear_line(3)
            controller_1.screen.set_cursor(3,1)
            controller_1.screen.print("Right recording.")
            recording_state=1
        elif recording_state == 1:
            CLEAR.log.recording.stop("Right")
            controller_1.screen.clear_line(3)
            controller_1.screen.set_cursor(3,1)
            controller_1.screen.print("Right Stopped.")
            CLEAR.log.recording.encode("Right", rightmove, leftmove, intakeupstart, intakestop, "R1", intakedownstart, intakestop, "R2", scoreupstart, scorestop, "L1", scoredownstart, scorestop, "L2", loadertoggle, none, "B", pushertoggle, none, "DOWN")
            controller_1.screen.clear_line(3)
            controller_1.screen.set_cursor(3,1)
            controller_1.screen.print("Right Encoded.")
            recording_state=0
    
    def recallhistory():
        CLEAR.log.archive.recall_log()

    def archiveright():
        CLEAR.log.archive.recall_recording("Right_pre_archived.txt")

    controller_1.buttonLeft.pressed(archiveright)
    controller_1.buttonRight.pressed(recordright)
    controller_1.buttonUp.pressed(recallhistory)

    def aton():
        CLEAR.log.recording.run("Right")

    def driver():
        pass
    
    comp=Competition(driver, aton)
    
    

# Event setup
Intake.set_velocity(100, PERCENT)
TopMotor.set_velocity(100, PERCENT)
controller_1.axis2.changed(rightside)
controller_1.axis3.changed(leftside)
controller_1.buttonR1.pressed(intakeup)
controller_1.buttonR2.pressed(intakedown)
controller_1.buttonL1.pressed(scoreup)
controller_1.buttonL2.pressed(scoredown)
controller_1.buttonDown.pressed(pushertoggle)
controller_1.buttonB.pressed(loadertoggle)

inertial_for_auton.calibrate()