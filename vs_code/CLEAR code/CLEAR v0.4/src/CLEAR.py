# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       CLEAR.py                                                     #
# 	Author:       Micah Bow                                                    #
# 	Created:      1/27/2026, 12:42 PM                                          #
#   Last Edited:  3/14/2026, 2:00 PM                                           #
# 	Description:  Capture, Logging, Encoding, Archiving, Recording.            #
#                                                                              #
# ---------------------------------------------------------------------------- #


from vex import *

brain=Brain()
log_time= Timer()

def none():
    pass

class Drivetrain:
    def __init__(self):
        # Sets used for tracking of the drivetrain.
        self.drivetrain_temp_monitoring={}
        self.drivetrain_power_monitoring={}
        self.drivetrain_disconnected={}
        self.drivetrain_current_monitoring={}
    
    def two_motor(self, left_motor, right_motor):
        left_id = id(left_motor)
        right_id = id(right_motor)
        
        # Initialize tracking
        for motor_id in [left_id, right_id]:
            if motor_id not in self.drivetrain_temp_monitoring:
                self.drivetrain_temp_monitoring[motor_id] = 0
            if motor_id not in self.drivetrain_power_monitoring:
                self.drivetrain_power_monitoring[motor_id] = 0
            if motor_id not in self.drivetrain_current_monitoring:
                self.drivetrain_power_monitoring[motor_id] = 0
            if motor_id not in self.drivetrain_disconnected:
                self.drivetrain_disconnected[motor_id] = 0
        
        temp_state = self.drivetrain_temp_monitoring.get('pair', 0)
        power_state = self.drivetrain_power_monitoring.get('pair', 0)
        current_state= self.drivetrain_current_monitoring.get('pair', 0)
        
        # Cheaks for the temps,  power, and cheaks for conecttions of the drivetrain.
        if (right_motor.temperature()>70 or left_motor.temperature()>70) and (temp_state==0 or temp_state==2):
            log.add("ED1", "Temp %s"%(max(right_motor.temperature(), left_motor.temperature())))
            self.drivetrain_temp_monitoring['pair'] = 1
        elif (right_motor.temperature()>50 or left_motor.temperature()>50) and (temp_state==0):
            log.add("WD0", "Temp %s"%(max(right_motor.temperature(), left_motor.temperature())))
            self.drivetrain_temp_monitoring['pair'] = 2
        elif right_motor.temperature()<=50 and left_motor.temperature()<=50 and (temp_state==1 or temp_state==2):
            log.add("WD0", "Temp %s"%(max(right_motor.temperature(), left_motor.temperature())))
            self.drivetrain_temp_monitoring['pair'] = 0
        
        if (right_motor.power(PowerUnits.WATT)>20 or left_motor.power(PowerUnits.WATT)>20) and (power_state==0 or power_state==2):
            log.add("ED2", "Power %s"%(max(right_motor.power(PowerUnits.WATT), left_motor.power(PowerUnits.WATT))))
            self.drivetrain_power_monitoring['pair'] = 1
        elif (right_motor.power(PowerUnits.WATT)>12 or left_motor.power(PowerUnits.WATT)>12) and (power_state==0):
            log.add("WD1", "Power %s"%(max(right_motor.power(PowerUnits.WATT), left_motor.power(PowerUnits.WATT))))
            self.drivetrain_power_monitoring['pair'] = 2
        elif right_motor.power(PowerUnits.WATT)<=12 and left_motor.power(PowerUnits.WATT)<=12 and (power_state==1 or power_state==2):
            log.add("DD1", "Power %s"%(max(right_motor.power(PowerUnits.WATT), left_motor.power(PowerUnits.WATT))))
            self.drivetrain_power_monitoring['pair'] = 0

        if (left_motor.current(CurrentUnits.AMP)>2 or right_motor.current(CurrentUnits.AMP)>2) and (current_state==0 or current_state==2):
            log.add("ED4", " %s"%(max(left_motor.current(CurrentUnits.AMP), right_motor.current(CurrentUnits.AMP))))
            self.drivetrain_current_monitoring['pair']=1
        elif (left_motor.current(CurrentUnits.AMP)>1.5 or right_motor.current(CurrentUnits.AMP)>1.5) and (current_state==0):
            log.add("WD2", " %s"%(max(left_motor.current(CurrentUnits.AMP), right_motor.current(CurrentUnits.AMP))))
            self.drivetrain_current_monitoring['pair']=2
        elif (left_motor.current(CurrentUnits.AMP)<=1.5 or right_motor.current(CurrentUnits.AMP)<=1.5) and (current_state==2 or current_state==1):
            log.add("DD2", " %s"%(max(left_motor.current(CurrentUnits.AMP), right_motor.current(CurrentUnits.AMP))))
            self.drivetrain_current_monitoring['pair']=0

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
            if motor_id not in self.drivetrain_current_monitoring:
                self.drivetrain_power_monitoring[motor_id] = 0
            if motor_id not in self.drivetrain_disconnected:
                self.drivetrain_disconnected[motor_id] = 0
        
        temp_state = self.drivetrain_temp_monitoring.get('four_motor', 0)
        power_state = self.drivetrain_power_monitoring.get('four_motor', 0)
        current_state= self.drivetrain_current_monitoring.get('four_motor', 0)
        
        # Cheaks for the temps,  power, and cheaks for conecttions of the drivetrain.
        if (front_left_motor.temperature()>70 or front_right_motor.temperature()>70 or back_left_motor.temperature()>70 or back_right_motor.temperature()>70) and (temp_state==0 or temp_state==2):
            log.add("ED1", "Temp %s"%(max(front_left_motor.temperature(), front_right_motor.temperature(), back_left_motor.temperature(), back_right_motor.temperature())))
            self.drivetrain_temp_monitoring['four_motor']=1
        elif (front_left_motor.temperature()>50 or front_right_motor.temperature()>50 or back_left_motor.temperature()>50 or back_right_motor.temperature()>50) and (temp_state==0):
            log.add("WD0", "Temp %s"%(max(front_left_motor.temperature(), front_right_motor.temperature(), back_left_motor.temperature(), back_right_motor.temperature())))
            self.drivetrain_temp_monitoring['four_motor']=2
        elif (front_left_motor.temperature()<=50 and front_right_motor.temperature()<=50 and back_left_motor.temperature()<=50 and back_right_motor.temperature()<=50) and (temp_state==1 or temp_state==2):
            log.add("WD0", "Temp %s"%(max(front_left_motor.temperature(), front_right_motor.temperature(), back_left_motor.temperature(), back_right_motor.temperature())))
            self.drivetrain_temp_monitoring['four_motor']=0
        
        if (front_left_motor.power(PowerUnits.WATT)>20 or front_right_motor.power(PowerUnits.WATT)>20 or back_left_motor.power(PowerUnits.WATT)>20 or back_right_motor.power(PowerUnits.WATT)>20) and (power_state==0 or power_state==2):
            log.add("ED2", "Power %s"%(max(front_left_motor.power(PowerUnits.WATT), front_right_motor.power(PowerUnits.WATT), back_left_motor.power(PowerUnits.WATT), back_right_motor.power(PowerUnits.WATT))))
            self.drivetrain_power_monitoring['four_motor']=1
        elif (front_left_motor.power(PowerUnits.WATT)>12 or front_right_motor.power(PowerUnits.WATT)>12 or back_left_motor.power(PowerUnits.WATT)>12 or back_right_motor.power(PowerUnits.WATT)>12) and (power_state==0):  
            log.add("WD1", "Power %s"%(max(front_left_motor.power(PowerUnits.WATT), front_right_motor.power(PowerUnits.WATT), back_left_motor.power(PowerUnits.WATT), back_right_motor.power(PowerUnits.WATT))))
            self.drivetrain_power_monitoring['four_motor']=2
        elif front_left_motor.power(PowerUnits.WATT)<=12 and front_right_motor.power(PowerUnits.WATT)<=12 and back_left_motor.power(PowerUnits.WATT)<=12 and back_right_motor.power(PowerUnits.WATT)<=12 and (power_state==1 or power_state==2):
            log.add("DD1", "Power %s"%(max(front_left_motor.power(PowerUnits.WATT), front_right_motor.power(PowerUnits.WATT), back_left_motor.power(PowerUnits.WATT), back_right_motor.power(PowerUnits.WATT))))
            self.drivetrain_power_monitoring['four_motor']=0
        
        if (front_left_motor.current(CurrentUnits.AMP)>2 or front_right_motor.current(CurrentUnits.AMP)>2 or back_left_motor.current(CurrentUnits.AMP)>2 or back_right_motor.current(CurrentUnits.AMP)>2) and (current_state==0 or current_state==2):
            log.add("ED4", " %s"%(max(front_left_motor.current(CurrentUnits.AMP), front_right_motor.current(CurrentUnits.AMP),  back_left_motor.current(CurrentUnits.AMP), back_right_motor.current(CurrentUnits.AMP))))
            self.drivetrain_current_monitoring['four_motor']=1
        elif (front_left_motor.current(CurrentUnits.AMP)>1.5 or front_right_motor.current(CurrentUnits.AMP)>1.5 or back_left_motor.current(CurrentUnits.AMP)>1.5 or back_right_motor.current(CurrentUnits.AMP)>1.5) and (current_state==0):
            log.add("WD2", " %s"%(max(front_left_motor.current(CurrentUnits.AMP), front_right_motor.current(CurrentUnits.AMP),  back_left_motor.current(CurrentUnits.AMP), back_right_motor.current(CurrentUnits.AMP))))
            self.drivetrain_current_monitoring['four_motor']=2
        elif (front_left_motor.current(CurrentUnits.AMP)<=1.5 or front_right_motor.current(CurrentUnits.AMP)<=1.5 or back_left_motor.current(CurrentUnits.AMP)<=1.5 or back_right_motor.current(CurrentUnits.AMP)<=1.5) and (current_state==2 or current_state==1):
            log.add("DD2", " %s"%(max(front_left_motor.current(CurrentUnits.AMP), front_right_motor.current(CurrentUnits.AMP),  back_left_motor.current(CurrentUnits.AMP), back_right_motor.current(CurrentUnits.AMP))))
            self.drivetrain_current_monitoring['four_motor']=0
        
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
            if motor_id not in self.drivetrain_current_monitoring:
                self.drivetrain_current_monitoring[motor_id] = 0
            if motor_id not in self.drivetrain_disconnected:
                self.drivetrain_disconnected[motor_id] = 0
        
        temp_state = self.drivetrain_temp_monitoring.get('six_motor', 0)
        power_state = self.drivetrain_power_monitoring.get('six_motor', 0)
        current_state = self.drivetrain_current_monitoring.get('six_motor', 0)
        
        # Cheaks for the temps,  power, and cheaks for conecttions of the drivetrain.
        if (front_left_motor.temperature(PERCENT)>70 or front_right_motor.temperature(PERCENT)>70 or middle_left_motor.temperature(PERCENT)>70 or middle_right_motor.temperature(PERCENT)>70 or back_left_motor.temperature(PERCENT)>70 or back_right_motor.temperature(PERCENT)>70) and (temp_state==0 or temp_state==2):
            log.add("ED1", "Temp %s"%(max(front_left_motor.temperature(PERCENT), front_right_motor.temperature(PERCENT), middle_left_motor.temperature(PERCENT), middle_right_motor.temperature(PERCENT), back_left_motor.temperature(PERCENT), back_right_motor.temperature(PERCENT))))
            self.drivetrain_temp_monitoring['six_motor']=1
        elif (front_left_motor.temperature(PERCENT)>50 or front_right_motor.temperature(PERCENT)>50 or middle_left_motor.temperature(PERCENT)>50 or middle_right_motor.temperature(PERCENT)>50 or back_left_motor.temperature(PERCENT)>50 or back_right_motor.temperature(PERCENT)>50) and (temp_state==0):
            log.add("WD0", "Temp %s"%(max(front_left_motor.temperature(PERCENT), front_right_motor.temperature(PERCENT), middle_left_motor.temperature(PERCENT), middle_right_motor.temperature(PERCENT), back_left_motor.temperature(PERCENT), back_right_motor.temperature(PERCENT))))
            self.drivetrain_temp_monitoring['six_motor']=2
        elif (front_left_motor.temperature(PERCENT)<=50 and front_right_motor.temperature(PERCENT)<=50 and middle_left_motor.temperature(PERCENT)<=50 and middle_right_motor.temperature(PERCENT)<=50 and back_left_motor.temperature(PERCENT)<=50 and back_right_motor.temperature(PERCENT)<=50) and (temp_state==1 or temp_state==2):
            log.add("DD0", "Temp %s"%(max(front_left_motor.temperature(PERCENT), front_right_motor.temperature(PERCENT), middle_left_motor.temperature(PERCENT), middle_right_motor.temperature(PERCENT), back_left_motor.temperature(PERCENT), back_right_motor.temperature(PERCENT))))
            self.drivetrain_temp_monitoring['six_motor']=0
        
        if (front_left_motor.power(PowerUnits.WATT)>20 or front_right_motor.power(PowerUnits.WATT)>20 or middle_left_motor.power(PowerUnits.WATT)>20 or middle_right_motor.power(PowerUnits.WATT)>20 or back_left_motor.power(PowerUnits.WATT)>20 or back_right_motor.power(PowerUnits.WATT)>20) and (power_state==0 or power_state==2):
            log.add("ED2", "Power Peak %s Total Power %s"%(max(front_left_motor.power(PowerUnits.WATT), front_right_motor.power(PowerUnits.WATT), middle_left_motor.power(PowerUnits.WATT), middle_right_motor.power(PowerUnits.WATT), back_left_motor.power(PowerUnits.WATT), back_right_motor.power(PowerUnits.WATT)), str(front_left_motor.power(PowerUnits.WATT) + front_right_motor.power(PowerUnits.WATT) + middle_left_motor.power(PowerUnits.WATT) + middle_right_motor.power(PowerUnits.WATT) + back_left_motor.power(PowerUnits.WATT) + back_right_motor.power(PowerUnits.WATT))))
            self.drivetrain_power_monitoring['six_motor']=1
        elif (front_left_motor.power(PowerUnits.WATT)>12 or front_right_motor.power(PowerUnits.WATT)>12 or middle_left_motor.power(PowerUnits.WATT)>12 or middle_right_motor.power(PowerUnits.WATT)>12 or back_left_motor.power(PowerUnits.WATT)>12 or back_right_motor.power(PowerUnits.WATT)>12) and (power_state==0):  
            log.add("WD1", "Power Peak %s Total Power %s"%(max(front_left_motor.power(PowerUnits.WATT), front_right_motor.power(PowerUnits.WATT), middle_left_motor.power(PowerUnits.WATT), middle_right_motor.power(PowerUnits.WATT), back_left_motor.power(PowerUnits.WATT), back_right_motor.power(PowerUnits.WATT)), str(front_left_motor.power(PowerUnits.WATT) + front_right_motor.power(PowerUnits.WATT) + middle_left_motor.power(PowerUnits.WATT) + middle_right_motor.power(PowerUnits.WATT) + back_left_motor.power(PowerUnits.WATT) + back_right_motor.power(PowerUnits.WATT))))
            self.drivetrain_power_monitoring['six_motor']=2
        elif front_left_motor.power(PowerUnits.WATT)<=12 and front_right_motor.power(PowerUnits.WATT)<=12 and middle_left_motor.power(PowerUnits.WATT)<=12 and middle_right_motor.power(PowerUnits.WATT)<=12 and back_left_motor.power(PowerUnits.WATT)<=12 and back_right_motor.power(PowerUnits.WATT)<=12 and (power_state==1 or power_state==2):
            log.add("DD1", "Power Peak %s Total Power %s"%(max(front_left_motor.power(PowerUnits.WATT), front_right_motor.power(PowerUnits.WATT), middle_left_motor.power(PowerUnits.WATT), middle_right_motor.power(PowerUnits.WATT), back_left_motor.power(PowerUnits.WATT), back_right_motor.power(PowerUnits.WATT)), str(front_left_motor.power(PowerUnits.WATT) + front_right_motor.power(PowerUnits.WATT) + middle_left_motor.power(PowerUnits.WATT) + middle_right_motor.power(PowerUnits.WATT) + back_left_motor.power(PowerUnits.WATT) + back_right_motor.power(PowerUnits.WATT))))
            self.drivetrain_power_monitoring['six_motor']=0

        if (front_left_motor.current(CurrentUnits.AMP)>2 or front_right_motor.current(CurrentUnits.AMP)>2 or middle_left_motor.current(CurrentUnits.AMP)>2 or middle_right_motor.current(CurrentUnits.AMP)>2 or back_left_motor.current(CurrentUnits.AMP)>2 or back_right_motor.current(CurrentUnits.AMP)>2) and (current_state==0 or current_state==2):
            log.add("ED4", " Peak Amps %s Total Amps %s"%(max(front_left_motor.current(CurrentUnits.AMP), front_right_motor.current(CurrentUnits.AMP), middle_left_motor.current(CurrentUnits.AMP), middle_right_motor.current(CurrentUnits.AMP), back_left_motor.current(CurrentUnits.AMP), back_right_motor.current(CurrentUnits.AMP)), str(front_left_motor.current(CurrentUnits.AMP) + front_right_motor.current(CurrentUnits.AMP) + middle_left_motor.current(CurrentUnits.AMP) + middle_right_motor.current(CurrentUnits.AMP) + back_left_motor.current(CurrentUnits.AMP) + back_right_motor.current(CurrentUnits.AMP))))
            self.drivetrain_current_monitoring['six_motor']=1
        elif (front_left_motor.current(CurrentUnits.AMP)>1.5 or front_right_motor.current(CurrentUnits.AMP)>1.5 or middle_left_motor.current(CurrentUnits.AMP)>1.5 or middle_right_motor.current(CurrentUnits.AMP)>1.5 or back_left_motor.current(CurrentUnits.AMP)>1.5 or back_right_motor.current(CurrentUnits.AMP)>1.5) and (current_state==0):
            log.add("WD2", " Peak Amps %s Total Amps %s"%(max(front_left_motor.current(CurrentUnits.AMP), front_right_motor.current(CurrentUnits.AMP), middle_left_motor.current(CurrentUnits.AMP), middle_right_motor.current(CurrentUnits.AMP), back_left_motor.current(CurrentUnits.AMP), back_right_motor.current(CurrentUnits.AMP)), str(front_left_motor.current(CurrentUnits.AMP) + front_right_motor.current(CurrentUnits.AMP) + middle_left_motor.current(CurrentUnits.AMP) + middle_right_motor.current(CurrentUnits.AMP) + back_left_motor.current(CurrentUnits.AMP) + back_right_motor.current(CurrentUnits.AMP))))
            self.drivetrain_current_monitoring['six_motor']=2
        elif (front_left_motor.current(CurrentUnits.AMP)<=1.5 or front_right_motor.current(CurrentUnits.AMP)<=1.5 or middle_left_motor.current(CurrentUnits.AMP)<=1.5 or middle_right_motor.current(CurrentUnits.AMP)<=1.5 or back_left_motor.current(CurrentUnits.AMP)<=1.5 or back_right_motor.current(CurrentUnits.AMP)<=1.5) and current_state!=0:
            log.add("DD2", " Peak Amps %s Total Amps %s"%(max(front_left_motor.current(CurrentUnits.AMP), front_right_motor.current(CurrentUnits.AMP), middle_left_motor.current(CurrentUnits.AMP), middle_right_motor.current(CurrentUnits.AMP), back_left_motor.current(CurrentUnits.AMP), back_right_motor.current(CurrentUnits.AMP)), str(front_left_motor.current(CurrentUnits.AMP) + front_right_motor.current(CurrentUnits.AMP) + middle_left_motor.current(CurrentUnits.AMP) + middle_right_motor.current(CurrentUnits.AMP) + back_left_motor.current(CurrentUnits.AMP) + back_right_motor.current(CurrentUnits.AMP))))
            self.drivetrain_current_monitoring['six_motor']=0

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


