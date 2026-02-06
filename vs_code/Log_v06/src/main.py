#region VEXcode Generated Robot Configuration
from vex import *
import urandom #type:ignore
import math

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


# Color to String Helper
def convert_color_to_string(col):
    if col == Color.RED:
        return "red"
    if col == Color.GREEN:
        return "green"
    if col == Color.BLUE:
        return "blue"
    if col == Color.WHITE:
        return "white"
    if col == Color.YELLOW:
        return "yellow"
    if col == Color.ORANGE:
        return "orange"
    if col == Color.PURPLE:
        return "purple"
    if col == Color.CYAN:
        return "cyan"
    if col == Color.BLACK:
        return "black"
    if col == Color.TRANSPARENT:
        return "transparent"
    return ""

def play_vexcode_sound(sound_name):
    # Helper to make playing sounds from the V5 in VEXcode easier and
    # keeps the code cleaner by making it clear what is happening.
    print("VEXPlaySound:" + sound_name)
    wait(5, MSEC)

# add a small delay to make sure we don't print in the middle of the REPL header
wait(200, MSEC)
# clear the console to make sure we don't have the REPL in the console
print("\033[2J")



# define variables used for controlling motors based on controller inputs
controller_1_right_shoulder_control_motors_stopped = True

# define a task that will handle monitoring inputs from controller_1
def rc_auto_loop_function_controller_1():
    global controller_1_right_shoulder_control_motors_stopped, remote_control_code_enabled
    # process the controller input every 20 milliseconds
    # update the motors based on the input values
    while True:
        if remote_control_code_enabled:
            # check the buttonR1/buttonR2 status
            # to control Intake
            if controller_1.buttonR1.pressing():
                Intake.spin(FORWARD)
                controller_1_right_shoulder_control_motors_stopped = False
            elif controller_1.buttonR2.pressing():
                Intake.spin(REVERSE)
                controller_1_right_shoulder_control_motors_stopped = False
            elif not controller_1_right_shoulder_control_motors_stopped:
                Intake.stop()
                # set the toggle so that we don't constantly tell the motor to stop when
                # the buttons are released
                controller_1_right_shoulder_control_motors_stopped = True
        # wait before repeating the process
        wait(20, MSEC)

# define variable for remote controller enable/disable
remote_control_code_enabled = True

rc_auto_loop_thread_controller_1 = Thread(rc_auto_loop_function_controller_1)

#endregion VEXcode Generated Robot Configuration

screen_precision = 0
console_precision = 0
ai_vision_2_index = 0
ai_vision_2_objects = []
controller_1_precision = 0
sd_is_in = False
Accuracy = 0
Front_Down = 0
right_temp = 0
left_temp = 0
Descoring = 0
turn_mod = 0
DegreesToTurn = 0
TurnData = 0
driveMod = 0
auto_side = 0
Auto_color = 0
leftData = 0
RightData = 0
IntakeData = 0
iteration = 0
LeftDriveData = 0
RightDriveData = 0
IntakeDriveData = 0
Left_Iter = 0
Right_Iter = 0
Intake_Iter = 0
textReadout = 0
LeftVP = 0
RightVP = 0
BreakParsing = 0
AuBP_MaxVP = 0
colortoggle = 0
skillsRun = 0
recording = 0
MatchLoadData = 0
TopMotorDATA = 0
TopMotorDriveDATA = 0
MatchLoadDriveDATA = 0
matchload_iter = 0
top_iter = 0
use_turningInertial = 0
LastFront_down = 0
turn_to_h_dif = 0
Kp = 0
Ki = 0
Kd = 0
error = 0
loop_delay = 0
last_error = 0
integral = 0
position = 0
integral_limit = 0
error_threshhold = 0
derivative = 0
POWER = 0
intake_speed = 0

# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       Logging.py                                                   #
# 	Author:       Micah Bow                                                    #
# 	Created:      1/27/2026, 12:42 PM                                          #
#   Last Edited:  2/4/2026, 12:02 PM                                           #
# 	Description:  Universal Logging software for Vex V5 Version 6              #
#                                                                              #
# ---------------------------------------------------------------------------- #
controller_2=Controller(PARTNER)

# Timer for log time
log_time= Timer()

