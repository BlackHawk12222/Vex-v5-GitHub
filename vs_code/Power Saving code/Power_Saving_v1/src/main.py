# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       MicaS                                                        #
# 	Created:      2/12/2026, 1:07:05 PM                                        #
# 	Description:  V5 project Test for powersaving.                             #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *

# Brain should be defined by default
brain=Brain()

controller_1 = Controller(PRIMARY)
motor_1 = Motor(Ports.PORT14, GearSetting.RATIO_6_1, False)
motor_2 = Motor(Ports.PORT15, GearSetting.RATIO_18_1, False)
motor_3 = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
right1 = Motor(Ports.PORT11, GearSetting.RATIO_6_1, False)
right2 = Motor(Ports.PORT12, GearSetting.RATIO_6_1, False)
right3 = Motor(Ports.PORT16, GearSetting.RATIO_6_1, False)
left1 = Motor(Ports.PORT13, GearSetting.RATIO_6_1, False)
left2 = Motor(Ports.PORT17, GearSetting.RATIO_6_1, False)
left3 = Motor(Ports.PORT20, GearSetting.RATIO_6_1, False)
timer=Timer()

left=0
right=0

class Power:
    def __init__(self):
        self.Sleep={}
    
    def sleep(self, motor):
        if self.Sleep.get(motor, False):
            motor.stop(COAST)
            motor.set_velocity(0, PERCENT)
            motor.set_torque(0, CurrentUnits.AMP)
            self.Sleep[motor] = True
    
    def wake(self, motor):
        if self.Sleep.get(motor, True):
            motor.set_velocity(100, PERCENT)
            motor.set_torque(100, CurrentUnits.AMP)
            motor.set_stopping(BRAKE)
            self.Sleep[motor] = False

power = Power()

def sleeping():
    power.sleep(motor_1)
    power.sleep(motor_2)
    power.sleep(motor_3)
    power.sleep(right1)
    power.sleep(right2)
    power.sleep(right3)
    power.sleep(left1)
    power.sleep(left2)
    power.sleep(left3)
    controller_1.screen.clear_row(3)
    controller_1.screen.set_cursor(3, 1)
    controller_1.screen.print("Motors are now sleeping.")

def waking():
    power.wake(motor_1)
    power.wake(motor_2)
    power.wake(motor_3)
    power.wake(right1)
    power.wake(right2)
    power.wake(right3)
    power.wake(left1)
    power.wake(left2)
    power.wake(left3)
    controller_1.screen.clear_row(3)
    controller_1.screen.set_cursor(3, 1)
    controller_1.screen.print("Motors are now waking.")

def left_drive():
    left=controller_1.axis3.position()/ 12.88
    left1.spin(FORWARD, left, VOLT)
    left2.spin(FORWARD, left, VOLT)
    left3.spin(FORWARD, left, VOLT)
    wait(5, MSEC)

def right_drive():
    right=controller_1.axis2.position()/ 12.88
    right1.spin(FORWARD, right, VOLT)
    right2.spin(FORWARD, right, VOLT)
    right3.spin(FORWARD, right, VOLT)
    wait(5, MSEC)

def intake_up():
    motor_1.spin(FORWARD, 100, PERCENT)

def intake_down():
    motor_1.spin(REVERSE, 100, PERCENT)

def sleep_timer():
    while True:
        if timer.value() > 10000:
            sleeping()
        
        if controller_1.buttonA.pressing() or controller_1.buttonB.pressing() or controller_1.buttonL1.pressing() or controller_1.buttonL2.pressing() or controller_1.axis3.position() != 0 or controller_1.axis2.position() != 0:
            timer.reset()
            waking()

controller_1.buttonA.pressed(sleeping)
controller_1.buttonB.pressed(waking)
controller_1.buttonL1.pressed(intake_up)
controller_1.buttonL2.pressed(intake_down)
Thread(left_drive)
Thread(right_drive)
Thread(sleep_timer)