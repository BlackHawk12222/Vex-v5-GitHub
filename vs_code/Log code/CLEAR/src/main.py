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
# 	Module:       CLEAR.py                                                     #
# 	Author:       Micah Bow                                                    #
# 	Created:      1/27/2026, 12:42 PM                                          #
#   Last Edited:  2/23/2026, 10:00 PM                                          #
# 	Description:  Capture, Logging, Encoding, Archiving , Recording.           #
#                                                                              #
# ---------------------------------------------------------------------------- #


# Timer for log time
log_time= Timer()
timer=Timer()
controller_2=Controller(PARTNER)
pusher_state = 0
loader_state = 0
record = 0
controlleraxis2positionhistory = 0
controlleraxis3positionhistory = 0
recording_state=0

def none():
    return(none)

class Drivetrain:
    def __init__(self):
        self.drivetrain_temp_monitoring={}  # Track per motor
        self.drivetrain_power_monitoring={}  # Track per motor
        self.drivetrain_disconnected={}  # Track per motor
    
    def two_motor(self, left_motor, right_motor):
        left_id = id(left_motor)
        right_id = id(right_motor)
        
        # Initialize tracking
        for motor_id in [left_id, right_id]:
            if motor_id not in self.drivetrain_temp_monitoring:
                self.drivetrain_temp_monitoring[motor_id] = 0
            if motor_id not in self.drivetrain_power_monitoring:
                self.drivetrain_power_monitoring[motor_id] = 0
            if motor_id not in self.drivetrain_disconnected:
                self.drivetrain_disconnected[motor_id] = 0
        
        temp_state = self.drivetrain_temp_monitoring.get('pair', 0)
        power_state = self.drivetrain_power_monitoring.get('pair', 0)
        
        if (right_motor.temperature()>70 or left_motor.temperature()>70) and (temp_state==0 or temp_state==2):
            log.add("ED1", "Temp: %s"%(max(right_motor.temperature(), left_motor.temperature())))
            self.drivetrain_temp_monitoring['pair'] = 1
        elif (right_motor.temperature()>50 or left_motor.temperature()>50) and (temp_state==0 or temp_state==1):
            log.add("WD0", "Temp: %s"%(max(right_motor.temperature(), left_motor.temperature())))
            self.drivetrain_temp_monitoring['pair'] = 2
        elif right_motor.temperature()<=50 and left_motor.temperature()<=50 and (temp_state==1 or temp_state==2):
            self.drivetrain_temp_monitoring['pair'] = 0
        
        if right_motor.power(PowerUnits.WATT)>40 or left_motor.power(PowerUnits.WATT)>40 and (power_state==0 or power_state==2):
            log.add("ED3", "Power: %s"%(max(right_motor.power(PowerUnits.WATT), left_motor.power(PowerUnits.WATT))))
            self.drivetrain_power_monitoring['pair'] = 1
        elif right_motor.power(PowerUnits.WATT)>30 or left_motor.power(PowerUnits.WATT)>30 and (power_state==0 or power_state==1):
            log.add("WD3", "Power: %s"%(max(right_motor.power(PowerUnits.WATT), left_motor.power(PowerUnits.WATT))))
            self.drivetrain_power_monitoring['pair'] = 2
        elif right_motor.power(PowerUnits.WATT)<=30 and left_motor.power(PowerUnits.WATT)<=30 and (power_state==1 or power_state==2):
            self.drivetrain_power_monitoring['pair'] = 0
        
        if right_motor.temperature(PERCENT)==2 and self.drivetrain_disconnected[right_id]==0:
            log.add("ED3", "Right Motor")
            self.drivetrain_disconnected[right_id]=1
        elif right_motor.temperature(PERCENT)!=2 and self.drivetrain_disconnected[right_id]==1:
            self.drivetrain_disconnected[right_id]=0

        if left_motor.temperature(PERCENT)==2 and self.drivetrain_disconnected[left_id]==0:
            log.add("ED3", "Left Motor")            
            self.drivetrain_disconnected[left_id]=1
        elif left_motor.temperature(PERCENT)!=2 and self.drivetrain_disconnected[left_id]==1:
            self.drivetrain_disconnected[left_id]=0
        
    def four_motor(self, front_left_motor, front_right_motor, back_left_motor, back_right_motor):
        fl_id = id(front_left_motor)
        fr_id = id(front_right_motor)
        bl_id = id(back_left_motor)
        br_id = id(back_right_motor)
        
        # Initialize tracking
        for motor_id in [fl_id, fr_id, bl_id, br_id]:
            if motor_id not in self.drivetrain_temp_monitoring:
                self.drivetrain_temp_monitoring[motor_id] = 0
            if motor_id not in self.drivetrain_power_monitoring:
                self.drivetrain_power_monitoring[motor_id] = 0
            if motor_id not in self.drivetrain_disconnected:
                self.drivetrain_disconnected[motor_id] = 0
        
        temp_state = self.drivetrain_temp_monitoring.get('four_motor', 0)
        power_state = self.drivetrain_power_monitoring.get('four_motor', 0)
        
        if (front_left_motor.temperature()>70 or front_right_motor.temperature()>70 or back_left_motor.temperature()>70 or back_right_motor.temperature()>70) and (temp_state==0 or temp_state==2):
            log.add("ED1", "Temp: %s"%(max(front_left_motor.temperature(), front_right_motor.temperature(), back_left_motor.temperature(), back_right_motor.temperature())))
            self.drivetrain_temp_monitoring['four_motor']=1
        elif (front_left_motor.temperature()>50 or front_right_motor.temperature()>50 or back_left_motor.temperature()>50 or back_right_motor.temperature()>50) and (temp_state==0 or temp_state==1):
            log.add("WD0", "Temp: %s"%(max(front_left_motor.temperature(), front_right_motor.temperature(), back_left_motor.temperature(), back_right_motor.temperature())))
            self.drivetrain_temp_monitoring['four_motor']=2
        elif (front_left_motor.temperature()<=50 and front_right_motor.temperature()<=50 and back_left_motor.temperature()<=50 and back_right_motor.temperature()<=50) and (temp_state==1 or temp_state==2):
            self.drivetrain_temp_monitoring['four_motor']=0
        
        if front_left_motor.power(PowerUnits.WATT)>40 or front_right_motor.power(PowerUnits.WATT)>40 or back_left_motor.power(PowerUnits.WATT)>40 or back_right_motor.power(PowerUnits.WATT)>40 and (power_state==0 or power_state==2):
            log.add("ED3", "Power: %s"%(max(front_left_motor.power(PowerUnits.WATT), front_right_motor.power(PowerUnits.WATT), back_left_motor.power(PowerUnits.WATT), back_right_motor.power(PowerUnits.WATT))))
            self.drivetrain_power_monitoring['four_motor']=1
        elif front_left_motor.power(PowerUnits.WATT)>30 or front_right_motor.power(PowerUnits.WATT)>30 or back_left_motor.power(PowerUnits.WATT)>30 or back_right_motor.power(PowerUnits.WATT)>30 and (power_state==0 or power_state==1):  
            log.add("WD3", "Power: %s"%(max(front_left_motor.power(PowerUnits.WATT), front_right_motor.power(PowerUnits.WATT), back_left_motor.power(PowerUnits.WATT), back_right_motor.power(PowerUnits.WATT))))
            self.drivetrain_power_monitoring['four_motor']=2
        elif front_left_motor.power(PowerUnits.WATT)<=30 and front_right_motor.power(PowerUnits.WATT)<=30 and back_left_motor.power(PowerUnits.WATT)<=30 and back_right_motor.power(PowerUnits.WATT)<=30 and (power_state==1 or power_state==2):
            self.drivetrain_power_monitoring['four_motor']=0
        
        if front_right_motor.temperature(PERCENT)==2 and self.drivetrain_disconnected[fr_id]==0:
            log.add("ED3", "Front Right Motor")
            self.drivetrain_disconnected[fr_id]=1
        elif front_right_motor.temperature(PERCENT)!=2 and self.drivetrain_disconnected[fr_id]==1:
            self.drivetrain_disconnected[fr_id]=0
        
        if front_left_motor.temperature(PERCENT)==2 and self.drivetrain_disconnected[fl_id]==0:
            log.add("ED3", "Front Left Motor")            
            self.drivetrain_disconnected[fl_id]=1
        elif front_left_motor.temperature(PERCENT)!=2 and self.drivetrain_disconnected[fl_id]==1:
            self.drivetrain_disconnected[fl_id]=0
        
        if back_right_motor.temperature(PERCENT)==2 and self.drivetrain_disconnected[br_id]==0:
            log.add("ED3", "Back Right Motor")
            self.drivetrain_disconnected[br_id]=1
        elif back_right_motor.temperature(PERCENT)!=2 and self.drivetrain_disconnected[br_id]==1:
            self.drivetrain_disconnected[br_id]=0
        
        if back_left_motor.temperature(PERCENT)==2 and self.drivetrain_disconnected[bl_id]==0:
            log.add("ED3", "Back Left Motor")            
            self.drivetrain_disconnected[bl_id]=1
        elif back_left_motor.temperature(PERCENT)!=2 and self.drivetrain_disconnected[bl_id]==1:
            self.drivetrain_disconnected[bl_id]=0
    
    def six_motor(self, front_left_motor, front_right_motor, middle_left_motor, middle_right_motor, back_left_motor, back_right_motor):
        fl_id = id(front_left_motor)
        fr_id = id(front_right_motor)
        ml_id = id(middle_left_motor)
        mr_id = id(middle_right_motor)
        bl_id = id(back_left_motor)
        br_id = id(back_right_motor)
        
        # Initialize tracking
        for motor_id in [fl_id, fr_id, ml_id, mr_id, bl_id, br_id]:
            if motor_id not in self.drivetrain_temp_monitoring:
                self.drivetrain_temp_monitoring[motor_id] = 0
            if motor_id not in self.drivetrain_power_monitoring:
                self.drivetrain_power_monitoring[motor_id] = 0
            if motor_id not in self.drivetrain_disconnected:
                self.drivetrain_disconnected[motor_id] = 0
        
        temp_state = self.drivetrain_temp_monitoring.get('six_motor', 0)
        power_state = self.drivetrain_power_monitoring.get('six_motor', 0)
        
        if (front_left_motor.temperature(PERCENT)>70 or front_right_motor.temperature(PERCENT)>70 or middle_left_motor.temperature(PERCENT)>70 or middle_right_motor.temperature(PERCENT)>70 or back_left_motor.temperature(PERCENT)>70 or back_right_motor.temperature(PERCENT)>70) and (temp_state==0 or temp_state==2):
            log.add("ED1", "Temp: %s"%(max(front_left_motor.temperature(PERCENT), front_right_motor.temperature(PERCENT), middle_left_motor.temperature(PERCENT), middle_right_motor.temperature(PERCENT), back_left_motor.temperature(PERCENT), back_right_motor.temperature(PERCENT))))
            self.drivetrain_temp_monitoring['six_motor']=1
        elif (front_left_motor.temperature(PERCENT)>50 or front_right_motor.temperature(PERCENT)>50 or middle_left_motor.temperature(PERCENT)>50 or middle_right_motor.temperature(PERCENT)>50 or back_left_motor.temperature(PERCENT)>50 or back_right_motor.temperature(PERCENT)>50) and (temp_state==0 or temp_state==1):
            log.add("WD0", "Temp: %s"%(max(front_left_motor.temperature(PERCENT), front_right_motor.temperature(PERCENT), middle_left_motor.temperature(PERCENT), middle_right_motor.temperature(PERCENT), back_left_motor.temperature(PERCENT), back_right_motor.temperature(PERCENT))))
            self.drivetrain_temp_monitoring['six_motor']=2
        elif (front_left_motor.temperature(PERCENT)<=50 and front_right_motor.temperature(PERCENT)<=50 and middle_left_motor.temperature(PERCENT)<=50 and middle_right_motor.temperature(PERCENT)<=50 and back_left_motor.temperature(PERCENT)<=50 and back_right_motor.temperature(PERCENT)<=50) and (temp_state==1 or temp_state==2):
            self.drivetrain_temp_monitoring['six_motor']=0
        
        if front_left_motor.power(PowerUnits.WATT)>40 or front_right_motor.power(PowerUnits.WATT)>40 or middle_left_motor.power(PowerUnits.WATT)>40 or middle_right_motor.power(PowerUnits.WATT)>40 or back_left_motor.power(PowerUnits.WATT)>40 or back_right_motor.power(PowerUnits.WATT)>40 and (power_state==0 or power_state==2):
            log.add("ED3", "Power: %s"%(max(front_left_motor.power(PowerUnits.WATT), front_right_motor.power(PowerUnits.WATT), middle_left_motor.power(PowerUnits.WATT), middle_right_motor.power(PowerUnits.WATT), back_left_motor.power(PowerUnits.WATT), back_right_motor.power(PowerUnits.WATT))))
            self.drivetrain_power_monitoring['six_motor']=1
        elif front_left_motor.power(PowerUnits.WATT)>30 or front_right_motor.power(PowerUnits.WATT)>30 or middle_left_motor.power(PowerUnits.WATT)>30 or middle_right_motor.power(PowerUnits.WATT)>30 or back_left_motor.power(PowerUnits.WATT)>30 or back_right_motor.power(PowerUnits.WATT)>30 and (power_state==0 or power_state==1):  
            log.add("WD3", "Power: %s"%(max(front_left_motor.power(PowerUnits.WATT), front_right_motor.power(PowerUnits.WATT), middle_left_motor.power(PowerUnits.WATT), middle_right_motor.power(PowerUnits.WATT), back_left_motor.power(PowerUnits.WATT), back_right_motor.power(PowerUnits.WATT))))
            self.drivetrain_power_monitoring['six_motor']=2
        elif front_left_motor.power(PowerUnits.WATT)<=30 and front_right_motor.power(PowerUnits.WATT)<=30 and middle_left_motor.power(PowerUnits.WATT)<=30 and middle_right_motor.power(PowerUnits.WATT)<=30 and back_left_motor.power(PowerUnits.WATT)<=30 and back_right_motor.power(PowerUnits.WATT)<=30 and (power_state==1 or power_state==2):
            self.drivetrain_power_monitoring['six_motor']=0

        if front_right_motor.temperature(PERCENT)==2 and self.drivetrain_disconnected[fr_id]==0:
            log.add("ED3", "Front Right Motor")
            self.drivetrain_disconnected[fr_id]=1
        elif front_right_motor.temperature(PERCENT)!=2 and self.drivetrain_disconnected[fr_id]==1:
            self.drivetrain_disconnected[fr_id]=0
        
        if front_left_motor.temperature(PERCENT)==2 and self.drivetrain_disconnected[fl_id]==0:
            log.add("ED3", "FrontLeft Motor")            
            self.drivetrain_disconnected[fl_id]=1
        elif front_left_motor.temperature(PERCENT)!=2 and self.drivetrain_disconnected[fl_id]==1:
            self.drivetrain_disconnected[fl_id]=0
        
        if middle_right_motor.temperature(PERCENT)==2 and self.drivetrain_disconnected[mr_id]==0:
            log.add("ED3", "Middle Right Motor")
            self.drivetrain_disconnected[mr_id]=1
        elif middle_right_motor.temperature(PERCENT)!=2 and self.drivetrain_disconnected[mr_id]==1:
            self.drivetrain_disconnected[mr_id]=0
        
        if middle_left_motor.temperature(PERCENT)==2 and self.drivetrain_disconnected[ml_id]==0:
            log.add("ED3", "Middle Left Motor")            
            self.drivetrain_disconnected[ml_id]=1
        elif middle_left_motor.temperature(PERCENT)!=2 and self.drivetrain_disconnected[ml_id]==1:
            self.drivetrain_disconnected[ml_id]=0
        
        if back_right_motor.temperature(PERCENT)==2 and self.drivetrain_disconnected[br_id]==0:
            log.add("ED3", "Back Right Motor")
            self.drivetrain_disconnected[br_id]=1
        elif back_right_motor.temperature(PERCENT)!=2 and self.drivetrain_disconnected[br_id]==1:
            self.drivetrain_disconnected[br_id]=0
        
        if back_left_motor.temperature(PERCENT)==2 and self.drivetrain_disconnected[bl_id]==0:
            log.add("ED3", "Back Left Motor")        
            self.drivetrain_disconnected[bl_id]=1
        elif back_left_motor.temperature(PERCENT)!=2 and self.drivetrain_disconnected[bl_id]==1:
            self.drivetrain_disconnected[bl_id]=0