# recoreding for controllers and variables
class Record:
    def __init__(self):
        self.axis=""
        self.value=0
        self.button_value=False
        self.index=0
        self.button=""

    
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

    def battery(self, code):
        if brain.sdcard.is_inserted():
            if code == "EB0":
                log.add("EB0", "%s"%(brain.battery.voltage(VoltageUnits.VOLT)))
            elif code == "EB1":
                log.add("EB1", "%s"%(brain.battery.current(CurrentUnits.AMP)))
            elif code == "EB2":
                log.add("EB2", "%s"%(brain.battery.temperature(PERCENT)))
            elif code == "WB0":
                log.add("WB0", "%s"%(brain.battery.voltage(VoltageUnits.VOLT)))
            elif code == "WB1":
                log.add("WB1", "%s"%(brain.battery.current(CurrentUnits.AMP)))
            elif code == "WB2":
                log.add("WB2", "%s"%(brain.battery.temperature(PERCENT)))
            else:
                pass
        else:
            if code == "EB0":
                print("Battery ERROR: Critically low Voltage. Voltage: %s V"%(brain.battery.voltage(VoltageUnits.VOLT)))
            elif code == "EB2":
                print("Battery ERROR: Critically High Current. Current: %s A"%(brain.battery.current(CurrentUnits.AMP)))
            elif code == "EB1":
                print("Battery ERROR: Critically Low Capacity. Capacity: %s %%"%(brain.battery.capacity()))
            elif code == "WB0":
                print("Battery WARNING: Low Voltage. Voltage: %s V"%(brain.battery.voltage(VoltageUnits.VOLT)))
            elif code == "WB1":
                print("Battery WARNING: Low Battery. capacity: %s %%"%(brain.battery.capacity()))
            else:
                pass
    
    def motor(self, motor, code):
        if brain.sdcard.is_inserted():
            if code == "EM0":
                log.add("EM0", "Motor %s Temp: %s"%(motor, motor.temperature(PERCENT)))
            elif code == "EM1":
                log.add("EM1", "Motor %s Power: %s"%(motor, motor.power(PowerUnits.WATT)))
            elif code == "WM0":
                log.add("WM0", "Motor %s Temp: %s"%(motor, motor.temperature(PERCENT)))
            elif code == "WM1":
                log.add("WM1", "Motor %s Power: %s"%(motor, motor.power(PowerUnits.WATT)))
            elif code == "WM2":
                log.add("WM2", "Motor %s Stalled: %s"%(motor, motor.is_stalled()))
            else:
                pass
        else:
            if code == "EM0":
                print("Motor %s ERROR: Critically High Temperature. Temp: %s %%"%(motor, motor.temperature(PERCENT)))
            elif code == "EM1":
                print("Motor %s ERROR: Critically High Power. Power: %s W"%(motor, motor.power(PowerUnits.WATT)))
            elif code == "WM0":
                print("Motor %s WARNING: High Temperature. Temp: %s %%"%(motor, motor.temperature(PERCENT)))
            elif code == "WM1":
                print("Motor %s WARNING: High Power. Power: %s W"%(motor, motor.power(PowerUnits.WATT)))
            else:
                pass
    
    def drivetrain(self, drivetrain, code):
        pass



class Read:
    def console(self):
        if brain.sdcard.is_inserted():
            Log_content=brain.sdcard.loadfile("Log.csv")
            print(Log_content.decode("utf-8"))
        else:
            print("No SD Card Inserted Cannot Read Log")

