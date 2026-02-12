# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       Micah Bow                                                    #
# 	Created:      1/27/2026, 12:41:53 PM                                       #
# 	Description:  Universal Logging software V03                               #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *

# Brain should be defined by default
# ---------------------------------------------------------------------------- #
# Section: Hardware / Devices
# ---------------------------------------------------------------------------- #
brain=Brain()

controller_1=Controller(PRIMARY)
controller_2=Controller(PARTNER)
Left1=Motor(Ports.PORT18, GearSetting.RATIO_6_1, False)
Left2=Motor(Ports.PORT19, GearSetting.RATIO_6_1, False)
Left3=Motor(Ports.PORT20, GearSetting.RATIO_6_1, False)
Right1=Motor(Ports.PORT11, GearSetting.RATIO_6_1, True)
Right2=Motor(Ports.PORT13, GearSetting.RATIO_6_1, True)
Right3=Motor(Ports.PORT12, GearSetting.RATIO_6_1, True)
Intake_Motor=Motor(Ports.PORT14, GearSetting.RATIO_6_1, False)
TopMotor=Motor(Ports.PORT1, GearSetting.RATIO_6_1, False)
colorsorting=Motor(Ports.PORT15, GearSetting.RATIO_6_1, False)

# Timer for log time
log_time= Timer()

example_variable=0