# logging for the log class
class Logging:

    def __init__(self):
        self.drivetrain=Drivetrain()
        self.motor_temp_monitoring={} 
        self.motor_power_monitoring={}  
        self.motor_disconnected={}  
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
        self.value_history=-1
        self.axis1=0
        self.axis2=0
        self.axis3=0
        self.axis4=0
        self.tolrance=3
        self.variables={}
    
    def motor(self, motor):
        motor_id = id(motor) 
        
        # Initialize tracking
        if motor_id not in self.motor_temp_monitoring:
            self.motor_temp_monitoring[motor_id] = 0
        if motor_id not in self.motor_power_monitoring:
            self.motor_power_monitoring[motor_id] = 0
        if motor_id not in self.motor_disconnected:
            self.motor_disconnected[motor_id] = 0
        
        if motor.temperature()>70 and (self.motor_temp_monitoring[motor_id]==0 or self.motor_temp_monitoring[motor_id]==2):
            log.add("EM0", "Motor %s Temp: %s"%(motor, motor.temperature(PERCENT)))
            self.motor_temp_monitoring[motor_id]=1
        elif motor.temperature()>50 and (self.motor_temp_monitoring[motor_id]==0 or self.motor_temp_monitoring[motor_id]==1):
            log.add("WM0", "Motor %s Temp: %s"%(motor, motor.temperature(PERCENT)))
            self.motor_temp_monitoring[motor_id]=2
        elif motor.temperature()<=50 and (self.motor_temp_monitoring[motor_id]==2 or self.motor_temp_monitoring[motor_id]==1):
            self.motor_temp_monitoring[motor_id]=0
        
        if motor.power(PowerUnits.WATT)>40 and (self.motor_power_monitoring[motor_id]==0 or self.motor_power_monitoring[motor_id]==2):
            log.add("EM2", "Motor %s Power: %s"%(motor, motor.power(PowerUnits.WATT)))
            self.motor_power_monitoring[motor_id]=1
        elif motor.power(PowerUnits.WATT)>30 and (self.motor_power_monitoring[motor_id]==0 or self.motor_power_monitoring[motor_id]==1):
            log.add("WM1", "Motor %s Power: %s"%(motor, motor.power(PowerUnits.WATT)))
            self.motor_power_monitoring[motor_id]=2
        elif motor.power(PowerUnits.WATT)<=30 and (self.motor_power_monitoring[motor_id]==1 or self.motor_power_monitoring[motor_id]==2):
            self.motor_power_monitoring[motor_id]=0
        
        if motor.temperature(PERCENT)==2 and self.motor_disconnected[motor_id]==0:
            log.add("EM1", "Motor %s Disconnected"%(motor))
            self.motor_disconnected[motor_id]=1
        
        if motor.temperature(PERCENT)!=2 and self.motor_disconnected[motor_id]==1:
            self.motor_disconnected[motor_id]=0

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
        
        elif brain.battery.capacity()<50 and (self.battery_capacity_monitoring==0):
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
    
    def controller(self, controller, monitormotor=Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)):
        if controller==1:
            Controller=controller_1
        elif controller==2:
            Controller=controller_2
        
        if Controller.axis1.position()!=0 and self.axis1 != Controller.axis1.position():
            degrees=monitormotor.position(DEGREES)
            monitormotor.set_position(0, DEGREES)
            log.add("DC1", "Controller_%d_Axis1: %d Moved: %d Degrees"%(controller, Controller.axis1.position(), degrees))
            self.axis1=Controller.axis1.position()
        elif 0 == Controller.axis1.position() and self.axis1!=0:
            degrees=monitormotor.position(DEGREES)
            monitormotor.set_position(0, DEGREES)
            log.add("DC1", "Controller_%d_Axis1: %d Moved: %d Degrees"%(controller, Controller.axis1.position(), degrees))
            self.axis1=0

        if Controller.axis2.position()!=0 and self.axis2 != Controller.axis2.position():
            degrees=monitormotor.position(DEGREES)
            monitormotor.set_position(0, DEGREES)
            log.add("DC1", "Controller_%d_Axis2: %d Moved: %d Degrees"%(controller, Controller.axis2.position(), degrees))
            self.axis2=Controller.axis2.position()
        elif 0 == Controller.axis2.position() and self.axis2!=0:
            degrees=monitormotor.position(DEGREES)
            monitormotor.set_position(0, DEGREES)
            log.add("DC1", "Controller_%d_Axis2: %d Moved: %d Degrees"%(controller, Controller.axis2.position(), degrees))
            self.axis2=0

        if Controller.axis3.position()!=0 and self.axis3 != Controller.axis3.position():
            degrees=monitormotor.position(DEGREES)
            monitormotor.set_position(0, DEGREES)
            log.add("DC1", "Controller_%d_Axis3: %d Moved: %d Degrees"%(controller, Controller.axis3.position(), degrees))
            self.axis3=Controller.axis3.position()
        elif 0 == Controller.axis3.position() and self.axis3!=0:
            degrees=monitormotor.position(DEGREES)
            monitormotor.set_position(0, DEGREES)
            log.add("DC1", "Controller_%d_Axis3: %d Moved: %d Degrees"%(controller, Controller.axis3.position(), degrees))
            self.axis3=0

        if Controller.axis4.position()!=0 and self.axis4 != Controller.axis4.position():
            degrees=monitormotor.position(DEGREES)
            monitormotor.set_position(0, DEGREES)
            log.add("DC1", "Controller_%d_Axis4: %d Moved: %d Degrees"%(controller, Controller.axis4.position(), degrees))
            self.axis4=Controller.axis4.position()
        elif 0 == Controller.axis4.position() and self.axis4!=0:
            degrees=monitormotor.position(DEGREES)
            monitormotor.set_position(0, DEGREES)
            log.add("DC1", "Controller_%d_Axis4: %d Moved: %d Degrees"%(controller, Controller.axis4.position(), degrees))
            self.axis4=0

        if Controller.buttonA.pressing() and self.button_a==True:
            log.add("DC0", "Controller_%d_Button A Pressed"%(controller))
            self.button_a=False
        elif Controller.buttonA.pressing()==False and self.button_a==False:
            log.add("DC0", "Controller_%d_Button A Released"%(controller))
            self.button_a=True


        if Controller.buttonB.pressing() and self.button_b==True:
            log.add("DC0", "Controller_%d_Button B Pressed"%(controller))
            self.button_b=False
        elif Controller.buttonB.pressing()==False and self.button_b==False:
            log.add("DC0", "Controller_%d_Button B Released"%(controller))
            self.button_b=True

        if Controller.buttonX.pressing() and self.button_x==True:
            log.add("DC0", "Controller_%d_Button X Pressed"%(controller))
            self.button_x=False
        elif Controller.buttonX.pressing()==False and self.button_x==False:
            log.add("DC0", "Controller_%d_Button X Released"%(controller))
            self.button_x=True

        if Controller.buttonY.pressing() and self.button_y==True:
            log.add("DC0", "Controller_%d_Button Y Pressed"%(controller))
            self.button_y=False
        elif Controller.buttonY.pressing()==False and self.button_y==False:
            log.add("DC0", "Controller_%d_Button Y Released"%(controller))
            self.button_y=True

        if Controller.buttonUp.pressing() and self.button_up==True:
            log.add("DC0", "Controller_%d_Button UP Pressed"%(controller))
            self.button_up=False
        elif Controller.buttonUp.pressing()==False and self.button_up==False:
            log.add("DC0", "Controller_%d_Button UP Released"%(controller))
            self.button_up=True

        if Controller.buttonDown.pressing() and self.button_down==True:
            log.add("DC0", "Controller_%d_Button DOWN Pressed"%(controller))
            self.button_down=False
        elif Controller.buttonDown.pressing()==False and self.button_down==False:
            log.add("DC0", "Controller_%d_Button DOWN Released"%(controller))
            self.button_down=True

        if Controller.buttonLeft.pressing() and self.button_left==True:
            log.add("DC0", "Controller_%d_Button LEFT Pressed"%(controller))
            self.button_left=False
        elif Controller.buttonLeft.pressing()==False and self.button_left==False:
            log.add("DC0", "Controller_%d_Button LEFT Released"%(controller))
            self.button_left=True

        if Controller.buttonRight.pressing() and self.button_right==True:
            log.add("DC0", "Controller_%d_Button RIGHT Pressed"%(controller))
            self.button_right=False
        elif Controller.buttonRight.pressing()==False and self.button_right==False:
            log.add("DC0", "Controller_%d_Button RIGHT Released"%(controller))
            self.button_right=True

        if Controller.buttonL1.pressing() and self.button_L1==True:
            log.add("DC0", "Controller_%d_Button L1 Pressed"%(controller))
            self.button_L1=False
        elif Controller.buttonL1.pressing()==False and self.button_L1==False:
            log.add("DC0", "Controller_%d_Button L1 Released"%(controller))
            self.button_L1=True

        if Controller.buttonL2.pressing() and self.button_L2==True:
            log.add("DC0", "Controller_%d_Button L2 Pressed"%(controller))
            self.button_L2=False
        elif Controller.buttonL2.pressing()==False and self.button_L2==False:
            log.add("DC0", "Controller_%d_Button L2 Released"%(controller))
            self.button_L2=True

        if Controller.buttonR1.pressing() and self.button_R1==True:
            log.add("DC0", "Controller_%d_Button R1 Pressed"%(controller))
            self.button_R1=False
        elif Controller.buttonR1.pressing()==False and self.button_R1==False:
            log.add("DC0", "Controller_%d_Button R1 Released"%(controller))
            self.button_R1=True

        if Controller.buttonR2.pressing() and self.button_R2==True:
            log.add("DC0", "Controller_%d_Button R2 Pressed"%(controller))
            self.button_R2=False
        elif Controller.buttonR2.pressing()==False and self.button_R2==False:
            log.add("DC0", "Controller_%d_Button R2 Released"%(controller))
            self.button_R2=True
        
    def variable(self, name, value):
        valueid=id(name)
        if valueid not in self.variables:
            self.variables[valueid]=0
        if value != self.variables[valueid]:
            log.add("DV0", "Variable %s Value: %s"%(name, value))
            self.variables[valueid] = value