# capture for the log class
class Capture:

    def __init__(self):
        self.drivetrain=Drivetrain()
        self.motor_temp_monitoring={} 
        self.motor_power_monitoring={}  
        self.motor_disconnected={}
        self.motor_current_monitoring={}
        self.variables={}  
        self.battery_voltage_monitoring=0
        self.battery_capacity_monitoring=0
        self.battery_current_monitoring=0
        self.battery_watt_monitoring=0
        self.axis1=0
        self.axis2=0
        self.axis3=0
        self.axis4=0
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
        motor_id = id(motor) 
        
        # Initialize tracking
        if motor_id not in self.motor_temp_monitoring:
            self.motor_temp_monitoring[motor_id] = 0
        if motor_id not in self.motor_power_monitoring:
            self.motor_power_monitoring[motor_id] = 0
        if motor_id not in self.motor_current_monitoring:
            self.motor_current_monitoring[motor_id] = 0
        if motor_id not in self.motor_disconnected:
            self.motor_disconnected[motor_id] = 0
        
        # Cheaks for the temps,  power, and cheaks for conecttions of motors(s).
        if motor.temperature()>70 and (self.motor_temp_monitoring[motor_id]==0 or self.motor_temp_monitoring[motor_id]==2):
            log.add("EM0", "Motor %s Temp %s"%(motor, motor.temperature(PERCENT)))
            self.motor_temp_monitoring[motor_id]=1
        elif motor.temperature()>50 and (self.motor_temp_monitoring[motor_id]==0):
            log.add("WM0", "Motor %s Temp %s"%(motor, motor.temperature(PERCENT)))
            self.motor_temp_monitoring[motor_id]=2
        elif motor.temperature()<=50 and (self.motor_temp_monitoring[motor_id]==2 or self.motor_temp_monitoring[motor_id]==1):
            log.add("DM0", "Motor %s Temp %s"%(motor, motor.temperature(PERCENT)))
            self.motor_temp_monitoring[motor_id]=0
        
        if motor.power(PowerUnits.WATT)>20 and (self.motor_power_monitoring[motor_id]==0 or self.motor_power_monitoring[motor_id]==2):
            log.add("EM2", "Motor %s Power %s"%(str(motor), str(motor.power(PowerUnits.WATT))))
            self.motor_power_monitoring[motor_id]=1
        elif motor.power(PowerUnits.WATT)>12 and (self.motor_power_monitoring[motor_id]==0):
            log.add("WM1", "Motor %s Power %s"%(str(motor), str(motor.power(PowerUnits.WATT))))
            self.motor_power_monitoring[motor_id]=2
        elif motor.power(PowerUnits.WATT)<=12 and (self.motor_power_monitoring[motor_id]==1 or self.motor_power_monitoring[motor_id]==2):
            log.add("DM1", "Motor %s Power %s"%(str(motor), str(motor.power(PowerUnits.WATT))))
            self.motor_power_monitoring[motor_id]=0

        if motor.current(CurrentUnits.AMP)>2 and (self.motor_current_monitoring[motor_id]==0 or self.motor_current_monitoring[motor_id]==2):
            log.add("EM3", "Motor %s Current %s"%(str(motor), str(motor.current(CurrentUnits.AMP))))
            self.motor_current_monitoring[motor_id]=1
        elif motor.current(CurrentUnits.AMP)>1.5 and (self.motor_current_monitoring[motor_id]==0):
            log.add("WM2", "Motor %s Current %s"%(str(motor), str(motor.current(CurrentUnits.AMP))))
            self.motor_current_monitoring[motor_id]=2
        elif motor.current(CurrentUnits.AMP)<=1.5 and (self.motor_current_monitoring[motor_id]==1 or self.motor_current_monitoring[motor_id]==2):
            log.add("DM2", "Motor %s Current %s"%(str(motor), str(motor.current(CurrentUnits.AMP))))
            self.motor_current_monitoring[motor_id]=0
        
        if motor.temperature(PERCENT)==2 and self.motor_disconnected[motor_id]==0:
            log.add("EM1", "Motor %s Disconnected"%(motor))
            self.motor_disconnected[motor_id]=1
        
        if motor.temperature(PERCENT)!=2 and self.motor_disconnected[motor_id]==1:
            self.motor_disconnected[motor_id]=0

    def battery(self):
        # Battery monitoring for voltage, capacity, and current.
        if brain.battery.voltage(VoltageUnits.VOLT)<11 and (self.battery_voltage_monitoring==0 or self.battery_voltage_monitoring==2):
            log.add("EB0", "%s"%(brain.battery.voltage(VoltageUnits.VOLT)))
            self.battery_voltage_monitoring=1
        elif brain.battery.voltage(VoltageUnits.VOLT)<12 and (self.battery_voltage_monitoring==0 or self.battery_voltage_monitoring==1):
            log.add("WB0", "%s"%(brain.battery.voltage(VoltageUnits.VOLT)))
            self.battery_voltage_monitoring=2
        elif brain.battery.voltage(VoltageUnits.VOLT)>=12 and (self.battery_voltage_monitoring==1 or self.battery_voltage_monitoring==2):
            log.add("DB0", "%s"%(brain.battery.voltage(VoltageUnits.VOLT)))
            self.battery_voltage_monitoring=0
        
        if brain.battery.capacity()<25 and self.battery_capacity_monitoring!=brain.battery.capacity():
            log.add("EB1", "%s"%(brain.battery.capacity()))
            self.battery_capacity_monitoring=brain.battery.capacity()
        elif brain.battery.capacity()<50 and self.battery_capacity_monitoring!=brain.battery.capacity():
            log.add("WB1", "%s"%(brain.battery.capacity()))
            self.battery_capacity_monitoring=brain.battery.capacity()
        elif brain.battery.capacity()>=50 and self.battery_capacity_monitoring!=brain.battery.capacity():
            log.add("DB3", "%s"%(brain.battery.capacity()))
            self.battery_capacity_monitoring=brain.battery.capacity()
        
        if brain.battery.current(CurrentUnits.AMP)>18 and (self.battery_current_monitoring==0 or self.battery_current_monitoring==2):
            log.add("EB2", "%s"%(brain.battery.current(CurrentUnits.AMP)))
            self.battery_current_monitoring=1
        elif brain.battery.current(CurrentUnits.AMP)>13 and (self.battery_current_monitoring==0 or self.battery_current_monitoring==1):
            log.add("WB2", "%s"%(brain.battery.current(CurrentUnits.AMP)))
            self.battery_current_monitoring=2
        elif brain.battery.current(CurrentUnits.AMP)<=5 and (self.battery_current_monitoring==1 or self.battery_current_monitoring==2):
            log.add("DB1","%s"%(brain.battery.current(CurrentUnits.AMP)))
            self.battery_current_monitoring=0

        if brain.battery.current(CurrentUnits.AMP) * brain.battery.voltage(VoltageUnits.VOLT)>200 and (self.battery_watt_monitoring==0 or self.battery_watt_monitoring==3):
            log.add("EB3", "%s"%(int(brain.battery.current(CurrentUnits.AMP) * brain.battery.voltage(VoltageUnits.VOLT))))
            self.battery_watt_monitoring=1
        elif brain.battery.current(CurrentUnits.AMP) * brain.battery.voltage(VoltageUnits.VOLT)>150 and (self.battery_watt_monitoring==0 or self.battery_watt_monitoring==1):
            log.add("WB3", "%s"%(int(brain.battery.current(CurrentUnits.AMP) * brain.battery.voltage(VoltageUnits.VOLT))))
            self.battery_watt_monitoring=2
        elif brain.battery.current(CurrentUnits.AMP) * brain.battery.voltage(VoltageUnits.VOLT)<=150 and (self.battery_watt_monitoring==1 or self.battery_watt_monitoring==2):
            log.add("DB2", "%s"%(int(brain.battery.current(CurrentUnits.AMP) * brain.battery.voltage(VoltageUnits.VOLT))))
            self.battery_watt_monitoring=0
    
    def controller(self, controller, monitormotor1=Motor(Ports.PORT21, GearSetting.RATIO_18_1, False), monitormotor2=Motor(Ports.PORT21, GearSetting.RATIO_18_1, False), monitormotor3=Motor(Ports.PORT21, GearSetting.RATIO_18_1, False), monitormotor4=Motor(Ports.PORT21, GearSetting.RATIO_18_1, False)):
        Controller=controller

        if not log.recording.record: # Only logs when not recoding to save space on the recording file.
            if Controller.axis1.position()!=0 and not (self.axis1 >= Controller.axis1.position() - log.tolrance and self.axis1 <= Controller.axis1.position() + log.tolrance):
                degrees=monitormotor1.position(DEGREES)
                monitormotor1.set_position(0, DEGREES)
                log.add("DC1", "%s_Axis1 %d Moved %d Degrees"%(str(controller), Controller.axis1.position(), degrees))
                self.axis1=Controller.axis1.position()
            elif 0 == Controller.axis1.position() and self.axis1!=0:
                degrees=monitormotor1.position(DEGREES)
                monitormotor1.set_position(0, DEGREES)
                log.add("DC1", "%s_Axis1 %d Moved %d Degrees"%(str(controller), 0, 0))
                self.axis1=0

        if log.recording.record:
            if Controller.axis2.position()!=0 and self.axis2 != Controller.axis2.position():
                degrees=monitormotor2.position(DEGREES)
                monitormotor2.set_position(0, DEGREES)
                log.add("DC1", "%s_Axis2 %d Moved %d Degrees"%(str(controller), Controller.axis2.position(), degrees))
                self.axis2=Controller.axis2.position()
            elif 0 == Controller.axis2.position() and self.axis2!=0:
                degrees=monitormotor2.position(DEGREES)
                monitormotor2.set_position(0, DEGREES)
                log.add("DC1", "%s_Axis2 %d Moved %d Degrees"%(str(controller), 0, 0))
                self.axis1=0
        else:
            if Controller.axis2.position()!=0 and not (self.axis2 >= Controller.axis2.position() - log.tolrance and self.axis2 <= Controller.axis2.position() + log.tolrance):
                degrees=monitormotor2.position(DEGREES)
                monitormotor2.set_position(0, DEGREES)
                log.add("DC1", "%s_Axis2 %d Moved %d Degrees"%(str(controller), Controller.axis2.position(), degrees))
                self.axis2=Controller.axis2.position()
            elif 0 == Controller.axis2.position() and self.axis2!=0:
                degrees=monitormotor2.position(DEGREES)
                monitormotor2.set_position(0, DEGREES)
                log.add("DC1", "%s_Axis2 %d Moved %d Degrees"%(str(controller), 0, 0))
                self.axis2=0

        if log.recording.record:
            if Controller.axis3.position()!=0 and self.axis3 != Controller.axis3.position():
                degrees=monitormotor3.position(DEGREES)
                monitormotor3.set_position(0, DEGREES)
                log.add("DC1", "%s_Axis3 %d Moved %d Degrees"%(str(controller), Controller.axis3.position(), degrees))
                self.axis3=Controller.axis3.position()
            elif 0 == Controller.axis3.position() and self.axis3!=0:
                degrees=monitormotor3.position(DEGREES)
                monitormotor3.set_position(0, DEGREES)
                log.add("DC1", "%s_Axis3 %d Moved %d Degrees"%(str(controller), 0, 0))
                self.axis3=0
        else:
            if Controller.axis3.position()!=0 and not (self.axis3 >= Controller.axis3.position() - log.tolrance and self.axis3 <= Controller.axis3.position() + log.tolrance):
                degrees=monitormotor3.position(DEGREES)
                monitormotor3.set_position(0, DEGREES)
                log.add("DC1", "%s_Axis3 %d Moved %d Degrees"%(str(controller), Controller.axis3.position(), degrees))
                self.axis3=Controller.axis3.position()
            elif 0 == Controller.axis3.position() and self.axis3!=0:
                degrees=monitormotor3.position(DEGREES)
                monitormotor3.set_position(0, DEGREES)
                log.add("DC1", "%s_Axis3 %d Moved %d Degrees"%(str(controller), 0, 0))
                self.axis3=0

        if not log.recording.record:
            if Controller.axis4.position()!=0 and not (self.axis4 >= Controller.axis4.position() - log.tolrance and self.axis4 <= Controller.axis4.position() + log.tolrance):
                degrees=monitormotor4.position(DEGREES)
                monitormotor4.set_position(0, DEGREES)
                log.add("DC1", "%s_Axis4 %d Moved %d Degrees"%(str(controller), Controller.axis4.position(), degrees))
                self.axis4=Controller.axis4.position()
            elif 0 == Controller.axis4.position() and self.axis4!=0:
                degrees=monitormotor4.position(DEGREES)
                monitormotor4.set_position(0, DEGREES)
                log.add("DC1", "%s_Axis4 %d Moved %d Degrees"%(str(controller), 0, 0))
                self.axis4=0

        if Controller.buttonA.pressing() and self.button_a==True:
            log.add("DC0", "%s_Button A Pressed"%(str(controller)))
            self.button_a=False
        elif Controller.buttonA.pressing()==False and self.button_a==False:
            log.add("DC0", "%s_Button A Released"%(str(controller)))
            self.button_a=True


        if Controller.buttonB.pressing() and self.button_b==True:
            log.add("DC0", "%s_Button B Pressed"%(str(Controller)))
            self.button_b=False
        elif Controller.buttonB.pressing()==False and self.button_b==False:
            log.add("DC0", "%s_Button B Released"%(str(controller)))
            self.button_b=True

        if Controller.buttonX.pressing() and self.button_x==True:
            log.add("DC0", "%s_Button X Pressed"%(str(controller)))
            self.button_x=False
        elif Controller.buttonX.pressing()==False and self.button_x==False:
            log.add("DC0", "%s_Button X Released"%(str(controller)))
            self.button_x=True

        if Controller.buttonY.pressing() and self.button_y==True:
            log.add("DC0", "%s_Button Y Pressed"%(str(controller)))
            self.button_y=False
        elif Controller.buttonY.pressing()==False and self.button_y==False:
            log.add("DC0", "%s_Button Y Released"%(str(controller)))
            self.button_y=True

        if Controller.buttonUp.pressing() and self.button_up==True:
            log.add("DC0", "%s_Button UP Pressed"%(str(controller)))
            self.button_up=False
        elif Controller.buttonUp.pressing()==False and self.button_up==False:
            log.add("DC0", "%s_Button UP Released"%(str(controller)))
            self.button_up=True

        if Controller.buttonDown.pressing() and self.button_down==True:
            log.add("DC0", "%s_Button DOWN Pressed"%(str(controller)))
            self.button_down=False
        elif Controller.buttonDown.pressing()==False and self.button_down==False:
            log.add("DC0", "%s_Button DOWN Released"%(str(controller)))
            self.button_down=True

        if Controller.buttonLeft.pressing() and self.button_left==True:
            log.add("DC0", "%s_Button LEFT Pressed"%(str(controller)))
            self.button_left=False
        elif Controller.buttonLeft.pressing()==False and self.button_left==False:
            log.add("DC0", "%s_Button LEFT Released"%(str(controller)))
            self.button_left=True

        if Controller.buttonRight.pressing() and self.button_right==True:
            log.add("DC0", "%s_Button RIGHT Pressed"%(str(controller)))
            self.button_right=False
        elif Controller.buttonRight.pressing()==False and self.button_right==False:
            log.add("DC0", "%s_Button RIGHT Released"%(str(controller)))
            self.button_right=True

        if Controller.buttonL1.pressing() and self.button_L1==True:
            log.add("DC0", "%s_Button L1 Pressed"%(str(controller)))
            self.button_L1=False
        elif Controller.buttonL1.pressing()==False and self.button_L1==False:
            log.add("DC0", "%s_Button L1 Released"%(str(controller)))
            self.button_L1=True

        if Controller.buttonL2.pressing() and self.button_L2==True:
            log.add("DC0", "%s_Button L2 Pressed"%(str(controller)))
            self.button_L2=False
        elif Controller.buttonL2.pressing()==False and self.button_L2==False:
            log.add("DC0", "%s_Button L2 Released"%(str(controller)))
            self.button_L2=True

        if Controller.buttonR1.pressing() and self.button_R1==True:
            log.add("DC0", "%s_Button R1 Pressed"%(str(controller)))
            self.button_R1=False
        elif Controller.buttonR1.pressing()==False and self.button_R1==False:
            log.add("DC0", "%s_Button R1 Released"%(str(controller)))
            self.button_R1=True

        if Controller.buttonR2.pressing() and self.button_R2==True:
            log.add("DC0", "%s_Button R2 Pressed"%(str(controller)))
            self.button_R2=False
        elif Controller.buttonR2.pressing()==False and self.button_R2==False:
            log.add("DC0", "%s_Button R2 Released"%(str(controller)))
            self.button_R2=True

    def variable(self, name, value):
        valueid=id(name)
        if valueid not in self.variables:
            if type(value)==bool:
                self.variables[valueid]=False
            else:
                self.variables[valueid]=0
        if value != self.variables[valueid]:
            log.add("DV0", "Variable %s Value %s"%(name, value))
            self.variables[valueid] = value