# Drivetrain recording
class Drivetrain:
    def __init__(self):
        pass
    
    def two_motor(self, left_motor, right_motor):
        self.drivetrin_temp_monitoring=0
        self.drivetrain_power_monitoring=0
        self.drivetrain_disconnected=0

        if (right_motor.temperature()>70 or left_motor.temperature()>70) and (self.drivetrin_temp_monitoring==0 or self.drivetrin_temp_monitoring==2):
            log.add("ED1", "Temp: %s"%(max(right_motor.temperature(), left_motor.temperature())))
            self.drivetrin_temp_monitoring=1
        elif (right_motor.temperature()>50 or left_motor.temperature()>50) and (self.drivetrin_temp_monitoring==0 or self.drivetrin_temp_monitoring==1):
            log.add("WD0", "Temp: %s"%(max(right_motor.temperature(), left_motor.temperature())))
            self.drivetrin_temp_monitoring=2
        elif right_motor.temperature()<=50 and left_motor.temperature()<=50 and (self.drivetrin_temp_monitoring==1 or self.drivetrin_temp_monitoring==2):
            self.drivetrin_temp_monitoring=0
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
        self.drivetrain_temp_monitoring=0
        self.drivetrain_power_monitoring=0
        
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
        self.drivetrain_temp_monitoring=0
        self.drivetrain_power_monitoring=0
        
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
        else:
            pass
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
    
    def motor(self, motor):
        self.temp_monitoring=0
        self.power_monitoring=0
        self.disconnected=0

        if motor.temperature()>70 and (self.temp_monitoring==0 or self.temp_monitoring==2):
            log.add("EM0", "%s Name: %s"%(motor.temperature(), motor()))
            self.temp_monitoring=1
        elif motor.temperature()>50 and (self.temp_monitoring==0 or self.temp_monitoring==1):
            log.add("WM0", "%s Name: %s"%(motor.temperature(), motor()))
            self.temp_monitoring=2
        elif motor.temperature()<=50 and (self.temp_monitoring==2 or self.temp_monitoring==1):
            self.temp_monitoring=0
        if motor.power(PowerUnits.WATT)>40 and (self.power_monitoring==0 or self.power_monitoring==2):
            log.add("EM2", "%s Name: %s"%(motor.power(PowerUnits.WATT), motor()))
            self.power_monitoring=1
        elif motor.power(PowerUnits.WATT)>30 and (self.power_monitoring==0 or self.power_monitoring==1):
            log.add("WM1", "%s Name: %s"%(motor.power(PowerUnits.WATT), motor()))
            self.power_monitoring=2
        elif motor.power(PowerUnits.WATT)<=30 and (self.power_monitoring==1 or self.power_monitoring==2):
            self.power_monitoring=0
        if motor.temperature(PERCENT)==2 and self.disconnected==0:
            log.add("EM2", "%s"%(motor()))
            self.disconnected=1
        if motor.temperature(PERCENT)!=2 and self.disconnected==1:
            log.add("EM2", "%s"%(motor()))
            self.disconnected=1
        if motor.temperature(PERCENT)!=2 and self.disconnected==1:
            self.disconnected=0
    
    def motor_group(self, motor_group):
        self.temp_monitoring=0
        self.power_monitoring=0
    
        max_temp=0
        for motor in motor_group:
            if motor.temperature()>max_temp:
                max_temp=motor.temperature()
        if max_temp>70 and (self.temp_monitoring==0 or self.temp_monitoring==2):
            log.add("EM0", "%s name: %s"%(max_temp, motor_group))
            self.temp_monitoring=1
        elif max_temp>50 and (self.temp_monitoring==0 or self.temp_monitoring==1):
            log.add("WM0", "%s name: %s"%(max_temp, motor_group()))
            self.temp_monitoring=2
        elif max_temp<=50 and (self.temp_monitoring==2 or self.temp_monitoring==1):
            self.temp_monitoring=0
        for motor in motor_group:
            if motor.power(PowerUnits.WATT)>40 and (self.power_monitoring==0 or self.power_monitoring==2):
                log.add("EM1", "%s Name: %s"%(motor.power(PowerUnits.WATT), motor_group))
                self.power_monitoring=1
            elif motor.power(PowerUnits.WATT)>30 and (self.power_monitoring==0 or self.power_monitoring==1):
                log.add("WM1", "%s Name: %s"%(motor.power(PowerUnits.WATT), motor_group))
                self.power_monitoring=2
            elif motor.power(PowerUnits.WATT)<=30 and (self.power_monitoring==1 or self.power_monitoring==2):
                self.power_monitoring=0

    def Battery(self):
        self.battery_voltage_monitoring=0
        self.battery_capacity_monitoring=0
        self.battery_current_monitoring=0

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
        
    
    def Controller_1(self):
        self.Controller_1_button_pressing=0

        if controller_1.axis1.position()!=0 :
            log.record.controller_1_axis("1")
        if controller_1.axis2.position()!=0:
            log.record.controller_1_axis("2")
        if controller_1.axis3.position()!=0:
            log.record.controller_1_axis("3")
        if controller_1.axis4.position()!=0:
            log.record.controller_1_axis("4")
        if controller_1.buttonA.pressing() and (self.Controller_1_button_pressing==0 or self.Controller_1_button_pressing>=2):
            log.record.controller_1_button("A")
            self.Controller_1_button_pressing=1
        if controller_1.buttonB.pressing() and (self.Controller_1_button_pressing<=1 or self.Controller_1_button_pressing>=3):
            log.record.controller_1_button("B")
            self.Controller_1_button_pressing=2
        if controller_1.buttonX.pressing() and (self.Controller_1_button_pressing<=2 or self.Controller_1_button_pressing>=4):
            log.record.controller_1_button("X")
            self.Controller_1_button_pressing=3
        if controller_1.buttonY.pressing() and (self.Controller_1_button_pressing<=3 or self.Controller_1_button_pressing>=5):
            log.record.controller_1_button("Y")
            self.Controller_1_button_pressing=4
        if controller_1.buttonUp.pressing() and (self.Controller_1_button_pressing<=4 or self.Controller_1_button_pressing>=6):
            log.record.controller_1_button("UP")
            self.Controller_1_button_pressing=5
        if controller_1.buttonDown.pressing() and (self.Controller_1_button_pressing<=5 or self.Controller_1_button_pressing>=7):
            log.record.controller_1_button("DOWN")
            self.Controller_1_button_pressing=6
        if controller_1.buttonLeft.pressing() and (self.Controller_1_button_pressing<=6 or self.Controller_1_button_pressing>=8):
            log.record.controller_1_button("LEFT")
            self.Controller_1_button_pressing=7
        if controller_1.buttonRight.pressing() and (self.Controller_1_button_pressing<=7 or self.Controller_1_button_pressing>=9):
            log.record.controller_1_button("RIGHT")
            self.Controller_1_button_pressing=8
        if controller_1.buttonL1.pressing() and (self.Controller_1_button_pressing<=8 or self.Controller_1_button_pressing>=10):
            log.record.controller_1_button("L1")
            self.Controller_1_button_pressing=9
        if controller_1.buttonL2.pressing() and (self.Controller_1_button_pressing<=9 or self.Controller_1_button_pressing>=11):
            log.record.controller_1_button("L2")
            self.Controller_1_button_pressing=10
        if controller_1.buttonR1.pressing() and (self.Controller_1_button_pressing<=10 or self.Controller_1_button_pressing==12):
            log.record.controller_1_button("R1")
            self.Controller_1_button_pressing=11
        if controller_1.buttonR2.pressing() and (self.Controller_1_button_pressing<=11):
            log.record.controller_1_button("R2")
            self.Controller_1_button_pressing=12
       
        if not(controller_1.buttonA.pressing() or controller_1.buttonB.pressing() or controller_1.buttonX.pressing() or controller_1.buttonY.pressing() or controller_1.buttonUp.pressing() or controller_1.buttonDown.pressing() or controller_1.buttonLeft.pressing() or controller_1.buttonRight.pressing() or controller_1.buttonL1.pressing() or controller_1.buttonL2.pressing() or controller_1.buttonR1.pressing() or controller_1.buttonR2.pressing()):
            self.Controller_1_button_pressing=0
    
    def Controller_2(self):
        self.Controller_2_button_pressing=0

        if controller_2.axis1.position()!=0:
            log.record.controller_2_axis("1")
        if controller_2.axis2.position()!=0:
            log.record.controller_2_axis("2")
        if controller_2.axis3.position()!=0:
            log.record.controller_2_axis("3")
        if controller_2.axis4.position()!=0:
            log.record.controller_2_axis("4")
        if controller_2.buttonA.pressing() and (self.Controller_2_button_pressing==0 or self.Controller_2_button_pressing>=1):
            log.record.controller_2_button("A")
            self.Controller_2_button_pressing=1
        if controller_2.buttonB.pressing() and (self.Controller_2_button_pressing<=1 or self.Controller_2_button_pressing>=2):
            log.record.controller_2_button("B")
            self.Controller_2_button_pressing=2
        if controller_2.buttonX.pressing() and (self.Controller_2_button_pressing<=2 or self.Controller_2_button_pressing>=3):
            log.record.controller_2_button("X")
            self.Controller_2_button_pressing=3
        if controller_2.buttonY.pressing() and (self.Controller_2_button_pressing<=3 or self.Controller_2_button_pressing>=4):
            log.record.controller_2_button("Y")
            self.Controller_2_button_pressing=4
        if controller_2.buttonUp.pressing() and (self.Controller_2_button_pressing<=4 or self.Controller_2_button_pressing>=5):
            log.record.controller_2_button("UP")
            self.Controller_2_button_pressing=5
        if controller_2.buttonDown.pressing() and (self.Controller_2_button_pressing<=5 or self.Controller_2_button_pressing>=6):
            log.record.controller_2_button("DOWN")
            self.Controller_2_button_pressing=6
        if controller_2.buttonLeft.pressing() and (self.Controller_2_button_pressing<=6 or self.Controller_2_button_pressing>=7):
            log.record.controller_2_button("LEFT")
            self.Controller_2_button_pressing=7
        if controller_2.buttonRight.pressing() and (self.Controller_2_button_pressing<=7 or self.Controller_2_button_pressing>=8):
            log.record.controller_2_button("RIGHT")
            self.Controller_2_button_pressing=8
        if controller_2.buttonL1.pressing() and (self.Controller_2_button_pressing<=8 or self.Controller_2_button_pressing>=9):
            log.record.controller_2_button("L1")
            self.Controller_2_button_pressing=9
        if controller_2.buttonL2.pressing() and (self.Controller_2_button_pressing<=9 or self.Controller_2_button_pressing>=10):
            log.record.controller_2_button("L2")
            self.Controller_2_button_pressing=10
        if controller_2.buttonR1.pressing() and (self.Controller_2_button_pressing<=10 or self.Controller_2_button_pressing>=11):
            log.record.controller_2_button("R1")
            self.Controller_2_button_pressing=11
        if controller_2.buttonR2.pressing() and (self.Controller_2_button_pressing<=11):
            log.record.controller_2_button("R2")
            self.Controller_2_button_pressing=12
        if not(controller_2.buttonA.pressing() or controller_2.buttonB.pressing() or controller_2.buttonX.pressing() or controller_2.buttonY.pressing() or controller_2.buttonUp.pressing() or controller_2.buttonDown.pressing() or controller_2.buttonLeft.pressing() or controller_2.buttonRight.pressing() or controller_2.buttonL1.pressing() or controller_2.buttonL2.pressing() or controller_2.buttonR1.pressing() or controller_2.buttonR2.pressing()):
            self.Controller_2_button_pressing=0
        
    def variable(self, name, value):
        log.record.Variable(name, value)