# snapshot for parts of robot
# ---------------------------------------------------------------------------- #
# Section: Classes
# ---------------------------------------------------------------------------- #
class Record:
    def __init__(self):
        self.axis=""
        self.value=0
        self.button_value=False
        self.index=0
        self.button=""

    # snapshot of controller 1 axis
    def controller_1_axis(self, axis):
        self.axis=axis
        if brain.sdcard.is_inserted():
            index_content=brain.sdcard.loadfile("index.txt")
            self.index=int(index_content.decode("utf-8"))
        if self.axis=="AXIS1" or self.axis=="1":
            self.value=controller_1.axis1.position()
            if brain.sdcard.is_inserted():
                brain.sdcard.appendfile("Log.csv", bytearray(", %s [%s] Controller_1_Axis1: %s \n" %(self.index, log_time, self.value), "utf-8"))
            else:
                print(", %s [%s] Controller_1_Axis1: %s"%(self.index, log_time, self.value))
        elif self.axis=="AXIS2" or self.axis=="2":
            self.value=controller_1.axis2.position()
            if brain.sdcard.is_inserted():
                brain.sdcard.appendfile("Log.csv", bytearray(", %s [%s] Controller_1_Axis2: %s \n"%(self.index, log_time, self.value), "utf-8"))
            else:
                print(", %s [%s] Controller_1_Axis2: %s"%(self.index, log_time, self.value))
        elif self.axis=="AXIS3" or self.axis=="3":
            self.value=controller_1.axis3.position()
            if brain.sdcard.is_inserted():
                brain.sdcard.appendfile("Log.csv", bytearray(", %s [%s] Controller_1_Axis3: %s \n"%(self.index, log_time, self.value), "utf-8"))
            else:
                print(", %s [%s] Controller_1_Axis3: %s"%(self.index, log_time, self.value))
        elif self.axis=="AXIS4" or self.axis=="4":
            self.value=controller_1.axis4.position()
            if brain.sdcard.is_inserted():
                brain.sdcard.appendfile("Log.csv", bytearray(", %s [%s] Controller_1_Axis4: %s \n"%(self.index, log_time, self.value), "utf-8"))
            else:
                print(", %s [%s] Controller_1_Axis4: %s"%(self.index, log_time, self.value))
        self.index+=1
        brain.sdcard.savefile("index.txt", bytearray("%d"%(self.index), "utf-8"))
    
    # snapshot of controller 1 button
    def controller_1_button(self, button):
        self.button=button
        if brain.sdcard.is_inserted():
            index_content=brain.sdcard.loadfile("index.txt")
            self.index=int(index_content.decode("utf-8"))
        if self.button=="A":
            self.button_value=controller_1.buttonA.pressing()
            if brain.sdcard.is_inserted():
                brain.sdcard.appendfile("Log.csv", bytearray(", %s [%s] Controller_1_ButtonA: %s \n"%(self.index, log_time, self.button_value), "utf-8"))
            else:
                print(", %s [%s] Controller_1_ButtonA: %s"%(self.index, log_time, self.button_value))
        elif self.button=="B" or self.button=="b":
            self.button_value=controller_1.buttonB.pressing()
            if brain.sdcard.is_inserted():
                brain.sdcard.appendfile("Log.csv", bytearray(", %s [%s] Controller_1_ButtonB: %s \n"%(self.index, log_time, self.button_value), "utf-8"))
            else:
                print(", %s [%s] Controller_1_ButtonB: %s"%(self.index, log_time, self.button_value))
        elif self.button=="Y" or self.button=="y":
            self.button_value=controller_1.buttonY.pressing()
            if brain.sdcard.is_inserted():
                brain.sdcard.appendfile("Log.csv", bytearray(", %s [%s] Controller_1_ButtonY: %s \n"%(self.index, log_time, self.button_value), "utf-8"))
            else:
                print(", %s [%s] Controller_1_ButtonY: %s"%(self.index, log_time, self.button_value))
        elif self.button=="X" or self.button=="x":
            self.button_value=controller_1.buttonX.pressing()
            if brain.sdcard.is_inserted():
                brain.sdcard.appendfile("Log.csv", bytearray(", %s [%s] Controller_1_ButtonX: %s \n"%(self.index, log_time, self.button_value), "utf-8"))
            else:
                print(", %s [%s] Controller_1_ButtonX: %s"%(self.index, log_time, self.button_value))
        elif self.button=="UP" or self.button=="up" or self.button=="Up":
            self.button_value=controller_1.buttonUp.pressing()
            if brain.sdcard.is_inserted():
                brain.sdcard.appendfile("Log.csv", bytearray(", %s [%s] Controller_1_ButtonUp: %s \n"%(self.index, log_time, self.button_value), "utf-8"))
            else:
                print(", %s [%s] Controller_1_ButtonUp: %s"%(self.index, log_time, self.button_value))
        elif self.button=="DOWN" or self.button=="down" or self.button=="Down":
            self.button_value=controller_1.buttonDown.pressing()
            if brain.sdcard.is_inserted():
                brain.sdcard.appendfile("Log.csv", bytearray(", %s [%s] Controller_1_ButtonDown: %s \n"%(self.index, log_time, self.button_value), "utf-8"))
            else:
                print(", %s [%s] Controller_1_ButtonDown: %s"%(self.index, log_time, self.button_value))
        elif self.button=="LEFT" or self.button=="left" or self.button=="Left":
            self.button_value=controller_1.buttonLeft.pressing()
            if brain.sdcard.is_inserted():
                brain.sdcard.appendfile("Log.csv", bytearray(", %s [%s] Controller_1_ButtonLeft: %s \n"%(self.index, log_time, self.button_value), "utf-8"))
            else:
                print(", %s [%s] Controller_1_ButtonLeft: %s"%(self.index, log_time, self.button_value))
        elif self.button=="RIGHT" or self.button=="right" or self.button=="Right":
            self.button_value=controller_1.buttonRight.pressing()
            if brain.sdcard.is_inserted():
                brain.sdcard.appendfile("Log.csv", bytearray(", %s [%s] Controller_1_ButtonRight: %s \n"%(self.index, log_time, self.button_value), "utf-8"))
            else:
                print(", %s [%s] Controller_1_ButtonRight: %s"%(self.index, log_time, self.button_value))
        elif self.button=="L1" or self.button=="l1":
            self.button_value=controller_1.buttonL1.pressing()
            if brain.sdcard.is_inserted():
                brain.sdcard.appendfile("Log.csv", bytearray(", %s [%s] Controller_1_ButtonL1: %s \n"%(self.index, log_time, self.button_value), "utf-8"))
            else:
                print(", %s [%s] Controller_1_ButtonL1: %s"%(self.index, log_time, self.button_value))
        elif self.button=="L2" or self.button=="l2":
            self.button_value=controller_1.buttonL2.pressing()
            if brain.sdcard.is_inserted():
                brain.sdcard.appendfile("Log.csv", bytearray(", %s [%s] Controller_1_ButtonL2: %s \n"%(self.index, log_time, self.button_value), "utf-8"))
            else:
                print(", %s [%s] Controller_1_ButtonL2: %s"%(self.index, log_time, self.button_value))
        elif self.button=="R1" or self.button=="r1":
            self.button_value=controller_1.buttonR1.pressing()
            if brain.sdcard.is_inserted():
                brain.sdcard.appendfile("Log.csv", bytearray(", %s [%s] Controller_1_ButtonR1: %s \n"%(self.index, log_time, self.button_value), "utf-8"))
            else:
                print(", %s [%s] Controller_1_ButtonR1: %s"%(self.index, log_time, self.button_value))
        elif self.button=="R2" or self.button=="r2":
            self.button_value=controller_1.buttonR2.pressing()
            if brain.sdcard.is_inserted():
                brain.sdcard.appendfile("Log.csv", bytearray(", %s [%s] Controller_1_ButtonR2: %s \n"%(self.index, log_time, self.button_value), "utf-8"))
            else:
                print(", %s [%s] Controller_1_ButtonR2: %s"%(self.index, log_time, self.button_value))
        self.index+=1
        brain.sdcard.savefile("index.txt", bytearray("%d"%(self.index), "utf-8"))

    # snapshot of controller 2 axis
    def controller_2_axis(self, axis):
        self.axis=axis
        if brain.sdcard.is_inserted():
            index_content=brain.sdcard.loadfile("index.txt")
            self.index=int(index_content.decode("utf-8"))
        if self.axis=="AXIS1" or self.axis=="1":
            self.value=controller_2.axis1.position()
            if brain.sdcard.is_inserted():
                brain.sdcard.appendfile("Log.csv", bytearray(", %s [%s] Controller_2_Axis1: %f \n"%(self.index, log_time, self.value), "utf-8"))
            else:
                print("Controller_2_Axis1: %f"%(self.value))
        elif self.axis=="AXIS2" or self.axis=="2":
            self.value=controller_2.axis2.position()
            if brain.sdcard.is_inserted():
                brain.sdcard.appendfile("Log.csv", bytearray(", %s [%s] Controller_2_Axis2: %f \n"%(self.index, log_time, self.value), "utf-8"))
            else:
                print("Controller_2_Axis2: %f"%(self.value))
        elif self.axis=="AXIS3" or self.axis=="3":
            self.value=controller_2.axis3.position()
            if brain.sdcard.is_inserted():
                brain.sdcard.appendfile("Log.csv", bytearray(", %s [%s] Controller_2_Axis3: %f \n"%(self.index, log_time, self.value), "utf-8"))
            else:
                print("Controller_2_Axis3: %f"%(self.value))
        elif self.axis=="AXIS4" or self.axis=="4":
            self.value=controller_2.axis4.position()
            if brain.sdcard.is_inserted():
                brain.sdcard.appendfile("Log.csv", bytearray(", %s [%s] Controller_2_Axis4: %f \n"%(self.index, log_time, self.value), "utf-8"))
            else:
                print("Controller_2_Axis4: %f"%(self.value))
        self.index+=1
        brain.sdcard.savefile("index.txt", bytearray("%d"%(self.index), "utf-8"))
    
    # snapshot of controller 2 button
    def controller_2_button(self, button):
        self.button=button
        if brain.sdcard.is_inserted():
            index_content=brain.sdcard.loadfile("index.txt")
            self.index=int(index_content.decode("utf-8"))
        if self.button=="A":
            self.button_value=controller_2.buttonA.pressing()
            if brain.sdcard.is_inserted():
                brain.sdcard.appendfile("Log.csv", bytearray(", %s [%s] Controller_2_ButtonA: %s \n"%(self.index, log_time, self.button_value), "utf-8"))
            else:
                print("Controller_2_ButtonA: %s"%(self.button_value))
        elif self.button=="B" or self.button=="b":
            self.button_value=controller_2.buttonB.pressing()
            if brain.sdcard.is_inserted():
                brain.sdcard.appendfile("Log.csv", bytearray(", %s [%s] Controller_2_ButtonB: %s \n"%(self.index, log_time, self.button_value), "utf-8"))
            else:
                print("Controller_2_ButtonB: %s"%(self.button_value))
        elif self.button=="Y" or self.button=="y":
            self.button_value=controller_2.buttonY.pressing()
            if brain.sdcard.is_inserted():
                brain.sdcard.appendfile("Log.csv", bytearray(", %s [%s] Controller_2_ButtonY: %s \n"%(self.index, log_time, self.button_value), "utf-8"))
            else:
                print("Controller_2_ButtonY: %s"%(self.button_value))
        elif self.button=="X" or self.button=="x":
            self.button_value=controller_2.buttonX.pressing()
            if brain.sdcard.is_inserted():
                brain.sdcard.appendfile("Log.csv", bytearray(", %s [%s] Controller_2_ButtonX: %s \n"%(self.index, log_time, self.button_value), "utf-8"))
            else:
                print("Controller_2_ButtonX: %s"%(self.button_value))
        elif self.button=="UP" or self.button=="up" or self.button=="Up":
            self.button_value=controller_2.buttonUp.pressing()
            if brain.sdcard.is_inserted():
                brain.sdcard.appendfile("Log.csv", bytearray(", %s [%s] Controller_2_ButtonUp: %s \n"%(self.index, log_time, self.button_value), "utf-8"))
            else:
                print("Controller_2_ButtonUp: %s"%(self.button_value))
        elif self.button=="DOWN" or self.button=="down" or self.button=="Down":
            self.button_value=controller_2.buttonDown.pressing()
            if brain.sdcard.is_inserted():
                brain.sdcard.appendfile("Log.csv", bytearray(", %s [%s] Controller_2_ButtonDown: %s \n"%(self.index, log_time, self.button_value), "utf-8"))
            else:
                print("Controller_2_ButtonDown: %s"%(self.button_value))
        elif self.button=="LEFT" or self.button=="left" or self.button=="Left":
            self.button_value=controller_2.buttonLeft.pressing()
            if brain.sdcard.is_inserted():
                brain.sdcard.appendfile("Log.csv", bytearray(", %s [%s] Controller_2_ButtonLeft: %s \n"%(self.index, log_time, self.button_value), "utf-8"))
            else:
                print("Controller_2_ButtonLeft: %s"%(self.button_value))
        elif self.button=="RIGHT" or self.button=="right" or self.button=="Right":
            self.button_value=controller_2.buttonRight.pressing()
            if brain.sdcard.is_inserted():
                brain.sdcard.appendfile("Log.csv", bytearray(", %s [%s] Controller_2_ButtonRight: %s \n"%(self.index, log_time, self.button_value), "utf-8"))
            else:
                print("Controller_2_ButtonRight: %s"%(self.button_value))
        elif self.button=="L1" or self.button=="l1":
            self.button_value=controller_2.buttonL1.pressing()
            if brain.sdcard.is_inserted():
                brain.sdcard.appendfile("Log.csv", bytearray(", %s [%s] Controller_2_ButtonL1: %s \n"%(self.index, log_time, self.button_value), "utf-8"))
            else:
                print("Controller_2_ButtonL1: %s"%(self.button_value))
        elif self.button=="L2" or self.button=="l2":
            self.button_value=controller_2.buttonL2.pressing()
            if brain.sdcard.is_inserted():
                brain.sdcard.appendfile("Log.csv", bytearray(", %s [%s] Controller_2_ButtonL2: %s \n"%(self.index, log_time, self.button_value), "utf-8"))
            else:
                print("Controller_2_ButtonL2: %s"%(self.button_value))
        elif self.button=="R1" or self.button=="r1":
            self.button_value=controller_2.buttonR1.pressing()
            if brain.sdcard.is_inserted():
                brain.sdcard.appendfile("Log.csv", bytearray(", %s [%s] Controller_2_ButtonR1: %s \n"%(self.index, log_time, self.button_value), "utf-8"))
            else:
                print("Controller_2_ButtonR1: %s"%(self.button_value))
        elif self.button=="R2" or self.button=="r2":
            self.button_value=controller_2.buttonR2.pressing()
            if brain.sdcard.is_inserted():
                brain.sdcard.appendfile("Log.csv", bytearray(", %s [%s] Controller_2_ButtonR2: %s \n"%(self.index, log_time, self.button_value), "utf-8"))
            else:
                print("Controller_2_ButtonR2: %s"%(self.button_value))
        self.index+=1
        brain.sdcard.savefile("index.txt", bytearray("%d"%(self.index), "utf-8"))

    #snapshot of variable
    def Variable(self, name, value):
        self.name=name
        self.value=value
        if brain.sdcard.is_inserted():
            index_content=brain.sdcard.loadfile("index.txt")
            self.index=int(index_content.decode("utf-8"))
            brain.sdcard.appendfile("Log.csv", bytearray(", %s [%s] Variable_%s: %s \n"%(self.index, log_time, self.name, self.value), "utf-8"))
        else:
            print(", %s [%s] Variable_%s: %s"%(self.index, log_time, self.name, self.value))
        self.index+=1
        brain.sdcard.savefile("index.txt", bytearray("%d"%(self.index), "utf-8"))

    def Add_function(self, name, print_out):
        pass