class Recording:
    def __init__(self):
        self.record=False
        self.log_timeecord=0
        self.postlog_timeecord=0
        self.Aton=""
        self.postlist=[]
        self.File=""
        self.poststring=""      

    def start(self, Aton):
        filename=str(Aton) + "_pre.txt"
        if self.record == False:
            self.record= True
            brain.sdcard.savefile(filename, bytearray("\n", log.format))
            self.Aton=Aton + "_pre.txt"
            log.add("DA0", filename)

    def stop(self, Aton):
        filename=str(Aton) + "_pre.txt"
        preatonfile=""
        self.record=False
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
        filename=Aton + ".txt"
        self.record=False
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
                            if "Axis3" in str(prelist):
                                brain.sdcard.appendfile(filename, bytearray("%s(%s, %s), "%(str(left[1]), str(prelist[11]).replace("'", ''), str(prelist[13]).replace("'", '')), log.format))
                            elif "Axis2" in str(prelist):
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
                                if "1_Axis3" in str(prelist):
                                    brain.sdcard.appendfile(filename, bytearray("%s(%s, %s), "%(str(left[1]), str(prelist[10]).replace("'", ''), str(prelist[12]).replace("'", '')), log.format))
                                elif "1_Axis2" in str(prelist):
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
    
    def log(self):
        speed=log_time.time()
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
                    speed2=log_time.time()
                    logline=line.split(':')
                    if len(logline)>=4:
                        loglines= ":" + str(logline[1]) + ":" + str(logline[2]) + ": "
                        brain.sdcard.appendfile("loghistory.txt", bytearray(str(logline[0]) + str(reversecodes.get(loglines)) + str(logline[3]) + '\n', log.format))
                    print("Archiving took: " + str(log_time.time() - speed2) + " MSEC")
            log.clear()
            log.adding=True
        except OSError: # If the log file is too big to load into memory, it will read the file line by line and write to the new file.
            log.adding=False
            reversecodes={value: key for key, value in log.codes.items()}
            with open("Log.csv", 'r') as file:
                for line in file:
                    speed2=log_time.time()
                    logline=line.split(':')
                    if len(logline)>=4:
                        loglines= ":" + str(logline[1]) + ":" + str(logline[2]) + ": "
                        brain.sdcard.appendfile("loghistory.txt", bytearray(str(logline[0]) + str(reversecodes.get(loglines)) + str(logline[3]) + '\n', log.format))
                    print("Archiving took: " + str(log_time.time() - speed2) + " MSEC")
            log.clear()
            log.adding=True
        log.add("DS1", str(log_time.time() - speed) + " MSEC")
    
    def recording(self, recordingname):
        speed=log_time.time()
        archivelist=""
        try:
            reversecodes={value: key for key, value in log.codes.items()}
            logfile=brain.sdcard.loadfile(recordingname).decode(log.format)
            loglist=logfile.split("\n")
            for i in range(len(loglist)):
                logline=loglist[i].split(':')
                if len(logline)>=4:
                    loglines= ":" + str(logline[1]) + ":" + str(logline[2]) + ": "
                    archivelist=archivelist + str(logline[0]) + str(reversecodes.get(loglines)) + str(logline[3]) + '\n'
            brain.sdcard.appendfile("loghistory.txt", bytearray(archivelist, log.format))
            logfile=""
            brain.sdcard.savefile(recordingname)
        except MemoryError: # If the recording file is too big to load into memory, it will read the file line by line and write to the new file.
            log.adding=False
            reversecodes={value: key for key, value in log.codes.items()}
            with open("Log.csv", 'r') as file:
                for line in file:
                    speed2=log_time.time()
                    logline=line.split(':')
                    if len(logline)>=4:
                        loglines= ":" + str(logline[1]) + ":" + str(logline[2]) + ": "
                        brain.sdcard.appendfile("loghistory.txt", bytearray(str(logline[0]) + str(reversecodes.get(loglines)) + str(logline[3]) + '\n', log.format))
                    print("Archiving took: " + str(log_time.time() - speed2) + " MSEC")
            log.clear()
            log.adding=True
        log.add("DS3", str(log_time.time() - speed) + " MSEC")
    
    def index_history(self):
        speed=log_time.time()
        index=0
        with open("loghistory.txt", 'r') as file:
            for line in file:
                index+=1
        brain.sdcard.savefile("index.txt", bytearray(str(index), log.format))
        brain.sdcard.savefile("loghistory.txt")
        log.add("DS2", str(log_time.time() - speed) + " MSEC")


    def recall(self, name):
        filename=(str(name).replace("history.txt", "recalled.txt"))
        print("recalling")
        try:
            file=brain.sdcard.loadfile(name).decode(log.format)
            brain.sdcard.savefile(filename)
            filelist=file.split(',')
            for i in range(len(filelist)):
                prelist=filelist[i].split(' ')
                if len(prelist) >= 5:
                    brain.sdcard.appendfile(filename, bytearray(str(prelist[0]) + " " + str(prelist[1]) + " " + str(prelist[2]) + " " + str(log.codes.get(prelist[3])) + str(prelist[4 : len(prelist)-1]) + "\n", log.format))
            print("Recall done.")
        except MemoryError: # Same thing as the last three exceptions.
            with open(name, 'r') as file:
                for line in file:
                    prelist=line.split(' ')
                    if len(prelist) >= 5:
                        brain.sdcard.appendfile(filename, bytearray(str(prelist[0]) + " " + str(prelist[1]) + " " + str(prelist[2]) + " " + str(log.codes.get(prelist[3])) + str(prelist[4 : len(prelist)-1]) + "\n", log.format))
            print("Recall done.")


