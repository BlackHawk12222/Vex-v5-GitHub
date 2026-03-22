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
import gc
import sys

brain=Brain()
log_time= Timer() # Main timer used.

    
def none():
    pass

class Log():
    """Main object for the CLEAR import. \n To start logging use the "logstart()" function in this object to do the main logging if you need help with its inputs use help() over the "logstart()" function."""

    

    class Capture:
        """Main object for capturing data of the robot and seeing if it needs to be logged."""

        class System:
            """Main object" for general program data like memory use ."""

            def __init__(self):
                self.modulelist=sys.modules.copy()
                self.memory_logged=False
                self.memory=0

            def memoryuse(self):
                if gc.mem_alloc()/1000 >= 700 and not self.memory_logged:   # type: ignore
                    if "DSM0" not in log.codes:
                        log.add_codes("DSM0", ":Memory WARNING: Memory useage high. Memory used: ")
                    log.add("DSM0", str(gc.mem_alloc()/ 1000) + " KB") # type: ignore
                    self.memory_logged=True
                    self.memory=gc.mem_alloc() # type: ignore
                elif self.memory_logged and (gc.mem_alloc()/1000 < 700 or (gc.mem_alloc() - self.memory)/1000 >= 100): # type: ignore
                    self.memory_logged=False
            
            def modules(self):
                if self.modulelist != sys.modules:
                    if "DSP0" not in log.codes:
                        log.add_codes("DSP0", ":System DATA: New module(s) added. Moduale: ")
                    filtered_list = [item for item in self.modulelist if item not in sys.modules]
                    log.add("DSP0", filtered_list)
                    self.modulelist= sys.modules.copy()

        class Drivetrain:
            """Capture for the drivetrain of robots has options for two, four, or six motor drivetrains."""

            def __init__(self):
                # Sets used for tracking of the drivetrain by motor.
                self.drivetrain_temp_monitoring=0
                self.drivetrain_power_monitoring=0
                self.drivetrain_disconnected={}
                self.drivetrain_current_monitoring=0
            
            def standerd(self, drivetrain, type):
                """Used for two/four motor drivtrains for standerd use."""
                if type=="four" or type=="Four":
                    currentlimitsE=10
                    currentlimitsW=6
                elif type=="two" or type=="Two":
                    currentlimitsE=5
                    currentlimitsW=3

                if id("standerd") not in self.drivetrain_disconnected:
                    self.drivetrain_disconnected[id("standerd")] = 0

                if drivetrain.temperature()>70 and (self.drivetrain_temp_monitoring==0 or self.drivetrain_temp_monitoring==2):
                    log.add("ED1", "Motor %s Temp %s"%(drivetrain, drivetrain.temperature(PERCENT)))
                    self.drivetrain_temp_monitoring=1
                elif drivetrain.temperature()>50 and (self.drivetrain_temp_monitoring==0):
                    log.add("WD0", "Motor %s Temp %s"%(drivetrain, drivetrain.temperature(PERCENT)))
                    self.drivetrain_temp_monitoring=2
                elif drivetrain.temperature()<=50 and (self.drivetrain_temp_monitoring==2 or self.drivetrain_temp_monitoring==1):
                    log.add("DD0", "Motor %s Temp %s"%(drivetrain, drivetrain.temperature(PERCENT)))
                    self.drivetrain_temp_monitoring=0
                
                if drivetrain.power(PowerUnits.WATT)>20 and (self.drivetrain_power_monitoring==0 or self.drivetrain_power_monitoring==2):
                    log.add("ED2", "Motor %s Power %s"%(str(drivetrain), str(drivetrain.power(PowerUnits.WATT))))
                    self.drivetrain_power_monitoring=1
                elif drivetrain.power(PowerUnits.WATT)>12 and (self.drivetrain_power_monitoring==0):
                    log.add("WD1", "Motor %s Power %s"%(str(drivetrain), str(drivetrain.power(PowerUnits.WATT))))
                    self.drivetrain_power_monitoring=2
                elif drivetrain.power(PowerUnits.WATT)<=12 and (self.drivetrain_power_monitoring==1 or self.drivetrain_power_monitoring==2):
                    log.add("DD1", "Motor %s Power %s"%(str(drivetrain), str(drivetrain.power(PowerUnits.WATT))))
                    self.drivetrain_power_monitoring=0

                if drivetrain.current(CurrentUnits.AMP)>currentlimitsE and (self.drivetrain_current_monitoring==0 or self.drivetrain_current_monitoring==2):
                    log.add("ED4", "Motor %s Current %s"%(str(drivetrain), str(drivetrain.current(CurrentUnits.AMP))))
                    self.drivetrain_current_monitoring=1
                elif drivetrain.current(CurrentUnits.AMP)>currentlimitsW and (self.drivetrain_current_monitoring==0):
                    log.add("WD2", "Motor %s Current %s"%(str(drivetrain), str(drivetrain.current(CurrentUnits.AMP))))
                    self.drivetrain_current_monitoring=2
                elif drivetrain.current(CurrentUnits.AMP)<=currentlimitsW and (self.drivetrain_current_monitoring==1 or self.drivetrain_current_monitoring==2):
                    log.add("DD2", "Motor %s Current %s"%(str(drivetrain), str(drivetrain.current(CurrentUnits.AMP))))
                    self.drivetrain_current_monitoring=0

                if ((drivetrain.temperature(PERCENT) % 2==1 and drivetrain.temperature(PERCENT) % 5!=0) or drivetrain.temperature(PERCENT)==2 or (drivetrain.temperature(PERCENT) % 2==0 and drivetrain.temperature(PERCENT) % 10!=0)) and self.drivetrain_disconnected[id("standerd")]==0:
                    log.add("ED3", "Unknown.")
                    self.drivetrain_disconnected[id("standerd")]=1
                elif not ((drivetrain.temperature(PERCENT) % 2==1 and drivetrain.temperature(PERCENT) % 5!=0) or drivetrain.temperature(PERCENT)==2 or (drivetrain.temperature(PERCENT) % 2==0 and drivetrain.temperature(PERCENT) % 10!=0)) and self.drivetrain_disconnected[id("standerd")]==1:
                    self.drivetrain_disconnected[id("standerd")]=0
                
                del currentlimitsE, currentlimitsW

            
            def six_motor(self, front_left_motor, front_right_motor, middle_left_motor, middle_right_motor, back_left_motor, back_right_motor):
                """Capture for a six motor drivetrain. Enter all drivtrain motors in order left, right from front to back."""
                
                # Cheaks for the temps,  power, and cheaks for conecttions of the drivetrain.
                if max(front_left_motor.temperature(PERCENT), front_right_motor.temperature(PERCENT), middle_left_motor.temperature(PERCENT), middle_right_motor.temperature(PERCENT), back_left_motor.temperature(PERCENT), back_right_motor.temperature(PERCENT)) >70 and (self.drivetrain_temp_monitoring==0 or self.drivetrain_temp_monitoring==2):
                    log.add("ED1", "Temp %s"%(max(front_left_motor.temperature(PERCENT), front_right_motor.temperature(PERCENT), middle_left_motor.temperature(PERCENT), middle_right_motor.temperature(PERCENT), back_left_motor.temperature(PERCENT), back_right_motor.temperature(PERCENT))))
                    self.drivetrain_temp_monitoring=1
                elif max(front_left_motor.temperature(PERCENT), front_right_motor.temperature(PERCENT), middle_left_motor.temperature(PERCENT), middle_right_motor.temperature(PERCENT), back_left_motor.temperature(PERCENT), back_right_motor.temperature(PERCENT)) >50 and (self.drivetrain_temp_monitoring==0):
                    log.add("WD0", "Temp %s"%(max(front_left_motor.temperature(PERCENT), front_right_motor.temperature(PERCENT), middle_left_motor.temperature(PERCENT), middle_right_motor.temperature(PERCENT), back_left_motor.temperature(PERCENT), back_right_motor.temperature(PERCENT))))
                    self.drivetrain_temp_monitoring=2
                elif (front_left_motor.temperature(PERCENT)<=50 and front_right_motor.temperature(PERCENT)<=50 and middle_left_motor.temperature(PERCENT)<=50 and middle_right_motor.temperature(PERCENT)<=50 and back_left_motor.temperature(PERCENT)<=50 and back_right_motor.temperature(PERCENT)<=50) and (self.drivetrain_temp_monitoring==1 or self.drivetrain_temp_monitoring==2):
                    log.add("DD0", "Temp %s"%(max(front_left_motor.temperature(PERCENT), front_right_motor.temperature(PERCENT), middle_left_motor.temperature(PERCENT), middle_right_motor.temperature(PERCENT), back_left_motor.temperature(PERCENT), back_right_motor.temperature(PERCENT))))
                    self.drivetrain_temp_monitoring=0
                
                if (front_left_motor.power(PowerUnits.WATT)>20 or front_right_motor.power(PowerUnits.WATT)>20 or middle_left_motor.power(PowerUnits.WATT)>20 or middle_right_motor.power(PowerUnits.WATT)>20 or back_left_motor.power(PowerUnits.WATT)>20 or back_right_motor.power(PowerUnits.WATT)>20) and (self.drivetrain_power_monitoring==0 or self.drivetrain_power_monitoring==2):
                    log.add("ED2", "Power Peak %s Total Power %s"%(max(front_left_motor.power(PowerUnits.WATT), front_right_motor.power(PowerUnits.WATT), middle_left_motor.power(PowerUnits.WATT), middle_right_motor.power(PowerUnits.WATT), back_left_motor.power(PowerUnits.WATT), back_right_motor.power(PowerUnits.WATT)), str(front_left_motor.power(PowerUnits.WATT) + front_right_motor.power(PowerUnits.WATT) + middle_left_motor.power(PowerUnits.WATT) + middle_right_motor.power(PowerUnits.WATT) + back_left_motor.power(PowerUnits.WATT) + back_right_motor.power(PowerUnits.WATT))))
                    self.drivetrain_power_monitoring=1
                elif (front_left_motor.power(PowerUnits.WATT)>12 or front_right_motor.power(PowerUnits.WATT)>12 or middle_left_motor.power(PowerUnits.WATT)>12 or middle_right_motor.power(PowerUnits.WATT)>12 or back_left_motor.power(PowerUnits.WATT)>12 or back_right_motor.power(PowerUnits.WATT)>12) and (self.drivetrain_power_monitoring==0):  
                    log.add("WD1", "Power Peak %s Total Power %s"%(max(front_left_motor.power(PowerUnits.WATT), front_right_motor.power(PowerUnits.WATT), middle_left_motor.power(PowerUnits.WATT), middle_right_motor.power(PowerUnits.WATT), back_left_motor.power(PowerUnits.WATT), back_right_motor.power(PowerUnits.WATT)), str(front_left_motor.power(PowerUnits.WATT) + front_right_motor.power(PowerUnits.WATT) + middle_left_motor.power(PowerUnits.WATT) + middle_right_motor.power(PowerUnits.WATT) + back_left_motor.power(PowerUnits.WATT) + back_right_motor.power(PowerUnits.WATT))))
                    self.drivetrain_power_monitoring=2
                elif front_left_motor.power(PowerUnits.WATT)<=12 and front_right_motor.power(PowerUnits.WATT)<=12 and middle_left_motor.power(PowerUnits.WATT)<=12 and middle_right_motor.power(PowerUnits.WATT)<=12 and back_left_motor.power(PowerUnits.WATT)<=12 and back_right_motor.power(PowerUnits.WATT)<=12 and (self.drivetrain_power_monitoring==1 or self.drivetrain_power_monitoring==2):
                    log.add("DD1", "Power Peak %s Total Power %s"%(max(front_left_motor.power(PowerUnits.WATT), front_right_motor.power(PowerUnits.WATT), middle_left_motor.power(PowerUnits.WATT), middle_right_motor.power(PowerUnits.WATT), back_left_motor.power(PowerUnits.WATT), back_right_motor.power(PowerUnits.WATT)), str(front_left_motor.power(PowerUnits.WATT) + front_right_motor.power(PowerUnits.WATT) + middle_left_motor.power(PowerUnits.WATT) + middle_right_motor.power(PowerUnits.WATT) + back_left_motor.power(PowerUnits.WATT) + back_right_motor.power(PowerUnits.WATT))))
                    self.drivetrain_power_monitoring=0

                if (front_left_motor.current(CurrentUnits.AMP)>2 or front_right_motor.current(CurrentUnits.AMP)>2 or middle_left_motor.current(CurrentUnits.AMP)>2 or middle_right_motor.current(CurrentUnits.AMP)>2 or back_left_motor.current(CurrentUnits.AMP)>2 or back_right_motor.current(CurrentUnits.AMP)>2) and (self.drivetrain_current_monitoring==0 or self.drivetrain_current_monitoring==2):
                    log.add("ED4", " Peak Amps %s Total Amps %s"%(max(front_left_motor.current(CurrentUnits.AMP), front_right_motor.current(CurrentUnits.AMP), middle_left_motor.current(CurrentUnits.AMP), middle_right_motor.current(CurrentUnits.AMP), back_left_motor.current(CurrentUnits.AMP), back_right_motor.current(CurrentUnits.AMP)), str(front_left_motor.current(CurrentUnits.AMP) + front_right_motor.current(CurrentUnits.AMP) + middle_left_motor.current(CurrentUnits.AMP) + middle_right_motor.current(CurrentUnits.AMP) + back_left_motor.current(CurrentUnits.AMP) + back_right_motor.current(CurrentUnits.AMP))))
                    self.drivetrain_current_monitoring=1
                elif (front_left_motor.current(CurrentUnits.AMP)>1.5 or front_right_motor.current(CurrentUnits.AMP)>1.5 or middle_left_motor.current(CurrentUnits.AMP)>1.5 or middle_right_motor.current(CurrentUnits.AMP)>1.5 or back_left_motor.current(CurrentUnits.AMP)>1.5 or back_right_motor.current(CurrentUnits.AMP)>1.5) and (self.drivetrain_current_monitoring==0):
                    log.add("WD2", " Peak Amps %s Total Amps %s"%(max(front_left_motor.current(CurrentUnits.AMP), front_right_motor.current(CurrentUnits.AMP), middle_left_motor.current(CurrentUnits.AMP), middle_right_motor.current(CurrentUnits.AMP), back_left_motor.current(CurrentUnits.AMP), back_right_motor.current(CurrentUnits.AMP)), str(front_left_motor.current(CurrentUnits.AMP) + front_right_motor.current(CurrentUnits.AMP) + middle_left_motor.current(CurrentUnits.AMP) + middle_right_motor.current(CurrentUnits.AMP) + back_left_motor.current(CurrentUnits.AMP) + back_right_motor.current(CurrentUnits.AMP))))
                    self.drivetrain_current_monitoring=2
                elif (front_left_motor.current(CurrentUnits.AMP)<=1.5 or front_right_motor.current(CurrentUnits.AMP)<=1.5 or middle_left_motor.current(CurrentUnits.AMP)<=1.5 or middle_right_motor.current(CurrentUnits.AMP)<=1.5 or back_left_motor.current(CurrentUnits.AMP)<=1.5 or back_right_motor.current(CurrentUnits.AMP)<=1.5) and self.drivetrain_current_monitoring!=0:
                    log.add("DD2", " Peak Amps %s Total Amps %s"%(max(front_left_motor.current(CurrentUnits.AMP), front_right_motor.current(CurrentUnits.AMP), middle_left_motor.current(CurrentUnits.AMP), middle_right_motor.current(CurrentUnits.AMP), back_left_motor.current(CurrentUnits.AMP), back_right_motor.current(CurrentUnits.AMP)), str(front_left_motor.current(CurrentUnits.AMP) + front_right_motor.current(CurrentUnits.AMP) + middle_left_motor.current(CurrentUnits.AMP) + middle_right_motor.current(CurrentUnits.AMP) + back_left_motor.current(CurrentUnits.AMP) + back_right_motor.current(CurrentUnits.AMP))))
                    self.drivetrain_current_monitoring=0

                for motor in (front_left_motor, front_right_motor, middle_left_motor, middle_right_motor, back_left_motor, back_right_motor):

                    if id(motor) not in self.drivetrain_disconnected:
                        self.drivetrain_disconnected[id(motor)] = 0

                    if motor.temperature(PERCENT)==2 and self.drivetrain_disconnected[id(motor)]==0:
                        log.add("ED3", motor)
                        self.drivetrain_disconnected[id(motor)]=1
                    elif motor.temperature(PERCENT)!=2 and self.drivetrain_disconnected[id(motor)]==1:
                        self.drivetrain_disconnected[id(motor)]=0

        class Smartport:
            def __init__(self):
                # Sets for other motors By there id.
                self.motor_temp_monitoring={} 
                self.motor_power_monitoring={}  
                self.motor_disconnected={}
                self.motor_current_monitoring={}
                self.optical_object={}
                self.optical_color={}
                self.optical_connected={}
                self.inertial_axis_tolerance=0.5
                self.inertial_gyro_tolerance=5
                self.inertial_calibrating=False
                self.inertial_connected=True
                self.inertial_rotation_history=0
                self.inertial_roll_history=0
                self.inertial_pitch_history=0
                self.inertial_heading_history=0
                self.inertial_x_axis_history=0
                self.inertial_y_axis_history=0
                self.inertial_z_axis_history=0
                self.rotation_connection={}
                self.rotation_angle_history={}
                self.rotation_position_history={}

            def motor(self, motor):
                """Capture for any general smart motor. Enter motor you wish to log as input. (Can take motor groups as well.)"""

                motor_id = id(motor) 
                
                # Setup id to sets if not there.
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
                    log.add("EM1", "%s"%(motor))
                    self.motor_disconnected[motor_id]=1
                
                if motor.temperature(PERCENT)!=2 and self.motor_disconnected[motor_id]==1:
                    self.motor_disconnected[motor_id]=0

                del motor_id
            
            def optical(self, opticalsensor):
                """Capture for an optical sensor. Enter optical sensor to Capture."""

                optical_id=id(opticalsensor)

                if  optical_id not in self.optical_connected:
                    self.optical_connected[optical_id]=True

                if  optical_id not in self.optical_object:
                    self.optical_object[optical_id]=False

                if  optical_id not in self.optical_color:
                    self.optical_color[optical_id]=0
                
                if opticalsensor.installed() and not self.optical_connected[optical_id]:

                    if "DO3" not in log.codes:
                        log.add_codes("DO3", ":Optical DATA: Optical Installed: ")
                    
                    log.add("DO3", "")
                    self.optical_connected[optical_id]=True
                elif not opticalsensor.installed() and self.optical_connected[optical_id]:

                    if "EO0" not in log.codes:
                        log.add_codes("EO0", ":Optical ERROR: Optical Disconnected: ")

                    log.add("EO0", "")
                    self.optical_connected[optical_id]=False

                if opticalsensor.is_near_object():

                    if not self.optical_object[optical_id]:

                        if "DO1" not in log.codes:
                            log.add_codes("DO1", ":Optical DATA: Optical Detected Object.: ")

                        log.add("DO1", "")
                        self.optical_object[optical_id]=True

                    if not (self.optical_color[optical_id] >= opticalsensor.hue() - log.tolrance and self.optical_color[optical_id] <= opticalsensor.hue() + log.tolrance):

                        if "DO0" not in log.codes:
                            log.add_codes("DO0", ":Optical DATA: Color Changed. Color: ")

                        log.add("DO0", opticalsensor.hue())
                        self.optical_color[optical_id]=opticalsensor.hue()
                        
                elif not opticalsensor.is_near_object() and self.optical_object[optical_id]:

                    if "DO2" not in log.codes:
                        log.add_codes("DO2", ":Optical DATA: Optical Lost Object.: ")

                    log.add("DO2", "")
                    self.optical_object[optical_id]=False
                    self.optical_color[optical_id]=0

            def inertial(self, inertialsensor):
                """Capture for inertal sensor. Enter inertial sensor to log."""
    
                if inertialsensor.is_calibrating() and not self.inertial_calibrating:

                    if "DI2" not in log.codes:
                        log.add_codes("DI2", ":Inertial DATA: Calibrating.: ")

                    log.add("DI2", "")
                    self.inertial_calibrating=True
                elif not inertialsensor.is_calibrating() and self.inertial_calibrating:

                    if "DI3" not in log.codes:
                        log.add_codes("DI3", ":Inertial DATA: Calibration Complete.: ")

                    log.add("DI3", "")
                    self.inertial_calibrating=False

                if inertialsensor.installed() and not self.inertial_connected:

                    if "DI7" not in log.codes:
                        log.add_codes("DI7", ":Inertial DATA: Inertial Installed: ")

                    log.add("DI7", "")
                    self.inertial_connected=True
                elif not inertialsensor.installed() and self.inertial_connected:

                    if "EI0" not in log.codes:
                        log.add_codes("EI0", ":Inertial ERROR: Inertial Disconnected.: ")

                    log.add("EI0", "")
                    self.inertial_connected=False

                if not (self.inertial_rotation_history >= inertialsensor.rotation() - self.inertial_gyro_tolerance and self.inertial_rotation_history <= inertialsensor.rotation() + self.inertial_gyro_tolerance):

                    if "DI0" not in log.codes:
                        log.add_codes("DI0", ":Inertial DATA: Rotation Changed. Rotation: ")

                    log.add("DI0", int(inertialsensor.rotation()))
                    self.inertial_rotation_history= inertialsensor.rotation()

                if not (self.inertial_roll_history >= inertialsensor.orientation(OrientationType.ROLL, DEGREES) - self.inertial_gyro_tolerance and self.inertial_roll_history <= inertialsensor.orientation(OrientationType.ROLL, DEGREES) + self.inertial_gyro_tolerance):

                    if "DI2" not in log.codes:
                        log.add_codes("DI2", ":Inertial DATA: Roll Changed. Roll: ")

                    log.add("DI2", int(inertialsensor.orientation(OrientationType.ROLL, DEGREES)))
                    self.inertial_roll_history= inertialsensor.orientation(OrientationType.ROLL, DEGREES)

                if not (self.inertial_pitch_history >= inertialsensor.orientation(OrientationType.PITCH, DEGREES) - self.inertial_gyro_tolerance and self.inertial_pitch_history <= inertialsensor.orientation(OrientationType.PITCH, DEGREES) + self.inertial_gyro_tolerance):

                    if "DI3" not in log.codes:
                        log.add_codes("DI3", ":Inertial DATA: Roll Changed. Roll: ")

                    log.add("DI3", int(inertialsensor.orientation(OrientationType.PITCH, DEGREES)))
                    self.inertial_pitch_history= inertialsensor.orientation(OrientationType.PITCH, DEGREES)
                
                if not (self.inertial_heading_history >= inertialsensor.heading() - self.inertial_gyro_tolerance and self.inertial_heading_history <= inertialsensor.heading() + self.inertial_gyro_tolerance):

                    if "DI1" not in log.codes:
                        log.add_codes("DI1", ":Inertial DATA: Heading Changed. Heading: ")

                    log.add("DI1", int(inertialsensor.heading()))
                    self.inertial_heading_history= inertialsensor.heading()
                
                if not (self.inertial_x_axis_history >= inertialsensor.acceleration(AxisType.XAXIS) - self.inertial_axis_tolerance and self.inertial_x_axis_history <= inertialsensor.acceleration(AxisType.XAXIS) + self.inertial_axis_tolerance):

                    if "DI4" not in log.codes:
                        log.add_codes("DI4", ":Inertial DATA: X Axis Changed. Acceleration: ")

                    log.add("DI4", round(inertialsensor.acceleration(AxisType.XAXIS), 2))
                    self.inertial_x_axis_history= inertialsensor.acceleration(AxisType.XAXIS)
                
                if not (self.inertial_y_axis_history >= inertialsensor.acceleration(AxisType.YAXIS) - self.inertial_axis_tolerance and self.inertial_y_axis_history <= inertialsensor.acceleration(AxisType.YAXIS) + self.inertial_axis_tolerance):

                    if "DI5" not in log.codes:
                        log.add_codes("DI5", ":Inertial DATA: Y Axis Changed. Acceleration: ")

                    log.add("DI5", round(inertialsensor.acceleration(AxisType.YAXIS), 2))
                    self.inertial_y_axis_history= inertialsensor.acceleration(AxisType.YAXIS)

                if not (self.inertial_z_axis_history >= inertialsensor.acceleration(AxisType.ZAXIS) - self.inertial_axis_tolerance and self.inertial_z_axis_history <= inertialsensor.acceleration(AxisType.ZAXIS) + self.inertial_axis_tolerance):

                    if "DI6" not in log.codes:
                        log.add_codes("DI6", ":Inertial DATA: Z Axis Changed. Acceleration: ")
                        
                    log.add("DI6", round(inertialsensor.acceleration(AxisType.ZAXIS), 2))
                    self.inertial_z_axis_history= inertialsensor.acceleration(AxisType.ZAXIS)

            def distance(self, distancesensor):
                pass

            def rotation(self, rotationsensor):
                """Capture for a rotation sensor. Enter rotation sensor to log"""

                rotaion_id=id(rotationsensor)

                if rotaion_id not in self.rotation_angle_history:
                    self.rotation_angle_history[rotaion_id]=0
                if rotaion_id not in self.rotation_position_history:
                    self.rotation_position_history[rotaion_id]=0
                if rotaion_id not in self.rotation_connection:
                    self.rotation_connection[rotaion_id]=True
                
                if rotationsensor.installed() and self.rotation_connection[rotaion_id]==False:

                    if "DR0" not in log.codes:
                        log.add_codes("DR0", ":Rotation DATA: Rotation Installed.: ")

                    log.add("DR0", "")
                    self.rotation_connection[rotaion_id]=True
                elif not rotationsensor.installed() and self.rotation_connection[rotaion_id]==True:

                    if "ER0" not in log.codes:
                        log.add_codes("ER0", ":Rotation ERROR: Rotation Disconnected.: ")

                    log.add("ER0", "")
                    self.rotation_connection[rotaion_id]=False
                
                if not (self.rotation_angle_history[rotaion_id] >= rotationsensor.angle() - log.tolrance and self.rotation_angle_history[rotaion_id] <= rotationsensor.angle() + log.tolrance):

                    if "DR1" not in log.codes:
                        log.add_codes("DR1", ":Rotation DATA: Angle Changed. Angle: ")

                    log.add("DR1", rotationsensor.angle())
                    self.rotation_angle_history[rotaion_id]= rotationsensor.angle()
                
                if not (self.rotation_position_history[rotaion_id] >= rotationsensor.position() - log.tolrance and self.rotation_position_history[rotaion_id] <= rotationsensor.position() + log.tolrance):

                    if "DR2" not in log.codes:
                        log.add_codes("DR2", ":Rotation DATA: Position Changed. Position: ")

                    log.add("DR2", rotationsensor.position())
                    self.rotation_position_history[rotaion_id]= rotationsensor.position()
            
        
        class Threewire:
            def __init__(self):
                self.digital_value={}
                self.analog_value={}
            
            def digitalinput(self, input):
                """Capture for digital input. Enter Digital input to log."""

                input_id=id(input)

                if input_id not in self.digital_value:
                    self.digital_value[input_id]=0

                if input.value()==1 and self.digital_value[input_id]==0:
                    if "DDI0" not in log.codes:
                        log.add_codes("DDI0", ":Digital DATA: Value High.: ")
                    log.add("DDI0", "")
                    self.digital_value[input_id]=1
                elif input.value()==0 and self.digital_value[input_id]==1:
                    if "DDI1" not in log.codes:
                        log.add_codes("DDI1", ":Digital DATA: Value Low.: ")
                    log.add("DDI1", "")
                    self.digital_value[input_id]=0

            def analog(self, input):
                """Capture for analog inputs. Enter analog input to log."""

                input_id=id(input)

                if input_id not in self.analog_value:
                    self.analog_value[input_id]=0

                if not (self.analog_value[input_id] >= input.value() - log.tolrance and self.analog_value[input_id] <= input.value() + log.tolrance):
                    if "DAI0" not in log.codes:
                        log.add_codes("DAI0", ":Analog DATA: Value Changed. Value: ")
                    log.add("DAI0", input.value())
                    self.analog_value[input_id]=input.value()
            
            def bumper(self, bumpersensor):
                """Capture for bumper switchs. Enter bumper to log."""

                bumper_id=id(bumpersensor)

                if bumper_id not in self.digital_value:
                    self.digital_value[bumper_id]=0

                if bumpersensor.value()==1 and self.digital_value[bumper_id]==0:
                    if "DBS0" not in log.codes:
                        log.add_codes("DBS0", ":Bumper DATA: Pressed.: ")
                    log.add("DBS0", "")
                    self.digital_value[bumper_id]=1
                elif bumpersensor.value()==0 and self.digital_value[bumper_id]==1:
                    if "DBS1" not in log.codes:
                        log.add_codes("DBS1", ":Bumper DATA: Released.: ")
                    log.add("DBS1", "")
                    self.digital_value[bumper_id]=0

            def limit(self, limitsensor):
                """Capture for limit switchs. Enter bumper to log."""

                limit_id=id(limitsensor)

                if limit_id not in self.digital_value:
                    self.digital_value[limit_id]=0

                if limitsensor.value()==1 and self.digital_value[limit_id]==0:
                    if "DLS0" not in log.codes:
                        log.add_codes("DLS0", ":Limit DATA: Pressed.: ")
                    log.add("DLS0", "")
                    self.digital_value[limit_id]=1
                elif limitsensor.value()==0 and self.digital_value[limit_id]==1:
                    if "DLS1" not in log.codes:
                        log.add_codes("DLS1", ":Limit DATA: Released.: ")
                    log.add("DLS1", "")
                    self.digital_value[limit_id]=0

            def potentiometer(self, sensor):
                """Capture for potentiometer inputs. Enter potentiometer input to log."""

                sensor_id=id(sensor)

                if sensor_id not in self.analog_value:
                    self.analog_value[sensor_id]=0

                if not (self.analog_value[sensor_id] >= sensor.angle() - log.tolrance and self.analog_value[sensor_id] <= sensor.angle() + log.tolrance):
                    if "DP0" not in log.codes:
                        log.add_codes("DP0", ":Potentiometer DATA: Value Changed. Value: ")
                    log.add("DP0", sensor.angle())
                    self.analog_value[sensor_id]=sensor.angle()

            def pwm(self, input):
                """
                Capture for pwm inputs. 
                Enter pwm input to log.

                Args:
                input= Pwm()
                """

                input_id=id(input)

                if input_id not in self.analog_value:
                    self.analog_value[input_id]=0

                if not (self.analog_value[input_id] >= input.value() - log.tolrance and self.analog_value[input_id] <= input.value() + log.tolrance):
                    if "DPW0" not in log.codes:
                        log.add_codes("DPW0", ":Pwm DATA: Value Changed. Value: ")
                    log.add("DPW0", input.value())
                    self.analog_value[input_id]=input.value()    

        def __init__(self):
            self.drivetrain=self.Drivetrain()
            self.smartport=self.Smartport()
            self.threewire=self.Threewire()
            self.system=self.System()
            # set for variables id.
            self.variables={}
            
            # Variables used to not have spam in log.  
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

        def battery(self):
            """
            Capture for the brains battery. 
            
            Args:
            None
            """

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
        
        def controller(self, controller):
            """
            Capture for the controllers. 
            Enter controller you wish to log. 
            
            Args:
            controller= Controller()
            """

            if not log.recording.record:  # Only logs when not recoding to save space on the recording file.
                if controller.axis1.position()!=0 and not (self.axis1 >= controller.axis1.position() - log.tolrance and self.axis1 <= controller.axis1.position() + log.tolrance):
                    log.add("DC1", "%s_Axis1 %d Moved"%(str(controller), controller.axis1.position()))
                    self.axis1=controller.axis1.position()
                elif 0 == controller.axis1.position() and self.axis1!=0:
                    log.add("DC1", "%s_Axis1 %d Moved"%(str(controller), 0))
                    self.axis1=0

            if log.recording.record:  # Uses more accurete logging when recording.
                if controller.axis2.position()!=0 and self.axis2 != controller.axis2.position():
                    log.add("DC1", "%s_Axis2 %d Moved"%(str(controller), controller.axis2.position()))
                    self.axis2=controller.axis2.position()
                elif 0 == controller.axis2.position() and self.axis2!=0:
                    log.add("DC1", "%s_Axis2 %d Moved"%(str(controller), 0))
                    self.axis2=0
            else:
                if controller.axis2.position()!=0 and not (self.axis2 >= controller.axis2.position() - log.tolrance and self.axis2 <= controller.axis2.position() + log.tolrance):
                    log.add("DC1", "%s_Axis2 %d Moved"%(str(controller), controller.axis2.position()))
                    self.axis2=controller.axis2.position()
                elif 0 == controller.axis2.position() and self.axis2!=0:
                    log.add("DC1", "%s_Axis2 %d Moved"%(str(controller), 0, ))
                    self.axis2=0

            if log.recording.record:  # Uses more accurete logging when recording.
                if controller.axis3.position()!=0 and self.axis3 != controller.axis3.position():
                    log.add("DC1", "%s_Axis3 %d Moved"%(str(controller), controller.axis3.position()))
                    self.axis3=controller.axis3.position()
                elif 0 == controller.axis3.position() and self.axis3!=0:
                    log.add("DC1", "%s_Axis3 %d Moved"%(str(controller), 0))
                    self.axis3=0
            else:
                if controller.axis3.position()!=0 and not (self.axis3 >= controller.axis3.position() - log.tolrance and self.axis3 <= controller.axis3.position() + log.tolrance):
                    log.add("DC1", "%s_Axis3 %d Moved"%(str(controller), controller.axis3.position()))
                    self.axis3=controller.axis3.position()
                elif 0 == controller.axis3.position() and self.axis3!=0:
                    log.add("DC1", "%s_Axis3 %d Moved"%(str(controller), 0))
                    self.axis3=0

            if not log.recording.record:  # Only logs when not recoding to save space on the recording file.
                if controller.axis4.position()!=0 and not (self.axis4 >= controller.axis4.position() - log.tolrance and self.axis4 <= controller.axis4.position() + log.tolrance):
                    log.add("DC1", "%s_Axis4 %d Moved"%(str(controller), controller.axis4.position()))
                    self.axis4=controller.axis4.position()
                elif 0 == controller.axis4.position() and self.axis4!=0:
                    log.add("DC1", "%s_Axis4 %d Moved"%(str(controller), 0))
                    self.axis4=0

            # Button logging for controller.

            if controller.buttonA.pressing() and self.button_a==True:
                log.add("DC0", "%s_Button A Pressed"%(str(controller)))
                self.button_a=False
            elif controller.buttonA.pressing()==False and self.button_a==False:
                log.add("DC0", "%s_Button A Released"%(str(controller)))
                self.button_a=True

            if controller.buttonB.pressing() and self.button_b==True:
                log.add("DC0", "%s_Button B Pressed"%(str(controller)))
                self.button_b=False
            elif controller.buttonB.pressing()==False and self.button_b==False:
                log.add("DC0", "%s_Button B Released"%(str(controller)))
                self.button_b=True

            if controller.buttonX.pressing() and self.button_x==True:
                log.add("DC0", "%s_Button X Pressed"%(str(controller)))
                self.button_x=False
            elif controller.buttonX.pressing()==False and self.button_x==False:
                log.add("DC0", "%s_Button X Released"%(str(controller)))
                self.button_x=True

            if controller.buttonY.pressing() and self.button_y==True:
                log.add("DC0", "%s_Button Y Pressed"%(str(controller)))
                self.button_y=False
            elif controller.buttonY.pressing()==False and self.button_y==False:
                log.add("DC0", "%s_Button Y Released"%(str(controller)))
                self.button_y=True

            if controller.buttonUp.pressing() and self.button_up==True:
                log.add("DC0", "%s_Button UP Pressed"%(str(controller)))
                self.button_up=False
            elif controller.buttonUp.pressing()==False and self.button_up==False:
                log.add("DC0", "%s_Button UP Released"%(str(controller)))
                self.button_up=True

            if controller.buttonDown.pressing() and self.button_down==True:
                log.add("DC0", "%s_Button DOWN Pressed"%(str(controller)))
                self.button_down=False
            elif controller.buttonDown.pressing()==False and self.button_down==False:
                log.add("DC0", "%s_Button DOWN Released"%(str(controller)))
                self.button_down=True

            if controller.buttonLeft.pressing() and self.button_left==True:
                log.add("DC0", "%s_Button LEFT Pressed"%(str(controller)))
                self.button_left=False
            elif controller.buttonLeft.pressing()==False and self.button_left==False:
                log.add("DC0", "%s_Button LEFT Released"%(str(controller)))
                self.button_left=True

            if controller.buttonRight.pressing() and self.button_right==True:
                log.add("DC0", "%s_Button RIGHT Pressed"%(str(controller)))
                self.button_right=False
            elif controller.buttonRight.pressing()==False and self.button_right==False:
                log.add("DC0", "%s_Button RIGHT Released"%(str(controller)))
                self.button_right=True

            if controller.buttonL1.pressing() and self.button_L1==True:
                log.add("DC0", "%s_Button L1 Pressed"%(str(controller)))
                self.button_L1=False
            elif controller.buttonL1.pressing()==False and self.button_L1==False:
                log.add("DC0", "%s_Button L1 Released"%(str(controller)))
                self.button_L1=True

            if controller.buttonL2.pressing() and self.button_L2==True:
                log.add("DC0", "%s_Button L2 Pressed"%(str(controller)))
                self.button_L2=False
            elif controller.buttonL2.pressing()==False and self.button_L2==False:
                log.add("DC0", "%s_Button L2 Released"%(str(controller)))
                self.button_L2=True

            if controller.buttonR1.pressing() and self.button_R1==True:
                log.add("DC0", "%s_Button R1 Pressed"%(str(controller)))
                self.button_R1=False
            elif controller.buttonR1.pressing()==False and self.button_R1==False:
                log.add("DC0", "%s_Button R1 Released"%(str(controller)))
                self.button_R1=True

            if controller.buttonR2.pressing() and self.button_R2==True:
                log.add("DC0", "%s_Button R2 Pressed"%(str(controller)))
                self.button_R2=False
            elif controller.buttonR2.pressing()==False and self.button_R2==False:
                log.add("DC0", "%s_Button R2 Released"%(str(controller)))
                self.button_R2=True

        def variable(self, name, value):
            """
            Capture for int, float, and bool variables. 
            Enter name of variable in a string and then the variable you wish to log.
            
            Args:
            name= String
            value= Int, Boolean, Float
            """

            valueid=id(name)

            # Adds id if not in set.
            if valueid not in self.variables:

                if type(value)==bool:
                    self.variables[valueid]=False
                else:
                    self.variables[valueid]=0
            
            if value != self.variables[valueid]:
                log.add("DV0", "Variable %s Value %s"%(name, value))
                self.variables[valueid] = value


    class Recording:
        """
        Main class for recording.
        """

        def __init__(self):
            self.record=False  # Bool to see if recording
            self.Aton=""  # Used for name of file recording
            self.postlist=[] # Used for prossesing files.
            self.poststring="" # Used to store list to string.     

        def start(self, Aton):
            """
            Starts recording. 
            Enter name of file to start recording in.
            
            Args:
            Aton= String
            """

            filename=str(Aton) + "_pre.txt"

            if self.record == False:
                self.record= True
                brain.sdcard.savefile(filename, bytearray("\n", log.format))
                self.Aton= Aton + "_pre.txt"
                log.add("DA0", filename)

        def stop(self, Aton):
            """
            Stops recording. 
            Enter name of recording you wish to stop.
            
            Args:
            Aton= String
            """

            filename=str(Aton) + "_pre.txt"
            preatonfile=""
            self.record=False

            try:
                log.unloadcache()
                preatonfile=brain.sdcard.loadfile(filename).decode(log.format)
                preatonlist=preatonfile.split("\n")
                for i in range(len(preatonlist)):
                    prelist=preatonlist[i].split(' ')
                    if ":Controller" in prelist:
                        self.postlist.append(str(prelist) + "\n")
                for i in range(len(self.postlist)):
                    self.poststring+= str(self.postlist[i])
                brain.sdcard.savefile(filename, bytearray(str(self.poststring), log.format))
            
            except MemoryError:
                preatonfile=""
                brain.sdcard.savefile("Overflow.txt")
                with open(filename, 'r') as file:
                    for line in file:
                        prelist=line.split(' ')
                        if ":Controller" in prelist:
                            brain.sdcard.appendfile("Overflow.txt", bytearray(str(prelist) + "\n", log.format))
                brain.sdcard.savefile(filename)
                with open("Overflow.txt", 'r') as file:
                    for line in file:
                        brain.sdcard.appendfile(filename, bytearray(line, log.format))
                #brain.sdcard.savefile("Overflow.txt")
                            

            log.add("DA1", filename)

        def encode(self, Aton, right, left, other1start=none, other1stop=none, other1button=none, other2start=none, other2stop=none, other2button=none, other3start=none, other3stop=none, other3button=none, other4start=none, other4stop=none, other4button=none, other5start=none, other5stop=none, other5button=none, other6start=none, other6stop=none, other6button=none):   
            """
            Encodes the recording to python executable str in .txt file. 
            Enter recording you wish to encode.
            Also the right side drive funtion, left side drive funtion the any other funtions start, stop, and button to call funtion.

            Args:
            Aton= String
            right= Funtion
            left= Funtion
            otherXstart= Funtion (optional, X is place holder from 1, 6)
            otherXstop= Funtion (optional, X is place holder from 1, 6)
            otherXbutton= String (optional, X is place holder from 1, 6)
            """
            
            filename=Aton + ".txt"
            self.record=False
            brain.sdcard.savefile(filename)
            prelist=[]  # Used for general prosessing

            # Takes funtions input and makes them useable for encoding.
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
                            
                            # Gets the wait between actions.
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
                                        brain.sdcard.appendfile(filename, bytearray("%s(%s), "%(str(left[1]), str(prelist[10]).replace("'", '')), log.format))
                                    elif "1_Axis2" in str(prelist):
                                        brain.sdcard.appendfile(filename, bytearray("%s(%s), "%(str(right[1]), str(prelist[10]).replace("'", '')), log.format))

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
                                
                                # Gets the wait between actions.
                                if len(prelist2) >= 3:
                                    brain.sdcard.appendfile(filename, bytearray("wait(" + str(abs(int(prelist[2].replace("[", '').replace("]", '').replace("'", '').replace("'", '').replace(",", '')) - int(prelist2[2].replace("[", '').replace("]", '').replace("'", '').replace("'", '').replace(",", '')))) + ", MSEC), ", log.format))
            
            log.archive.recording(Aton + "_pre.txt")
            log.add("DA2", filename)
            print("Encode done.")            
        
        def run(self, Aton):
            """
            Runs encoded file. 
            Enter file to run.
            
            Args:
            Aton= String
            """

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
        """
        Main object for archiving files made by CLEAR.
        """

        def __init__(self):
            self.format="utf-8"
        
        def log(self):
            """
            Archives the Log.txt file.
            
            Args:
            None
            """

            speed=log_time.time()
            archivelist=""
            try:
                log.adding=False
                reversecodes={value: key for key, value in log.codes.items()}
                logfile=brain.sdcard.loadfile("Log.csv").decode(log.format)
                loglist=logfile.split("\n")
                for i in range(len(loglist)):
                    logline=loglist[i].split(':')
                    print("For code Split took: ", log_time.time()-speed)
                    if len(logline)>=4:
                        loglines= ":" + str(logline[1]) + ":" + str(logline[2]) + ": "
                        archivelist+=str(logline[0]) + str(reversecodes.get(loglines)) + str(logline[3]) + '\n'
                brain.sdcard.appendfile("loghistory.txt", bytearray(archivelist, log.format))
                log.clear()
                log.adding=True
                del logfile, reversecodes, loglist, i, logline, archivelist
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
                del reversecodes, loglist, i, logline, archivelist
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
                del reversecodes, loglist, i, logline, archivelist
            log.add("DS1", str(log_time.time() - speed) + " MSEC")
            del speed

        def recording(self, recordingname):
            """
            Archives recording file. 
            Enter full name of file.

            Args:
            recordingname= String
            """

            print("Archiving...")
            filename=str(recordingname).replace(".txt", "_archived.txt")
            brain.sdcard.savefile(filename)
            with open(recordingname, 'r') as recording:
                for line in recording:
                    prelist=line.split(' ')
                    brain.sdcard.appendfile(filename, bytearray("%s %s %s %s \n" %(prelist[2], prelist[9], prelist[10], prelist[11]), log.format))
            brain.sdcard.savefile(recordingname)
            log.add("DS3", recordingname)

        def index_history(self):
            """
            Gets lines of loghistory puts number in file.
            
            Args:
            None
            """

            speed=log_time.time()
            index=0
            with open("loghistory.txt", 'r') as file:
                for line in file:
                    index+=1
            brain.sdcard.savefile("index.txt", bytearray(str(index), log.format))
            log.add("DS2", str(log_time.time() - speed) + " MSEC")
            del speed, index


        def recall_log(self,):
            """
            Unarchives The log.

            Args:
            None
            """

            filename=("logrecalled.txt")
            print("recalling")
            try:
                file=brain.sdcard.loadfile("loghistory.txt").decode(log.format)
                brain.sdcard.savefile(filename)
                filelist=file.split(',')
                for i in range(len(filelist)):
                    prelist=filelist[i].split(' ')
                    if len(prelist) >= 5:
                        brain.sdcard.appendfile(filename, bytearray(str(prelist[0]) + " " + str(prelist[1]) + " " + str(prelist[2]) + " " + str(log.codes.get(prelist[3])) + str(prelist[4 : len(prelist)-1]) + "\n", log.format))
                print("Recall done.")
            except MemoryError: # Same thing as the last three exceptions.
                with open("loghistory.txt", 'r') as file:
                    for line in file:
                        prelist=line.split(' ')
                        if len(prelist) >= 5:
                            brain.sdcard.appendfile(filename, bytearray(str(prelist[0]) + " " + str(prelist[1]) + " " + str(prelist[2]) + " " + str(log.codes.get(prelist[3])) + str(prelist[4 : len(prelist)-1]) + "\n", log.format))
                print("Recall done.")
        
        def recall_recording(self, name):
            """
            Restores recording file to an uncompressed state. 
            Enter full name of the archived file.

            Args:
            name=String, full name of file
            """

            recording=brain.sdcard.loadfile(name).decode(log.format).split('\n')
            filename=name.replace("_archived.txt", ".txt")
            brain.sdcard.savefile(filename)
            for item in recording:
                prelist=item.split(' ')
                print(prelist)
                if "Moved" in item:
                    brain.sdcard.appendfile(filename, bytearray("[',', '0', %s ':Controller', 'DATA:', 'Axis', 'Changed.', 'Axis:', '', %s %s 'Moved', '0', 'Degrees', ''] \n"%(prelist[0], prelist[1], prelist[2]), log.format))
                elif "Pressed" in item or "Released" in item:
                    brain.sdcard.appendfile(filename, bytearray("[',', '0', %s ':Controller', 'DATA:', 'Button', 'Changed.', 'Button:', '', %s %s %s ''] \n"%(prelist[0], prelist[1], prelist[2], prelist[3]), log.format))
            log.add("DS5", name)
                

    def __init__(self):
        self.capture=self.Capture()
        self.recording=self.Recording()
        self.archive=self.Archive()
        self.index=0
        self.adding=True  # Used to pause logging.
        self.format="utf-8"  # General format for all files in the code.
        self.cache=""
        self.brainscreen=False  # Used to see if need to print to brain screen.
        self.tolrance=3  # tolerance for controller stick diffrence when not recording and for general tolrance for sensors.
        self.manual_control=False

        brain.sdcard.savefile("Logstart.txt")  # Clears Logstart file for refresh of instructions in it.

        # Predefined Log Codes dictionary
        self.codes={
            """Main dictionary for CLEAR"""
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
                    "DS0": ":System DATA: Init setup complete.: ",
                    "DS1": ":System DATA: Archive Log complete. Time: ",
                    "DS2": ":System DATA: Index Log History complete. Time: ",
                    "DS3": ":System DATA: Archive Recording complete. Time: ",
                    "DS5": ":System DATA: Recalled Recording complete. Recording: ",
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
                    "DC0": ":Controller DATA: Button Changed. Button: ",
                    "DC1": ":Controller DATA: Axis Changed. Axis: ",
                }
        
        # Setting up Log Files if they dont exist and setting index.
        log_lines=[]
        log_number=0
        if not brain.sdcard.exists("Log.csv"):
            brain.sdcard.savefile("Log.csv", bytearray("log Start: \n", self.format))
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
            except OSError: # Same as the memory error but for an os error that works the same way.
                print("Log.csv cannot be decoded trying step open.")
                log_lines=[]
                with open("Log.csv", 'r') as log_file:
                    for line in log_file:
                        log_number+=1
                print("Log done")
            if not brain.sdcard.exists("loghistory.txt"):
                brain.sdcard.savefile("loghistory.txt")
            
            if not brain.sdcard.exists("index.txt"):
                brain.sdcard.savefile("index.txt", bytearray("0", self.format))

            historyindex=int(brain.sdcard.loadfile("index.txt").decode(self.format))

            self.index=len(log_lines) + log_number + historyindex - 1

            # Clears lists to free memory.
            del log_lines, log_number

    def unloadcache(self): # This is only ment for the recording.
        """
        When cache has items in it put them in the Log and the recording file.

        Args:
        None
        """
        if self.cache!="":
            brain.sdcard.appendfile(self.recording.Aton, bytearray(self.cache, self.format))
            brain.sdcard.appendfile("Log.csv", bytearray(self.cache, self.format))
            self.cache=""
            print("Unloaded cache")

    def add(self, add_code, add_details):
        """
        Main funtion for Log.

        Takes code and the added details gets runtime and index. 
        Then, prints it, puts them in Log or cache, and see if it needs to print to brain screen. 
        Enter code then the details you want as a string.

        Args:
        add_code= String
        add_details= String
        """

        if not self.adding:
            return

        entry = ", %d [%d] %s %s \n" % (self.index, log_time.time(), self.codes.get(add_code), add_details)       
        print(entry)
        if self.recording.record:
            self.cache += entry
        else:
            brain.sdcard.appendfile("Log.csv", bytearray(entry, self.format))

        if self.brainscreen:  # Checks if pinting to brainscreen is enabled.

            if brain.screen.row()>=20:  # Checks if at end of screen row
                brain.screen.clear_screen()
                brain.screen.set_cursor(1,1)

            brain.screen.print(entry)
            brain.screen.new_line()
        self.index += 1
        
    def add_codes(self, code_add, Decoded_text):
        """
        Adds codes to the codes dictionary. 
        Enter new code key, then the full string.

        Args:
        code_add= String
        Decoded_text= String
        """

        self.codes.update({code_add : "%s"%(Decoded_text)})

    def remove_codes(self, code_remove):
        """
        Removes codes from dictionary.
        Enter code key to remove.

        Args:
        code_remove= String
        """

        if code_remove in self.codes:
            self.codes.pop(code_remove)
        else:
            print("Code Not Found In Log Codes")

    def edit_codes(self, code_edit, new_decoded_text):
        """
        Edits existing codes in dictionary. 
        Enter code key and then new full string
        
        Args:
        code_edit= String
        new_decoded_text= String
        """

        if code_edit in self.codes:
            self.codes.update({code_edit : "%s"%(new_decoded_text)})

    # Clearing the log file
    def clear(self):
        """
        Clears the Log.csv file.
        
        Args:
        None
        """

        brain.sdcard.savefile("Log.csv", bytearray("Log Start: \n", self.format))
    
    # Displaying log codes dictionary
    def table(self):
        """
        Prints codes dictionary.

        Args:
        None
        """

        print(self.codes)

    def read(self):
        """
        Prints the Log.csv file. 
        
        Args:
        None
        """

        log_content=brain.sdcard.loadfile("Log.csv")
        print(log_content.decode(self.format))
    
    def logstart(self, *drivemotors, drivetrain=None, drivetraintype=None, controller1=None, controller2=None, brainread=False, **othermotors):
        """
        Main way to use CLEAR.
         
        Enter drivetrain motors going right, left from front to back. for a six motor.
        if four or two drivetrain enter the drivetrain in drivetrain= and enter in drivetraintype how many motors are in there.
        Then, add genaric smart motors by entering "motor1=___, motor2=___, etc.". 
        Optional: Enter controller1 and controller2 like "controller1=___, etc.". 
        Next, if you want brain read enter "brainread=True". 
        If you want to not index the history when it gets to big by entering "indexhistory=False".
        Last thing is using the "add_logstart()" function for variables and other things.

        Args:
        *drivemotors=motors() (optional)
        drivetrain=drivetrain() (optional)
        drivetraintype=strings "Four", or "Two" (optional)
        controller1=controller (Optional)
        controller2=controller (Optional)
        brainread= bool (optional)
        **othermotors=  motor1=motor, etc (optional)
        """
        self.manual_control=True

        if brainread:
            brain.screen.set_font(FontType.MONO12)
            self.brainscreen=True

        # Loads extra funtions from file.
        try:    
            addedfuntion=brain.sdcard.loadfile("Logstart.txt").decode(self.format)
        except AttributeError:
            addedfuntion=""

        self.archive.log()
        self.archive.index_history()

        # Logs system start.
        self.add("DS0", 0)
        
        while True:
            for i in range(10):
                for i in range(20):
                    speed2=log_time.time()

                    if not self.recording.record:
                        self.capture.battery()

                    if controller1 != None:
                        self.capture.controller(controller1)

                    if controller2!= None and not self.recording.record:
                        self.capture.controller(controller2)
                    
                    # Checks for how much motors there are and does the proper funtion.
                    if drivetrain!= None:
                        self.capture.drivetrain.standerd(drivetrain, drivetraintype)
                    else:
                        self.capture.drivetrain.six_motor(*drivemotors)

                    for key, motor in othermotors.items():
                        if "motor" in key:
                            self.capture.smartport.motor(motor)
                        else:
                            raise NameError("Keyword argument not valid use motor1=, motor2=, etc. for the other motors.")
                    
                    if not self.recording.record:
                        try:
                            exec(addedfuntion)
                        except Exception as e:
                            sys.print_exception(e) # type: ignore

                    if not self.recording.record:
                        wait(200 - (log_time.time() - speed2), MSEC)
                    else:
                        wait(2, MSEC)
                    
                gc.collect()

            self.unloadcache()
    
    def add_logstart(self, funtion):
        """
        Used in logstart. 
        Enter the funtion for variables like so "log.capture.variable()" then in the inner parentheses add the name of variable as a string and the variable. 
        Can also be used for any capture funtion in CLEAR.

        Args:
        funtion= Funtion for object Log
        """

        brain.sdcard.appendfile("Logstart.txt" , bytearray(funtion + ", ", self.format))
        
    def auto_start(self, brainread=False):
        """
        An easy way to use the log start.
        all that is needed if to call it but if you want you can make it print to the brain by adding True in the input.

        Args:
        brainread=Bool(optional)
        """

        if brainread:
            brain.screen.set_font(FontType.MONO12)
            self.brainscreen=True

        self.archive.log()
        self.archive.index_history()

        # Logs system start.
        self.add("DS0", 0)
        
        globallogging= dir()

        for item in globallogging:
            if self.manual_control:
                break
            print(item)
            print(type(eval(item)))
            print("")

            item_type=str(type(eval(item)))

            if  item_type == "<class 'int'>" or item_type == "<class 'bool'>" or item_type == "<class 'float'>":
                log.add_logstart("log.capture.variable('%s', %s)"%(item, item.replace("'", "")))
            elif item_type == "<class 'motor'>":
                log.add_logstart("log.capture.smartport.motor(%s)"%(item.replace("'", "")))
            elif item_type == "<class 'controller'>":
                log.add_logstart("log.capture.controller(%s)"%(item.replace("'", "")))
            elif item_type == "<class 'inertial'>":
                log.add_logstart("log.capture.smartport.inertial(%s)"%(item.replace("'", "")))
            elif item_type == "<class 'optical'>":
                log.add_logstart("log.capture.smartport.optical(%s)"%(item.replace("'", "")))
            elif item_type == "<class 'rotation'>":
                log.add_logstart("log.capture.smartport.rotation(%s)"%(item.replace("'", "")))
            elif item_type == "<class 'triport_bumper'>":
                log.add_logstart("log.capture.threewire.bumper(%s)"%(item.replace("'", "")))
            elif item_type == "<class 'triport_limit'>":
                log.add_logstart("log.capture.threewire.limit(%s)"%(item.replace("'", "")))
            elif item_type == "<class 'triport_digitalin'>":
                log.add_logstart("log.capture.threewire.digitalinput(%s)"%(item.replace("'", "")))
            elif item_type == "<class 'triport_potv2'>":
                log.add_logstart("log.capture.threewire.potentiometer(%s)"%(item.replace("'", "")))
            elif item_type == "<class 'triport_analog'>":
                log.add_logstart("log.capture.threewire.analog(%s)"%(item.replace("'", "")))
        
        wait(20, MSEC)
        print("DONE!!!")

        # Loads extra funtions from file.
        try:    
            addedfuntion=brain.sdcard.loadfile("Logstart.txt").decode(self.format)
        except AttributeError:
            addedfuntion=""
        
        while True:
            if self.manual_control:
                break

            for i in range(10):

                for i in range(20):

                    speed2=log_time.time()

                    if not self.recording.record:
                        self.capture.battery()
                        self.capture.system.memoryuse()
                        self.capture.system.modules()

                    try:
                        exec(addedfuntion)
                    except Exception as e:
                        sys.print_exception(e) # type: ignore
                    
                    if not self.recording.record:
                        wait(200 - (log_time.time() - speed2), MSEC)
                    else:
                        wait(2, MSEC)
                    
                gc.collect()

            self.unloadcache()

log=Log()