class Recording:
    def __init__(self):
        self.record=False
        self.timerecord=0
        self.posttimerecord=0
        self.Aton=""
        self.postlist=[]
        self.File=""
        self.poststring=""


    def start(self, Aton):
        filename=str(Aton) + "_pre.txt"
        if self.record == False:
            if brain.sdcard.is_inserted():
                self.record=True
                brain.sdcard.savefile(filename, bytearray("\n", log.format))
                self.Aton=Aton + "_pre.txt"
            else:
                print("Put in sdcard")
        else:
            print("Cant start recording because recording is on.")

    def stop(self, Aton):
        if brain.sdcard.is_inserted():
            filename=str(Aton) + "_pre.txt"
            preatonfile=""
            self.record=False
            preatonfile=brain.sdcard.loadfile(filename).decode(log.format)
            preatonlist=preatonfile.split("\n")
            for i in range(len(preatonlist)):
                prelist=preatonlist[i].split(' ')
                if len(prelist) >= 3:
                    if prelist[3] == ":Controller":
                        self.postlist.append(str(prelist) + "\n")
            for i in range(len(self.postlist)):
                self.poststring= self.poststring + str(self.postlist[i])
            brain.sdcard.savefile(filename, bytearray(str(self.poststring), log.format))
        else:
            print("Put in sdcard.")

    def encode(self, Aton, Forward, right, left, other1start=none, other1stop=none, other1button=none, other2start=none, other2stop=none, other2button=none, other3start=none, other3stop=none, other3button=none, other4start=none, other4stop=none, other4button=none, other5start=none, other5stop=none, other5button=none, other6start=none, other6stop=none, other6button=none):
        if brain.sdcard.is_inserted:
            filename=Aton + ".txt"
            self.record=False
            brain.sdcard.savefile(filename)
            prelist=[]
            preatonfile=brain.sdcard.loadfile(Aton + "_pre.txt")
            preatonlist=preatonfile.decode(log.format).split("\n")
            for i in range(len(preatonlist)):
                prelist=str(preatonlist[i]).split(',')
                try:
                    prelist2=str(preatonlist[i+1]).split(',')
                except IndexError:
                    pass
                if len(prelist)>=2:
                    if "Controller" in str(prelist):
                        print("found controller")
                        if "Axis" in str(prelist):
                            print("found axis")
                            if "Controller_1_Axis2" in str(prelist):
                                brain.sdcard.appendfile(filename, bytearray("%s(%s, %s), "%(str(left), str(prelist[11]), str(prelist[13])), log.format))
                            elif "Controller_1_Axis3" in str(prelist):
                                brain.sdcard.appendfile(filename, bytearray("%s(%s, %s), "%(str(right), str(prelist[11]), str(prelist[13])), log.format))

                        elif "Button" in str(prelist):
                            print("found button")
                            if "Released" in str(prelist):
                                if other1button in str(prelist[11]):
                                    brain.sdcard.appendfile(filename, bytearray(str(other1start) + '(), ', log.format))
                                elif other2button in str(prelist[11]):
                                    brain.sdcard.appendfile(filename, bytearray(str(other2start) + '(), ', log.format))
                                elif other3button in str(prelist[11]):
                                    brain.sdcard.appendfile(filename, bytearray(str(other3start) + '(), ', log.format))
                                elif other4button in str(prelist[11]):
                                    brain.sdcard.appendfile(filename, bytearray(str(other4start) + '(), ', log.format))
                                elif other5button in str(prelist[11]):
                                    brain.sdcard.appendfile(filename, bytearray(str(other5start) + '(), ', log.format))
                                elif other6button in str(prelist[11]):
                                    brain.sdcard.appendfile(filename, bytearray(str(other6start) + '(), ', log.format))
                            elif "Pressed" in str(prelist):
                                if other1button in str(prelist[11]):
                                    brain.sdcard.appendfile(filename, bytearray(str(other1stop) + '(), ', log.format))
                                elif other2button in str(prelist[11]):
                                    brain.sdcard.appendfile(filename, bytearray(str(other2stop) + '(), ', log.format))
                                elif other3button in str(prelist[11]):
                                    brain.sdcard.appendfile(filename, bytearray(str(other3stop) + '(), ', log.format))
                                elif other4button in str(prelist[11]):
                                    brain.sdcard.appendfile(filename, bytearray(str(other4stop) + '(), ', log.format))
                                elif other5button in str(prelist[11]):
                                    brain.sdcard.appendfile(filename, bytearray(str(other5stop) + '(), ', log.format))
                                elif other6button in str(prelist[11]):
                                    brain.sdcard.appendfile(filename, bytearray(str(other6stop) + '(), ', log.format))
                    if len(prelist2) >= 3:
                        brain.sdcard.appendfile(filename, bytearray("wait(" + str(abs(int(prelist[3].replace("[", '').replace("]", '').replace("'", '').replace("'", '')) - int(prelist2[3].replace("[", '').replace("]", '').replace("'", '').replace("'", '')))) + ", MSEC)", log.format))
            print("Encode done.")            
                            
        else:
            print("Put in sdcard.")

    
    def run(self, Aton):
        Atonfile=brain.sdcard.loadfile(Aton + ".txt")
        exec(Atonfile.decode(log.format))

