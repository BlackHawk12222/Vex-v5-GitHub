# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       MicaS                                                        #
# 	Created:      1/27/2026, 12:41:53 PM                                       #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *

# Brain should be defined by default
brain=Brain()

controller_1=Controller(PRIMARY)
controller_2=Controller(PARTNER)

class record:
    def record(self):
        self.axis=""
        self.value=0
        self.button=""


    def controller_1_axis(self, axis):
        self.axis=axis
        if brain.sdcard.is_inserted():
            index_content=brain.sdcard.loadfile("index.txt")
            self.index=int(index_content.decode("utf-8"))
        if self.axis=="AXIS1" or self.axis=="1":
            self.value=controller_1.axis1.position()
            if brain.sdcard.is_inserted():
                brain.sdcard.appendfile("Log.csv", bytearray(", %s Controller_1_Axis1: %s \n" %(self.index, self.value), "utf-8"))
            else:
                print("Controller_1_Axis1: %f"%(self.value))
        elif self.axis=="AXIS2" or self.axis=="2":
            self.value=controller_1.axis2.position()
            if brain.sdcard.is_inserted():
                brain.sdcard.appendfile("Log.csv", bytearray(", %s Controller_1_Axis2: %s \n"%(self.index, self.value), "utf-8"))
            else:
                print("Controller_1_Axis2: %f"%(self.value))
        elif self.axis=="AXIS3" or self.axis=="3":
            self.value=controller_1.axis3.position()
            if brain.sdcard.is_inserted():
                brain.sdcard.appendfile("Log.csv", bytearray(", %s Controller_1_Axis3: %s \n"%(self.index, self.value), "utf-8"))
            else:
                print("Controller_1_Axis3: %f"%(self.value))
        elif self.axis=="AXIS4" or self.axis=="4":
            self.value=controller_1.axis4.position()
            if brain.sdcard.is_inserted():
                brain.sdcard.appendfile("Log.csv", bytearray(", %s Controller_1_Axis4: %s \n"%(self.index, self.value), "utf-8"))
            else:
                print("Controller_1_Axis4: %f"%(self.value))
        self.index+=1
        brain.sdcard.savefile("index.txt", bytearray("%d"%(self.index), "utf-8"))
    
    def controller_1_button(self, button):
        self.button=button
        if brain.sdcard.is_inserted():
            index_content=brain.sdcard.loadfile("index.txt")
            self.index=int(index_content.decode("utf-8"))
        if self.button=="A":
            self.value=controller_1.buttonA.pressing()
            if brain.sdcard.is_inserted():
                brain.sdcard.appendfile("Log.csv", bytearray(", %s Controller_1_ButtonA: %s \n"%(self.index, self.value), "utf-8"))
            else:
                print("Controller_1_ButtonA: %s"%(self.value))
        elif self.button=="B" or self.button=="b":
            self.value=controller_1.buttonB.pressing()
            if brain.sdcard.is_inserted():
                brain.sdcard.appendfile("Log.csv", bytearray(", %s Controller_1_ButtonB: %s \n"%(self.index, self.value), "utf-8"))
            else:
                print("Controller_1_ButtonB: %s"%(self.value))
        elif self.button=="Y" or self.button=="y":
            self.value=controller_1.buttonY.pressing()
            if brain.sdcard.is_inserted():
                brain.sdcard.appendfile("Log.csv", bytearray(", %s Controller_1_ButtonY: %s \n"%(self.index, self.value), "utf-8"))
            else:
                print("Controller_1_ButtonY: %s"%(self.value))
        elif self.button=="X" or self.button=="x":
            self.value=controller_1.buttonX.pressing()
            if brain.sdcard.is_inserted():
                brain.sdcard.appendfile("Log.csv", bytearray(", %s Controller_1_ButtonX: %s \n"%(self.index, self.value), "utf-8"))
            else:
                print("Controller_1_ButtonX: %s"%(self.value))
        elif self.button=="UP" or self.button=="up" or self.button=="Up":
            self.value=controller_1.buttonUp.pressing()
            if brain.sdcard.is_inserted():
                brain.sdcard.appendfile("Log.csv", bytearray(", %s Controller_1_ButtonUp: %s \n"%(self.index, self.value), "utf-8"))
            else:
                print("Controller_1_ButtonUp: %s"%(self.value))
        elif self.button=="DOWN" or self.button=="down" or self.button=="Down":
            self.value=controller_1.buttonDown.pressing()
            if brain.sdcard.is_inserted():
                brain.sdcard.appendfile("Log.csv", bytearray(", %s Controller_1_ButtonDown: %s \n"%(self.index, self.value), "utf-8"))
            else:
                print("Controller_1_ButtonDown: %s"%(self.value))
        elif self.button=="LEFT" or self.button=="left" or self.button=="Left":
            self.value=controller_1.buttonLeft.pressing()
            if brain.sdcard.is_inserted():
                brain.sdcard.appendfile("Log.csv", bytearray(", %s Controller_1_ButtonLeft: %s \n"%(self.index, self.value), "utf-8"))
            else:
                print("Controller_1_ButtonLeft: %s"%(self.value))
        elif self.button=="RIGHT" or self.button=="right" or self.button=="Right":
            self.value=controller_1.buttonRight.pressing()
            if brain.sdcard.is_inserted():
                brain.sdcard.appendfile("Log.csv", bytearray(", %s Controller_1_ButtonRight: %s \n"%(self.index, self.value), "utf-8"))
            else:
                print("Controller_1_ButtonRight: %s"%(self.value))
        elif self.button=="L1" or self.button=="l1":
            self.value=controller_1.buttonL1.pressing()
            if brain.sdcard.is_inserted():
                brain.sdcard.appendfile("Log.csv", bytearray(", %s Controller_1_ButtonL1: %s \n"%(self.index, self.value), "utf-8"))
            else:
                print("Controller_1_ButtonL1: %s"%(self.value))
        elif self.button=="L2" or self.button=="l2":
            self.value=controller_1.buttonL2.pressing()
            if brain.sdcard.is_inserted():
                brain.sdcard.appendfile("Log.csv", bytearray(", %s Controller_1_ButtonL2: %s \n"%(self.index, self.value), "utf-8"))
            else:
                print("Controller_1_ButtonL2: %s"%(self.value))
        elif self.button=="R1" or self.button=="r1":
            self.value=controller_1.buttonR1.pressing()
            if brain.sdcard.is_inserted():
                brain.sdcard.appendfile("Log.csv", bytearray(", %s Controller_1_ButtonR1: %s \n"%(self.index, self.value), "utf-8"))
            else:
                print("Controller_1_ButtonR1: %s"%(self.value))
        elif self.button=="R2" or self.button=="r2":
            self.value=controller_1.buttonR2.pressing()
            if brain.sdcard.is_inserted():
                brain.sdcard.appendfile("Log.csv", bytearray(", %s Controller_1_ButtonR2: %s \n"%(self.index, self.value), "utf-8"))
            else:
                print("Controller_1_ButtonR2: %s"%(self.value))
        self.index+=1
        brain.sdcard.savefile("index.txt", bytearray("%d"%(self.index), "utf-8"))

    def controller_2_axis(self, axis):
        self.axis=axis
        if brain.sdcard.is_inserted():
            index_content=brain.sdcard.loadfile("index.txt")
            self.index=int(index_content.decode("utf-8"))
        if self.axis=="AXIS1" or self.axis=="1":
            self.value=controller_2.axis1.position()
            if brain.sdcard.is_inserted():
                brain.sdcard.appendfile("Log.csv", bytearray(", %s Controller_2_Axis1: %f \n"%(self.index, self.value), "utf-8"))
            else:
                print("Controller_2_Axis1: %f"%(self.value))
        elif self.axis=="AXIS2" or self.axis=="2":
            self.value=controller_2.axis2.position()
            if brain.sdcard.is_inserted():
                brain.sdcard.appendfile("Log.csv", bytearray(", %s Controller_2_Axis2: %f \n"%(self.index, self.value), "utf-8"))
            else:
                print("Controller_2_Axis2: %f"%(self.value))
        elif self.axis=="AXIS3" or self.axis=="3":
            self.value=controller_2.axis3.position()
            if brain.sdcard.is_inserted():
                brain.sdcard.appendfile("Log.csv", bytearray(", %s Controller_2_Axis3: %f \n"%(self.index, self.value), "utf-8"))
            else:
                print("Controller_2_Axis3: %f"%(self.value))
        elif self.axis=="AXIS4" or self.axis=="4":
            self.value=controller_2.axis4.position()
            if brain.sdcard.is_inserted():
                brain.sdcard.appendfile("Log.csv", bytearray(", %s Controller_2_Axis4: %f \n"%(self.index, self.value), "utf-8"))
            else:
                print("Controller_2_Axis4: %f"%(self.value))
        self.index+=1
        brain.sdcard.savefile("index.txt", bytearray("%d"%(self.index), "utf-8"))
        
    def controller_2_button(self, button):
        self.button=button
        if brain.sdcard.is_inserted():
            index_content=brain.sdcard.loadfile("index.txt")
            self.index=int(index_content.decode("utf-8"))
        if self.button=="A":
            self.value=controller_2.buttonA.pressing()
            if brain.sdcard.is_inserted():
                brain.sdcard.appendfile("Log.csv", bytearray(", %s Controller_2_ButtonA: %s \n"%(self.index, self.value), "utf-8"))
            else:
                print("Controller_2_ButtonA: %s"%(self.value))
        elif self.button=="B" or self.button=="b":
            self.value=controller_2.buttonB.pressing()
            if brain.sdcard.is_inserted():
                brain.sdcard.appendfile("Log.csv", bytearray(", %s Controller_2_ButtonB: %s \n"%(self.index, self.value), "utf-8"))
            else:
                print("Controller_2_ButtonB: %s"%(self.value))
        elif self.button=="Y" or self.button=="y":
            self.value=controller_2.buttonY.pressing()
            if brain.sdcard.is_inserted():
                brain.sdcard.appendfile("Log.csv", bytearray(", %s Controller_2_ButtonY: %s \n"%(self.index, self.value), "utf-8"))
            else:
                print("Controller_2_ButtonY: %s"%(self.value))
        elif self.button=="X" or self.button=="x":
            self.value=controller_2.buttonX.pressing()
            if brain.sdcard.is_inserted():
                brain.sdcard.appendfile("Log.csv", bytearray(", %s Controller_2_ButtonX: %s \n"%(self.index, self.value), "utf-8"))
            else:
                print("Controller_2_ButtonX: %s"%(self.value))
        elif self.button=="UP" or self.button=="up" or self.button=="Up":
            self.value=controller_2.buttonUp.pressing()
            if brain.sdcard.is_inserted():
                brain.sdcard.appendfile("Log.csv", bytearray(", %s Controller_2_ButtonUp: %s \n"%(self.index, self.value), "utf-8"))
            else:
                print("Controller_2_ButtonUp: %s"%(self.value))
        elif self.button=="DOWN" or self.button=="down" or self.button=="Down":
            self.value=controller_2.buttonDown.pressing()
            if brain.sdcard.is_inserted():
                brain.sdcard.appendfile("Log.csv", bytearray(", %s Controller_2_ButtonDown: %s \n"%(self.index, self.value), "utf-8"))
            else:
                print("Controller_2_ButtonDown: %s"%(self.value))
        elif self.button=="LEFT" or self.button=="left" or self.button=="Left":
            self.value=controller_2.buttonLeft.pressing()
            if brain.sdcard.is_inserted():
                brain.sdcard.appendfile("Log.csv", bytearray(", %s Controller_2_ButtonLeft: %s \n"%(self.index, self.value), "utf-8"))
            else:
                print("Controller_2_ButtonLeft: %s"%(self.value))
        elif self.button=="RIGHT" or self.button=="right" or self.button=="Right":
            self.value=controller_2.buttonRight.pressing()
            if brain.sdcard.is_inserted():
                brain.sdcard.appendfile("Log.csv", bytearray(", %s Controller_2_ButtonRight: %s \n"%(self.index, self.value), "utf-8"))
            else:
                print("Controller_2_ButtonRight: %s"%(self.value))
        elif self.button=="L1" or self.button=="l1":
            self.value=controller_2.buttonL1.pressing()
            if brain.sdcard.is_inserted():
                brain.sdcard.appendfile("Log.csv", bytearray(", %s Controller_2_ButtonL1: %s \n"%(self.index, self.value), "utf-8"))
            else:
                print("Controller_2_ButtonL1: %s"%(self.value))
        elif self.button=="L2" or self.button=="l2":
            self.value=controller_2.buttonL2.pressing()
            if brain.sdcard.is_inserted():
                brain.sdcard.appendfile("Log.csv", bytearray(", %s Controller_2_ButtonL2: %s \n"%(self.index, self.value), "utf-8"))
            else:
                print("Controller_2_ButtonL2: %s"%(self.value))
        elif self.button=="R1" or self.button=="r1":
            self.value=controller_2.buttonR1.pressing()
            if brain.sdcard.is_inserted():
                brain.sdcard.appendfile("Log.csv", bytearray(", %s Controller_2_ButtonR1: %s \n"%(self.index, self.value), "utf-8"))
            else:
                print("Controller_2_ButtonR1: %s"%(self.value))
        elif self.button=="R2" or self.button=="r2":
            self.value=controller_2.buttonR2.pressing()
            if brain.sdcard.is_inserted():
                brain.sdcard.appendfile("Log.csv", bytearray(", %s Controller_2_ButtonR2: %s \n"%(self.index, self.value), "utf-8"))
            else:
                print("Controller_2_ButtonR2: %s"%(self.value))
        self.index+=1
        brain.sdcard.savefile("index.txt", bytearray("%d"%(self.index), "utf-8"))

    def Add_function(self, name, print_out):
        pass

