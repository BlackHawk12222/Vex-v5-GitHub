#region VEXcode Generated Robot Configuration
from vex import *
import urandom #type:ignore

# Brain should be defined by default
brain=Brain()

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
    # Helper to make playing sounds from the V5 in VEXcode easier and
    # keeps the code cleaner by making it clear what is happening.
    print("VEXPlaySound:" + sound_name)
    wait(5, MSEC)

# add a small delay to make sure we don't print in the middle of the REPL header
wait(200, MSEC)
# clear the console to make sure we don't have the REPL in the console
print("\033[2J")

#endregion VEXcode Generated Robot Configuration
screen_precision = 0
console_precision = 0

# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       Logging.py                                                   #
# 	Author:       Micah Bow                                                    #
# 	Created:      1/27/2026, 12:42 PM                                          #
#   Last Edited:  2/4/2026, 12:02 PM                                           #
# 	Description:  Universal Logging software for Vex V5 Version 8              #
#                                                                              #
# ---------------------------------------------------------------------------- #


# Timer for log time
log_time= Timer()
controller_2=Controller(PARTNER)


# Drivetrain recording
class Drivetrain:
    def __init__(self):
        self.drivetrain_temp_monitoring=0
        self.drivetrain_power_monitoring=0
        self.drivetrain_disconnected=0
    
    def two_motor(self, left_motor, right_motor):

        if (right_motor.temperature()>70 or left_motor.temperature()>70) and (self.drivetrain_temp_monitoring==0 or self.drivetrain_temp_monitoring==2):
            log.add("ED1", "Temp: %s"%(max(right_motor.temperature(), left_motor.temperature())))
            self.drivetrain_temp_monitoring=1
        elif (right_motor.temperature()>50 or left_motor.temperature()>50) and (self.drivetrain_temp_monitoring==0 or self.drivetrain_temp_monitoring==1):
            log.add("WD0", "Temp: %s"%(max(right_motor.temperature(), left_motor.temperature())))
            self.drivetrain_temp_monitoring=2
        elif right_motor.temperature()<=50 and left_motor.temperature()<=50 and (self.drivetrain_temp_monitoring==1 or self.drivetrain_temp_monitoring==2):
            self.drivetrain_temp_monitoring=0
        
        if right_motor.power(PowerUnits.WATT)>40 or left_motor.power(PowerUnits.WATT)>40 and (self.drivetrain_power_monitoring==0 or self.drivetrain_power_monitoring==2):
            log.add("ED3", "Power: %s"%(max(right_motor.power(PowerUnits.WATT), left_motor.power(PowerUnits.WATT))))
            self.drivetrain_power_monitoring=1
        elif right_motor.power(PowerUnits.WATT)>30 or left_motor.power(PowerUnits.WATT)>30 and (self.drivetrain_power_monitoring==0 or self.drivetrain_power_monitoring==1):
            log.add("WD3", "Power: %s"%(max(right_motor.power(PowerUnits.WATT), left_motor.power(PowerUnits.WATT))))
            self.drivetrain_power_monitoring=2
        elif right_motor.power(PowerUnits.WATT)<=30 and left_motor.power(PowerUnits.WATT)<=30 and (self.drivetrain_power_monitoring==1 or self.drivetrain_power_monitoring==2):
            self.drivetrain_power_monitoring=0
        
        if right_motor.temperature(PERCENT)==2 and self.drivetrain_disconnected==0:
            log.add("ED3", "Right Motor")
            self.drivetrain_disconnected=1

        if left_motor.temperature(PERCENT)==2 and self.drivetrain_disconnected==0:
            log.add("ED3", "Left Motor")            
            self.drivetrain_disconnected=1
        
        if right_motor.temperature(PERCENT)!=2 and left_motor.temperature(PERCENT)!=2 and self.drivetrain_disconnected==1:
            self.drivetrain_disconnected=0
        
    def four_motor(self, front_left_motor, front_right_motor, back_left_motor, back_right_motor):
        
        if (front_left_motor.temperature()>70 or front_right_motor.temperature()>70 or back_left_motor.temperature()>70 or back_right_motor.temperature()>70) and (self.drivetrain_temp_monitoring==0 or self.drivetrain_temp_monitoring==2):
            log.add("ED1", "Temp: %s"%(max(front_left_motor.temperature(), front_right_motor.temperature(), back_left_motor.temperature(), back_right_motor.temperature())))
            self.drivetrain_temp_monitoring=1
        elif (front_left_motor.temperature()>50 or front_right_motor.temperature()>50 or back_left_motor.temperature()>50 or back_right_motor.temperature()>50) and (self.drivetrain_temp_monitoring==0 or self.drivetrain_temp_monitoring==1):
            log.add("WD0", "Temp: %s"%(max(front_left_motor.temperature(), front_right_motor.temperature(), back_left_motor.temperature(), back_right_motor.temperature())))
            self.drivetrain_temp_monitoring=2
        elif (front_left_motor.temperature()<=50 and front_right_motor.temperature()<=50 and back_left_motor.temperature()<=50 and back_right_motor.temperature()<=50) and (self.drivetrain_temp_monitoring==1 or self.drivetrain_temp_monitoring==2):
            self.drivetrain_temp_monitoring=0
        
        if front_left_motor.power(PowerUnits.WATT)>40 or front_right_motor.power(PowerUnits.WATT)>40 or back_left_motor.power(PowerUnits.WATT)>40 or back_right_motor.power(PowerUnits.WATT)>40 and (self.drivetrain_power_monitoring==0 or self.drivetrain_power_monitoring==2):
            log.add("ED3", "Power: %s"%(max(front_left_motor.power(PowerUnits.WATT), front_right_motor.power(PowerUnits.WATT), back_left_motor.power(PowerUnits.WATT), back_right_motor.power(PowerUnits.WATT))))
            self.drivetrain_power_monitoring=1
        elif front_left_motor.power(PowerUnits.WATT)>30 or front_right_motor.power(PowerUnits.WATT)>30 or back_left_motor.power(PowerUnits.WATT)>30 or back_right_motor.power(PowerUnits.WATT)>30 and (self.drivetrain_power_monitoring==0 or self.drivetrain_power_monitoring==1):  
            log.add("WD3", "Power: %s"%(max(front_left_motor.power(PowerUnits.WATT), front_right_motor.power(PowerUnits.WATT), back_left_motor.power(PowerUnits.WATT), back_right_motor.power(PowerUnits.WATT))))
            self.drivetrain_power_monitoring=2
        elif front_left_motor.power(PowerUnits.WATT)<=30 and front_right_motor.power(PowerUnits.WATT)<=30 and back_left_motor.power(PowerUnits.WATT)<=30 and back_right_motor.power(PowerUnits.WATT)<=30 and (self.drivetrain_power_monitoring==1 or self.drivetrain_power_monitoring==2):
            self.drivetrain_power_monitoring=0
        
        if front_right_motor.temperature(PERCENT)==2 and self.drivetrain_disconnected==0:
            log.add("ED3", "Front Right Motor")
            self.drivetrain_disconnected=1
        
        if front_left_motor.temperature(PERCENT)==2 and self.drivetrain_disconnected==0:
            log.add("ED3", "Front Left Motor")            
            self.drivetrain_disconnected=1
        
        if back_right_motor.temperature(PERCENT)==2 and self.drivetrain_disconnected==0:
            log.add("ED3", "Back Right Motor")
            self.drivetrain_disconnected=1
        
        if back_left_motor.temperature(PERCENT)==2 and self.drivetrain_disconnected==0:
            log.add("ED3", "Back Left Motor")            
            self.drivetrain_disconnected=1
        
        if front_right_motor.temperature(PERCENT)!=2 and front_left_motor.temperature(PERCENT)!=2 and back_right_motor.temperature(PERCENT)!=2 and back_left_motor.temperature(PERCENT)!=2 and self.drivetrain_disconnected==1:
            self.drivetrain_disconnected=0
    
    def six_motor(self, front_left_motor, front_right_motor, middle_left_motor, middle_right_motor, back_left_motor, back_right_motor):
        
        if (front_left_motor.temperature(PERCENT)>70 or front_right_motor.temperature(PERCENT)>70 or middle_left_motor.temperature(PERCENT)>70 or middle_right_motor.temperature(PERCENT)>70 or back_left_motor.temperature(PERCENT)>70 or back_right_motor.temperature(PERCENT)>70) and (self.drivetrain_temp_monitoring==0 or self.drivetrain_temp_monitoring==2):
            log.add("ED1", "Temp: %s"%(max(front_left_motor.temperature(PERCENT), front_right_motor.temperature(PERCENT), middle_left_motor.temperature(PERCENT), middle_right_motor.temperature(PERCENT), back_left_motor.temperature(PERCENT), back_right_motor.temperature(PERCENT))))
            self.drivetrain_temp_monitoring=1
        elif (front_left_motor.temperature(PERCENT)>50 or front_right_motor.temperature(PERCENT)>50 or middle_left_motor.temperature(PERCENT)>50 or middle_right_motor.temperature(PERCENT)>50 or back_left_motor.temperature(PERCENT)>50 or back_right_motor.temperature(PERCENT)>50) and (self.drivetrain_temp_monitoring==0 or self.drivetrain_temp_monitoring==1):
            log.add("WD0", "Temp: %s"%(max(front_left_motor.temperature(PERCENT), front_right_motor.temperature(PERCENT), middle_left_motor.temperature(PERCENT), middle_right_motor.temperature(PERCENT), back_left_motor.temperature(PERCENT), back_right_motor.temperature(PERCENT))))
            self.drivetrain_temp_monitoring=2
        elif (front_left_motor.temperature(PERCENT)<=50 and front_right_motor.temperature(PERCENT)<=50 and middle_left_motor.temperature(PERCENT)<=50 and middle_right_motor.temperature(PERCENT)<=50 and back_left_motor.temperature(PERCENT)<=50 and back_right_motor.temperature(PERCENT)<=50) and (self.drivetrain_temp_monitoring==1 or self.drivetrain_temp_monitoring==2):
            self.drivetrain_temp_monitoring=0
        
        if front_left_motor.power(PowerUnits.WATT)>40 or front_right_motor.power(PowerUnits.WATT)>40 or middle_left_motor.power(PowerUnits.WATT)>40 or middle_right_motor.power(PowerUnits.WATT)>40 or back_left_motor.power(PowerUnits.WATT)>40 or back_right_motor.power(PowerUnits.WATT)>40 and (self.drivetrain_power_monitoring==0 or self.drivetrain_power_monitoring==2):
            log.add("ED3", "Power: %s"%(max(front_left_motor.power(PowerUnits.WATT), front_right_motor.power(PowerUnits.WATT), middle_left_motor.power(PowerUnits.WATT), middle_right_motor.power(PowerUnits.WATT), back_left_motor.power(PowerUnits.WATT), back_right_motor.power(PowerUnits.WATT))))
            self.drivetrain_power_monitoring=1
        elif front_left_motor.power(PowerUnits.WATT)>30 or front_right_motor.power(PowerUnits.WATT)>30 or middle_left_motor.power(PowerUnits.WATT)>30 or middle_right_motor.power(PowerUnits.WATT)>30 or back_left_motor.power(PowerUnits.WATT)>30 or back_right_motor.power(PowerUnits.WATT)>30 and (self.drivetrain_power_monitoring==0 or self.drivetrain_power_monitoring==1):  
            log.add("WD3", "Power: %s"%(max(front_left_motor.power(PowerUnits.WATT), front_right_motor.power(PowerUnits.WATT), middle_left_motor.power(PowerUnits.WATT), middle_right_motor.power(PowerUnits.WATT), back_left_motor.power(PowerUnits.WATT), back_right_motor.power(PowerUnits.WATT))))
            self.drivetrain_power_monitoring=2
        elif front_left_motor.power(PowerUnits.WATT)<=30 and front_right_motor.power(PowerUnits.WATT)<=30 and middle_left_motor.power(PowerUnits.WATT)<=30 and middle_right_motor.power(PowerUnits.WATT)<=30 and back_left_motor.power(PowerUnits.WATT)<=30 and back_right_motor.power(PowerUnits.WATT)<=30 and (self.drivetrain_power_monitoring==1 or self.drivetrain_power_monitoring==2):
            self.drivetrain_power_monitoring=0

        if front_right_motor.temperature(PERCENT)==2 and self.drivetrain_disconnected==0:
            log.add("ED3", "Front Right Motor")
            self.drivetrain_disconnected=1
        
        if front_left_motor.temperature(PERCENT)==2 and self.drivetrain_disconnected==0:
            log.add("ED3", "FrontLeft Motor")            
            self.drivetrain_disconnected=1
        
        if middle_right_motor.temperature(PERCENT)==2 and self.drivetrain_disconnected==0:
            log.add("ED3", "Middle Right Motor")
            self.drivetrain_disconnected=1
        
        if middle_left_motor.temperature(PERCENT)==2 and self.drivetrain_disconnected==0:
            log.add("ED3", "Middle Left Motor")            
            self.drivetrain_disconnected=1
        
        if back_right_motor.temperature(PERCENT)==2 and self.drivetrain_disconnected==0:
            log.add("ED3", "Back Right Motor")
            self.drivetrain_disconnected=1
        
        if back_left_motor.temperature(PERCENT)==2 and self.drivetrain_disconnected==0:
            log.add("ED3", "Back Left Motor")        
            self.drivetrain_disconnected=1
        
        if front_right_motor.temperature(PERCENT)!=2 and front_left_motor.temperature(PERCENT)!=2 and middle_right_motor.temperature(PERCENT)!=2 and middle_left_motor.temperature(PERCENT)!=2 and back_right_motor.temperature(PERCENT)!=2 and back_left_motor.temperature(PERCENT)!=2 and self.drivetrain_disconnected==1:
            self.drivetrain_disconnected=0