class Archive:
    def __init__(self):
        self.format="utf-8"
        self.logfile=""
        self.loglist=[]
        if not brain.sdcard.exists("loghistory.txt"):
            brain.sdcard.savefile("loghistory.txt")
    
    def log(self):
        try:
            if brain.sdcard.is_inserted():
                log.adding=False
                reversecodes={value: key for key, value in log.codes.items()}
                self.logfile=brain.sdcard.loadfile("Log.csv").decode(log.format)
                self.loglist=self.logfile.split("\n")
                for i in range(len(self.loglist)):
                    logline=self.loglist[i].split(':')
                    if len(logline)>=3:
                        loglines= ":" + str(logline[1]) + ":" + str(logline[2]) + ": "
                        brain.sdcard.appendfile("loghistory.txt", bytearray(str(reversecodes.get(loglines)) + str(logline[0]), log.format))
                self.logfile=""
                log.adding=True
            else:
                print("Put in the sdcard.")
        except MemoryError:
            if brain.sdcard.is_inserted():
                self.logfile=""
                log.adding=False
                reversecodes={value: key for key, value in log.codes.items()}
                with open("Log.csv", 'r') as self.logfile:
                    for line in self.logfile:
                        logline=line.split(':')
                        loglines= str(logline[1]) + str(logline[2])
                        brain.sdcard.appendfile("loghistory.txt", bytearray(str(reversecodes.get(loglines)) + str(logline[0]), log.format))
                log.adding=True
            else:
                print("Put in the sdcard.")
        log.clear()
    
    def recording(self, name):
        try:
            if brain.sdcard.is_inserted():
                archname=(name - ".txt") + "history.txt"
                reversecodes={value: key for key, value in log.codes.items()}
                self.file=brain.sdcard.loadfile(name).decode(log.format)
                self.list=self.file.split("\n")
                for i in range(len(self.list)):
                    line=self.list[i].split(':')
                    if len(line)>=3:
                        lines= ":" + str(line[1]) + ":" + str(line[2]) + ": "
                        brain.sdcard.appendfile(archname, bytearray(str(reversecodes.get(lines)) + str(line[0]), log.format))
                self.logfile=""
                brain.sdcard.savefile(name)
            else:
                print("Put in the sdcard.")
        except MemoryError:
            self.file=""
            if brain.sdcard.is_inserted():
                archname=(name - ".txt") + "history.txt"
                reversecodes={value: key for key, value in log.codes.items()}
                with open(name, 'r') as self.file:
                    for line in self.file:
                        logline=line.split(':')
                        loglines= str(logline[1]) + str(logline[2])
                        brain.sdcard.appendfile(archname, bytearray(str(reversecodes.get(loglines)) + str(logline[0]), log.format))
                brain.sdcard.savefile(name)
            else:
                print("Put in the sdcard.")
    
    def recall(self, name):
        filename=name - "history"
        try:
            file=brain.sdcard.loadfile(name).decode(log.format)
            brain.sdcard.savefile(filename)
            filelist=file.split(',')
            for i in range(len(filelist)):
                prelist=filelist[i].split(' ')
                prelist2=filelist[i+1].split(' ')
                if len(prelist) >= 2 and len(prelist2) >=1:
                    brain.sdcard.appendfile(filename, bytearray(str(prelist2[0]) + str(prelist2[1]) + str(log.codes.get(prelist[2])), log.format))
        except MemoryError:
            with open(name, 'r') as file:
                for line in file:
                    prelist=line.split(' ')
                    try:
                        prelist2=next(file).split(' ')
                    except StopIteration:
                        pass
                    if len(prelist) >= 2 and len(prelist2) >=1:
                        brain.sdcard.appendfile(filename, bytearray(str(prelist2[0]) + str(prelist2[1]) + str(log.codes.get(prelist[2])), log.format))

