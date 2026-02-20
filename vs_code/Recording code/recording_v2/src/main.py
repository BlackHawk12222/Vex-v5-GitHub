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
timer=Timer()

record=0
pusher_state=0
loader_state=0
controlleraxis2positionhistory=0
controlleraxis3positionhistory=0
right=0
left=0
timehistory=0
waittime=0
tolrance=3
timemax1=0
timemax2=0
preleftrecordingfile=""
prerightrecordingfile=""
preleftrecordinglist=[]
prerightrecordinglist=[]
preleftlist1=[]
preleftlist2=[]
prosesingrecording=[]


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
    brain.sdcard.appendfile("prerightrecording.txt", bytearray("Intake: Up" + str(timer.time()) + "\n","utf-8"))

def intakedown():
    intake.spin(REVERSE, 12, VOLT)
    brain.sdcard.appendfile("prerightrecording.txt", bytearray("Intake: Down" + str(timer.time()) + "\n","utf-8"))

def scoreup():
    topmotor.spin(FORWARD, 12, VOLT)
    intake.spin(FORWARD, 12, VOLT)
    brain.sdcard.appendfile("prerightrecording.txt", bytearray("Score: Up" + str(timer.time()) + "\n","utf-8"))

def scoredown():
    topmotor.spin(FORWARD, 12, VOLT)
    intake.spin(REVERSE, 12, VOLT)
    brain.sdcard.appendfile("prerightrecording.txt", bytearray("Score: Down" + str(timer.time()) + "\n","utf-8"))

def pushertoggle():
    global pusher_state
    if pusher_state==0:
        pusher.set(True)
        pusher_state=1
        brain.sdcard.appendfile("prerightrecording.txt", bytearray("Pusher: " + "True, " + str(timer.time()) + "\n", "utf-8"))
    else:
        pusher.set(False)
        pusher_state=0
        brain.sdcard.appendfile("prerightrecording.txt", bytearray("Pusher: " + "False, " + str(timer.time()) + "\n", "utf-8"))

def loadertoggle():
    global loader_state
    if loader_state==0:
        loader.set(True)
        loader_state=1
        brain.sdcard.appendfile("prerightrecording.txt", bytearray("Loader: " + "True, " + str(timer.time()) + "\n", "utf-8"))
    else:
        loader.set(False)
        loader_state=0
        brain.sdcard.appendfile("prerightrecording.txt", bytearray("Loader: " + "False, " + str(timer.time()) + "\n", "utf-8"))

def selection():
    while True:
        controller_1.screen.clear_row(3)
        controller_1.screen.set_cursor(1, 3)
        controller_1.screen.print("Press A for right recording")
        if record!=0:
            break
        wait(500, MSEC)
        controller_1.screen.clear_row(3)
        controller_1.screen.set_cursor(1, 3)
        controller_1.screen.print("Press B for left recording")
        if record!=0:
            break
        wait(500, MSEC)

def rightrecording():
    global record, controlleraxis2positionhistory, controlleraxis3positionhistory
    record=1
    controller_1.screen.clear_row(3)
    controller_1.screen.set_cursor(1, 3)
    controller_1.screen.print("Right Recording")
    brain.sdcard.savefile("prerightrecording.txt")
    while record==1:
        if controller_1.axis2.position() != 0:
            left1.set_position(0, DEGREES) #left joystick/drive
            while controller_1.axis2.position() != 0:
                if controller_1.axis2.position() != controlleraxis2positionhistory:
                    controlleraxis2positionhistory=controller_1.axis2.position()
                    brain.sdcard.appendfile("prerightrecording.txt", bytearray("Left Joystick: " + str(controller_1.axis2.position()) + ", left side degrees moved: " + str(left1.position(DEGREES)) + ", time: " + str(timer.time()) + "\n", "utf-8"))
                    left1.set_position(0, DEGREES)

        if controller_1.axis3.position() != 0:
            right1.set_position(0, DEGREES) #right joystick/drive
            while controller_1.axis3.position() != 0:
                if controller_1.axis3.position() != controlleraxis3positionhistory:
                    controlleraxis3positionhistory=controller_1.axis3.position()
                    brain.sdcard.appendfile("prerightrecording.txt", bytearray("Right Joystick: " + str(controller_1.axis3.position()) + ", right side degrees moved: " + str(right1.position(DEGREES)) + ", time: " + str(timer.time()) + "\n", "utf-8"))
                    right1.set_position(0, DEGREES)

def leftrecording():
    global record, controlleraxis2positionhistory, controlleraxis3positionhistory
    record=2
    controller_1.screen.clear_row(3)
    controller_1.screen.set_cursor(1, 3)
    controller_1.screen.print("Left Recording")
    brain.sdcard.savefile("preleftrecording.txt")
    while record==2:
        if controller_1.axis2.position() != 0:
            right1.set_position(0, DEGREES) #right joystick/drive
            while controller_1.axis2.position() != 0:
                if controller_1.axis2.position() != controlleraxis2positionhistory:
                    controlleraxis2positionhistory=controller_1.axis2.position()
                    brain.sdcard.appendfile("preleftrecording.txt", bytearray("Left Joystick:, " + str(controller_1.axis2.position()) + ", left side degrees moved:, " + str(left1.position(DEGREES)) + ", time:, " + str(timer.time()) + "\n", "utf-8"))
                    left1.set_position(0, DEGREES)

        if controller_1.axis3.position() != 0:
            right1.set_position(0, DEGREES) #right joystick/drive
            while controller_1.axis3.position() != 0:
                if controller_1.axis3.position() != controlleraxis3positionhistory:
                    controlleraxis3positionhistory=controller_1.axis3.position()
                    brain.sdcard.appendfile("preleftrecording.txt", bytearray("Right Joystick:, " + str(controller_1.axis3.position()) + ", right side degrees moved:, " + str(right1.position(DEGREES)) + ", time:, " + str(timer.time()) + "\n", "utf-8"))
                    right1.set_position(0, DEGREES)