# Reading Log
class Read:
    def console(self):
        if brain.sdcard.is_inserted():
            Log_content=brain.sdcard.loadfile("Log.csv")
            print(Log_content.decode("utf-8"))
        else:
            print("No SD Card Inserted Cannot Read Log")
        
    
    def brain(self):
        if brain.sdcard.is_inserted():
            Log_content=brain.sdcard.loadfile("Log.csv")
            brain.screen.print(Log_content.decode("utf-8")) 
        else:
            brain.screen.print("No SD Card Inserted Cannot Read Log")

# Drivetrain monitoring
class Drivetrain:
    def __init__(self):
        self.front_left_motor=""
        self.front_right_motor=""
        self.middle_left_motor=""
        self.middle_right_motor=""
        self.back_left_motor=""
        self.back_right_motor=""
        self.left_motor=""
        self.right_motor=""
    
    # two motor drivetrain Logging
    def two_motor(self, left_motor, right_motor):
        self.left_motor=left_motor
        self.right_motor=right_motor
        self.temp_monitoring=0
        self.power_monitoring=0
        self.voltage_monitoring=False
        while True:    
            if (right_motor.temperature()>70 or left_motor.temperature()>70) and (self.temp_monitoring==0 or self.temp_monitoring==2):
                log.add("ED1", "Temp: %s"%(max(right_motor.temperature(), left_motor.temperature())))
                self.temp_monitoring=1
            elif (right_motor.temperature()>50 or left_motor.temperature()>50) and (self.temp_monitoring==0 or self.temp_monitoring==1):
                log.add("WD0", "Temp: %s"%(max(right_motor.temperature(), left_motor.temperature())))
                self.temp_monitoring=2
            elif right_motor.temperature()<=50 and left_motor.temperature()<=50 and (self.temp_monitoring==1 or self.temp_monitoring==2):
                self.temp_monitoring=0
            if right_motor.power(PowerUnits.WATT)>40 or left_motor.power(PowerUnits.WATT)>40 and (self.power_monitoring==0 or self.power_monitoring==2):
                log.add("ED3", "Power: %s"%(max(right_motor.power(PowerUnits.WATT), left_motor.power(PowerUnits.WATT))))
                self.power_monitoring=1
            elif right_motor.power(PowerUnits.WATT)>30 or left_motor.power(PowerUnits.WATT)>30 and (self.power_monitoring==0 or self.power_monitoring==1):
                log.add("WD3", "Power: %s"%(max(right_motor.power(PowerUnits.WATT), left_motor.power(PowerUnits.WATT))))
                self.power_monitoring=2
            elif right_motor.power(PowerUnits.WATT)<=30 and left_motor.power(PowerUnits.WATT)<=30 and (self.power_monitoring==1 or self.power_monitoring==2):
                self.power_monitoring=0
            wait(100, MSEC)

    #four motor drivetrain Logging
    def four_motor(self, front_left_motor, front_right_motor, back_left_motor, back_right_motor):
        self.front_left_motor=front_left_motor
        self.front_right_motor=front_right_motor
        self.back_left_motor=back_left_motor
        self.back_right_motor=back_right_motor
        self.temp_monitoring=0
        self.power_monitoring=0
        self.voltage_monitoring=False
        while True:
            if (front_left_motor.temperature()>70 or front_right_motor.temperature()>70 or back_left_motor.temperature()>70 or back_right_motor.temperature()>70) and (self.temp_monitoring==0 or self.temp_monitoring==2):
                log.add("ED1", "Temp: %s"%(max(front_left_motor.temperature(), front_right_motor.temperature(), back_left_motor.temperature(), back_right_motor.temperature())))
                self.temp_monitoring=1
            elif (front_left_motor.temperature()>50 or front_right_motor.temperature()>50 or back_left_motor.temperature()>50 or back_right_motor.temperature()>50) and (self.temp_monitoring==0 or self.temp_monitoring==1):
                log.add("WD0", "Temp: %s"%(max(front_left_motor.temperature(), front_right_motor.temperature(), back_left_motor.temperature(), back_right_motor.temperature())))
                self.temp_monitoring=2
            elif (front_left_motor.temperature()<=50 and front_right_motor.temperature()<=50 and back_left_motor.temperature()<=50 and back_right_motor.temperature()<=50) and (self.temp_monitoring==1 or self.temp_monitoring==2):
                self.temp_monitoring=0
            if front_left_motor.power(PowerUnits.WATT)>40 or front_right_motor.power(PowerUnits.WATT)>40 or back_left_motor.power(PowerUnits.WATT)>40 or back_right_motor.power(PowerUnits.WATT)>40 and (self.power_monitoring==0 or self.power_monitoring==2):
                log.add("ED3", "Power: %s"%(max(front_left_motor.power(PowerUnits.WATT), front_right_motor.power(PowerUnits.WATT), back_left_motor.power(PowerUnits.WATT), back_right_motor.power(PowerUnits.WATT))))
                self.power_monitoring=1
            elif front_left_motor.power(PowerUnits.WATT)>30 or front_right_motor.power(PowerUnits.WATT)>30 or back_left_motor.power(PowerUnits.WATT)>30 or back_right_motor.power(PowerUnits.WATT)>30 and (self.power_monitoring==0 or self.power_monitoring==1):  
                log.add("WD3", "Power: %s"%(max(front_left_motor.power(PowerUnits.WATT), front_right_motor.power(PowerUnits.WATT), back_left_motor.power(PowerUnits.WATT), back_right_motor.power(PowerUnits.WATT))))
                self.power_monitoring=2
            elif front_left_motor.power(PowerUnits.WATT)<=30 and front_right_motor.power(PowerUnits.WATT)<=30 and back_left_motor.power(PowerUnits.WATT)<=30 and back_right_motor.power(PowerUnits.WATT)<=30 and (self.power_monitoring==1 or self.power_monitoring==2):
                self.power_monitoring=0
            wait(100, MSEC)
    
    # Six motor drivetrain Logging
    def six_motor(self, front_left_motor, front_right_motor, middle_left_motor, middle_right_motor, back_left_motor, back_right_motor):
        self.front_left_motor=front_left_motor
        self.front_right_motor=front_right_motor
        self.middle_left_motor=middle_left_motor
        self.middle_right_motor=middle_right_motor
        self.back_left_motor=back_left_motor
        self.back_right_motor=back_right_motor
        self.temp_monitoring=0
        self.power_monitoring=0
        self.voltage_monitoring=False
        while True:
            if (self.front_left_motor.temperature(PERCENT)>70 or self.front_right_motor.temperature(PERCENT)>70 or self.middle_left_motor.temperature(PERCENT)>70 or self.middle_right_motor.temperature(PERCENT)>70 or self.back_left_motor.temperature(PERCENT)>70 or self.back_right_motor.temperature(PERCENT)>70) and (self.temp_monitoring==0 or self.temp_monitoring==2):
                log.add("ED1", "Temp: %s"%(max(self.front_left_motor.temperature(PERCENT), self.front_right_motor.temperature(PERCENT), self.middle_left_motor.temperature(PERCENT), self.middle_right_motor.temperature(PERCENT), self.back_left_motor.temperature(PERCENT), self.back_right_motor.temperature(PERCENT))))
                self.temp_monitoring=1
            elif (self.front_left_motor.temperature(PERCENT)>50 or self.front_right_motor.temperature(PERCENT)>50 or self.middle_left_motor.temperature(PERCENT)>50 or self.middle_right_motor.temperature(PERCENT)>50 or self.back_left_motor.temperature(PERCENT)>50 or self.back_right_motor.temperature(PERCENT)>50) and (self.temp_monitoring==0 or self.temp_monitoring==1):
                log.add("WD0", "Temp: %s"%(max(self.front_left_motor.temperature(PERCENT), self.front_right_motor.temperature(PERCENT), self.middle_left_motor.temperature(PERCENT), self.middle_right_motor.temperature(PERCENT), self.back_left_motor.temperature(PERCENT), self.back_right_motor.temperature(PERCENT))))
                self.temp_monitoring=2
            elif (self.front_left_motor.temperature(PERCENT)<=50 and self.front_right_motor.temperature(PERCENT)<=50 and self.middle_left_motor.temperature(PERCENT)<=50 and self.middle_right_motor.temperature(PERCENT)<=50 and self.back_left_motor.temperature(PERCENT)<=50 and self.back_right_motor.temperature(PERCENT)<=50) and (self.temp_monitoring==1 or self.temp_monitoring==2):
                self.temp_monitoring=0
            if self.front_left_motor.power(PowerUnits.WATT)>40 or self.front_right_motor.power(PowerUnits.WATT)>40 or self.middle_left_motor.power(PowerUnits.WATT)>40 or self.middle_right_motor.power(PowerUnits.WATT)>40 or self.back_left_motor.power(PowerUnits.WATT)>40 or self.back_right_motor.power(PowerUnits.WATT)>40 and (self.power_monitoring==0 or self.power_monitoring==2):
                log.add("ED3", "Power: %s"%(max(self.front_left_motor.power(PowerUnits.WATT), self.front_right_motor.power(PowerUnits.WATT), self.middle_left_motor.power(PowerUnits.WATT), self.middle_right_motor.power(PowerUnits.WATT), self.back_left_motor.power(PowerUnits.WATT), self.back_right_motor.power(PowerUnits.WATT))))
                self.power_monitoring=1
            elif self.front_left_motor.power(PowerUnits.WATT)>30 or self.front_right_motor.power(PowerUnits.WATT)>30 or self.middle_left_motor.power(PowerUnits.WATT)>30 or self.middle_right_motor.power(PowerUnits.WATT)>30 or self.back_left_motor.power(PowerUnits.WATT)>30 or self.back_right_motor.power(PowerUnits.WATT)>30 and (self.power_monitoring==0 or self.power_monitoring==1):  
                log.add("WD3", "Power: %s"%(max(self.front_left_motor.power(PowerUnits.WATT), self.front_right_motor.power(PowerUnits.WATT), self.middle_left_motor.power(PowerUnits.WATT), self.middle_right_motor.power(PowerUnits.WATT), self.back_left_motor.power(PowerUnits.WATT), self.back_right_motor.power(PowerUnits.WATT))))
                self.power_monitoring=2
            elif self.front_left_motor.power(PowerUnits.WATT)<=30 and self.front_right_motor.power(PowerUnits.WATT)<=30 and self.middle_left_motor.power(PowerUnits.WATT)<=30 and self.middle_right_motor.power(PowerUnits.WATT)<=30 and self.back_left_motor.power(PowerUnits.WATT)<=30 and self.back_right_motor.power(PowerUnits.WATT)<=30 and (self.power_monitoring==1 or self.power_monitoring==2):
                self.power_monitoring=0
            else:
                pass
            wait(100, MSEC)

