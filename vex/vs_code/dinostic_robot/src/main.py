# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       micah's                                                      #
# 	Created:      1/20/2026, 4:16:41 PM                                        #
# 	Description:  V5 Robot Health check                                        #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *

# Brain should be defined by default
brain=Brain()

#Robot configureation code
controller_1 = Controller(PRIMARY)
Right1 = Motor(Ports.PORT11, GearSetting.RATIO_6_1, False)
Right2 = Motor(Ports.PORT13, GearSetting.RATIO_6_1, False)
Right3 = Motor(Ports.PORT12, GearSetting.RATIO_6_1, True)
Left1 = Motor(Ports.PORT20, GearSetting.RATIO_6_1, True)
Left3 = Motor(Ports.PORT18, GearSetting.RATIO_6_1, False)
Intake_Motor = Motor(Ports.PORT14, GearSetting.RATIO_6_1, True)
optical_9 = Optical(Ports.PORT9)
colorsorting = Motor(Ports.PORT15, GearSetting.RATIO_18_1, True)
Left2 = Motor(Ports.PORT19, GearSetting.RATIO_6_1, True)
TopMotor = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
frontPiston = DigitalOut(brain.three_wire_port.a)
inertial_for_auton = Inertial(Ports.PORT6)
Pusher = DigitalOut(brain.three_wire_port.b)

# Brain should be defined by default
brain=Brain()

# Shortcuts for brain screen functions
B_print=brain.screen.print
B_nl=brain.screen.new_line
B_cs=brain.screen.clear_screen
B_penc=brain.screen.set_pen_color

def Motor_Check(Motor_port, Motor_name): #checks if Motor installed, temperature, and if it spins
    if Motor_name.temperature(PERCENT) == 2:
        B_penc(Color.RED)
        B_print(Motor_name, " not detected. Port: ", Motor_port)
        B_nl()
    elif Motor_name.temperature(PERCENT) >= 50 and Motor_name.temperature(PERCENT) < 80:
       B_penc(Color.YELLOW)
       B_print(Motor_name, "hot. Port: ", Motor_port)
       B_nl()
    elif Motor_name.temperature(PERCENT) >=80:
        B_penc(Color.ORANGE)
        B_print(Motor_name, "critical. Port: ", Motor_port)
        B_nl()
    if Motor_name.temperature(PERCENT) < 50 and Motor_name.temperature(PERCENT) != 2:
        Motor_name.set_velocity(100,PERCENT)
        Motor_name.set_position(0,DEGREES)
        Motor_name.spin(FORWARD)
        wait(200,MSEC)
        if Motor_name.position(DEGREES) < 40:
            B_penc(Color.PURPLE)
            B_print(Motor_name,"not spinning Forward. Port:", Motor_port, Motor_name.position(DEGREES))
            B_nl()
        Motor_name.stop()
        wait(500,MSEC)
        Motor_name.set_position(0,DEGREES)
        Motor_name.spin(REVERSE)
        wait(200,MSEC)
        if  Motor_name.position(DEGREES) > -40:
            B_penc(Color.PURPLE)
            B_print(Motor_name,"not spinning Reverse. Port:", Motor_port, Motor_name.position(DEGREES))
            B_nl()
        Motor_name.stop()

B_print("Checking health...")
B_nl()

# Motor Checks function calls:
Motor_Check(11, Right1)
Motor_Check(13, Right2)
Motor_Check(12, Right3)
Motor_Check(20, Left1)
Motor_Check(19, Left2)
Motor_Check(18, Left3)
Motor_Check(1, TopMotor)
Motor_Check(14, Intake_Motor)
Motor_Check(15, colorsorting)

# Battery Check:

# Battery capacity Check
if brain.battery.capacity() <=25:
    B_penc(Color.ORANGE)
    B_print("Battery Critical")
    B_nl()
elif brain.battery.capacity() <=50:
    B_penc(Color.YELLOW)
    B_print("battery low")
    B_nl()

# Battery voltage Check
if brain.battery.voltage(VoltageUnits.VOLT) < 10:
    B_penc(Color.RED)
    B_print("Battery Voltage Critical. Voltage: ", brain.battery.voltage(VoltageUnits.VOLT))
    B_nl()
elif brain.battery.voltage(VoltageUnits.VOLT) < 12:
    B_penc(Color.YELLOW)
    B_print("Battery Voltage Low. Voltage: ", brain.battery.voltage(VoltageUnits.VOLT))
    B_nl()
if inertial_for_auton.installed() == False:
    B_penc(Color.RED)
    B_print("Inertial Sensor not detected. Port: 6")
    B_nl()

B_print("Health Check Complete.")