def leftmove(leftspeed, degrees):
    left1.set_velocity(leftspeed, PERCENT)
    left1.spin_for(FORWARD, degrees, DEGREES)
    left2.set_velocity(leftspeed, PERCENT)
    left2.spin_for(FORWARD, degrees, DEGREES)
    left3.set_velocity(leftspeed, PERCENT)
    left3.spin_for(FORWARD, degrees, DEGREES)

def rightmove(rightspeed, degrees):
    right1.set_velocity(rightspeed, PERCENT)
    right1.spin_for(FORWARD, degrees, DEGREES)
    right2.set_velocity(rightspeed, PERCENT)
    right2.spin_for(FORWARD, degrees, DEGREES)
    right3.set_velocity(rightspeed, PERCENT)
    right3.spin_for(FORWARD, degrees, DEGREES)

def when_started():
    while True:
        if record==0:
            selection()
        wait(20, MSEC)

def encode():
    brain.sdcard.savefile("Right Aton.txt", bytearray(", ", "utf-8"))
    brain.sdcard.savefile("Left Aton.txt",  bytearray(", ", "utf-8"))
    preleftrecordingfile=brain.sdcard.loadfile("preleftrecording.txt").decode("utf-8")
    prerightrecordingfile=brain.sdcard.loadfile("prerightrecording.txt").decode("utf-8")
    preleftrecordinglist=preleftrecordingfile.splitlines()
    prerightrecordinglist=prerightrecordingfile.splitlines()

    for i in range(len(preleftrecordinglist)):
        preleftlist1=preleftrecordinglist[i].split(',')
        preleftlist2=preleftrecordinglist[i+1].split(',')
        if preleftlist1[0] == "Left Joystick:":

            if preleftlist2[0] == "Left Joystick:":

                if math.isclose(int(preleftlist1[1]), int(preleftlist2[1]), abs_tol=tolrance):
                    timemax1=int(preleftlist1[5])
                    timemax2=int(preleftlist2[5])
                    preleftrecordinglist[i+1]="Left Joystick:, " + str(int(preleftlist1[1]) + int(preleftlist2[1])/2) + ", left side degrees moved:, " + str(int(preleftlist1[3]) + int(preleftlist2[3])) + ", time:, " + str(max(timemax1, timemax2)) + "\n"
                    preleftrecordinglist[i]=""
                    continue
            elif preleftlist2[0]== "Right Joystick":
                timemax1=int(preleftlist1[5])
                timemax2=int(preleftlist2[5])
                preleftrecordinglist[i+1]="Forward:, Left:, " + str(preleftlist1[1]) + ", Right:, " + str(preleftlist2[1]) + ", left side degrees moved:, " + str(preleftlist1[3]) + "right side degrees moved:, " + str(preleftlist2[3]) + ", time:, " + str(max(timemax1, timemax2)) + "\n"
                preleftrecordinglist[i]=""
                continue

        if preleftlist1[0] == "Right Joystick:":

            if preleftlist2[0] == "Right Joystick:":

                if math.isclose(int(preleftlist1[1]), int(preleftlist2[1]), abs_tol=tolrance):
                    timemax1=int(preleftlist1[5])
                    timemax2=int(preleftlist2[5])
                    preleftrecordinglist[i+1]="Right Joystick:, " + str(int(preleftlist1[1]) + int(preleftlist2[1])/2) + ", Right side degrees moved:, " + str(int(preleftlist1[3]) + int(preleftlist2[3])) + ", time:, " + str(max(timemax1, timemax2)) + "\n"
                    preleftrecordinglist[i]=""
                    continue
            elif preleftlist2[0]== "Left Joystick":
                timemax1=int(preleftlist1[5])
                timemax2=int(preleftlist2[5])
                preleftrecordinglist[i+1]="Forward:, Left:, " + str(preleftlist2[1]) + ", Right:, " + str(preleftlist1[1]) + ", left side degrees moved:, " + str(preleftlist2[3]) + "right side degrees moved:, " + str(preleftlist1[3]) + ", time:, " + str(max(timemax1, timemax2)) + "\n"
                preleftrecordinglist[i]=""
                continue
        

                

def driver():
    pass

def autonomous():
    rightatonfile=brain.sdcard.loadfile("Right Aton.txt").decode("utf-8")
    exec(rightatonfile)


comp=Competition(driver, autonomous)
controller_1.axis2.changed(rightside)
controller_1.axis3.changed(leftside)
controller_1.buttonR1.pressed(intakeup)
controller_1.buttonR2.pressed(intakedown)
controller_1.buttonL1.pressed(scoreup)
controller_1.buttonL2.pressed(scoredown)
controller_1.buttonY.pressed(pushertoggle)
controller_1.buttonB.pressed(loadertoggle)
controller_1.buttonRight.pressed(rightrecording)
controller_1.buttonLeft.pressed(leftrecording)
controller_1.buttonDown.pressed(encode)
when_started()