class Logging:

    # Drivetrain object for drivetrain monitoring
    def __init__(self):
        self.drivetrain=Drivetrain()
    
    # Logging Motor
    def motor(self, motor):
        self.Motor=motor
        self.temp_monitoring=0
        self.power_monitoring=0
        self.voltage_monitoring=False
        self.capacity_monitoring=0
        while True:
            if motor.temperature()>70 and (self.temp_monitoring==0 or self.temp_monitoring==2):
                log.add("EM0", "%s Name: %s"%(motor.temperature(), self.Motor()))
                self.temp_monitoring=1
            elif motor.temperature()>50 and (self.temp_monitoring==0 or self.temp_monitoring==1):
                log.add("WM0", "%s Name: %s"%(motor.temperature(), self.Motor()))
                self.temp_monitoring=2
            elif motor.temperature()<=50 and (self.temp_monitoring==2 or self.temp_monitoring==1):
                self.temp_monitoring=0
            if motor.power(PowerUnits.WATT)>40 and (self.power_monitoring==0 or self.power_monitoring==2):
                log.add("EM1", "%s Name: %s"%(motor.power(PowerUnits.WATT), self.Motor()))
                self.power_monitoring=1
            elif motor.power(PowerUnits.WATT)>30 and (self.power_monitoring==0 or self.power_monitoring==1):
                log.add("WM1", "%s Name: %s"%(motor.power(PowerUnits.WATT), self.Motor()))
                self.power_monitoring=2
            elif motor.power(PowerUnits.WATT)<=30 and (self.power_monitoring==1 or self.power_monitoring==2):
                self.power_monitoring=0
            wait(100, MSEC)
    
    # Logging Motor Group
    def motor_group(self, motor_group):
        self.Motor_group=motor_group
        self.temp_monitoring=0
        while True:
            max_temp=0
            for motor in motor_group:
                if motor.temperature()>max_temp:
                    max_temp=motor.temperature()
            if max_temp>70 and (self.temp_monitoring==0 or self.temp_monitoring==2):
                log.add("EM0", "%s name: %s"%(max_temp, self.Motor_group()))
                self.temp_monitoring=1
            elif max_temp>50 and (self.temp_monitoring==0 or self.temp_monitoring==1):
                log.add("WM0", "%s name: %s"%(max_temp, self.Motor_group()))
                self.temp_monitoring=2
            elif max_temp<=50 and (self.temp_monitoring==2 or self.temp_monitoring==1):
                self.temp_monitoring=0
            for motor in motor_group:
                if motor.power(PowerUnits.WATT)>40 and (self.power_monitoring==0 or self.power_monitoring==2):
                    log.add("EM1", "%s Name: %s"%(motor.power(PowerUnits.WATT), self.Motor_group))
                    self.power_monitoring=1
                elif motor.power(PowerUnits.WATT)>30 and (self.power_monitoring==0 or self.power_monitoring==1):
                    log.add("WM1", "%s Name: %s"%(motor.power(PowerUnits.WATT), self.Motor_group))
                    self.power_monitoring=2
                elif motor.power(PowerUnits.WATT)<=30 and (self.power_monitoring==1 or self.power_monitoring==2):
                    self.power_monitoring=0
            wait(100, MSEC)
    
    # Logging Battery
    def battery(self):
        self.voltage_monitoring=0
        self.capacity_monitoring=0
        self.current_monitoring=0
        while True:
            if brain.battery.voltage(VoltageUnits.VOLT)<11 and (self.voltage_monitoring==0 or self.voltage_monitoring==2):
                log.add("EB0", "Voltage: %s"%(brain.battery.voltage(VoltageUnits.VOLT)))
                self.voltage_monitoring=1
            elif brain.battery.voltage(VoltageUnits.VOLT)<12 and (self.voltage_monitoring==0 or self.voltage_monitoring==1):
                log.add("WB0", "Voltage: %s"%(brain.battery.voltage(VoltageUnits.VOLT)))
                self.voltage_monitoring=2
            elif brain.battery.voltage(VoltageUnits.VOLT)>=12 and (self.voltage_monitoring==1 or self.voltage_monitoring==2):
                self.voltage_monitoring=0
            if brain.battery.capacity()<25 and (self.capacity_monitoring==0 or self.capacity_monitoring==2):
                log.add("EB1", "Capacity: %s"%(brain.battery.capacity()))
                self.capacity_monitoring=1
            elif brain.battery.capacity()<50 and (self.capacity_monitoring==0 or self.capacity_monitoring==1):
                log.add("WB1", "Capacity: %s"%(brain.battery.capacity()))
                self.capacity_monitoring=2
            elif brain.battery.capacity()>=50 and (self.capacity_monitoring==1 or self.capacity_monitoring==2):
                self.capacity_monitoring=0
            if brain.battery.current(CurrentUnits.AMP)>10 and (self.current_monitoring==0 or self.current_monitoring==2):
                log.add("EB2", "Current: %s"%(brain.battery.current(CurrentUnits.AMP)))
                self.current_monitoring=1
            elif brain.battery.current(CurrentUnits.AMP)>5 and (self.current_monitoring==0 or self.current_monitoring==1):
                log.add("WB2", "Current: %s"%(brain.battery.current(CurrentUnits.AMP)))
                self.current_monitoring=2
            elif brain.battery.current(CurrentUnits.AMP)<=5 and (self.current_monitoring==1):
                self.current_monitoring=0
            wait(100, MSEC)
    
    # Logging Controller 1
    def Controller_1(self):
        self.button_pressing=0
        while True:
            if controller_1.axis1.position()!=0 :
                log.record.controller_1_axis("1")
            if controller_1.axis2.position()!=0:
                log.record.controller_1_axis("2")
            if controller_1.axis3.position()!=0:
                log.record.controller_1_axis("3")
            if controller_1.axis4.position()!=0:
                log.record.controller_1_axis("4")
            if controller_1.buttonA.pressing() and (self.button_pressing==0 or self.button_pressing>=2):
                log.record.controller_1_button("A")
                self.button_pressing=1
            if controller_1.buttonB.pressing() and (self.button_pressing<=1 or self.button_pressing>=3):
                log.record.controller_1_button("B")
                self.button_pressing=2
            if controller_1.buttonX.pressing() and (self.button_pressing<=2 or self.button_pressing>=4):
                log.record.controller_1_button("X")
                self.button_pressing=3
            if controller_1.buttonY.pressing() and (self.button_pressing<=3 or self.button_pressing>=5):
                log.record.controller_1_button("Y")
                self.button_pressing=4
            if controller_1.buttonUp.pressing() and (self.button_pressing<=4 or self.button_pressing>=6):
                log.record.controller_1_button("UP")
                self.button_pressing=5
            if controller_1.buttonDown.pressing() and (self.button_pressing<=5 or self.button_pressing>=7):
                log.record.controller_1_button("DOWN")
                self.button_pressing=6
            if controller_1.buttonLeft.pressing() and (self.button_pressing<=6 or self.button_pressing>=8):
                log.record.controller_1_button("LEFT")
                self.button_pressing=7
            if controller_1.buttonRight.pressing() and (self.button_pressing<=7 or self.button_pressing>=9):
                log.record.controller_1_button("RIGHT")
                self.button_pressing=8
            if controller_1.buttonL1.pressing() and (self.button_pressing<=8 or self.button_pressing>=10):
                log.record.controller_1_button("L1")
                self.button_pressing=9
            if controller_1.buttonL2.pressing() and (self.button_pressing<=9 or self.button_pressing>=11):
                log.record.controller_1_button("L2")
                self.button_pressing=10
            if controller_1.buttonR1.pressing() and (self.button_pressing<=10 or self.button_pressing==12):
                log.record.controller_1_button("R1")
                self.button_pressing=11
            if controller_1.buttonR2.pressing() and (self.button_pressing<=11):
                log.record.controller_1_button("R2")
                self.button_pressing=12
            wait(100, MSEC)
            if not(controller_1.buttonA.pressing() or controller_1.buttonB.pressing() or controller_1.buttonX.pressing() or controller_1.buttonY.pressing() or controller_1.buttonUp.pressing() or controller_1.buttonDown.pressing() or controller_1.buttonLeft.pressing() or controller_1.buttonRight.pressing() or controller_1.buttonL1.pressing() or controller_1.buttonL2.pressing() or controller_1.buttonR1.pressing() or controller_1.buttonR2.pressing()):
                self.button_pressing=0
    
    # Logging Controller 2
    def Controller_2(self):
        self.button_pressing=0
        while True:
            if controller_2.axis1.position()!=0:
                log.record.controller_2_axis("1")
            if controller_2.axis2.position()!=0:
                log.record.controller_2_axis("2")
            if controller_2.axis3.position()!=0:
                log.record.controller_2_axis("3")
            if controller_2.axis4.position()!=0:
                log.record.controller_2_axis("4")
            if controller_2.buttonA.pressing() and (self.button_pressing==0 or self.button_pressing>=1):
                log.record.controller_2_button("A")
                self.button_pressing=1
            if controller_2.buttonB.pressing() and (self.button_pressing<=1 or self.button_pressing>=2):
                log.record.controller_2_button("B")
                self.button_pressing=2
            if controller_2.buttonX.pressing() and (self.button_pressing<=2 or self.button_pressing>=3):
                log.record.controller_2_button("X")
                self.button_pressing=3
            if controller_2.buttonY.pressing() and (self.button_pressing<=3 or self.button_pressing>=4):
                log.record.controller_2_button("Y")
                self.button_pressing=4
            if controller_2.buttonUp.pressing() and (self.button_pressing<=4 or self.button_pressing>=5):
                log.record.controller_2_button("UP")
                self.button_pressing=5
            if controller_2.buttonDown.pressing() and (self.button_pressing<=5 or self.button_pressing>=6):
                log.record.controller_2_button("DOWN")
                self.button_pressing=6
            if controller_2.buttonLeft.pressing() and (self.button_pressing<=6 or self.button_pressing>=7):
                log.record.controller_2_button("LEFT")
                self.button_pressing=7
            if controller_2.buttonRight.pressing() and (self.button_pressing<=7 or self.button_pressing>=8):
                log.record.controller_2_button("RIGHT")
                self.button_pressing=8
            if controller_2.buttonL1.pressing() and (self.button_pressing<=8 or self.button_pressing>=9):
                log.record.controller_2_button("L1")
                self.button_pressing=9
            if controller_2.buttonL2.pressing() and (self.button_pressing<=9 or self.button_pressing>=10):
                log.record.controller_2_button("L2")
                self.button_pressing=10
            if controller_2.buttonR1.pressing() and (self.button_pressing<=10 or self.button_pressing>=11):
                log.record.controller_2_button("R1")
                self.button_pressing=11
            if controller_2.buttonR2.pressing() and (self.button_pressing<=11):
                log.record.controller_2_button("R2")
                self.button_pressing=12
            wait(100, MSEC)
            if not(controller_2.buttonA.pressing() or controller_2.buttonB.pressing() or controller_2.buttonX.pressing() or controller_2.buttonY.pressing() or controller_2.buttonUp.pressing() or controller_2.buttonDown.pressing() or controller_2.buttonLeft.pressing() or controller_2.buttonRight.pressing() or controller_2.buttonL1.pressing() or controller_2.buttonL2.pressing() or controller_2.buttonR1.pressing() or controller_2.buttonR2.pressing()):
                self.button_pressing=0
    
    # Logging Variables
    def variable(self, name, value):
        self.name=name
        self.value=value
        while True:
            log.record.Variable(self.name, self.value)
            wait(200, MSEC)

