# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       CLEAR.py                                                     #
# 	Author:       Micah Bow                                                    #
# 	Created:      1/27/2026, 12:42 PM                                          #
#   Last Edited:  2/23/2026, 10:00 PM                                          #
# 	Description:  Capture, Logging, Encoding, Archiving, Recording.            #
#                                                                              #
# ---------------------------------------------------------------------------- #


from vex import *

# Timer for log time
brain=Brain()
log_time= Timer()
timer=Timer()
controller_1=Controller(PRIMARY)
controller_2=Controller(PARTNER)
pusher_state = 0
loader_state = 0
record = False
controlleraxis2positionhistory = 0
controlleraxis3positionhistory = 0
recording_state=0

def none():
    return(none)

class Drivetrain:
    def __init__(self):
        # Sets used for tracking of the drivetrain.
        self.drivetrain_temp_monitoring={}
        self.drivetrain_power_monitoring={}
        self.drivetrain_disconnected={}
    
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
        
        # Cheaks for the temps,  power, and cheaks for conecttions of the drivetrain.
        if (right_motor.temperature()>70 or left_motor.temperature()>70) and (temp_state==0 or temp_state==2):
            log.add("ED1", "Temp %s"%(max(right_motor.temperature(), left_motor.temperature())))
            self.drivetrain_temp_monitoring['pair'] = 1
        elif (right_motor.temperature()>50 or left_motor.temperature()>50) and (temp_state==0 or temp_state==1):
            log.add("WD0", "Temp %s"%(max(right_motor.temperature(), left_motor.temperature())))
            self.drivetrain_temp_monitoring['pair'] = 2
        elif right_motor.temperature()<=50 and left_motor.temperature()<=50 and (temp_state==1 or temp_state==2):
            self.drivetrain_temp_monitoring['pair'] = 0
        
        if right_motor.power(PowerUnits.WATT)>40 or left_motor.power(PowerUnits.WATT)>40 and (power_state==0 or power_state==2):
            log.add("ED3", "Power %s"%(max(right_motor.power(PowerUnits.WATT), left_motor.power(PowerUnits.WATT))))
            self.drivetrain_power_monitoring['pair'] = 1
        elif right_motor.power(PowerUnits.WATT)>30 or left_motor.power(PowerUnits.WATT)>30 and (power_state==0 or power_state==1):
            log.add("WD3", "Power %s"%(max(right_motor.power(PowerUnits.WATT), left_motor.power(PowerUnits.WATT))))
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
        
        # Cheaks for the temps,  power, and cheaks for conecttions of the drivetrain.
        if (front_left_motor.temperature()>70 or front_right_motor.temperature()>70 or back_left_motor.temperature()>70 or back_right_motor.temperature()>70) and (temp_state==0 or temp_state==2):
            log.add("ED1", "Temp %s"%(max(front_left_motor.temperature(), front_right_motor.temperature(), back_left_motor.temperature(), back_right_motor.temperature())))
            self.drivetrain_temp_monitoring['four_motor']=1
        elif (front_left_motor.temperature()>50 or front_right_motor.temperature()>50 or back_left_motor.temperature()>50 or back_right_motor.temperature()>50) and (temp_state==0 or temp_state==1):
            log.add("WD0", "Temp %s"%(max(front_left_motor.temperature(), front_right_motor.temperature(), back_left_motor.temperature(), back_right_motor.temperature())))
            self.drivetrain_temp_monitoring['four_motor']=2
        elif (front_left_motor.temperature()<=50 and front_right_motor.temperature()<=50 and back_left_motor.temperature()<=50 and back_right_motor.temperature()<=50) and (temp_state==1 or temp_state==2):
            self.drivetrain_temp_monitoring['four_motor']=0
        
        if front_left_motor.power(PowerUnits.WATT)>40 or front_right_motor.power(PowerUnits.WATT)>40 or back_left_motor.power(PowerUnits.WATT)>40 or back_right_motor.power(PowerUnits.WATT)>40 and (power_state==0 or power_state==2):
            log.add("ED3", "Power %s"%(max(front_left_motor.power(PowerUnits.WATT), front_right_motor.power(PowerUnits.WATT), back_left_motor.power(PowerUnits.WATT), back_right_motor.power(PowerUnits.WATT))))
            self.drivetrain_power_monitoring['four_motor']=1
        elif front_left_motor.power(PowerUnits.WATT)>30 or front_right_motor.power(PowerUnits.WATT)>30 or back_left_motor.power(PowerUnits.WATT)>30 or back_right_motor.power(PowerUnits.WATT)>30 and (power_state==0 or power_state==1):  
            log.add("WD3", "Power %s"%(max(front_left_motor.power(PowerUnits.WATT), front_right_motor.power(PowerUnits.WATT), back_left_motor.power(PowerUnits.WATT), back_right_motor.power(PowerUnits.WATT))))
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
        #speed=timer.time()
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
        
        # Cheaks for the temps,  power, and cheaks for conecttions of the drivetrain.
        if (front_left_motor.temperature(PERCENT)>70 or front_right_motor.temperature(PERCENT)>70 or middle_left_motor.temperature(PERCENT)>70 or middle_right_motor.temperature(PERCENT)>70 or back_left_motor.temperature(PERCENT)>70 or back_right_motor.temperature(PERCENT)>70) and (temp_state==0 or temp_state==2):
            log.add("ED1", "Temp %s"%(max(front_left_motor.temperature(PERCENT), front_right_motor.temperature(PERCENT), middle_left_motor.temperature(PERCENT), middle_right_motor.temperature(PERCENT), back_left_motor.temperature(PERCENT), back_right_motor.temperature(PERCENT))))
            self.drivetrain_temp_monitoring['six_motor']=1
        elif (front_left_motor.temperature(PERCENT)>50 or front_right_motor.temperature(PERCENT)>50 or middle_left_motor.temperature(PERCENT)>50 or middle_right_motor.temperature(PERCENT)>50 or back_left_motor.temperature(PERCENT)>50 or back_right_motor.temperature(PERCENT)>50) and (temp_state==0 or temp_state==1):
            log.add("WD0", "Temp %s"%(max(front_left_motor.temperature(PERCENT), front_right_motor.temperature(PERCENT), middle_left_motor.temperature(PERCENT), middle_right_motor.temperature(PERCENT), back_left_motor.temperature(PERCENT), back_right_motor.temperature(PERCENT))))
            self.drivetrain_temp_monitoring['six_motor']=2
        elif (front_left_motor.temperature(PERCENT)<=50 and front_right_motor.temperature(PERCENT)<=50 and middle_left_motor.temperature(PERCENT)<=50 and middle_right_motor.temperature(PERCENT)<=50 and back_left_motor.temperature(PERCENT)<=50 and back_right_motor.temperature(PERCENT)<=50) and (temp_state==1 or temp_state==2):
            self.drivetrain_temp_monitoring['six_motor']=0
        
        if front_left_motor.power(PowerUnits.WATT)>40 or front_right_motor.power(PowerUnits.WATT)>40 or middle_left_motor.power(PowerUnits.WATT)>40 or middle_right_motor.power(PowerUnits.WATT)>40 or back_left_motor.power(PowerUnits.WATT)>40 or back_right_motor.power(PowerUnits.WATT)>40 and (power_state==0 or power_state==2):
            log.add("ED3", "Power %s"%(max(front_left_motor.power(PowerUnits.WATT), front_right_motor.power(PowerUnits.WATT), middle_left_motor.power(PowerUnits.WATT), middle_right_motor.power(PowerUnits.WATT), back_left_motor.power(PowerUnits.WATT), back_right_motor.power(PowerUnits.WATT))))
            self.drivetrain_power_monitoring['six_motor']=1
        elif front_left_motor.power(PowerUnits.WATT)>30 or front_right_motor.power(PowerUnits.WATT)>30 or middle_left_motor.power(PowerUnits.WATT)>30 or middle_right_motor.power(PowerUnits.WATT)>30 or back_left_motor.power(PowerUnits.WATT)>30 or back_right_motor.power(PowerUnits.WATT)>30 and (power_state==0 or power_state==1):  
            log.add("WD3", "Power %s"%(max(front_left_motor.power(PowerUnits.WATT), front_right_motor.power(PowerUnits.WATT), middle_left_motor.power(PowerUnits.WATT), middle_right_motor.power(PowerUnits.WATT), back_left_motor.power(PowerUnits.WATT), back_right_motor.power(PowerUnits.WATT))))
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
        #print(str(timer.time() - speed) + " Drivetrain Time")