class Log:
    def __init__(self):
        self.record=Record()
        self.read=Read()
        self.logging=Logging()
        # Predefined Log Codes dictionary
        self.codes={
                    "ED0": "Drivetrain ERROR: No response from drivetrain.",
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
                }
        # Setting up Log Files if they dont exist 
        if brain.sdcard.is_inserted():
            if not brain.sdcard.exists("Log.csv"):
                brain.sdcard.savefile("Log.csv", bytearray("log Start: \n", "utf-8"))
            if not brain.sdcard.exists("index.txt"):
                brain.sdcard.savefile("index.txt", bytearray("0", "utf-8"))
        else:
            self.index=0

    def add(self, add_code, add_details):
        if brain.sdcard.is_inserted():
            index_content=brain.sdcard.loadfile("index.txt")
            self.index=int(index_content.decode("utf-8"))
            brain.sdcard.appendfile("Log.csv", bytearray(", %s [%s] %s %s \n"%(self.index, log_time, self.codes.get(add_code), add_details), "utf-8"))
            self.index+=1
            brain.sdcard.savefile("index.txt", bytearray("%d"%(self.index), "utf-8"))
        else:
            print(", %s [%s] %s %s"%(self.index, log_time, self.codes.get(add_code), add_details))
    
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


log=Log()  