class Log:
    def __init__(self):
        self.logging=Logging()
        self.recording=Recording()
        self.archive=Archive()
        self.index=0
        self.adding=True
        self.format="utf-8"
        # Predefined Log Codes dictionary
        self.codes={
                    "ED1": ":Drivetrain ERROR: Motor(s) Criticaly Hot. Temp: ",
                    "ED2": ":Drivetrain ERROR: Motor(s) Very High Power. Power: ",
                    "ED3": ":Drivetrain ERROR: Motor(s) Disconnected. Name: ",
                    "WD0": ":Drivetrain WARNING: Motor(s) Hot. Temp: ",
                    "WD1": ":Drivetrain WARNING: High Current Draw. Current: ",
                    "WD2": ":Drivetrain WARNING: Low Voltage. Voltage: ",
                    "WD3": ":Drivetrain WARNING: High Power. Power: ",
                    "DD0": ":Drivetrain Data: Velocity Changed. New Velocity: ",
                    "DD1": ":Drivetrain Data: Done Spinning.",
                    "EI0": ":Intake ERROR: No response from intake system.:",
                    "EI1": ":Intake ERROR: Motor Criticaly Hot. Temp: ",
                    "WI0": ":Intake WARNING: Motor Hot. Temp: ",
                    "WI1": ":Intake WARNING: High Current Draw. Current: ",
                    "WI2": ":Intake WARNING: High Voltage. Voltage: ",
                    "WI3": ":Intake WARNING: High Power. Power: ",
                    "DI0": ":Intake INFO: Done Spinning.:",
                    "DI1": ":Intake INFO: Velocity Changed. New Velocity: ",
                    "EB0": ":Battery ERROR: Critically Low Voltage. Voltage: ",
                    "EB1": ":Battery ERROR: Critically Low Battery. Capacity: ",
                    "EB2": ":Battery ERROR: Critically High Current. Current: ",
                    "WB0": ":Battery WARNING: Low Voltage. Voltage: ",
                    "WB1": ":Battery WARNING: Low Battery. capacity: ",
                    "EA0": ":Aton ERROR: No response from auton system.:",
                    "EA1": ":Aton ERROR: Inertial Sensor Failure.:",
                    "EA2": ":Aton ERROR: Move failed. Move:",
                    "WA0": ":Aton WARNING: Inertial Sensor Calibrating.:",
                    "WA1": ":Aton WARNING: Left Aton Missing.:",
                    "WA2": ":Aton WARNING: Right Aton Missing.:",
                    "DA0": ":Aton DATA: Recording Started.:",
                    "DA1": ":Aton DATA: Recording Stopped.:",
                    "DA2": ":Aton DATA: Recording Saved.:",
                    "DA3": ":Aton DATA: Recording Loaded.:",
                    "DA4": ":Aton DATA: Move Forward MM. MM: ",
                    "DA5": ":Aton DATA: Drive Left Degrees. Degrees: ",
                    "DA6": ":Aton DATA: Drive Right Degrees. Degrees: ",
                    "DA7": ":Aton DATA: Curved Move. Left Degrees: , Right Degrees: ",
                    "DA8": ":Aton DATA: Turn to Rotation. Degrees: ",
                    "DA9": ":Aton DATA: Turn Degrees. Degrees: ",
                    "DA10": ":Aton DATA: Loaded Right Aton from SD Card.:",
                    "DA11": ":Aton DATA: Loaded Left Aton from SD Card.:",
                    "DS0": ":System DATA: Init setup complete.:",
                    "DS1": ":System DATA: Driver Init setup complete.:",
                    "DS2": ":System DATA: Aton Init setup complete.:",
                    "EM0": ":Motor ERROR: Motor Criticaly Hot. Temp: ",
                    "EM1": ":Motor ERROR: Motor Disconnected. Name: ",
                    "EM2": ":Motor ERROR: Motor Very High Power. Power: ",
                    "WM0": ":Motor WARNING: Motor Hot. Temp: ",
                    "WM1": ":Motor WARNING: Motor High Power. Power: ",
                    "EE0": ":Exeption ERROR: Type Error. Problem in: ",
                    "EE1": ":Exeption ERROR: Value Error. Problem in: ",
                    "EE2": ":Exeption ERROR: Name Error. Problem in: ",
                    "EE3": ":Exeption ERROR: Exeption Used. Problem in: ",
                    "EE4": ":Exeption ERROR: Attribute Error. Problem in: ",
                    "DV0": ":Variable DATA: Variable Changed. Name: ",
                    "DC0": ":Controller DATA: Button Pressed. Button: ",
                    "DC1": ":Controller DATA: Axis Changed. Axis: ",
                }
        # Setting up Log Files if they dont exist 
        if brain.sdcard.is_inserted():
            if not brain.sdcard.exists("Log.csv"):
                brain.sdcard.savefile("Log.csv", bytearray("log Start: \n", self.format))

            if not brain.sdcard.exists("index.txt"):
                brain.sdcard.savefile("index.txt", bytearray("0", self.format))
            index_content=brain.sdcard.loadfile("index.txt")
            self.index=int(index_content.decode(self.format))
        else:
            self.index=0

    def add(self, add_code, add_details):
        if self.adding == True:
            print(", %s [%s] %s %s"%(self.index, log_time, self.codes.get(add_code), add_details))
            if brain.sdcard.is_inserted():
                brain.sdcard.appendfile("Log.csv", bytearray(", %s [%s] %s %s \n"%(self.index, log_time, self.codes.get(add_code), add_details), self.format))
                brain.sdcard.savefile("index.txt", bytearray("%d"%(self.index), self.format))
                if self.recording.record:
                    brain.sdcard.appendfile(self.recording.Aton, bytearray(", %s [%s] %s %s \n"%(self.index, log_time, self.codes.get(add_code), add_details), self.format))       
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
            brain.sdcard.savefile("Log.csv", bytearray("Log Start: \n", self.format))
            brain.sdcard.savefile("index.txt", bytearray("0", self.format))
        else:
            print("No SD Card Inserted Cannot Clear Log")
    
    # Displaying log codes dictionary
    def table(self):
        print(self.codes)

    def read(self):
        if brain.sdcard.is_inserted():
            log_content=brain.sdcard.loadfile("Log.csv")
            print(log_content.decode(self.format))
        else:
            print("No SD Card Inserted Cannot Read Log")