# logging for the log class
class Logging:

    def __init__(self):
        self.drivetrain=Drivetrain()
        self.temp_monitoring=0
        self.power_monitoring=0
        self.disconnected=0
        self.battery_voltage_monitoring=0
        self.battery_capacity_monitoring=0
        self.battery_current_monitoring=0
        self.button_a=True
        self.button_b=True
        self.button_x=True
        self.button_y=True
        self.button_up=True
        self.button_down=True
        self.button_left=True
        self.button_right=True
        self.button_L1=True
        self.button_L2=True
        self.button_R1=True
        self.button_R2=True
    
    def motor(self, motor):
        
        if motor.temperature()>70 and (self.temp_monitoring==0 or self.temp_monitoring==2):
            log.add("EM0", "Motor %s Temp: %s"%(motor, motor.temperature(PERCENT)))
            self.temp_monitoring=1
        elif motor.temperature()>50 and (self.temp_monitoring==0 or self.temp_monitoring==1):
            log.add("WM0", "Motor %s Temp: %s"%(motor, motor.temperature(PERCENT)))
            self.temp_monitoring=2
        elif motor.temperature()<=50 and (self.temp_monitoring==2 or self.temp_monitoring==1):
            self.temp_monitoring=0
        
        if motor.power(PowerUnits.WATT)>40 and (self.power_monitoring==0 or self.power_monitoring==2):
            log.add("EM2", "Motor %s Power: %s"%(motor, motor.power(PowerUnits.WATT)))
            self.power_monitoring=1
        elif motor.power(PowerUnits.WATT)>30 and (self.power_monitoring==0 or self.power_monitoring==1):
            log.add("WM1", "Motor %s Power: %s"%(motor, motor.power(PowerUnits.WATT)))
            self.power_monitoring=2
        elif motor.power(PowerUnits.WATT)<=30 and (self.power_monitoring==1 or self.power_monitoring==2):
            self.power_monitoring=0
        
        if motor.temperature(PERCENT)==2 and self.disconnected==0:
            log.add("EM1", "Motor %s Disconnected"%(motor))
            self.disconnected=1
        
        if motor.temperature(PERCENT)==2 and self.disconnected==0:
            log.add("EM1", "Motor %s Disconnected"%(motor))
            self.disconnected=1
        
        if motor.temperature(PERCENT)!=2 and self.disconnected==1:
            self.disconnected=0

    def Battery(self):

        if brain.battery.voltage(VoltageUnits.VOLT)<11 and (self.battery_voltage_monitoring==0 or self.battery_voltage_monitoring==2):
            log.add("EB0", "%s"%(brain.battery.voltage(VoltageUnits.VOLT)))
            self.battery_voltage_monitoring=1
        elif brain.battery.voltage(VoltageUnits.VOLT)<12 and (self.battery_voltage_monitoring==0 or self.battery_voltage_monitoring==1):
            log.add("WB0", "%s"%(brain.battery.voltage(VoltageUnits.VOLT)))
            self.battery_voltage_monitoring=2
        elif brain.battery.voltage(VoltageUnits.VOLT)>=12 and (self.battery_voltage_monitoring==1 or self.battery_voltage_monitoring==2):
            self.battery_voltage_monitoring=0
        
        if brain.battery.capacity()<25 and (self.battery_capacity_monitoring==0 or self.battery_capacity_monitoring==2):
            log.add("EB1", "%s"%(brain.battery.capacity()))
            self.battery_capacity_monitoring=1
        
        elif brain.battery.capacity()<50 and (self.battery_capacity_monitoring==0 or self.battery_capacity_monitoring==1):
            log.add("WB1", "%s"%(brain.battery.capacity()))
            self.battery_capacity_monitoring=2
        elif brain.battery.capacity()>=50 and (self.battery_capacity_monitoring==1 or self.battery_capacity_monitoring==2):
            self.battery_capacity_monitoring=0
        
        if brain.battery.current(CurrentUnits.AMP)>15 and (self.battery_current_monitoring==0 or self.battery_current_monitoring==2):
            log.add("EB2", "%s"%(brain.battery.current(CurrentUnits.AMP)))
            self.battery_current_monitoring=1
        elif brain.battery.current(CurrentUnits.AMP)>10 and (self.battery_current_monitoring==0 or self.battery_current_monitoring==1):
            log.add("WB2", "%s"%(brain.battery.current(CurrentUnits.AMP)))
            self.battery_current_monitoring=2
        elif brain.battery.current(CurrentUnits.AMP)<=5 and (self.battery_current_monitoring==1 or self.battery_current_monitoring==2):
            self.battery_current_monitoring=0
    
    def controller(self, controller):
        if controller==1:
            Controller=controller_1
        elif controller==2:
            Controller=controller_2

        axis_1=Controller.axis1.position()
        axis_2=Controller.axis2.position()
        axis_3=Controller.axis3.position()
        axis_4=Controller.axis4.position()
        wait(50, MSEC)

        if Controller.axis1.position()!=0 and axis_1!=Controller.axis1.position():
            log.add("DC1", "Controller_%d_Axis1: %d"%(controller, Controller.axis1.position()))

        if Controller.axis2.position()!=0 and axis_2!=Controller.axis2.position():
            log.add("DC1", "Controller_%d_Axis2: %d"%(controller, Controller.axis2.position()))

        if Controller.axis3.position()!=0 and axis_3!=Controller.axis3.position():
            log.add("DC1", "Controller_%d_Axis3: %d"%(controller, Controller.axis3.position()))

        if Controller.axis4.position()!=0 and axis_4!=Controller.axis4.position():
            log.add("DC1", "Controller_%d_Axis4: %d"%(controller, Controller.axis4.position()))

        if Controller.buttonA.pressing() and self.button_a==True:
            log.add("DC0", "Controller_%d_Button A Pressed"%(controller))
            self.button_a=False

        if Controller.buttonB.pressing() and self.button_b==True:
            log.add("DC0", "Controller_%d_Button B Pressed"%(controller))
            self.button_b=False

        if Controller.buttonX.pressing() and self.button_x==True:
            log.add("DC0", "Controller_%d_Button X Pressed"%(controller))
            self.button_x=False

        if Controller.buttonY.pressing() and self.button_y==True:
            log.add("DC0", "Controller_%d_Button Y Pressed"%(controller))
            self.button_y=False

        if Controller.buttonUp.pressing() and self.button_up==True:
            log.add("DC0", "Controller_%d_Button UP Pressed"%(controller))
            self.button_up=False

        if Controller.buttonDown.pressing() and self.button_down==True:
            log.add("DC0", "Controller_%d_Button DOWN Pressed"%(controller))
            self.button_down=False

        if Controller.buttonLeft.pressing() and self.button_left==True:
            log.add("DC0", "Controller_%d_Button LEFT Pressed"%(controller))
            self.button_left=False

        if Controller.buttonRight.pressing() and self.button_right==True:
            log.add("DC0", "Controller_%d_Button RIGHT Pressed"%(controller))
            self.button_right=False

        if Controller.buttonL1.pressing() and self.button_L1==True:
            log.add("DC0", "Controller_%d_Button L1 Pressed"%(controller))
            self.button_L1=False

        if Controller.buttonL2.pressing() and self.button_L2==True:
            log.add("DC0", "Controller_%d_Button L2 Pressed"%(controller))
            self.button_L2=False

        if Controller.buttonR1.pressing() and self.button_R1==True:
            log.add("DC0", "Controller_%d_Button R1 Pressed"%(controller))
            self.button_R1=False

        if Controller.buttonR2.pressing() and self.button_R2==True:
            log.add("DC0", "Controller_%d_Button R2 Pressed"%(controller))
            self.button_R2=False

        if not Controller.buttonA.pressing():
            self.button_a=True

        if not Controller.buttonB.pressing():
            self.button_b=True

        if not Controller.buttonX.pressing():
            self.button_x=True

        if not Controller.buttonY.pressing():
            self.button_y=True

        if not Controller.buttonUp.pressing():
            self.button_up=True

        if not Controller.buttonDown.pressing():
            self.button_down=True

        if not Controller.buttonLeft.pressing():
            self.button_left=True

        if not Controller.buttonRight.pressing():
            self.button_right=True

        if not Controller.buttonL1.pressing():
            self.button_L1=True

        if not Controller.buttonL2.pressing():
            self.button_L2=True

        if not Controller.buttonR1.pressing():
            self.button_R1=True

        if not Controller.buttonR2.pressing():
            self.button_R2=True
        
    def variable(self, name, value):
        log.add("DV0", "Variable %s Value: %s"%(name, value))