# capture for the log class
class Capture:

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
        global record
    
    def motor(self, motor):
        #speed=timer.time()
        motor_id = id(motor) 
        
        # Initialize tracking
        if motor_id not in self.motor_temp_monitoring:
            self.motor_temp_monitoring[motor_id] = 0
        if motor_id not in self.motor_power_monitoring:
            self.motor_power_monitoring[motor_id] = 0
        if motor_id not in self.motor_disconnected:
            self.motor_disconnected[motor_id] = 0
        
        # Cheaks for the temps,  power, and cheaks for conecttions of motors(s).
        if motor.temperature()>70 and (self.motor_temp_monitoring[motor_id]==0 or self.motor_temp_monitoring[motor_id]==2):
            log.add("EM0", "Motor %s Temp %s"%(motor, motor.temperature(PERCENT)))
            self.motor_temp_monitoring[motor_id]=1
        elif motor.temperature()>50 and (self.motor_temp_monitoring[motor_id]==0 or self.motor_temp_monitoring[motor_id]==1):
            log.add("WM0", "Motor %s Temp %s"%(motor, motor.temperature(PERCENT)))
            self.motor_temp_monitoring[motor_id]=2
        elif motor.temperature()<=50 and (self.motor_temp_monitoring[motor_id]==2 or self.motor_temp_monitoring[motor_id]==1):
            self.motor_temp_monitoring[motor_id]=0
        
        if motor.power(PowerUnits.WATT)>40 and (self.motor_power_monitoring[motor_id]==0 or self.motor_power_monitoring[motor_id]==2):
            log.add("EM2", "Motor %s Power %s"%(motor, motor.power(PowerUnits.WATT)))
            self.motor_power_monitoring[motor_id]=1
        elif motor.power(PowerUnits.WATT)>30 and (self.motor_power_monitoring[motor_id]==0 or self.motor_power_monitoring[motor_id]==1):
            log.add("WM1", "Motor %s Power %s"%(motor, motor.power(PowerUnits.WATT)))
            self.motor_power_monitoring[motor_id]=2
        elif motor.power(PowerUnits.WATT)<=30 and (self.motor_power_monitoring[motor_id]==1 or self.motor_power_monitoring[motor_id]==2):
            self.motor_power_monitoring[motor_id]=0
        
        if motor.temperature(PERCENT)==2 and self.motor_disconnected[motor_id]==0:
            log.add("EM1", "Motor %s Disconnected"%(motor))
            self.motor_disconnected[motor_id]=1
        
        if motor.temperature(PERCENT)!=2 and self.motor_disconnected[motor_id]==1:
            self.motor_disconnected[motor_id]=0
        #print(str(timer.time() - speed) + " Motor Time")

    def battery(self):
        #speed=timer.time()
        # Battery monitoring for voltage, capacity, and current.
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
        #print(str(timer.time() - speed) + " Battery Time")
    
    def controller(self, controller, monitormotor1=Motor(Ports.PORT1, GearSetting.RATIO_18_1, False), monitormotor2=Motor(Ports.PORT1, GearSetting.RATIO_18_1, False), monitormotor3=Motor(Ports.PORT1, GearSetting.RATIO_18_1, False), monitormotor4=Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)):
        #speed=timer.time()
        # controller assignment
        if controller==1:
            Controller=controller_1
        elif controller==2:
            Controller=controller_2

        
        if not log.recording.record or not record: # Only logs when not recoding to save space on the recording file.
            if Controller.axis1.position()!=0 and self.axis1 != Controller.axis1.position():
                degrees=monitormotor1.position(DEGREES)
                monitormotor1.set_position(0, DEGREES)
                log.add("DC1", "Controller_%d_Axis1 %d Moved %d Degrees"%(controller, Controller.axis1.position(), degrees))
                self.axis1=Controller.axis1.position()
            elif 0 == Controller.axis1.position() and self.axis1!=0:
                degrees=monitormotor1.position(DEGREES)
                monitormotor1.set_position(0, DEGREES)
                #log.add("DC1", "Controller_%d_Axis1 %d Moved %d Degrees"%(controller, self.axis1, degrees))
                log.add("DC1", "Controller_%d_Axis1 %d Moved %d Degrees"%(controller, 0, 0))
                self.axis1=0

        if Controller.axis2.position()!=0 and self.axis2 != Controller.axis2.position():
            #speed=timer.time()
            degrees=monitormotor2.position(DEGREES)
            monitormotor2.set_position(0, DEGREES)
            log.add("DC1", "Controller_%d_Axis2 %d Moved %d Degrees"%(controller, Controller.axis2.position(), degrees))
            self.axis2=Controller.axis2.position()
            #print(str(timer.time() - speed) + " Controller Time")
        elif 0 == Controller.axis2.position() and self.axis2!=0:
            #speed=timer.time()
            degrees=monitormotor2.position(DEGREES)
            monitormotor2.set_position(0, DEGREES)
            #log.add("DC1", "Controller_%d_Axis2 %d Moved %d Degrees"%(controller, self.axis2, degrees))
            log.add("DC1", "Controller_%d_Axis2 %d Moved %d Degrees"%(controller, 0, 0))
            self.axis2=0
            #print(str(timer.time() - speed) + " Controller Time")

        if Controller.axis3.position()!=0 and self.axis3 != Controller.axis3.position():
            degrees=monitormotor3.position(DEGREES)
            monitormotor3.set_position(0, DEGREES)
            log.add("DC1", "Controller_%d_Axis3 %d Moved %d Degrees"%(controller, Controller.axis3.position(), degrees))
            self.axis3=Controller.axis3.position()
        elif 0 == Controller.axis3.position() and self.axis3!=0:
            degrees=monitormotor3.position(DEGREES)
            monitormotor3.set_position(0, DEGREES)
            #log.add("DC1", "Controller_%d_Axis3 %d Moved %d Degrees"%(controller, self.axis3, degrees))
            log.add("DC1", "Controller_%d_Axis3 %d Moved %d Degrees"%(controller, 0, 0))
            self.axis3=0

        if not log.recording.record or not record:
            if Controller.axis4.position()!=0 and self.axis4 != Controller.axis4.position():
                degrees=monitormotor4.position(DEGREES)
                monitormotor4.set_position(0, DEGREES)
                log.add("DC1", "Controller_%d_Axis4 %d Moved %d Degrees"%(controller, Controller.axis4.position(), degrees))
                self.axis4=Controller.axis4.position()
            elif 0 == Controller.axis4.position() and self.axis4!=0:
                degrees=monitormotor4.position(DEGREES)
                monitormotor4.set_position(0, DEGREES)
                #log.add("DC1", "Controller_%d_Axis4 %d Moved %d Degrees"%(controller, self.axis4, degrees))
                log.add("DC1", "Controller_%d_Axis4 %d Moved %d Degrees"%(controller, 0, 0))
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
        
        #print(str(timer.time() - speed) + " Controller Time")

    def variable(self, name, value):
        #speed=timer.time()
        valueid=id(name)
        if valueid not in self.variables:
            self.variables[valueid]=0
        if value != self.variables[valueid]:
            log.add("DV0", "Variable %s Value %s"%(name, value))
            self.variables[valueid] = value
        #print(str(timer.time() - speed) + " Variable Time")