class Log:

    def __init__(self):
        self.code="__0"
        self.details=0
        self.record=record()
        self.codes={
                    "ED0": "Drivetrain ERROR: No response from drivetrain.",
                    "ED1": "Drivetrain ERROR: Motor(s) Criticaly Hot. Temp: ",
                    "WD0": "Drivetrain WARNING: Motor(s) Hot. Temp: ",
                    "WD1": "Drivetrain WARNING: High Current Draw. Current: ",
                    "WD2": "Drivetrain WARNING: High Voltage. Voltage: ",
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
                    "EB1": "Battery ERROR: Critically Low Battery.",
                    "WB0": "Battery WARNING: Low Voltage.",
                    "WB1": "Battery WARNING: Low Battery",
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
                    "DS0": "System DATA: Driver Init setup complete.",
                    "DS1": "System DATA: Aton Init setup complete."
                    } 
        if brain.sdcard.is_inserted():
            if not brain.sdcard.exists("Log.csv"):
                brain.sdcard.savefile("Log.csv", bytearray("log Start: \n", "utf-8"))
            if not brain.sdcard.exists("index.txt"):
                brain.sdcard.savefile("index.txt", bytearray("0", "utf-8"))
        else:
            self.index=0

    def add(self, add_code, add_details):
        self.code=add_code
        self.details=add_details
        if brain.sdcard.is_inserted():
            index_content=brain.sdcard.loadfile("index.txt")
            self.index=int(index_content.decode("utf-8"))
            brain.sdcard.appendfile("Log.csv", bytearray(", %s %s %s \n"%(self.index, self.codes.get(self.code), self.details), "utf-8"))
            self.index+=1
            brain.sdcard.savefile("index.txt", bytearray("%d"%(self.index), "utf-8"))
        else:
            print("%s %s"%(self.codes.get(self.code), self.details))
    
    def read(self):
        if brain.sdcard.is_inserted():
            Log_content=brain.sdcard.loadfile("Log.csv")
            print(Log_content.decode("utf-8")) 
        else:
            print("No SD Card Inserted Cannot Read Log")    

    def add_codes(self, code_add, Decoded_text):
        self.codes.update({code_add : "%f"%(Decoded_text)})

    def clear(self):
        if brain.sdcard.is_inserted():
            brain.sdcard.savefile("Log.csv", bytearray("Log Start: \n", "utf-8"))
            brain.sdcard.savefile("index.txt", bytearray("0", "utf-8"))
        else:
            print("No SD Card Inserted Cannot Clear Log")
    
    def table(self):
        print(self.codes)
    



log=Log()

log.clear()
log.add("WD1", 12)
log.record.controller_1_axis("1")
log.record.controller_1_button("A")
log.add("ED0", 0)
log.read()