log=Log()
log.add_codes("DZ0", ":Colorsort DATA: detected red.:")
log.add_codes("DZ1", ":Colorsort DATA: detected blue.:")

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
            log.logging.controller(1, Right1)
        except Exception as e:
            log.add("EE3", "Controller Logging Thread: %s"%(e))
        
        try:
            log.logging.variable("Pusher", pusher_state)
            log.logging.variable("Loader", loader_state)
        except Exception as e:
                log.add("EE3", "Variable Logging Thread: %s"%(e))
        
        if 340 < optical_9.hue() <20:
            log.add("DC1", 0)
        elif 240 < optical_9.hue() < 260:
            log.add("DC0", 0)
        wait(50, MSEC)

log.archive.log()

log.add("DS0", 0)
Thread(logging_setup)

def rightside():
    rightspeed = controller_1.axis3.position() / 8.33
    Right1.spin(FORWARD, rightspeed, VOLT)
    Right2.spin(FORWARD, rightspeed, VOLT)
    Right3.spin(FORWARD, rightspeed, VOLT)

def leftside():
    leftspeed=controller_1.axis2.position()/8.33
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


def leftmove(leftspeed, degrees):
    left1.set_velocity(leftspeed, PERCENT)
    left1.spin_for(FORWARD, degrees, DEGREES)
    left2.set_velocity(leftspeed, PERCENT)
    left2.spin_for(FORWARD, degrees, DEGREES)
    left3.set_velocity(leftspeed, PERCENT)
    left3.spin_for(FORWARD, degrees, DEGREES)