class Recording:
    def __init__(self):
        self.record=False
        self.timerecord=0
        self.posttimerecord=0
        self.Aton=""
        self.postlist=[]
        self.File=""
        self.poststring=""      
        global record


    def start(self, Aton):
        global record
        filename=str(Aton) + "_pre.txt"
        if self.record == False:
            self.record= True
            record=True
            brain.sdcard.savefile(filename, bytearray("\n", log.format))
            self.Aton=Aton + "_pre.txt"
            log.add("DA0", filename)

    def stop(self, Aton):
        global record
        
        filename=str(Aton) + "_pre.txt"
        preatonfile=""
        self.record=False
        record=False
        try:
            log.unloadcache()
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
        except MemoryError:
            preatonfile=""
            with open(filename, 'r') as f:
                for line in f:
                    prelist=line.split(' ')
                if len(prelist) >= 3:
                    if prelist[3] == ":Controller":
                        brain.sdcard.appendfile(filename, bytearray(str(prelist) + "\n", log.format))

        log.add("DA1", filename)

    def encode(self, Aton, right, left, other1start=none, other1stop=none, other1button=none, other2start=none, other2stop=none, other2button=none, other3start=none, other3stop=none, other3button=none, other4start=none, other4stop=none, other4button=none, other5start=none, other5stop=none, other5button=none, other6start=none, other6stop=none, other6button=none):
        global record   
        filename=Aton + ".txt"
        self.record=False
        record=False
        brain.sdcard.savefile(filename)
        prelist=[]
        left=str(left).split(' ')
        right=str(right).split(' ')
        other1start=str(other1start).split(' ')
        other2start=str(other2start).split(' ')
        other3start=str(other3start).split(' ')
        other4start=str(other4start).split(' ')
        other5start=str(other5start).split(' ')
        other6start=str(other6start).split(' ')
        other1stop=str(other1stop).split(' ')
        other2stop=str(other2stop).split(' ')
        other3stop=str(other3stop).split(' ')
        other4stop=str(other4stop).split(' ')
        other5stop=str(other5stop).split(' ')
        other6stop=str(other6stop).split(' ')
        try:
            preatonfile=brain.sdcard.loadfile(Aton + "_pre.txt")
            preatonlist=preatonfile.decode(log.format).split("\n")
            for i in range(len(preatonlist)):
                prelist=str(preatonlist[i]).split(',')
                try:
                    prelist2=str(preatonlist[i+1]).split(',')
                except IndexError:
                    pass
                if len(prelist)>=12:
                    if "Controller" in str(prelist):
                        print("found controller")
                        if "Axis" in str(prelist):
                            print("found axis")
                            if "Controller_1_Axis3" in str(prelist):
                                brain.sdcard.appendfile(filename, bytearray("%s(%s, %s), "%(str(left[1]), str(prelist[11]).replace("'", ''), str(prelist[13]).replace("'", '')), log.format))
                            elif "Controller_1_Axis2" in str(prelist):
                                brain.sdcard.appendfile(filename, bytearray("%s(%s, %s), "%(str(right[1]), str(prelist[11]).replace("'", ''), str(prelist[13]).replace("'", '')), log.format))

                        elif "Button" in str(prelist):
                            print("found button")
                            if "Released" in str(prelist):
                                if other1button in str(prelist[11]):
                                    brain.sdcard.appendfile(filename, bytearray(str(other1stop[1]) + '(), ', log.format))
                                elif other2button in str(prelist[11]):
                                    brain.sdcard.appendfile(filename, bytearray(str(other2stop[1]) + '(), ', log.format))
                                elif other3button in str(prelist[11]):
                                    brain.sdcard.appendfile(filename, bytearray(str(other3stop[1]) + '(), ', log.format))
                                elif other4button in str(prelist[11]):
                                    brain.sdcard.appendfile(filename, bytearray(str(other4stop[1]) + '(), ', log.format))
                                elif other5button in str(prelist[11]):
                                    brain.sdcard.appendfile(filename, bytearray(str(other5stop[1]) + '(), ', log.format))
                                elif other6button in str(prelist[11]):
                                    brain.sdcard.appendfile(filename, bytearray(str(other6stop[1]) + '(), ', log.format))
                            elif "Pressed" in str(prelist):
                                if other1button in str(prelist[11]):
                                    brain.sdcard.appendfile(filename, bytearray(str(other1start[1]) + '(), ', log.format))
                                elif other2button in str(prelist[11]):
                                    brain.sdcard.appendfile(filename, bytearray(str(other2start[1]) + '(), ', log.format))
                                elif other3button in str(prelist[11]):
                                    brain.sdcard.appendfile(filename, bytearray(str(other3start[1]) + '(), ', log.format))
                                elif other4button in str(prelist[11]):
                                    brain.sdcard.appendfile(filename, bytearray(str(other4start[1]) + '(), ', log.format))
                                elif other5button in str(prelist[11]):
                                    brain.sdcard.appendfile(filename, bytearray(str(other5start[1]) + '(), ', log.format))
                                elif other6button in str(prelist[11]):
                                    brain.sdcard.appendfile(filename, bytearray(str(other6start[1]) + '(), ', log.format))
                        
                        if len(prelist2) >= 3:
                            brain.sdcard.appendfile(filename, bytearray("wait(" + str(abs(int(prelist[3].replace("[", '').replace("]", '').replace("'", '').replace("'", '')) - int(prelist2[3].replace("[", '').replace("]", '').replace("'", '').replace("'", '')))) + ", MSEC), ", log.format))
        except MemoryError: # If the preatonfile is too big to load into memory, it will read the file line by line and write to the new file.
            preatonlist=[]
            with open(Aton + "_pre.txt", 'r') as f:
                for line in f:
                    prelist=str(line).split(' ')
                    print(prelist)
                    try:
                        prelist2=str(next(f)).split(' ')
                    except StopIteration:
                        prelist2=[]
                    if len(prelist)>=12:
                        if "Controller" in str(prelist):
                            print("found controller")
                            if "Axis" in str(prelist):
                                print("found axis")
                                if "Controller_1_Axis3" in str(prelist):
                                    brain.sdcard.appendfile(filename, bytearray("%s(%s, %s), "%(str(left[1]), str(prelist[10]).replace("'", ''), str(prelist[12]).replace("'", '')), log.format))
                                elif "Controller_1_Axis2" in str(prelist):
                                    brain.sdcard.appendfile(filename, bytearray("%s(%s, %s), "%(str(right[1]), str(prelist[10]).replace("'", ''), str(prelist[12]).replace("'", '')), log.format))

                            elif "Button" in str(prelist):
                                print("found button")
                                if "Released" in str(prelist):
                                    if other1button in str(prelist[11]):
                                        brain.sdcard.appendfile(filename, bytearray(str(other1stop[1]) + '(), ', log.format))
                                    elif other2button in str(prelist[11]):
                                        brain.sdcard.appendfile(filename, bytearray(str(other2stop[1]) + '(), ', log.format))
                                    elif other3button in str(prelist[11]):
                                        brain.sdcard.appendfile(filename, bytearray(str(other3stop[1]) + '(), ', log.format))
                                    elif other4button in str(prelist[11]):
                                        brain.sdcard.appendfile(filename, bytearray(str(other4stop[1]) + '(), ', log.format))
                                    elif other5button in str(prelist[11]):
                                        brain.sdcard.appendfile(filename, bytearray(str(other5stop[1]) + '(), ', log.format))
                                    elif other6button in str(prelist[11]):
                                        brain.sdcard.appendfile(filename, bytearray(str(other6stop[1]) + '(), ', log.format))
                                elif "Pressed" in str(prelist):
                                    if other1button in str(prelist[11]):
                                        brain.sdcard.appendfile(filename, bytearray(str(other1start[1]) + '(), ', log.format))
                                    elif other2button in str(prelist[11]):
                                        brain.sdcard.appendfile(filename, bytearray(str(other2start[1]) + '(), ', log.format))
                                    elif other3button in str(prelist[11]):
                                        brain.sdcard.appendfile(filename, bytearray(str(other3start[1]) + '(), ', log.format))
                                    elif other4button in str(prelist[11]):
                                        brain.sdcard.appendfile(filename, bytearray(str(other4start[1]) + '(), ', log.format))
                                    elif other5button in str(prelist[11]):
                                        brain.sdcard.appendfile(filename, bytearray(str(other5start[1]) + '(), ', log.format))
                                    elif other6button in str(prelist[11]):
                                        brain.sdcard.appendfile(filename, bytearray(str(other6start[1]) + '(), ', log.format))
                            
                            if len(prelist2) >= 3:
                                print(prelist[2].replace("[", '').replace("]", '').replace("'", '').replace("'", ''))
                                print(prelist2[2].replace("[", '').replace("]", '').replace("'", '').replace("'", ''))
                                brain.sdcard.appendfile(filename, bytearray("wait(" + str(abs(int(prelist[2].replace("[", '').replace("]", '').replace("'", '').replace("'", '').replace(",", '')) - int(prelist2[2].replace("[", '').replace("]", '').replace("'", '').replace("'", '').replace(",", '')))) + ", MSEC), ", log.format))
        log.add("DA2", filename)
        print("Encode done.")            
                        
    
    def run(self, Aton):
        log.add("DA3", Aton + ".txt")
        try:
            Atonfile=brain.sdcard.loadfile(Aton + ".txt")
            exec(Atonfile.decode(log.format))
        except MemoryError:
            with open(Aton + ".txt", 'r') as f:
                for line in f:
                    for item in line.split(','):
                        item = item.strip()
                        if item:
                            exec(item)