class Log:
    def __init__(self):
        self.code="__0"
        self.details=0
        self.record=Record()
        self.read=Read()
        self.logging=Logging()
        # Predefined Log Codes dictionary
        self.codes={
                    "ED0": "Drivetrain ERROR: No response from drivetrain.",
                    "ED1": "Drivetrain ERROR: Motor(s) Criticaly Hot. Temp: ",
                    "ED2": "Drivetrain ERROR: Motor(s) Very High Power. Power: ",
                    "WD0": "Drivetrain WARNING: Motor(s) Hot. Temp: ",
                    "WD1": "Drivetrain WARNING: High Current Draw. Current: ",
                    "WD2": "Drivetrain WARNING: Low Voltage. Voltage: ",
                    "WD3": "Drivetrain WARNING: High Power. Power: ",
                    "DD0": "Drivetrain Data: Velocity Changed. New Velocity: ",
                    "DD1": "Drivetrain Data: Done Spinning.",
                    "EI0": "Intake ERROR: No response from intake system.",
                    "EI1": "Intake ERROR: Motor Criticaly Hot. Temp: ",
                    "WI0": "Intake WARNING: Motor Hot. Temp: ",
                    "WI1": "Intake WARNING: High Current Draw. Current: ",
                    "WI2": "Intake WARNING: High Voltage. Voltage: ",
                    "WI3": "Intake WARNING: High Power. Power: ",
                    "DI0": "Intake INFO: Done Spinning.",
                    "DI1": "Intake INFO: Velocity Changed. New Velocity: ",
                    "EB0": "Battery ERROR: Critically Low Voltage. Voltage: ",
                    "EB1": "Battery ERROR: Critically Low Battery. capacity: ",
                    "WB0": "Battery WARNING: Low Voltage. Voltage: ",
                    "WB1": "Battery WARNING: Low Battery. capacity: ",
                    "EA0": "Aton ERROR: No response from auton system.",
                    "EA1": "Aton ERROR: Inertial Sensor Failure.",
                    "EA2": "Aton ERROR: Move failed. Move:",
                    "WA0": "Aton WARNING: Inertial Sensor Calibrating.",
                    "WA1": "Aton WARNING: Left Aton Missing.",
                    "WA2": "Aton WARNING: Right Aton Missing.",
                    "DA0": "Aton DATA: Recording Started.",
                    "DA1": "Aton DATA: Recording Stopped.",
                    "DA2": "Aton DATA: Recording Saved.",
                    "DA3": "Aton DATA: Recording Loaded.",
                    "DA4": "Aton DATA: Move Forward MM. MM: ",
                    "DA5": "Aton DATA: Drive Left Degrees. Degrees: ",
                    "DA6": "Aton DATA: Drive Right Degrees. Degrees: ",
                    "DA7": "Aton DATA: Curved Move. Left Degrees: , Right Degrees: ",
                    "DA8": "Aton DATA: Turn to Rotation. Degrees: ",
                    "DA9": "Aton DATA: Turn Degrees. Degrees: ",
                    "DA10": "Aton DATA: Loaded Right Aton from SD Card.",
                    "DA11": "Aton DATA: Loaded Left Aton from SD Card.",
                    "DS0": "System DATA: Init setup complete.",
                    "DS1": "System DATA: Driver Init setup complete.",
                    "DS2": "System DATA: Aton Init setup complete.",
                    "EM0": "Motor ERROR: Motor Criticaly Hot. Temp: ",
                    "WM0": "Motor WARNING: Motor Hot. Temp: ",
                    }
        # Setting up Log Files if they dont exist 
        if brain.sdcard.is_inserted():
            if not brain.sdcard.exists("Log.csv"):
                brain.sdcard.savefile("Log.csv", bytearray("log Start: \n", "utf-8"))
            if not brain.sdcard.exists("index.txt"):
                brain.sdcard.savefile("index.txt", bytearray("0", "utf-8"))
        else:
            self.index=0

    # Adding log entry
    def add(self, add_code, add_details):
        self.code=add_code
        self.details=add_details
        if brain.sdcard.is_inserted():
            index_content=brain.sdcard.loadfile("index.txt")
            self.index=int(index_content.decode("utf-8"))
            brain.sdcard.appendfile("Log.csv", bytearray(", %s [%s] %s %s \n"%(self.index, log_time, self.codes.get(self.code), self.details), "utf-8"))
            self.index+=1
            brain.sdcard.savefile("index.txt", bytearray("%d"%(self.index), "utf-8"))
        else:
            print(", %s [%s] %s %s"%(self.index, log_time, self.codes.get(self.code), self.details))

    # Adding custom log codes
    def add_codes(self, code_add, Decoded_text):
        self.codes.update({code_add : "%s"%(Decoded_text)})

    # Removing log codes
    def remove_codes(self, code_remove):
        if code_remove in self.codes:
            self.codes.pop(code_remove)
        else:
            print("Code Not Found In Log Codes")
    
    # Editing existing log codes
    def edit_codes(self, code_edit, new_decoded_text):
        if code_edit in self.codes:
            self.codes.update({code_edit : "%s"%( new_decoded_text)})

    # Clearing the log file
    def clear(self):
        if brain.sdcard.is_inserted():
            brain.sdcard.savefile("Log.csv", bytearray("Log Start: \n", "utf-8"))
            brain.sdcard.savefile("index.txt", bytearray("0", "utf-8"))
        else:
            print("No SD Card Inserted Cannot Clear Log")
    
    # Displaying log codes dictionary
    def table(self):
        print(self.codes)