class Log:
    def __init__(self):
        self.capture=Capture()
        self.recording=Recording()
        self.archive=Archive()
        self.index=0
        self.adding=True
        self.format="utf-8"
        self.cache=""
        self.brainscreen=False
        self.row=0
        self.tolrance=3
        brain.sdcard.savefile("Logstart.txt")
        # Predefined Log Codes dictionary
        self.codes={
                    "ED1": ":Drivetrain ERROR: Motor(s) Criticaly Hot. Temp: ",
                    "ED2": ":Drivetrain ERROR: Motor(s) Very High Power. Power: ",
                    "ED3": ":Drivetrain ERROR: Motor(s) Disconnected. Name: ",
                    "ED4": ":Drivetrain ERROR: Motor(s) Very High Current. Current: ",
                    "WD0": ":Drivetrain WARNING: Motor(s) Hot. Temp: ",
                    "WD1": ":Drivetrain WARNING: High Power. Power: ",
                    "WD2": ":Drivetrain WARNING: High Current. Current: ",
                    "DD0": ":Drivetrain DATA: Temps Back To Normal. Temp: ",
                    "DD1": ":Drivetrain DATA: Power Back To Normal. Power: ",
                    "DD2": ":Drivetrain DATA: Current Back To Normal. Current: ",
                    "EB0": ":Battery ERROR: Critically Low Voltage. Voltage: ",
                    "EB1": ":Battery ERROR: Critically Low Battery. Capacity: ",
                    "EB2": ":Battery ERROR: Critically High Current. Current: ",
                    "EB3": ":Battery ERROR: Critically High Wattage. Wattage: ",
                    "WB0": ":Battery WARNING: Low Voltage. Voltage: ",
                    "WB1": ":Battery WARNING: Low Battery. capacity: ",
                    "WB2": ":Battery WARNING: High Current. Current: ",
                    "WB3": ":Battery WARNING: High Wattage. Wattage: ",
                    "DB0": ":Battery DATA: Voltage Back To Normal. Voltage: ",
                    "DB1": ":Battery DATA: Current Back To Normal. Current: ",
                    "DB2": ":Battery DATA: Wattage Back To Normal. Wattage: ",
                    "DB3": ":Battery DATA: Capacity Changed. Capacity: ",
                    "DA0": ":Aton DATA: Recording Started.: ",
                    "DA1": ":Aton DATA: Recording Stopped.: ",
                    "DA2": ":Aton DATA: Recording Saved.: ",
                    "DA3": ":Aton DATA: Recording Loaded.: ",
                    "WS0": ":System WARNING: Loop Slowish. Time: ",
                    "DS0": ":System DATA: Init setup complete.: ",
                    "DS1": ":System DATA: Archive Log complete. Time: ",
                    "DS2": ":System DATA: Index Log History complete. Time: ",
                    "DS3": ":System DATA: Archive Recording complete. Time: ",
                    "DS4": ":System DATA: Loop Speed. Time: ",
                    "EM0": ":Motor ERROR: Motor Criticaly Hot. Temp: ",
                    "EM1": ":Motor ERROR: Motor Disconnected. Name: ",
                    "EM2": ":Motor ERROR: Motor Very High Power. Power: ",
                    "EM3": ":Motor ERROR: Motor Very High Current. Current: ",
                    "WM0": ":Motor WARNING: Motor Hot. Temp: ",
                    "WM1": ":Motor WARNING: Motor High Power. Power: ",
                    "WM2": ":Motor WARNING: Motor High Current. Current: ",
                    "DM0": ":Motor DATA: Motor Temps Back To Normal. Temps:",
                    "DM1": ":Motor DATA: Motor Power Back To Normal. Power:",
                    "DM2": ":Motor DATA: Motor Current Back To Normal. Current:",
                    "DV0": ":Variable DATA: Variable Changed. Name: ",
                    "DC0": ":Controller DATA: Button Pressed. Button: ",
                    "DC1": ":Controller DATA: Axis Changed. Axis: ",
                }
        # Setting up Log Files if they dont exist and setting index.
        
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
                    try:
                        loghistory_lines=brain.sdcard.loadfile("loghistory.txt").decode(self.format).split("\n")
                    except AttributeError:
                        pass
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
            if not brain.sdcard.exists("index.txt"):
                brain.sdcard.savefile("index.txt", bytearray("0", self.format))

            historyindex=int(brain.sdcard.loadfile("index.txt").decode(self.format))
            self.index=len(log_lines) + len(loghistory_lines) + log_number + historyindex - 1
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
        if not self.adding:
            return

        entry = ", %s [%s] %s %s \n" % (self.index, log_time, self.codes.get(add_code), add_details)       
        print(entry)
        if self.recording.record:
            self.cache += entry
        else:
            brain.sdcard.appendfile("Log.csv", bytearray(entry, self.format))

        if self.brainscreen:
            if self.row>=20:
                brain.screen.clear_screen()
                brain.screen.set_cursor(1,1)
                self.row=0
            brain.screen.print(entry)
            brain.screen.new_line()
            self.row+=1
            
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
            self.codes.update({code_edit : "%s"%(new_decoded_text)})

    # Clearing the log file
    def clear(self):
        brain.sdcard.savefile("Log.csv", bytearray("Log Start: \n", self.format))
    
    # Displaying log codes dictionary
    def table(self):
        print(self.codes)

    def read(self):
        log_content=brain.sdcard.loadfile("Log.csv")
        print(log_content.decode(self.format))
    
    def logstart(self, Right1, Left1, Right2=None, Left2=None, Right3=None, Left3=None, motor1=None, motor2=None, motor3=None, motor4=None, motor5=None, motor6=None, controller1=Controller(PRIMARY), controller2=None, brainread=False, indexhistory=True):
        if brainread:
            brain.screen.set_font(FontType.MONO12)
            self.brainscreen=True
        try:    
            addedfuntion=brain.sdcard.loadfile("Logstart.txt").decode(self.format)
        except AttributeError:
            pass
        self.archive.log()
        if brain.sdcard.filesize("loghistory.txt") >= 250000 and indexhistory==True:
            log.archive.index_history()
        self.add("DS0", 0)
        
        while True:
            speed=log_time.time()
            for i in range(200):
                self.capture.battery()
                self.capture.controller(controller1, Right1, Right1, Left1, Left1)

                if controller2!=None:
                    self.capture.controller(controller2, Right1, Right1, Left1, Left1)
                
                if Right2==None and Right3==None:
                    self.capture.drivetrain.two_motor(Right1, Left1)
                elif Right3==None:
                    self.capture.drivetrain.four_motor(Right1, Left1, Right2, Left2)
                else:
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
                
                try:
                    exec(addedfuntion)
                    pass
                except Exception as e:
                    print("ERROR exec in logstart Error: ", e)
                
                if self.recording.record==False:
                    wait(200, MSEC)
                else:
                    pass
            self.unloadcache()
            if self.recording.record==False and (log_time.time() - speed) > 40400:
                log.add("WS0", str(log_time.time() - speed))
            else:
                log.add("DS4", str(log_time.time() - speed))
    
    def add_logstart(self, funtion):
        brain.sdcard.appendfile("Logstart.txt" , bytearray(funtion + ", ", self.format))


log=Log()