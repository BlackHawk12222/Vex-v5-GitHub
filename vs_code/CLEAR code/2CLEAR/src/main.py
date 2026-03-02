#region VEXcode Generated Robot Configuration
from vex import *
#try:
#    from CLEAR import *#type:ignore
#except ImportError:
#        print("CLEAR.py not found. Make sure it is in the sdcard and try again.")

import urandom #type:ignore

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

# wait for rotation sensor to fully initialize
wait(30, MSEC)


# Make random actually random
def initializeRandomSeed():
    wait(100, MSEC)
    random = brain.battery.voltage(MV) + brain.battery.current(CurrentUnits.AMP) * 100 + brain.timer.system_high_res()
    urandom.seed(int(random))
      
# Set random seed 
initializeRandomSeed()

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
pusher_state = 0
loader_state = 0
record = 0
controlleraxis2positionhistory = 0
controlleraxis3positionhistory = 0
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
    if pusher_state==0:
        DeScorer.set(True)
        pusher_state=1
        Pusher=1
    else:
        DeScorer.set(False)
        pusher_state=0
        Pusher=0

def loadertoggle():
    global loader_state
    if loader_state==0:
        frontPiston.set(True)
        loader_state=1
    else:
        frontPiston.set(False)
        loader_state=0

# Aton Functions

def leftmove(leftspeed, degrees):
    print("left: ", leftspeed)
    if leftspeed != 0:
        leftspeed=leftspeed/8.33
    left1.spin(FORWARD, leftspeed, VOLT)
    left2.spin(FORWARD, leftspeed, VOLT)
    left3.spin(FORWARD, leftspeed, VOLT)

def rightmove(rightspeed, degrees):
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
if brain.sdcard.is_inserted():
    try:
        import CLEAR
        Clear=CLEAR

        def capture_setup():
            Clear.log.add_codes("DZ0", ":Colorsort DATA: detected red.:")
            Clear.log.add_codes("DZ1", ":Colorsort DATA: detected blue.:")
            Clear.log.archive.log()
            Clear.log.add("DS0", 0)
            Clear.log.logstart(Right1, left1, Right2, left2, Right3, left3, Intake, TopMotor, colorsorting, variable1=pusher_state, variable1name="pusher_state", variable2=loader_state, variable2name="loader_state")
        Thread(capture_setup)

        def recordright():
            global recording_state
            if recording_state == 0:
                Clear.log.recording.start("Right")
                controller_1.screen.clear_line(3)
                controller_1.screen.set_cursor(3,1)
                controller_1.screen.print("Right recording.")
                recording_state=1
            elif recording_state == 1:
                Clear.log.recording.stop("Right")
                controller_1.screen.clear_line(3)
                controller_1.screen.set_cursor(3,1)
                controller_1.screen.print("Right Stopped.")
                Clear.log.recording.encode("Right", rightmove, leftmove, intakeupstart, intakestop, "R1", intakedownstart, intakestop, "R2", scoreupstart, scorestop, "L1", scoredownstart, scorestop, "L2", loadertoggle, none, "B", pushertoggle, none, "DOWN")
                controller_1.screen.clear_line(3)
                controller_1.screen.set_cursor(3,1)
                controller_1.screen.print("Right Encoded.")
                recording_state=0

        controller_1.buttonRight.pressed(recordright)
        def aton():
            Clear.log.recording.run("Right")

        def driver():
            pass
        
        comp=Competition(driver, aton)
    except ImportError:
        print("CLEAR.py not found. Make sure it is in the sdcard and try again.")
    except AttributeError:
        print("CLEAR.py not found. Make sure it is in the sdcard and try again.")
    
    

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

# Colorsort loop
while True:
    while optical_9.is_near_object():
        if 340 < optical_9.hue() <20:
            colorsorting.spin(FORWARD, 12, VOLT)
        else:
            colorsorting.spin(REVERSE, 12, VOLT)
    colorsorting.stop()