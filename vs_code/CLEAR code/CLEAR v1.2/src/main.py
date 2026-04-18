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
left1 = Motor(Ports.PORT20, GearSetting.RATIO_6_1, True)
left2 = Motor(Ports.PORT19, GearSetting.RATIO_6_1, True)

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
pushing=False

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
left1.set_stopping(HOLD)
left2.set_stopping(HOLD)

# Driver Control Functions

def rightside():
    rightspeed = controller_1.axis2.position() / 8.33
    Right1.spin(FORWARD, rightspeed, VOLT)
    Right2.spin(FORWARD, rightspeed, VOLT)

def leftside():
    leftspeed = controller_1.axis3.position() / 8.33
    left1.spin(FORWARD, leftspeed, VOLT)
    left2.spin(FORWARD, leftspeed, VOLT)

# Aton Functions

def leftmove(leftspeed):
    print("left: ", leftspeed)
    if leftspeed != 0:
        leftspeed=leftspeed/8.33
    left1.spin(FORWARD, leftspeed, VOLT)
    left2.spin(FORWARD, leftspeed, VOLT)

def rightmove(rightspeed):
    print("Right: ", rightspeed)
    if rightspeed != 0:
        rightspeed=rightspeed/8.33
    Right1.spin(FORWARD, rightspeed, VOLT)
    Right2.spin(FORWARD, rightspeed, VOLT)

# Recording Functions
if brain.sdcard.is_inserted() and brain.sdcard.exists("CLEAR.py"):
    import CLEAR
    Thread(CLEAR.log.auto_start)

    def recordright():
        global recording_state
        if recording_state == 0:
            CLEAR.recording.start("Right")
            controller_1.screen.clear_line(3)
            controller_1.screen.set_cursor(3,1)
            controller_1.screen.print("Right recording.")
            recording_state=1
        elif recording_state == 1:
            CLEAR.recording.stop("Right")
            controller_1.screen.clear_line(3)
            controller_1.screen.set_cursor(3,1)
            controller_1.screen.print("Right Stopped.")
            CLEAR.recording.encode("Right", rightmove, leftmove)
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
        CLEAR.recording.run("Right")

    def driver():
        pass
    
    comp=Competition(driver, aton)
    
    

# Event setup
controller_1.axis2.changed(rightside)
controller_1.axis3.changed(leftside)