# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       CLEAR.py                                                     #
# 	Author:       Micah Bow                                                    #
# 	Created:      1/27/2026, 12:42 PM                                          #
#   Last Edited:  3/22/2026, 2:00 PM                                           #
# 	Description:  Capture, Logging, Encoding, Archiving, Recording.            #
#                                                                              #
# ---------------------------------------------------------------------------- #
from vex import *
    
import gc, sys, uasyncio, ustruct  # type: ignore

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
                self.modulelist={}
                self.memory=0
                self.currentMemory=0
                self.memory_tolrance=int(str(settings.settings.get('memory_tolrance_KB ')))
                self.aton=False
                self.driver=False
                self.comp_switch=False
                self.field=False

            def memoryuse(self) -> None:
                self.currentMemory=gc.mem_alloc()/1000  # type: ignore
                if not (self.memory >= self.currentMemory - self.memory_tolrance and self.memory <= self.currentMemory + self.memory_tolrance):
                    if "DSM0" not in log.codes:
                        log.add_codes("DSM0", ":Memory DATA: Memory Useage Changed. Memory Used: ")
                    log.add("DSM0", str(self.currentMemory) + " KB")
                    self.memory=self.currentMemory
            
            def modules(self) -> None:
                if self.modulelist != sys.modules:
                    if "DSP0" not in log.codes:
                        log.add_codes("DSP0", ":System DATA: New module(s) added. Module(s): ")
                    filtered_list = [item for item in sys.modules if item not in self.modulelist]
                    log.add("DSP0", filtered_list)
                    self.modulelist= sys.modules.copy()
            
            def control(self, comp: Competition):
                if comp.is_autonomous() and not self.aton:
                    if "DSC0" not in log.codes:
                        log.add_codes("DSC0", ":Competition DATA: Atonomous Started:")
                    log.add("DSC0", "")
                    self.aton=True
                    self.driver=False
                elif comp.is_driver_control() and not self.driver:
                    if "DSC1" not in log.codes:
                        log.add_codes("DSC1", ":Competition DATA: Driver Control Started:")
                    log.add("DSC1", "")
                    self.driver=True
                    self.aton=False
                elif comp.is_competition_switch() and not self.comp_switch:
                    if "DSC2" not in log.codes:
                        log.add_codes("DSC2", ":Competition DATA: Competition Connected:")
                    log.add("DSC2", "")
                    self.comp_switch=True
                elif not comp.is_field_control() and self.field:
                    if "DSC5" not in log.codes:
                        log.add_codes("DSC5", ":Competition DATA: Competition Disconnected:")
                    log.add("DSC5", "")
                    self.field=False
                elif comp.is_field_control() and not self.field:
                    if "DSC3" not in log.codes:
                        log.add_codes("DSC3", ":Competition DATA: Field Connected:")
                    log.add("DSC3", "")
                    self.field=True
                elif not comp.is_field_control() and self.field:
                    if "DSC4" not in log.codes:
                        log.add_codes("DSC4", ":Competition DATA: Field Disconnected:")
                    log.add("DSC4", "")
                    self.field=False

        class Smartport:
            def __init__(self):
                # Sets for other motors By there id.
                self.motor_temp_monitoring={} 
                self.motor_power_monitoring={}  
                self.motor_disconnected={}
                self.motor_current_monitoring={}
                self.setup={}
                self.optical_object={}
                self.optical_color={}
                self.optical_connected={}
                self.inertial_axis_tolerance=float(str(settings.settings.get('inertial_axis_tolrance_Gs ')))
                self.inertial_gyro_tolerance=int(str(settings.settings.get('inertial_gyro_tolrance_DEGREES ')))
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
                self.distance_tolrance=int(str(settings.settings.get('distance_tolrance_MM ')))
                self.distance_connection={}
                self.distance_object={}
                self.distance_history={}

            def motor(self, motor: Motor|None=None) -> None:
                """Capture for any general smart motor. Enter motor you wish to log as input. (Can take motor groups as well.)"""

                if motor!=None and motor not in log.Motors:
                    log.Motors.append(motor)

                for motor_ in log.Motors:
                    motor_id=str(motor_)
                    setup=self.setup
                    
                    # Setup id to sets if not there.
                    if motor_id not in setup:
                        self.motor_temp_monitoring[motor_id] = 0
                        self.motor_power_monitoring[motor_id] = 0
                        self.motor_current_monitoring[motor_id] = 0
                        self.motor_disconnected[motor_id] = False
                        self.setup[motor_id]=True

                    self.motor_temp:int=motor_.temperature(PERCENT)
                    self.current_motor_disconnected:int=self.motor_disconnected[motor_id]

                    if recording.record:
                        return

                    if self.motor_temp==2:
                        if not self.current_motor_disconnected:
                            log.add("EM1", "%s"%(motor_))
                            self.motor_disconnected[motor_id]=True
                        else:
                            return
                    elif self.motor_temp!=2 and self.current_motor_disconnected:
                        self.motor_disconnected[motor_id]=False

                    self.current_motor_current_monitoring:int=self.motor_current_monitoring[motor_id]
                    self.current_motor_temp_monitoring:int=self.motor_temp_monitoring[motor_id]
                    self.current_motor_power_monitoring:int=self.motor_power_monitoring[motor_id]
                    self.current_motor_power:int=int(motor_.power(PowerUnits.WATT))
                    self.current_motor_current:int=int(motor_.current(CurrentUnits.AMP) * 10)
                    
                    # Cheaks for the temps,  power, and cheaks for conecttions of motors(s).
                    if self.motor_temp<=50: 
                        if self.current_motor_temp_monitoring>0:
                            log.add("DM0", "Motor %s Temp %s"%(motor_, self.motor_temp))
                            self.motor_temp_monitoring[motor_id]=0
                    elif self.motor_temp>70: 
                        if (self.current_motor_temp_monitoring==0 or self.current_motor_temp_monitoring==2):
                            log.add("EM0", "Motor %s Temp %s"%(motor_, self.motor_temp))
                            self.motor_temp_monitoring[motor_id]=1  
                    elif self.motor_temp>50: 
                        if self.current_motor_temp_monitoring==0:
                            log.add("WM0", "Motor %s Temp %s"%(motor_, self.motor_temp))
                            self.motor_temp_monitoring[motor_id]=2
                    

                    if self.current_motor_power<=12: 
                        if self.current_motor_power_monitoring>0:
                            log.add("DM1", "Motor %s Power %s"%(str(motor_), str(self.current_motor_power)))
                            self.motor_power_monitoring[motor_id]=0
                    elif self.current_motor_power>20: 
                        if (self.current_motor_power_monitoring==0 or self.current_motor_power_monitoring==2):
                            log.add("EM2", "Motor %s Power %s"%(str(motor_), str(self.current_motor_power)))
                            self.motor_power_monitoring[motor_id]=1
                    elif self.current_motor_power>12: 
                        if self.current_motor_power_monitoring==0:
                            log.add("WM1", "Motor %s Power %s"%(str(motor_), str(self.current_motor_power)))
                            self.motor_power_monitoring[motor_id]=2

                    if self.current_motor_current<=15: 
                        if self.current_motor_current_monitoring>0:
                            log.add("DM2", "Motor %s Current %1.1f"%(str(motor_), float(self.current_motor_current)/10))
                            self.motor_current_monitoring[motor_id]=0
                    elif self.current_motor_current>20: 
                        if (self.current_motor_current_monitoring==0 or self.current_motor_current_monitoring==2):
                            log.add("EM3", "Motor %s Current %1.1f"%(str(motor_), float(self.current_motor_current)/10))
                            self.motor_current_monitoring[motor_id]=1
                    elif self.current_motor_current>15:
                        if self.current_motor_current_monitoring==0:
                            log.add("WM2", "Motor %s Current %1.1f"%(str(motor_), float(self.current_motor_current)/10))
                            self.motor_current_monitoring[motor_id]=2
            
            def optical(self, opticalsensor: Optical) -> None:
                """Capture for an optical sensor. Enter optical sensor to Capture."""

                self.optical_id=id(opticalsensor)

                if  self.optical_id not in self.optical_connected:
                    self.optical_connected[self.optical_id]=True

                if  self.optical_id not in self.optical_object:
                    self.optical_object[self.optical_id]=False

                if  self.optical_id not in self.optical_color:
                    self.optical_color[self.optical_id]=0
                
                if opticalsensor.installed() and not self.optical_connected[self.optical_id]:

                    if "DO3" not in log.codes:
                        log.add_codes("DO3", ":Optical DATA: Optical Installed: ")
                    
                    log.add("DO3", str(opticalsensor))
                    self.optical_connected[self.optical_id]=True
                elif not opticalsensor.installed() and self.optical_connected[self.optical_id]:

                    if "EO0" not in log.codes:
                        log.add_codes("EO0", ":Optical ERROR: Optical Disconnected: ")

                    log.add("EO0", str(opticalsensor))
                    self.optical_connected[self.optical_id]=False

                if opticalsensor.is_near_object():

                    if not self.optical_object[self.optical_id]:

                        if "DO1" not in log.codes:
                            log.add_codes("DO1", ":Optical DATA: Optical Detected Object.: ")

                        log.add("DO1", str(opticalsensor))
                        self.optical_object[self.optical_id]=True

                    if not (self.optical_color[self.optical_id] >= opticalsensor.hue() - log.tolrance and self.optical_color[self.optical_id] <= opticalsensor.hue() + log.tolrance):

                        if "DO0" not in log.codes:
                            log.add_codes("DO0", ":Optical DATA: Color Changed. Color: ")

                        log.add("DO0", str(opticalsensor.hue()) + " Sensor " + str(opticalsensor))
                        self.optical_color[self.optical_id]=opticalsensor.hue()
                        
                elif not opticalsensor.is_near_object() and self.optical_object[self.optical_id]:

                    if "DO2" not in log.codes:
                        log.add_codes("DO2", ":Optical DATA: Optical Lost Object.: ")

                    log.add("DO2", str(opticalsensor))
                    self.optical_object[self.optical_id]=False
                    self.optical_color[self.optical_id]=0

            def inertial(self, inertialsensor: Inertial) -> None:
                """Capture for inertal sensor. Enter inertial sensor to log."""
    
                if inertialsensor.installed():

                    self.heading=inertialsensor.heading()
                    self.rotation_values:int=inertialsensor.rotation()
                    self.acceleration_y=inertialsensor.acceleration(AxisType.YAXIS)
                    self.acceleration_z=inertialsensor.acceleration(AxisType.ZAXIS)
                    self.acceleration_x=inertialsensor.acceleration(AxisType.XAXIS)
                    self.pitch=inertialsensor.orientation(OrientationType.PITCH, DEGREES)
                    self.roll=inertialsensor.orientation(OrientationType.ROLL, DEGREES)


                    if not self.inertial_connected:
                        if "DI7" not in log.codes:
                            log.add_codes("DI7", ":Inertial DATA: Inertial Installed: ")

                        log.add("DI7", "")
                        self.inertial_connected=True

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

                    if not (self.inertial_rotation_history >= self.rotation_values - self.inertial_gyro_tolerance and self.inertial_rotation_history <= self.rotation_values + self.inertial_gyro_tolerance):

                        if "DI0" not in log.codes:
                            log.add_codes("DI0", ":Inertial DATA: Rotation Changed. Rotation: ")

                        log.add("DI0", int(self.rotation_values))
                        self.inertial_rotation_history= self.rotation_values

                    if not (self.inertial_roll_history >= self.roll - self.inertial_gyro_tolerance and self.inertial_roll_history <= self.roll + self.inertial_gyro_tolerance):

                        if "DI9" not in log.codes:
                            log.add_codes("DI9", ":Inertial DATA: Roll Changed. Roll: ")

                        log.add("DI9", int(self.roll))
                        self.inertial_roll_history= self.roll

                    if not (self.inertial_pitch_history >= self.pitch - self.inertial_gyro_tolerance and self.inertial_pitch_history <= self.pitch + self.inertial_gyro_tolerance):

                        if "DI8" not in log.codes:
                            log.add_codes("DI8", ":Inertial DATA: Pitch Changed. Pitch: ")

                        log.add("DI8", int(self.pitch))
                        self.inertial_pitch_history= self.pitch
                    
                    if not (self.inertial_heading_history >= self.heading - self.inertial_gyro_tolerance and self.inertial_heading_history <= self.heading + self.inertial_gyro_tolerance):

                        if "DI1" not in log.codes:
                            log.add_codes("DI1", ":Inertial DATA: Heading Changed. Heading: ")

                        log.add("DI1", int(self.heading))
                        self.inertial_heading_history= self.heading
                    
                    if not (self.inertial_x_axis_history >= self.acceleration_x - self.inertial_axis_tolerance and self.inertial_x_axis_history <= self.acceleration_x + self.inertial_axis_tolerance):

                        if "DI4" not in log.codes:
                            log.add_codes("DI4", ":Inertial DATA: X Axis Changed. Acceleration: ")

                        log.add("DI4", round(self.acceleration_x, 2))
                        self.inertial_x_axis_history= self.acceleration_x
                    
                    if not (self.inertial_y_axis_history >= self.acceleration_y - self.inertial_axis_tolerance and self.inertial_y_axis_history <= self.acceleration_y + self.inertial_axis_tolerance):

                        if "DI5" not in log.codes:
                            log.add_codes("DI5", ":Inertial DATA: Y Axis Changed. Acceleration: ")

                        log.add("DI5", round(self.acceleration_y, 2))
                        self.inertial_y_axis_history= self.acceleration_y

                    if not (self.inertial_z_axis_history >= self.acceleration_z - self.inertial_axis_tolerance and self.inertial_z_axis_history <= self.acceleration_z + self.inertial_axis_tolerance):

                        if "DI6" not in log.codes:
                            log.add_codes("DI6", ":Inertial DATA: Z Axis Changed. Acceleration: ")
                            
                        log.add("DI6", round(self.acceleration_z, 2))
                        self.inertial_z_axis_history= self.acceleration_z
                        
                elif self.inertial_connected:

                    if "EI0" not in log.codes:
                        log.add_codes("EI0", ":Inertial ERROR: Inertial Disconnected.: ")

                    log.add("EI0", "")
                    self.inertial_connected=False

                

            def distance(self, distancesensor: Distance) -> None:
                distance_id=id(distancesensor)

                if distance_id not in self.distance_connection:
                    self.distance_connection[distance_id]=True
                if distance_id not in self.distance_object:
                    self.distance_object[distance_id]=False
                if distance_id not in self.distance_history:
                    self.distance_history[distance_id]=0

                if distancesensor.installed() and not self.distance_connection[distance_id]:
                    if "DDS3" not in log.codes:
                        log.add_codes("DDS3", ":Distance DATA: Distance Installed.: ")
                    log.add("DDS3", str(distancesensor))
                    self.distance_connection[distance_id]=True
                elif not distancesensor.installed() and self.distance_connection[distance_id]:
                    if "EDS0" not in log.codes:
                        log.add_codes("EDS0", ":Distance ERROR: Distance Disconnected.: ")
                    log.add("EDS0", str(distancesensor))
                    self.distance_connection[distance_id]=False

                if distancesensor.is_object_detected():
                    if not self.distance_object[distance_id]:
                        if "DDS0" not in log.codes:
                            log.add_codes("DDS0", ":Distance DATA: Distance Detected Object.: ")

                        log.add("DDS0", distancesensor)
                        self.distance_object[distance_id]=True

                    if not (self.distance_history[distance_id] >= distancesensor.object_distance() - self.distance_tolrance and self.distance_history[distance_id] <= distancesensor.object_distance() + self.distance_tolrance):
                        if "DDS1" not in log.codes:
                            log.add_codes("DDS1", ":Distance DATA: Distance Changed. Distance: ")
                        log.add("DDS1", str(distancesensor.object_distance()) + " Sensor " + str(distancesensor))
                        self.distance_history[distance_id]=distancesensor.object_distance()
                elif not distancesensor.is_object_detected() and self.distance_object[distance_id]:
                    if "DDS4" not in log.codes:
                        log.add_codes("DDS4", ":Distance DATA: Distance Lost Object.: ")
                    log.add("DDS4", distancesensor)
                    self.distance_object[distance_id]=False

            def rotation(self, rotationsensor: Rotation) -> None:
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

                    log.add("DR0", str(rotationsensor))
                    self.rotation_connection[rotaion_id]=True
                elif not rotationsensor.installed() and self.rotation_connection[rotaion_id]==True:

                    if "ER0" not in log.codes:
                        log.add_codes("ER0", ":Rotation ERROR: Rotation Disconnected.: ")

                    log.add("ER0", str(rotationsensor))
                    self.rotation_connection[rotaion_id]=False
                
                if not (self.rotation_angle_history[rotaion_id] >= rotationsensor.angle() - log.tolrance and self.rotation_angle_history[rotaion_id] <= rotationsensor.angle() + log.tolrance):

                    if "DR1" not in log.codes:
                        log.add_codes("DR1", ":Rotation DATA: Angle Changed. Angle: ")

                    log.add("DR1", str(rotationsensor.angle()) + " Sensor " + str(rotationsensor))
                    self.rotation_angle_history[rotaion_id]= rotationsensor.angle()
                
                if not (self.rotation_position_history[rotaion_id] >= rotationsensor.position() - log.tolrance and self.rotation_position_history[rotaion_id] <= rotationsensor.position() + log.tolrance):

                    if "DR2" not in log.codes:
                        log.add_codes("DR2", ":Rotation DATA: Position Changed. Position: ")

                    log.add("DR2", str(rotationsensor.position()) + " Sensor " + str(rotationsensor))
                    self.rotation_position_history[rotaion_id]= rotationsensor.position()
            
        
        class Threewire:
            def __init__(self):
                self.digital_value={}
                self.analog_value={}
            
            def digitalinput(self, input: DigitalIn) -> None:
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

            def analog(self, input: AnalogIn) -> None:
                """Capture for analog inputs. Enter analog input to log."""

                input_id=id(input)

                if input_id not in self.analog_value:
                    self.analog_value[input_id]=0

                if not (self.analog_value[input_id] >= input.value() - log.tolrance and self.analog_value[input_id] <= input.value() + log.tolrance):
                    if "DAI0" not in log.codes:
                        log.add_codes("DAI0", ":Analog DATA: Value Changed. Value: ")
                    log.add("DAI0", input.value())
                    self.analog_value[input_id]=input.value()
            
            def bumper(self, bumpersensor: Bumper) -> None:
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

            def limit(self, limitsensor: Limit) -> None:
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

            def potentiometer(self, sensor: PotentiometerV2) -> None:
                """Capture for potentiometer inputs. Enter potentiometer input to log."""

                sensor_id=id(sensor)

                if sensor_id not in self.analog_value:
                    self.analog_value[sensor_id]=0

                if not (self.analog_value[sensor_id] >= sensor.angle() - log.tolrance and self.analog_value[sensor_id] <= sensor.angle() + log.tolrance):
                    if "DP0" not in log.codes:
                        log.add_codes("DP0", ":Potentiometer DATA: Value Changed. Value: ")
                    log.add("DP0", sensor.angle())
                    self.analog_value[sensor_id]=sensor.angle()

            def pwm(self, input: Pwm) -> None:
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
            self.smartport=self.Smartport()
            self.threewire=self.Threewire()
            self.system=self.System()
            # set for variables id.
            self.variables={}
            self.valueid=0
            
            # Variables used to not have spam in log.  
            self.battery_voltage_monitoring=0
            self.battery_capacity_monitoring=0
            self.battery_current_monitoring=0
            self.battery_watt_monitoring=0
            self.battery_temp_monitoring=0
            self.voltage:int=0
            self.current:int=0
            self.capacity:int=0
            self.watts:int=0
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
            self.button_objs=[]
            self.button_names = [
                "A", "B", "X", "Y",
                "UP", "DOWN", "LEFT", "RIGHT",
                "L1", "L2", "R1", "R2",
            ]
            self.button_values = [
                self.button_a,
                self.button_b,
                self.button_x,
                self.button_y,
                self.button_up,
                self.button_down,
                self.button_left,
                self.button_right,
                self.button_L1,
                self.button_L2,
                self.button_R1,
                self.button_R2,
            ]

        def battery(self) -> None:
            """
            Capture for the brains battery. 
            
            Args:
            None
            """

            self.voltage:int=int(brain.battery.voltage(VoltageUnits.VOLT))
            self.current:int=brain.battery.current(CurrentUnits.AMP)
            self.capacity:int=brain.battery.capacity()
            self.watts:int=int(brain.battery.current(CurrentUnits.AMP)) * int(brain.battery.voltage(VoltageUnits.VOLT))
            self.temps:int=int(brain.battery.temperature(PERCENT))

            # Battery monitoring for voltage, capacity, and current.
            if self.voltage>=12:
                if self.battery_voltage_monitoring==1 or self.battery_voltage_monitoring==2:
                    log.add("DB0", "%s"%(self.voltage))
                    self.battery_voltage_monitoring=0
            elif self.voltage<12:
                if self.battery_voltage_monitoring==0 or self.battery_voltage_monitoring==1:
                    log.add("WB0", "%s"%(self.voltage))
                    self.battery_voltage_monitoring=2
            elif self.voltage<11:
                if self.battery_voltage_monitoring==0 or self.battery_voltage_monitoring==2:
                    log.add("EB0", "%s"%(self.voltage))
                    self.battery_voltage_monitoring=1

            if self.capacity>=50:
                if self.battery_capacity_monitoring!=self.capacity:
                    log.add("DB3", "%s"%(self.capacity))
                    self.battery_capacity_monitoring=self.capacity
            elif self.capacity<50:
                if self.battery_capacity_monitoring!=self.capacity:
                    log.add("WB1", "%s"%(self.capacity))
                    self.battery_capacity_monitoring=self.capacity
            elif self.capacity<25:
                if self.battery_capacity_monitoring!=self.capacity:
                    log.add("EB1", "%s"%(self.capacity))
                    self.battery_capacity_monitoring=self.capacity
            
            if self.current<=10:
                if self.battery_current_monitoring==1 or self.battery_current_monitoring==2:
                    log.add("DB1", "%s"%(self.current))
                    self.battery_current_monitoring=0
            elif self.current>10:
                if self.battery_current_monitoring==0 or self.battery_current_monitoring==1:
                    log.add("WB2", "%s"%(self.current))
                    self.battery_current_monitoring=2
            elif self.current>15:
                if self.battery_current_monitoring==0 or self.battery_current_monitoring==2:
                    log.add("EB2", "%s"%(self.current))
                    self.battery_current_monitoring=1
            
            if self.watts<=150:
                if self.battery_watt_monitoring==1 or self.battery_watt_monitoring==2:
                    log.add("DB2", "%s"%(self.watts))
                    self.battery_watt_monitoring=0
            elif self.watts>150:
                if self.battery_watt_monitoring==0 or self.battery_watt_monitoring==1:
                    log.add("WB3", "%s"%(self.watts))
                    self.battery_watt_monitoring=2
            elif self.watts>200:
                if self.battery_watt_monitoring==0 or self.battery_watt_monitoring==3:
                    log.add("EB3", "%s"%(self.watts))
                    self.battery_watt_monitoring=1  

            if self.temps<=30:
                if self.battery_temp_monitoring==1 or self.battery_temp_monitoring==2:
                    log.add("DB4", "%s"%(self.temps))
                    self.battery_temp_monitoring=0
            elif self.temps>30:
                if self.battery_temp_monitoring==0 or self.battery_temp_monitoring==1:
                    log.add("WB4", "%s"%(self.temps))
                    self.battery_temp_monitoring=2
            elif self.temps>50:
                if self.battery_watt_monitoring==0 or self.battery_temp_monitoring==3:
                    log.add("EB4", "%s"%(self.temps))
                    self.battery_temp_monitoring=1  

        def controller(self, controller: Controller) -> None:
            """
            Capture for the controllers. 
            Enter controller you wish to log. 
            
            Args:
            controller= Controller()
            """

            self.record = recording.record
            self.ctrl_name = str(controller)

            if self.record:  # Uses more accurate logging when recording.
                self.axis3 = self.axis3
                self.c_axis2 = controller.axis2.position()
                self.c_axis3 = controller.axis3.position()

                if self.c_axis2 != self.axis2:
                    log.add("DC1", "%s_Axis2 %d Moved"%(self.ctrl_name, self.c_axis2))
                    self.axis2 = self.c_axis2
                if self.c_axis3 != self.axis3:
                    log.add("DC1", "%s_Axis3 %d Moved"%(self.ctrl_name, self.c_axis3))
                    self.axis3 = self.c_axis3
            else:
                self.c_axis1 = controller.axis1.position()
                self.c_axis2 = controller.axis2.position()
                self.c_axis3 = controller.axis3.position()
                self.c_axis4 = controller.axis4.position()

                if self.c_axis1 != 0 and not (self.axis1 >= self.c_axis1 - log.tolrance and self.axis1 <= self.c_axis1 + log.tolrance):
                    log.add("DC1", "%s_Axis1 %d Moved"%(self.ctrl_name, self.c_axis1))
                    self.axis1 = self.c_axis1
                elif self.c_axis1 == 0 and self.axis1 != 0:
                    log.add("DC1", "%s_Axis1 %d Moved"%(self.ctrl_name, 0))
                    self.axis1 = 0

                if self.c_axis2 != 0 and not (self.axis2 >= self.c_axis2 - log.tolrance and self.axis2 <= self.c_axis2 + log.tolrance):
                    log.add("DC1", "%s_Axis2 %d Moved"%(self.ctrl_name, self.c_axis2))
                    self.axis2 = self.c_axis2
                elif self.c_axis2 == 0 and self.axis2 != 0:
                    log.add("DC1", "%s_Axis2 %d Moved"%(self.ctrl_name, 0))
                    self.axis2 = 0

                if self.c_axis3 != 0 and not (self.axis3 >= self.c_axis3 - log.tolrance and self.axis3 <= self.c_axis3 + log.tolrance):
                    log.add("DC1", "%s_Axis3 %d Moved"%(self.ctrl_name, self.c_axis3))
                    self.axis3 = self.c_axis3
                elif self.c_axis3 == 0 and self.axis3 != 0:
                    log.add("DC1", "%s_Axis3 %d Moved"%(self.ctrl_name, 0))
                    self.axis3 = 0

                if self.c_axis4 != 0 and not (self.axis4 >= self.c_axis4 - log.tolrance and self.axis4 <= self.c_axis4 + log.tolrance):
                    log.add("DC1", "%s_Axis4 %d Moved"%(self.ctrl_name, self.c_axis4))
                    self.axis4 = self.c_axis4
                elif self.c_axis4 == 0 and self.axis4 != 0:
                    log.add("DC1", "%s_Axis4 %d Moved"%(self.ctrl_name, 0))
                    self.axis4 = 0

            # Button logging for controller.

            
            self.button_objs = [
                controller.buttonA,
                controller.buttonB,
                controller.buttonX,
                controller.buttonY,
                controller.buttonUp,
                controller.buttonDown,
                controller.buttonLeft,
                controller.buttonRight,
                controller.buttonL1,
                controller.buttonL2,
                controller.buttonR1,
                controller.buttonR2,
            ]
            

            for i in range(12):
                if self.button_objs[i].pressing():
                    if self.button_values[i]:
                        log.add("DC0", "%s_Button %s Pressed"%(self.ctrl_name, self.button_names[i]))
                        self.button_values[i] = False
                else:
                    if not self.button_values[i]:
                        log.add("DC0", "%s_Button %s Released"%(self.ctrl_name, self.button_names[i]))
                        self.button_values[i] = True

            (
                self.button_a,
                self.button_b,
                self.button_x,
                self.button_y,
                self.button_up,
                self.button_down,
                self.button_left,
                self.button_right,
                self.button_L1,
                self.button_L2,
                self.button_R1,
                self.button_R2,
            ) = self.button_values

        def variable(self, name: str, value: Any) -> None:
            """
            Capture for int, float, and bool variables. 
            Enter name of variable in a string and then the variable you wish to log.
            
            Args:
            name= String
            value= Int, Boolean, Float
            """

            self.valueid=id(name)

            # Adds id if not in set.
            if self.valueid not in self.variables:

                if type(value)==bool:
                    self.variables[self.valueid]=False
                else:
                    self.variables[self.valueid]=0
            
            if value != self.variables[self.valueid]:
                log.add("DV0", "Variable %s Value %s"%(name, value))
                self.variables[self.valueid] = value

    class Archive:
        """
        Main object for archiving files made by CLEAR.
        """
        
        def log(self) -> None:
            """
            Archives the Log.txt file.
            
            Args:
            None
            """

            speed=log_time.time()
            log.adding=False
            reversecodes={value: key for key, value in log.codes.items()}
            if brain.sdcard.filesize("Log.csv") < 300000:
                archivelist=bytearray()  
                logfile=brain.sdcard.loadfile("Log.csv").decode(log.format)
                loglist=logfile.split("\n")
                del logfile
                for i in range(len(loglist)):
                    logline=loglist[i].split(':')
                    if len(logline)>=4:
                        loglines= ":%s: %s: "%(logline[1], logline[2].strip())
                        archivelist.extend(b"%s %s %s \n"%(logline[0], reversecodes.get(loglines, ":Archive ERROR: No Key Matches Input. Input: %s"%(loglines)), logline[3]))
                    del logline
                
            else:
                with open("Log.csv", "r") as file:
                    chunk_size=10240
                    archivelist=bytearray()
                    while True:
                        chunk=file.read(chunk_size)
                        if not chunk:
                            break

                        loglist=chunk.split("\n")
                        for i in range(len(loglist)):
                            logline=loglist[i].split(':')
                            if len(logline)>=4:
                                loglines= ":%s: %s: "%(logline[1], logline[2].strip())
                                archivelist.extend(b"%s %s %s \n"%(logline[0], reversecodes.get(loglines, ":Archive ERROR: No Key Matches Input. Input: %s"%(loglines)), logline[3]))
                            del logline
                        brain.sdcard.appendfile("loghistory.txt", archivelist)
                        archivelist=bytearray()
                        del chunk
            
            brain.sdcard.appendfile("loghistory.txt", archivelist)
            log.clear()
            log.adding=True

            gc.collect()
            log.add("DS1", str(log_time.time() - speed) + " MSEC")
            del speed

        def recording(self, recordingname: str) -> None:
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
                chunk_size=10240
                buffer=bytearray()
                while True:
                    chunk=recording.read(chunk_size)
                    if not chunk:
                        break
                    
                    list=chunk.split("\n")
                    for line in list:
                        prelist=line.split(' ')
                        buffer.extend(b"%s %s %s %s \n" %(prelist[2], prelist[9], prelist[10], prelist[11]))
                    brain.sdcard.appendfile(filename, buffer)
   
            brain.sdcard.savefile(recordingname)
            log.add("DS3", recordingname)

        def index_history(self) -> None:
            """
            Gets lines of loghistory puts number in file.
            
            Args:
            None
            """

            speed=log_time.time()
            index=0
            chunk=bytes(2)
            
            with open("loghistory.txt", 'rb') as file:
                chunk_size = 10240
                while True:
                    chunk = file.read(chunk_size)
                    if not chunk:
                        break
                    index += chunk.count(b'\n')
            log._index+=index
            log.add("DS2", str(log_time.time() - speed) + " MSEC")
            del speed, index

        def recall_log(self) -> None:
            """
            Unarchives The log.

            Args:
            None
            """

            filename=("logrecalled.txt")
            print("recalling...")
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
        
        def recall_recording(self, name: str) -> None:
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
                if "Moved" in item:
                    brain.sdcard.appendfile(filename, bytearray("[',', '0', %s ':Controller', 'DATA:', 'Axis', 'Changed.', 'Axis:', '', %s %s 'Moved', '0', 'Degrees', ''] \n"%(prelist[0], prelist[1], prelist[2]), log.format))
                elif "Pressed" in item or "Released" in item:
                    brain.sdcard.appendfile(filename, bytearray("[',', '0', %s ':Controller', 'DATA:', 'Button', 'Changed.', 'Button:', '', %s %s %s ''] \n"%(prelist[0], prelist[1], prelist[2], prelist[3]), log.format))
            log.add("DS5", name)
                
    def __init__(self):
        self.capture=self.Capture()
        self.archive=self.Archive()
        self._index:int=0
        self.adding:bool=True  # Used to pause logging.
        self.format:str="utf-8"  # General format for all files in the code.
        self._cache:bytearray=bytearray()
        self.brainscreen:bool=False  # Used to see if need to print to brain screen.
        self.tolrance:int=3  # tolerance for controller stick diffrence when not recording and for general tolrance for sensors.
        self.printing:bool=True
        self.logging:bool=True
        self.buffer=bytearray(10240)
        self._bufferSize=0
        self._buffer_offset=0
        self._last_write=0
        self.speed=0
        self.Motors=[]

        brain.sdcard.savefile("Logstart.txt")  # Clears Logstart file for refresh of instructions in it.

        # Predefined Log Codes dictionary
        self.codes:dict={
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
                "EB4": ":Battery ERROR: Critically High Temps. Temps: ",
                "WB0": ":Battery WARNING: Low Voltage. Voltage: ",
                "WB1": ":Battery WARNING: Low Battery. capacity: ",
                "WB2": ":Battery WARNING: High Current. Current: ",
                "WB3": ":Battery WARNING: High Wattage. Wattage: ",
                "WB4": ":Battery WARNING: High Temps. Temps: ",
                "DB0": ":Battery DATA: Voltage Back To Normal. Voltage: ",
                "DB1": ":Battery DATA: Current Back To Normal. Current: ",
                "DB2": ":Battery DATA: Wattage Back To Normal. Wattage: ",
                "DB3": ":Battery DATA: Capacity Changed. Capacity: ",
                "DB4": ":Battery DATA: Temps Back To Normal. Temps: ",
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
        log_number=0
        if not brain.sdcard.exists("Log.csv"):
            brain.sdcard.savefile("Log.csv", bytearray("log Start: \n", self.format))
        else:
            if brain.sdcard.filesize("Log.csv") < 300000:
                log_lines=[]
                log_lines=brain.sdcard.loadfile("Log.csv").decode(self.format).split("\n")
                log_number=len(log_lines)
                del log_lines
            else:
                print("Log.csv cannot be decoded.")
                with open("Log.csv", 'rb') as log_file:
                    chunk_size=10240
                    while True:
                        chunk=log_file.read(chunk_size)
                        if not chunk:
                            break

                        log_number+=chunk.count(b'\n')

                print("Log done")

            if not brain.sdcard.exists("loghistory.txt"):
                brain.sdcard.savefile("loghistory.txt")

            self._index= log_number - 1

            # Clears lists to free memory.
            del log_number

    async def append_recording(self) -> None: # This is only ment for the recording.
        """
        Appends to current recording file and to the log.

        Args:
        entry= String
        """
        entry=self.buffer[0:self._bufferSize]
        brain.sdcard.appendfile("Log.csv", entry)
        brain.sdcard.appendfile(recording.Aton, entry)

    def append_log(self) -> None:
        """
        Appends to log file.

        Args:
        entry= String
        """
        if log_time.time()-self._last_write>3000 and self._bufferSize !=0: 
            brain.sdcard.appendfile("Log.csv", self.buffer[0:self._buffer_offset])
            print("saved.")
            self._buffer_offset=0
            self._last_write=log_time.time()
            self._bufferSize=0
    
    def brain_read(self) -> None:
        """
        Prints to brain screen.

        Args:
        entry= String
        """

        if brain.screen.row()>=20:
            brain.screen.clear_screen()
            brain.screen.set_cursor(1,1)

        brain.screen.print(self.entry)
        brain.screen.new_line()
    
    def add(self, add_code: str, add_details: Any) -> None:
        """
        Main funtion for Log.

        Takes code and the added details gets runtime and index. 
        Then, prints it, puts them in Log or cache, and see if it needs to print to brain screen. 
        Enter code then the details you want as a string.

        Args:
        add_code= String
        add_details= Any
        """

        if not self.adding:
            self._cache.extend(b", %d [%d] %s %s \n" % (self._index, log_time.time(), self.codes.get(add_code), add_details))
            return 
        else:
            if self._cache:
                self.entry=self._cache
                if self.printing:
                    print(self._cache.decode(self.format))
                if self.logging:
                    brain.sdcard.appendfile("Log.csv", self._cache)
                if self.brainscreen:
                    self.brain_read()
                self._cache=bytearray()
                return
            
        self.entry=b", %d [%d] %s %s \n" %(self._index, log_time.time(), self.codes.get(add_code), add_details)
        self._bufferSize=len(self.entry)

        ustruct.pack_into("=%ds"%(self._bufferSize), self.buffer, self._buffer_offset, self.entry)
        self._buffer_offset+=self._bufferSize

        if self.logging:
            if recording.record:
                uasyncio.create_task(self.append_recording())
            else:
                self.append_log()

        if self.brainscreen:  # Checks if pinting to brainscreen is enabled.
            self.brain_read()
        
        if self.printing:
            print(self.entry)

        self._index += 1
        
    def add_codes(self, code_add: str, Decoded_text: str) -> None:
        """
        Adds codes to the codes dictionary. 
        Enter new code key, then the full string.

        Args:
        code_add= String
        Decoded_text= String
        """

        self.codes.update({code_add : "%s"%(Decoded_text)})

    def remove_codes(self, code_remove: str) -> None:
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

    def edit_codes(self, code_edit: str, new_decoded_text: str) -> None:
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
    def clear(self) -> None:
        """
        Clears the Log.csv file.
        
        Args:
        None
        """

        brain.sdcard.savefile("Log.csv", bytearray("Log Start: \n", self.format))
    
    def add_logstart(self, funtion) -> None:
        """
        Used in logstart. 
        Enter the funtion for variables like so "log.capture.variable()" then in the inner parentheses add the name of variable as a string and the variable. 
        Can also be used for any capture funtion in CLEAR.

        Args:
        funtion= Funtion for object Log
        """

        brain.sdcard.appendfile("Logstart.txt" , bytearray(funtion + ", ", self.format))     
        
    def auto_start(self):
        """
        The main way to CLEAR.
        All that is need is to call it.

        Args:
        None
        """
        self.format:str=str(settings.settings.get('format_used '))
        self.tolrance:int=int(str(settings.settings.get('default_tolrance ')))
        wait_time_logging:int=int(str(settings.settings.get('logging_loop_wait ')))
        wait_time_recording:int=int(str(settings.settings.get('recording_loop_wait ')))

        if "True" in str(settings.settings.get('gc_use ')):
            gc_use:bool=True
        else:
            gc_use:bool=False

        if "True" in str(settings.settings.get('log_battery ')):
            log_battery:bool=True
        else:
            log_battery:bool=False

        if "True" in str(settings.settings.get('log_memory ')):
            log_memory:bool=True
        else:
            log_memory:bool=False

        if "True" in str(settings.settings.get('log_modules ')):
            log_modules:bool=True
        else:
            log_modules:bool=False

        if "True" in str(settings.settings.get('print_read ')):
            self.printing:bool=True
        else:
            self.printing:bool=False

        if "True" in str(settings.settings.get('sdcard_read ')):
            self.logging:bool=True
        else:
            self.logging:bool=False

        if "True" in str(settings.settings.get('brain_read ')):
            self.brainscreen:bool=True
        else:
            self.brainscreen:bool=False

        if self.brainscreen:
            brain.screen.set_font(FontType.MONO12)

        # Logs system start.
        self.add("DS0", "")
        
        if "True" in str(settings.settings.get('auto_do_variables ')):
            auto_do_variables:bool=True
        else:
            auto_do_variables:bool=False

        if "True" in str(settings.settings.get('auto_do_control ')):
            auto_do_control:bool=True
        else:
            auto_do_control:bool=False

        if "True" in str(settings.settings.get('auto_do_three_wire ')):
            auto_do_three_wire:bool=True
        else:
            auto_do_three_wire:bool=False

        if "True" in str(settings.settings.get('auto_do_smart_port ')):
            auto_do_smart_port:bool=True
        else:
            auto_do_smart_port:bool=False

        if "True" in str(settings.settings.get('auto_do_motors ')):
            auto_do_motors:bool=True
        else:
            auto_do_motors:bool=False

        if "True" in str(settings.settings.get('auto_do_controller ')):
            auto_do_controller:bool=True
        else:
            auto_do_controller:bool=False

        controllers=[]
        globallogging= dir()

        for item in globallogging:

            item_type=str(type(eval(item)))

            if  (item_type == "<class 'int'>" or item_type == "<class 'bool'>" or item_type == "<class 'float'>") and auto_do_variables:
                log.add_logstart("log.capture.variable('%s', %s)"%(item, item.replace("'", "")))
            elif item_type == "<class 'motor'>" and auto_do_motors:
                self.Motors+=[eval(item)]
            elif item_type == "<class 'controller'>" and auto_do_controller:
                controllers+=[eval(item)]
            elif item_type == "<class 'inertial'>" and auto_do_smart_port:
                log.add_logstart("log.capture.smartport.inertial(%s)"%(item.replace("'", "")))
            elif item_type == "<class 'optical'>" and auto_do_smart_port:
                log.add_logstart("log.capture.smartport.optical(%s)"%(item.replace("'", "")))
            elif item_type == "<class 'rotation'>" and auto_do_smart_port:
                log.add_logstart("log.capture.smartport.rotation(%s)"%(item.replace("'", "")))
            elif item_type == "<class 'distance'>" and auto_do_smart_port:
                log.add_logstart("log.capture.smartport.distance(%s)"%(item.replace("'", "")))
            elif item_type == "<class 'triport_bumper'>" and auto_do_three_wire:
                log.add_logstart("log.capture.threewire.bumper(%s)"%(item.replace("'", "")))
            elif item_type == "<class 'triport_limit'>" and auto_do_three_wire:
                log.add_logstart("log.capture.threewire.limit(%s)"%(item.replace("'", "")))
            elif item_type == "<class 'triport_digitalin'>" and auto_do_three_wire:
                log.add_logstart("log.capture.threewire.digitalinput(%s)"%(item.replace("'", "")))
            elif item_type == "<class 'triport_potv2'>" and auto_do_three_wire:
                log.add_logstart("log.capture.threewire.potentiometer(%s)"%(item.replace("'", "")))
            elif item_type == "<class 'triport_analog'>" and auto_do_three_wire:
                log.add_logstart("log.capture.threewire.analog(%s)"%(item.replace("'", "")))
            elif item_type == "<class 'competition'>" and auto_do_control:
                log.add_logstart("log.capture.system.control(%s)"%(item.replace("'", "")))
            
            del item_type            

        del auto_do_variables, auto_do_three_wire, auto_do_control, auto_do_smart_port, auto_do_motors, auto_do_controller, globallogging

        _exec=exec
        lwait=wait
        capture_memory=self.capture.system.memoryuse
        capture_modules=self.capture.system.modules
        capture_battery=log.capture.battery
        timer=log_time.time
        gc_collect=gc.collect
        motorcapture=log.capture.smartport.motor
        controllercapture=log.capture.controller
        log_check=log.append_log
        local_range=range

        # Loads extra funtions from file.
        try:
            addedfuntion=brain.sdcard.loadfile("Logstart.txt").decode(self.format)
            added_bytes=compile(addedfuntion, '<string>' ,'exec', 0,  True, 2)
        except AttributeError:
            addedfuntion=""
            added_bytes=compile("", '<string>' ,'exec', 0,  True, 2)
        
        if addedfuntion:
            _exec(added_bytes)

        self.archive.index_history()
        if log_modules:
            capture_modules()
        if brain.sdcard.filesize("Log.csv") > 100000:
            self.archive.log()
        
        gc_collect()

        while True:
            for _ in local_range(20):

                start:int=timer()

                if controllers:
                    for controller in controllers:
                        controllercapture(controller)

                if not recording.record:
                    log_check()

                    if addedfuntion:
                        _exec(added_bytes)
                    
                    if self.Motors:
                        motorcapture()
   
                    if log_memory:
                        capture_memory()

                    if log_modules:
                        capture_modules()
                    
                    if log_battery:
                        capture_battery()
                    
                    print(timer()-start)

                    lwait(wait_time_logging - (timer() - start))
                else:
                    print(timer()-start)
                    lwait(wait_time_recording - (timer() - start))

            if gc_use:
                gc_collect()

class Recording:
    """
    Main class for recording.
    """

    def __init__(self):
        self.record:bool=False  # Bool to see if recording
        self.Aton:str=""  # Used for name of file recording
        self.postlist:list=[] # Used for prossesing files.
        self.poststring:str="" # Used to store list to string.     

    def start(self, Aton) -> None:
        """
        Starts recording. 
        Enter name of file to start recording in.
        
        Args:
        Aton= String
        """

        filename:str=str(Aton) + "_pre.txt"

        if self.record == False:
            self.record= True
            brain.sdcard.savefile(filename, bytearray("\n", log.format))
            self.Aton= Aton + "_pre.txt"
            log.add("DA0", filename)

    def stop(self, Aton) -> None:
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
            preatonfile=brain.sdcard.loadfile(filename).decode(log.format)
            preatonlist=preatonfile.split("\n")
            del preatonfile
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

    def encode(self, Aton, right, left, other1start=none, other1stop=none, other1button=none, other2start=none, other2stop=none, other2button=none, other3start=none, other3stop=none, other3button=none, other4start=none, other4stop=none, other4button=none, other5start=none, other5stop=none, other5button=none, other6start=none, other6stop=none, other6button=none) -> None:   
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

        if brain.sdcard.filesize(Aton + "_pre.txt") < 300000:
            preatonfile=brain.sdcard.loadfile(Aton + "_pre.txt")
            preatonlist=preatonfile.decode(log.format).split("\n")
            del preatonfile

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
        
        else:
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
    
    def run(self, Aton) -> None:
        """
        Runs encoded file. 
        Enter file to run.
        
        Args:
        Aton= String
        """

        log.add("DA3", Aton + ".txt")
        if brain.sdcard.filesize(Aton+ ".txt") < 200000:
            Atonfile=brain.sdcard.loadfile(Aton + ".txt")
            exec(Atonfile.decode(log.format))
        else:
            with open(Aton + ".txt") as Atonfile:
                chunk_size=20480
                while True:
                    chunk=Atonfile.read(chunk_size)
                    if not chunk:
                        break

                    exec(chunk)

class Settings():
    """Used to congigure the log in a more permenet way using the Sd card"""

    def __init__(self):
        self.changes=""
        self.settings={}
        self.default_settings_dictonary={
            "brain_read": False,
            "print_read": True,
            "sdcard_read": True,
            "gc_use": True,
            "archive_log": True,
            "archive_recordings": True,
            "log_memory": False,
            "log_modules": True,
            "log_battery": True,
            "logging_loop_wait": 200,
            "recording_loop_wait": 1,
            "format_used": "utf-8",
            "auto_do_motors": True,
            "auto_do_variables": True,
            "auto_do_control": True,
            "auto_do_three_wire": True,
            "auto_do_smart_port": True,
            "auto_do_controller": True,
            "default_tolrance": 3,
            "memory_tolrance_KB": 100,
            "distance_tolrance_MM": 100,
            "inertial_gyro_tolrance_DEGREES": 5,
            "inertial_axis_tolrance_Gs": 0.5,
        }
        
        if brain.sdcard.is_inserted() and not brain.sdcard.exists("settings.txt"):
            setting=""
            for value, key in self.default_settings_dictonary.items():
                setting+="%s : %s \n"%(value, key)
            brain.sdcard.savefile("settings.txt", bytearray(setting, "utf-8"))
            self.settings_text=brain.sdcard.loadfile("settings.txt").decode("utf-8").split("\n")
            for line in self.settings_text:
                dict_stuff=line.split(":")

                if len(dict_stuff) >= 2:
                    self.settings[dict_stuff[0]]=dict_stuff[1]
            
        else:
            self.settings_text=brain.sdcard.loadfile("settings.txt").decode("utf-8").split("\n")
            for line in self.settings_text:
                dict_stuff=line.split(":")

                if len(dict_stuff) >= 2:
                    self.settings[dict_stuff[0]]=dict_stuff[1]   

settings=Settings()
log=Log()
recording=Recording()