def rightmove(rightspeed, degrees):
    Right1.set_velocity(rightspeed, PERCENT)
    Right1.spin_for(FORWARD, degrees, DEGREES)
    Right2.set_velocity(rightspeed, PERCENT)
    Right2.spin_for(FORWARD, degrees, DEGREES)
    Right3.set_velocity(rightspeed, PERCENT)
    Right3.spin_for(FORWARD, degrees, DEGREES)

def forwardmove(leftspeed, rightspeed, leftdegrees, rightdegrees):
    left1.set_velocity(leftspeed, PERCENT)
    left1.spin_for(FORWARD, leftdegrees, DEGREES)
    Right1.set_velocity(rightspeed, PERCENT)
    Right1.spin_for(FORWARD, rightdegrees, DEGREES)
    left2.set_velocity(leftspeed, PERCENT)
    left2.spin_for(FORWARD, leftdegrees, DEGREES)
    Right2.set_velocity(rightspeed, PERCENT)
    Right2.spin_for(FORWARD, rightdegrees, DEGREES)
    left3.set_velocity(leftspeed, PERCENT)
    left3.spin_for(FORWARD, leftdegrees, DEGREES)
    Right3.set_velocity(rightspeed, PERCENT)
    Right3.spin_for(FORWARD, rightdegrees, DEGREES)