class Log:
    def __init__(self):
        self.logging=Logging()
        self.index=0
        # Predefined Log Codes dictionary
        self.codes={
                    "ED1": "Drivetrain ERROR: Motor(s) Criticaly Hot. Temp: ",
                    "ED2": "Drivetrain ERROR: Motor(s) Very High Power. Power: ",
                    "ED3": "Drivetrain ERROR: Motor(s) Disconnected. Name: ",
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
                    "EB1": "Battery ERROR: Critically Low Battery. Capacity: ",
                    "EB2": "Battery ERROR: Critically High Current. Current: ",
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
                    "EM1": "Motor ERROR: Motor Disconnected. Name: ",
                    "EM2": "Motor ERROR: Motor Very High Power. Power: ",
                    "WM0": "Motor WARNING: Motor Hot. Temp: ",
                    "WM1": "Motor WARNING: Motor High Power. Power: ",
                    "EE0": "Exeption ERROR: Type Error. Problem in: ",
                    "EE1": "Exeption ERROR: Value Error. Problem in: ",
                    "EE2": "Exeption ERROR: Name Error. Problem in: ",
                    "EE3": "Exeption ERROR: Exeption Used. Problem in: ",
                    "EE4": "Exeption ERROR: Attribute Error. Problem in: ",
                    "DV0": "Variable DATA: Variable Changed. Name: ",
                    "DC0": "controller DATA: Button Pressed. Button: ",
                    "DC1": "controller DATA: Axis Changed. Axis: ",
                }
        # Setting up Log Files if they dont exist 
        if brain.sdcard.is_inserted():
            if not brain.sdcard.exists("Log.csv"):
                brain.sdcard.savefile("Log.csv", bytearray("log Start: \n", "utf-8"))

            if not brain.sdcard.exists("index.txt"):
                brain.sdcard.savefile("index.txt", bytearray("0", "utf-8"))
            index_content=brain.sdcard.loadfile("index.txt")
            self.index=int(index_content.decode("utf-8"))
        else:
            self.index=0

    def add(self, add_code, add_details):
        if brain.sdcard.is_inserted():
            brain.sdcard.appendfile("Log.csv", bytearray(", %s [%s] %s %s \n"%(self.index, log_time, self.codes.get(add_code), add_details), "utf-8"))
            brain.sdcard.savefile("index.txt", bytearray("%d"%(self.index), "utf-8"))
            self.index+=1
        else:
            print(", %s [%s] %s %s"%(self.index, log_time, self.codes.get(add_code), add_details))
            self.index+=1
    
    def add_codes(self, code_add, Decoded_text):
        self.codes.update({code_add : "%s"%(Decoded_text)})

    def remove_codes(self, code_remove):
        if code_remove in self.codes:
            self.codes.pop(code_remove)
        else:
            print("Code Not Found In Log Codes")

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

    def read(self):
        if brain.sdcard.is_inserted():
            log_content=brain.sdcard.loadfile("Log.csv")
            print(log_content.decode("utf-8"))
        else:
            print("No SD Card Inserted Cannot Read Log")


log=Log()   

def logging_setup():
    while True:
        try:
            log.logging.drivetrain.six_motor(left1, Right1, left2, Right2, left3, Right3)
            log.logging.motor(Intake)
            log.logging.motor(TopMotor)
            log.logging.motor(colorsorting)
        except Exception as e:
            log.add("EE3", "Motor Logging Thread: %s"%(e))

        try:
            log.logging.Battery()
        except Exception as e:
            log.add("EE3", "Battery Logging Thread: %s"%(e))

        try:
            log.logging.controller(1)
        except Exception as e:
            log.add("EE3", "Controller Logging Thread: %s"%(e))
        wait(100, MSEC)

log.add("DS0",0)
print("Logging System Setup Complete")
Thread(logging_setup)