# defining Log object
log=Log()  

# funtions for threading
def log_drivetrain():
    log.logging.drivetrain.six_motor(Left1, Right1, Left2, Right2, Left3, Right3)

def log_intake():
    log.logging.motor(Intake_Motor)

def log_top():
    log.logging.motor(TopMotor)

def log_colorsorting():
    log.logging.motor(colorsorting)

def log_variable_example():
    log.logging.variable("Example_Variable", example_variable)
        
        
# Starting Logging Example
log.clear()
log.add("DS0",0)
print("Logging Started")
Log_drivetrain=Thread(log_drivetrain)
print("Drivetrain Monitoring Started")
Log_controller_1=Thread(log.logging.Controller_1)
print("Controller 1 Monitoring Started")
Log_intake_motor=Thread(log_intake)
print("Intake Motor Monitoring Started")
Log_top_motor=Thread(log_top)
print("Top Motor Monitoring Started")
Log_colorsorting_motor=Thread(log_colorsorting)
print("Color Sorting Motor Monitoring Started")
Log_battery=Thread(log.logging.battery)
print("Battery Monitoring Started")
Log_variable=Thread(log_variable_example)
print("Variable Logging Started")

for i in range(20):
    wait(100, MSEC)
    example_variable+=1

wait(10, SECONDS)
print("Reading Log Content:")
log.read.console()