def intakeupstart():
    Intake.spin(FORWARD)

def intakedownstart():
    Intake.spin(REVERSE)

def intakestop():
    Intake.stop()

def scoreupstart():
    Intake.spin(FORWARD)
    TopMotor.spin(FORWARD)

def scoredownstart():
    Intake.spin(REVERSE)
    TopMotor.spin(FORWARD)

def scorestop():
    Intake.stop()
    TopMotor.stop()

def recordright():
    global recording_state
    if recording_state == 0:
        log.recording.start("Right")
        controller_1.screen.clear_line(3)
        controller_1.screen.set_cursor(3,1)
        controller_1.screen.print("Right recording.")
        recording_state=1
    elif recording_state == 1:
        log.recording.stop("Right")
        log.recording.encode("Right", forwardmove, rightmove, leftmove, intakeupstart, intakestop, "R1", intakedownstart, intakestop, "R2", scoreupstart, scorestop, "L1", scoredownstart, scorestop, "L2", loadertoggle, loadertoggle, "B", pushertoggle, pushertoggle, "DOWN")
        controller_1.screen.clear_line(3)
        controller_1.screen.set_cursor(3,1)
        controller_1.screen.print("Right Stopped.")
        recording_state=0

controller_1.axis2.changed(rightside)
controller_1.axis3.changed(leftside)
controller_1.buttonR1.pressed(intakeup)
controller_1.buttonR2.pressed(intakedown)
controller_1.buttonL1.pressed(scoreup)
controller_1.buttonL2.pressed(scoredown)
controller_1.buttonDown.pressed(pushertoggle)
controller_1.buttonB.pressed(loadertoggle)
controller_1.buttonRight.pressed(recordright)