class Archive:
    def __init__(self):
        self.format="utf-8"
        logfile=""
        loglist=[]
    
    def log(self):
        speed=timer.time()
        archivelist=""
        try:
            log.adding=False
            reversecodes={value: key for key, value in log.codes.items()}
            logfile=brain.sdcard.loadfile("Log.csv").decode(log.format)
            loglist=logfile.split("\n")
            for i in range(len(loglist)):
                logline=loglist[i].split(':')
                if len(logline)>=4:
                    loglines= ":" + str(logline[1]) + ":" + str(logline[2]) + ": "
                    archivelist=archivelist + str(logline[0]) + str(reversecodes.get(loglines)) + str(logline[3]) + '\n'
            brain.sdcard.appendfile("loghistory.txt", bytearray(archivelist, log.format))
            logfile=""
            log.clear()
            log.adding=True
        except MemoryError: # If the log file is too big to load into memory, it will read the file line by line and write to the new file.
            log.adding=False
            reversecodes={value: key for key, value in log.codes.items()}
            with open("Log.csv", 'r') as file:
                for line in file:
                    speed2=timer.time()
                    logline=line.split(':')
                    if len(logline)>=4:
                        loglines= ":" + str(logline[1]) + ":" + str(logline[2]) + ": "
                        brain.sdcard.appendfile("loghistory.txt", bytearray(str(logline[0]) + str(reversecodes.get(loglines)) + str(logline[3]) + '\n', log.format))
                    print("Archiving took: " + str(timer.time() - speed2) + " MSEC")
            log.clear()
            log.adding=True
        print("Archive took: " + str(timer.time() - speed) + " MSEC")

    
    def recording(self, name):
        try:
            archname=(name - ".txt") + "history.txt"
            reversecodes={value: key for key, value in log.codes.items()}
            self.file=brain.sdcard.loadfile(name).decode(log.format)
            self.list=self.file.split("\n")
            for i in range(len(self.list)):
                line=self.list[i].split(':')
                if len(line)>=3:
                    lines= ":" + str(line[1]) + ":" + str(line[2]) + ": "
                    brain.sdcard.appendfile(archname, bytearray(str(reversecodes.get(lines)) + str(line[0]), log.format))
            logfile=""
            brain.sdcard.savefile(name)
        except MemoryError: # Same thing as the last two exceptions.
            self.file=""
            archname=(name - ".txt") + "history.txt"
            reversecodes={value: key for key, value in log.codes.items()}
            with open(name, 'r') as self.file:
                for line in self.file:
                    logline=line.split(':')
                    loglines= str(logline[1]) + str(logline[2])
                    brain.sdcard.appendfile(archname, bytearray(str(reversecodes.get(loglines)) + str(logline[0]), log.format))                        
            brain.sdcard.savefile(name)
    
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
        except MemoryError: # Same thing as the last three exceptions.
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
        self.capture=Capture()
        self.recording=Recording()
        self.archive=Archive()
        self.index=0
        self.adding=True
        self.format="utf-8"
        self.cache=""
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
        
        log_lines=[]
        loghistory_lines=[]
        log_number=0
        if not brain.sdcard.exists("Log.csv"):
            brain.sdcard.savefile("Log.csv", bytearray("log Start: \n", self.format))
            self.index=0
        else:
            try:
                log_lines=brain.sdcard.loadfile("Log.csv").decode(self.format).split("\n")
            except MemoryError: # If the log file is too big to load into memory, it will read the file line by line and count the number of lines to set the index.
                print("Log.csv cannot be decoded.")
                log_lines=[]
                with open("Log.csv", 'r') as log_file:
                    for line in log_file:
                        log_number+=1
                print("Log done")
            except OSError: # same as the memory error but for an os error that works the same way.
                print("Log.csv cannot be decoded trying step open.")
                log_lines=[]
                with open("Log.csv", 'r') as log_file:
                    for line in log_file:
                        log_number+=1
                print("Log done")
            if not brain.sdcard.exists("loghistory.txt"):
                brain.sdcard.savefile("loghistory.txt", bytearray("", self.format))                   
            else:
                try:
                    loghistory_lines=brain.sdcard.loadfile("loghistory.txt").decode(self.format).split("\n")
                except MemoryError: # If the log history file is too big to load into memory, it will read the file line by line and count the number of lines to set the index.
                    print("loghistory.txt cannot be decoded.")
                    loghistory_lines=[]
                    with open("loghistory.txt", 'r') as loghistory_file:
                        for line in loghistory_file:
                            log_number+=1
                    print("loghistory done")
                except OSError: # same as the memory error but for an os error that works the same way.
                    print("loghistory.txt cannot be decoded trying step open.")
                    loghistory_lines=[]
                    with open("loghistory.txt", 'r') as loghistory_file:
                        for line in loghistory_file:
                            log_number+=1
                    print("loghistory done")
            self.index=len(log_lines) + len(loghistory_lines) + log_number - 1
            log_lines=[]
            loghistory_lines=[]
            log_number=0

    def unloadcache(self): # this is only ment for the recording.
        if self.cache!="":
            brain.sdcard.appendfile(self.recording.Aton, bytearray(self.cache, self.format))
            brain.sdcard.appendfile("Log.csv", bytearray(self.cache, self.format))
            self.cache=""
            print("Unloaded cache")

    def add(self, add_code, add_details):
        global record
        if not self.adding:
            return

        entry = ", %s [%s] %s %s \n" % (self.index, log_time, self.codes.get(add_code), add_details)       
        print(entry)
        if self.recording.record:
            self.cache += entry
            #print(self.cache)
            #print("Added to cache: " + str(self.index) + " Cache input: " + entry)
        else:
            if self.cache: #checks if cache has things in it.
                brain.sdcard.appendfile("Log.csv", bytearray(self.cache, self.format))
                self.cache = ""
            brain.sdcard.appendfile("Log.csv", bytearray(entry, self.format))
            #print("Added to log: " + str(self.index))

        self.index += 1
        
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
        brain.sdcard.savefile("Log.csv", bytearray("Log Start: \n", self.format))
    
    # Displaying log codes dictionary
    def table(self):
        print(self.codes)

    def read(self):
        log_content=brain.sdcard.loadfile("Log.csv")
        print(log_content.decode(self.format))
    
    def logstart(self, Right1, Left1, Right2=None, Left2=None, Right3=None, Left3=None, motor1=None, motor2=None, motor3=None, motor4=None, motor5=None, motor6=None, variable1=None, variable1name="", variable2=None, variable2name="", variable3=None, variable3name="", variable4=None, variable4name="", variable5=None, variable5name="", variable6=None, variable6name=""):
        while True:
            for i in range(200):
                global record
                self.capture.battery()
                self.capture.controller(1, Right1, Right1, Left1, Left1)
                if Right2==None and Left2==None and Right3==None and Left3==None:
                    self.capture.drivetrain.two_motor(Right1, Left1)
                elif Right3==None and Left3==None:
                    self.capture.drivetrain.four_motor(Right1, Left1, Right2, Left2)
                elif Right3!=None and Left3!=None:
                    self.capture.drivetrain.six_motor(Right1, Left1, Right2, Left2, Right3, Left3)

                if motor1!=None:
                    self.capture.motor(motor1)

                if motor2!=None:
                    self.capture.motor(motor2)

                if motor3!=None:
                    self.capture.motor(motor3)

                if motor4!=None:
                    self.capture.motor(motor4)

                if motor5!=None:
                    self.capture.motor(motor5)

                if motor6!=None:
                    self.capture.motor(motor6)

                if variable1!=None:
                    self.capture.variable(variable1name, variable1)

                if variable2!=None:
                    self.capture.variable(variable2name, variable2)

                if variable3!=None:
                    self.capture.variable(variable3name, variable3)

                if variable4!=None:
                    self.capture.variable(variable4name, variable4)

                if variable5!=None:
                    self.capture.variable(variable5name, variable5)

                if variable6!=None:
                    self.capture.variable(variable6name, variable6)

                if self.recording.record==False:
                    wait(200, MSEC)
                else:
                    record=True
                    pass
            print(self.cache)
            self.unloadcache()

log=Log()