# funtions for threading
def log_setup(): 
    while True: 
        try:
            log.logging.drivetrain.six_motor(left1, Right1, left2, Right2, left3, Right3)
            log.logging.motor(Intake)
            log.logging.motor(TopMotor)
            log.logging.motor(colorsorting)
        except AttributeError:
            log.add("EE4", "Logging Thread")
        except NameError:
            log.add("EE2", "Logging Thread")
        except ValueError:
            log.add("EE1", "Logging Thread")
        except TypeError:
            log.add("EE0", "Logging Thread")
        except Exception as e:
            log.add("EE3", "Logging Thread: %s"%(e))
        wait(50, MSEC)

def battery_log():
    while True:
        try:
            log.logging.Battery()
        except AttributeError:
            log.add("EE4", "Battery Logging Thread")
        except NameError:
            log.add("EE2", "Battery Logging Thread")
        except ValueError:
            log.add("EE1", "Battery Logging Thread")
        except TypeError:
            log.add("EE0", "Battery Logging Thread")
        except Exception as e:
            log.add("EE3", "Battery Logging Thread: %s"%(e))
        wait(50, MSEC)

def controller_log():
    while True:
        try:
            log.logging.Controller_1()
        except AttributeError:
            log.add("EE4", "Controller Logging Thread")
        except NameError:
            log.add("EE2", "Controller Logging Thread")
        except ValueError:
            log.add("EE1", "Controller Logging Thread")
        except TypeError:
            log.add("EE0", "Controller Logging Thread")
        except Exception as e:
            log.add("EE3", "Controller Logging Thread: %s"%(e))
        wait(50, MSEC)


# Logging
log.add("DS0",0)
Thread(log_setup)
Thread(battery_log)
Thread(controller_log)
