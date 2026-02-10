#region VEXcode Generated Robot Configuration
from vex import *
import urandom # type: ignore
import time
import math

# Brain should be defined by default
brain=Brain()

# Robot configuration code
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

#endregion VEXcode Generated Robot Configuration


# ---------------------------------------------------------------------------- #
# Section: Globals / State
# ---------------------------------------------------------------------------- #
screen_precision = 0
console_precision = 0
controller_1_precision = 0
Accuracy = 0
Front_Down = 0
Degees_to_mm = 0
Speed_To_Volts = 0
Push = 0
degrees_to_Degrees = 0
Degrees_to_mm = 0
inertial_mm = 0
degrees_of_rotation = 0
degrees_2 = 0
Degrees_to_mm_2 = 0
volosity_history = 0
color_select = 0
Aton_select = 0
Recording = 0
Volosity_Aton=0
PreVolosity=0
No=0
controller_1_Velosity_Left=[]
controller_1_Velosity_Right=[]
Left_Velosity=0
Right_velosity=0
screen_options=0
Left_Aton_file=""
Right_Aton_file=""
code=""
details=0

code_dictionary = {"ED0": "Drivetrain ERROR: No response from drivetrain.",
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

def Logger(code, details):
    if details == 0:
        details = ""
    timestamp =0
    decoded_message = code_dictionary.get(code),details, "Code: ", code
    log_entry = "[%s] %s\n"%(timestamp, decoded_message)

    brain.sdcard.appendfile("log.txt", bytearray(log_entry, "utf-8"))
    print(log_entry)

Logger(code, details)

def Logging():
    global code, details
    while True:
        if Right1.temperature(PERCENT) >= 80 and details!=Right1.temperature(PERCENT):
            details=Right1.temperature(PERCENT)
            Logger("ED1", details)
        elif Right1.temperature(PERCENT) >= 50 and details!=Right1.temperature(PERCENT):
            details=Right1.temperature(PERCENT)
            Logger("WD0", details)
        if Left1.temperature(PERCENT) >= 80 and details!=Left1.temperature(PERCENT):
            details=Left1.temperature(PERCENT)
            Logger("ED1", details)
        elif Left1.temperature(PERCENT) >= 50 and details!=Left1.temperature(PERCENT):
            details=Left1.temperature(PERCENT)
            Logger("WD0", details)
        if Intake_Motor.temperature(PERCENT) >= 80 and details!=Intake_Motor.temperature(PERCENT):
            details=Intake_Motor.temperature(PERCENT)
            Logger("EI1", details)
        elif Intake_Motor.temperature(PERCENT) >= 50 and details!=Intake_Motor.temperature(PERCENT):
            details=Intake_Motor.temperature(PERCENT)
            Logger("WI0", details)
        if brain.battery.voltage(VOLT) <= 11.0:
            details=brain.battery.voltage(VOLT)
            Logger("WB0", details)
        elif brain.battery.voltage(VOLT) <= 10:
            details=brain.battery.voltage(VOLT)
            Logger("EB0", details)
        if brain.battery.capacity() <= 50 and details!=brain.battery.capacity():
            details=brain.battery.capacity()
            Logger("WB1", details)
        elif brain.battery.capacity() <= 25 and details!=brain.battery.capacity():
            details=brain.battery.capacity()
            Logger("EB1", details)
        wait(1, SECONDS)

def Aton_init_setup():
    global my_event, Consle_output
    if brain.sdcard.is_inserted():
        if not brain.sdcard.exists("log.txt"):
            brain.sdcard.savefile("log.txt", bytearray("", "utf-8"))
    set_drivetrain_volosity_v(100)
    if inertial_for_auton.rotation(DEGREES) > 2 or inertial_for_auton.rotation(DEGREES) < -2:
        inertial_for_auton.calibrate()
        while inertial_for_auton.is_calibrating():
            sleep(50)
    inertial_for_auton.set_rotation(0, DEGREES)
    TopMotor.set_velocity(100, PERCENT)
    colorsorting.set_velocity(100, PERCENT)
    Intake_Motor.set_velocity(100, PERCENT)
    TopMotor.set_stopping(HOLD)
    optical_9.set_light(LedStateType.ON)
    optical_9.set_light_power(100, PERCENT)
    Logger("DS1", 0)
    print("Aton Init Setup Done")

def Driver_init_setup():
    global my_event, Consle_output
    if brain.sdcard.is_inserted():
        if not brain.sdcard.exists("log.txt"):
            brain.sdcard.savefile("log.txt", bytearray("", "utf-8"))
    set_drivetrain_volosity_v(100)
    TopMotor.set_velocity(100, PERCENT)
    colorsorting.set_velocity(100, PERCENT)
    Intake_Motor.set_velocity(100, PERCENT)
    optical_9.set_light(LedStateType.ON)
    optical_9.set_light_power(100, PERCENT)
    Logger("DS0", 0)
    print("Driver Init Setup Done")

def Drive_left_degrees_F_R(Drive_left_degrees_degrees_Forward_Reverse_F_R__degrees, Drive_left_degrees_degrees_Forward_Reverse_F_R__F_R):
    global my_event, Consle_output
    if Drive_left_degrees_degrees_Forward_Reverse_F_R__F_R == "F" or Drive_left_degrees_degrees_Forward_Reverse_F_R__F_R == "f":
        Left1.spin_for(FORWARD, Drive_left_degrees_degrees_Forward_Reverse_F_R__degrees, DEGREES, wait=False)
        Left2.spin_for(FORWARD, Drive_left_degrees_degrees_Forward_Reverse_F_R__degrees, DEGREES, wait=False)
        Left3.spin_for(FORWARD, Drive_left_degrees_degrees_Forward_Reverse_F_R__degrees, DEGREES, wait=False)
    else:
        Left1.spin_for(REVERSE, Drive_left_degrees_degrees_Forward_Reverse_F_R__degrees, DEGREES, wait=False)
        Left2.spin_for(REVERSE, Drive_left_degrees_degrees_Forward_Reverse_F_R__degrees, DEGREES, wait=False)
        Left3.spin_for(REVERSE, Drive_left_degrees_degrees_Forward_Reverse_F_R__degrees, DEGREES, wait=False)
    print("\033[32m")
    print(str("Move left Sucessful: ") + str(Drive_left_degrees_degrees_Forward_Reverse_F_R__degrees))
    Logger("DA5", Drive_left_degrees_degrees_Forward_Reverse_F_R__degrees)

def stop_l_r_drive_l_r(stop_l_r_drive_l_r__l_r):
    global my_event, Consle_output, Accuracy, Front_Down, Degees_to_mm, Speed_To_Volts, Push, degrees_to_Degrees, Degrees_to_mm, inertial_mm, degrees_of_rotation, degrees_2, Degrees_to_mm_2, volosity_history, color_select, Aton_select, screen_precision, console_precision, controller_1_precision
    if stop_l_r_drive_l_r__l_r == "l":
        Left1.stop()
        Left3.stop()
        Left2.stop()
    else:
        Right1.stop()
        Right2.stop()
        Right3.stop()

def Color_sorting_Color(Color_sorting_Color__Color):
    global my_event, Consle_output, Accuracy, Front_Down, Degees_to_mm, Speed_To_Volts, Push, degrees_to_Degrees, Degrees_to_mm, inertial_mm, degrees_of_rotation, degrees_2, Degrees_to_mm_2, volosity_history, color_select, Aton_select, screen_precision, console_precision, controller_1_precision
    if Color_sorting_Color__Color:
        colorsorting.spin(REVERSE)
    else:
        colorsorting.stop()
    wait(0.05, SECONDS)

def Drive_Right_degrees_F_R(Drive_Right_degrees_degrees_Forward_Reverse_F_R__degrees, Drive_Right_degrees_degrees_Forward_Reverse_F_R__F_R):
    global my_event, Consle_output
    if Drive_Right_degrees_degrees_Forward_Reverse_F_R__F_R == "F" or Drive_Right_degrees_degrees_Forward_Reverse_F_R__F_R == "f":
        Right2.spin_for(FORWARD, Drive_Right_degrees_degrees_Forward_Reverse_F_R__degrees, DEGREES, wait=False)
        Right3.spin_for(FORWARD, Drive_Right_degrees_degrees_Forward_Reverse_F_R__degrees, DEGREES, wait=False)
        Right1.spin_for(FORWARD, Drive_Right_degrees_degrees_Forward_Reverse_F_R__degrees, DEGREES, wait=False)
    else:
        Right2.spin_for(REVERSE, Drive_Right_degrees_degrees_Forward_Reverse_F_R__degrees, DEGREES, wait=False)
        Right3.spin_for(REVERSE, Drive_Right_degrees_degrees_Forward_Reverse_F_R__degrees, DEGREES, wait=False)
        Right1.spin_for(REVERSE, Drive_Right_degrees_degrees_Forward_Reverse_F_R__degrees, DEGREES, wait=False)
    print("\033[32m")
    print(str("Move R Sucessful: ") + str(Drive_Right_degrees_degrees_Forward_Reverse_F_R__degrees))
    Logger("DA6", Drive_Right_degrees_degrees_Forward_Reverse_F_R__degrees)

def Move_Forward_MM_mm_Right_or_left_R_L(Move_Forward_MM_mm_Right_or_left_R_L__mm, Move_Forward_MM_mm_Right_or_left_R_L__R_L):
    global my_event, Consle_output, Accuracy, Front_Down, Degees_to_mm, Speed_To_Volts, Push, degrees_to_Degrees, Degrees_to_mm, inertial_mm, degrees_of_rotation, degrees_2, Degrees_to_mm_2, volosity_history, color_select, Aton_select, screen_precision, console_precision, controller_1_precision
    # ratio for turning the mm input to degrees for Left or Right motors
    Degees_to_mm = (Move_Forward_MM_mm_Right_or_left_R_L__mm / ((69.85 * 3.14) / 360)) / 0.76
    if Move_Forward_MM_mm_Right_or_left_R_L__R_L == "R" or Move_Forward_MM_mm_Right_or_left_R_L__R_L == "r":
        Drive_Right_degrees_F_R(Degees_to_mm, "f")
    elif Move_Forward_MM_mm_Right_or_left_R_L__R_L == "L" or Move_Forward_MM_mm_Right_or_left_R_L__R_L == "l":
        Drive_left_degrees_F_R(Degees_to_mm, "f")
    else:
        print("\033[31m")
        print("ERROR Drive malfuntion Forward R/L")
        Logger("EA2", "Drive malfuntion Forward R/L")
    Logger("DA4", Move_Forward_MM_mm_Right_or_left_R_L__mm)

def Curved_move(Left_degrees,Right_degrees):
    global my_event, Consle_output, Accuracy, Front_Down, Degees_to_mm, Speed_To_Volts, Push, degrees_to_Degrees, Degrees_to_mm, inertial_mm, degrees_of_rotation, degrees_2, Degrees_to_mm_2, volosity_history, color_select, Aton_select, screen_precision, console_precision, controller_1_precision
    Right1.spin_for(FORWARD, Right_degrees, DEGREES, wait=False)
    Left1.spin_for(FORWARD, Left_degrees, DEGREES, wait=False)
    Right2.spin_for(FORWARD, Right_degrees, DEGREES, wait=False)
    Left2.spin_for(FORWARD, Left_degrees, DEGREES, wait=False)
    Right3.spin_for(FORWARD, Right_degrees, DEGREES, wait=False)
    Left3.spin_for(FORWARD, Left_degrees, DEGREES)
    Logger("DA7", str(Left_degrees) + ", " + str(Right_degrees))


def set_drivetrain_volosity_v(set_drivetrain_volosity_v__v):
    global my_event, Consle_output, volosity_history
    Right1.set_velocity(set_drivetrain_volosity_v__v, PERCENT)
    Right2.set_velocity(set_drivetrain_volosity_v__v, PERCENT)
    Right3.set_velocity(set_drivetrain_volosity_v__v, PERCENT)
    Left1.set_velocity(set_drivetrain_volosity_v__v, PERCENT)
    Left2.set_velocity(set_drivetrain_volosity_v__v, PERCENT)
    Left3.set_velocity(set_drivetrain_volosity_v__v, PERCENT)
    volosity_history=set_drivetrain_volosity_v__v
    print("\033[30m")
    print(str("Velosity") + str(set_drivetrain_volosity_v__v))
    Logger("DD0", set_drivetrain_volosity_v__v)

def Turn_to_rotation__degrees_degrees(Turn_to_rotation__degrees_degrees__degrees):
    global my_event, Consle_output, degrees_2
    degrees_2 = Turn_to_rotation__degrees_degrees__degrees - inertial_for_auton.rotation(DEGREES)
    if degrees_2 > 180:
        Turn_Degrees_Degrees(0 - (360 - degrees_2))
    else:
        Turn_Degrees_Degrees(degrees_2)
    Logger("DA9", Turn_to_rotation__degrees_degrees__degrees)

def Turn_Degrees_Degrees(Turn_Degrees_Degrees__Degrees):
    global my_event, Consle_output, degrees_to_Degrees, volosity_history, color_select
    set_drivetrain_volosity_v(100)
    inertial_history= inertial_for_auton.rotation(DEGREES)
    # Ratio for Degrees of robot turn to degrees or motor turn (turns both sides of drivetrain)
    degrees_to_Degrees = Turn_Degrees_Degrees__Degrees * 6.25
    wait(10, MSEC)
    Drive_Right_degrees_F_R(degrees_to_Degrees, "r")
    Drive_left_degrees_F_R(degrees_to_Degrees, "f")
    # using inertial to see how off it is
    while not Right1.is_done():
        wait(5, MSEC)
    wait(20,MSEC)
    print("\033[33m")
    print(str("Turn Off by: ") + str((Turn_Degrees_Degrees__Degrees - (inertial_for_auton.rotation(DEGREES)-inertial_history))))
    for repeat_count in range(2):
        degrees_to_Degrees = (Turn_Degrees_Degrees__Degrees - (inertial_for_auton.rotation(DEGREES)-inertial_history)) * 6.25
        Drive_Right_degrees_F_R(degrees_to_Degrees, "r")
        Drive_left_degrees_F_R(degrees_to_Degrees, "f")
        while not Right1.is_done():
            wait(5, MSEC)
        print("\033[91m")
        print(str("Inertial Turn off By: ") + str((Turn_Degrees_Degrees__Degrees - (inertial_for_auton.rotation(DEGREES)-inertial_history))))
        wait(5, MSEC)
    set_drivetrain_volosity_v(volosity_history)
    Logger("DA8", Turn_Degrees_Degrees__Degrees)

def Drive_Forward_MM_mm(Drive_Forward_MM_mm__mm):
    global my_event, Consle_output, Degrees_to_mm_2
    Degrees_to_mm_2 = (Drive_Forward_MM_mm__mm / ((69.85 * 3.14) / 360)) / 0.76
    Right1.spin_for(FORWARD, Degrees_to_mm_2, DEGREES, wait=False)
    Left1.spin_for(FORWARD, Degrees_to_mm_2, DEGREES, wait=False)
    Right2.spin_for(FORWARD, Degrees_to_mm_2, DEGREES, wait=False)
    Left2.spin_for(FORWARD, Degrees_to_mm_2, DEGREES, wait=False)
    Right3.spin_for(FORWARD, Degrees_to_mm_2, DEGREES, wait=False)
    Left3.spin_for(FORWARD, Degrees_to_mm_2, DEGREES)
    print(str("Degrees turned: ") + str(Degrees_to_mm_2))
    Logger("DA4", Drive_Forward_MM_mm__mm)

def when_started1():
    global my_event, Consle_output, color_select, Aton_select
    # Code for selection and configureing for robot
    while True:
        controller_1.screen.set_cursor(3, 1)
        controller_1.screen.print("Please config robot")
        brain.screen.set_pen_color(Color.BLACK)
        brain.screen.set_fill_color(Color.WHITE)
        brain.screen.set_cursor(2, 9)
        brain.screen.set_font(FontType.MONO30)
        brain.screen.draw_rectangle(90, 0, 100, 100)
        brain.screen.print("Red")
        brain.screen.set_cursor(2, 15)
        brain.screen.draw_rectangle(190, 0, 100, 100)
        brain.screen.print("Blue")
        brain.screen.set_cursor(2, 22)
        brain.screen.draw_rectangle(290, 0, 100, 100)
        brain.screen.print("None")
        brain.screen.set_cursor(5, 8)
        brain.screen.draw_rectangle(90, 100, 100, 100)
        brain.screen.print("Right")
        brain.screen.set_cursor(5, 15)
        brain.screen.draw_rectangle(190, 100, 100, 100)
        brain.screen.print("Left")
        brain.screen.set_cursor(5, 22)
        brain.screen.draw_rectangle(290, 100, 100, 100)
        brain.screen.print("None")
        while Aton_select==0 or color_select==0:
            if brain.screen.x_position() < 190 and brain.screen.x_position() > 90 and brain.screen.y_position() < 100:
                color_select = 2
            if brain.screen.x_position() > 190 and brain.screen.x_position() <290  and brain.screen.y_position() < 100:
                color_select = 3
            if brain.screen.x_position() > 290 and brain.screen.x_position() < 390 and brain.screen.y_position() < 100:
                color_select = 4
            if color_select == 2:
                brain.screen.set_fill_color(Color.RED)
                brain.screen.draw_rectangle(90, 0, 100, 100)
                brain.screen.set_cursor(2, 9)
                brain.screen.print("Red")
                brain.screen.set_fill_color(Color.WHITE)
                brain.screen.set_cursor(2, 15)
                brain.screen.draw_rectangle(190, 0, 100, 100)
                brain.screen.print("Blue")
                brain.screen.set_cursor(2, 22)
                brain.screen.draw_rectangle(290, 0, 100, 100)
                brain.screen.print("None")
            if color_select == 3:
                brain.screen.set_fill_color(Color.WHITE)
                brain.screen.draw_rectangle(90, 0, 100, 100)
                brain.screen.set_cursor(2, 9)
                brain.screen.print("Red")
                brain.screen.set_fill_color(Color.BLUE)
                brain.screen.set_cursor(2, 15)
                brain.screen.draw_rectangle(190, 0, 100, 100)
                brain.screen.print("Blue")
                brain.screen.set_fill_color(Color.WHITE)
                brain.screen.set_cursor(2, 22)
                brain.screen.draw_rectangle(290, 0, 100, 100)
                brain.screen.print("None")
            if color_select == 4:
                brain.screen.set_fill_color(Color.WHITE)
                brain.screen.draw_rectangle(90, 0, 100, 100)
                brain.screen.set_cursor(2, 9)
                brain.screen.print("Red")
                brain.screen.set_cursor(2, 15)
                brain.screen.draw_rectangle(190, 0, 100, 100)
                brain.screen.print("Blue")
                brain.screen.set_fill_color(Color.ORANGE)
                brain.screen.set_cursor(2, 22)
                brain.screen.draw_rectangle(290, 0, 100, 100)
                brain.screen.print("None")
            if brain.screen.x_position() < 190 and brain.screen.x_position() > 90 and brain.screen.y_position() > 100:
                Aton_select = 2
            if brain.screen.x_position() > 190 and brain.screen.x_position() < 290 and brain.screen.y_position() > 100:
                Aton_select = 3
            if brain.screen.x_position() > 290 and brain.screen.x_position() < 390 and brain.screen.y_position() > 100:
                Aton_select = 4
            if Aton_select == 2:
                brain.screen.set_fill_color(Color.GREEN)
                brain.screen.set_cursor(5, 8)
                brain.screen.draw_rectangle(90, 100, 100, 100)
                brain.screen.print("Right")
                brain.screen.set_fill_color(Color.WHITE)
                brain.screen.set_cursor(5, 15)
                brain.screen.draw_rectangle(190, 100, 100, 100)
                brain.screen.print("Left")
                brain.screen.set_fill_color(Color.WHITE)
                brain.screen.set_cursor(5, 22)
                brain.screen.draw_rectangle(290, 100, 100, 100)
                brain.screen.print("None")
            if Aton_select == 3:
                brain.screen.set_fill_color(Color.WHITE)
                brain.screen.set_cursor(5, 8)
                brain.screen.draw_rectangle(90, 100, 100, 100)
                brain.screen.print("Right")
                brain.screen.set_fill_color(Color.GREEN)
                brain.screen.set_cursor(5, 15)
                brain.screen.draw_rectangle(190, 100, 100, 100)
                brain.screen.print("Left")
                brain.screen.set_fill_color(Color.WHITE)
                brain.screen.set_cursor(5, 22)
                brain.screen.draw_rectangle(290, 100, 100, 100)
                brain.screen.print("None")
            if Aton_select == 4:
                brain.screen.set_fill_color(Color.WHITE)
                brain.screen.set_cursor(5, 8)
                brain.screen.draw_rectangle(90, 100, 100, 100)
                brain.screen.print("Right")
                brain.screen.set_fill_color(Color.WHITE)
                brain.screen.set_cursor(5, 15)
                brain.screen.draw_rectangle(190, 100, 100, 100)
                brain.screen.print("Left")
                brain.screen.set_fill_color(Color.GREEN)
                brain.screen.set_cursor(5, 22)
                brain.screen.draw_rectangle(290, 100, 100, 100)
                brain.screen.print("None")
            brain.screen.render()
            wait(5, MSEC)
        # Clearing of setup screen
        controller_1.screen.clear_row(1)
        controller_1.screen.set_cursor(1,3)
        brain.screen.clear_screen()
        brain.screen.set_font(FontType.MONO15)
        brain.screen.set_fill_color(Color.BLACK)
        brain.screen.pressed(Options)
        # Motor data print and face
        while screen_options==0:
            if Right1.temperature(PERCENT) >= 0 and Right1.temperature(PERCENT) < 50 or Left1.temperature(PERCENT) >= 0 and Left1.temperature(PERCENT) < 50 or Intake_Motor.temperature(PERCENT) >= 0 and Intake_Motor.temperature(PERCENT) < 50:
                brain.screen.set_pen_color(Color.GREEN)
                brain.screen.draw_circle(250, 30, 30)
                brain.screen.draw_line(240, 10, 240, 20)
                brain.screen.draw_line(260, 10, 260, 20)
                brain.screen.draw_line(240, 50, 260, 50)
                brain.screen.draw_line(260, 50, 270, 40)
                brain.screen.draw_line(240, 50, 230, 40)
            wait(0.1, SECONDS)
            if Right1.temperature(PERCENT) >= 50 and Right1.temperature(PERCENT) < 80 or Left1.temperature(PERCENT) >= 50 and Left1.temperature(PERCENT) < 80 or Intake_Motor.temperature(PERCENT) >= 50 and Intake_Motor.temperature(PERCENT) < 80:
                brain.screen.set_pen_color(Color.YELLOW)
                brain.screen.draw_circle(250, 30, 30)
                brain.screen.draw_line(240, 10, 240, 20)
                brain.screen.draw_line(260, 10, 260, 20)
                brain.screen.draw_line(235, 35, 265, 35)
            wait(0.1, SECONDS)
            if Right1.temperature(PERCENT) >= 80 or Left1.temperature(PERCENT) >= 80 or Intake_Motor.temperature(PERCENT) >= 80:
                brain.screen.set_pen_color(Color.RED)
                brain.screen.draw_circle(30, 30, 30)
                brain.screen.draw_line(240, 10, 240, 20)
                brain.screen.draw_line(260, 10, 260, 20)
                brain.screen.draw_line(240, 40, 260, 40)
                brain.screen.draw_line(260, 50, 270, 50)
                brain.screen.draw_line(240, 50, 230, 50)
            wait(0.1, SECONDS)
            for repeat_count in range(10):
                #motor print for data
                brain.screen.set_pen_color(Color.WHITE)

                B_print=brain.screen.print
                B_new_line=brain.screen.next_row

                brain.screen.set_font(FontType.MONO20)
                brain.screen.set_cursor(1,1)
                B_print("Selected program: ")
                B_new_line()
                if color_select==2:
                    B_print("Red ")
                elif color_select==3:
                    B_print("Blue ")
                elif color_select==4:
                    B_print("None ")
                if Aton_select==2:
                    B_print("Right.")
                elif Aton_select==3:
                    B_print("Left.")
                elif Aton_select==4:
                    B_print("None.")
                brain.screen.set_font(FontType.MONO15)
                brain.screen.set_cursor(6, 1)
                brain.screen.set_pen_color(Color.GREEN)
                B_print( "Port   Name      Temp Power Torque efficiency")
                B_new_line()
                if Intake_Motor.temperature(PERCENT)>50 and Intake_Motor.temperature(PERCENT)<80:
                    brain.screen.set_pen_color(Color.YELLOW)
                elif Intake_Motor.temperature(PERCENT) > 80:
                    brain.screen.set_pen_color(Color.RED)
                else:
                    brain.screen.set_pen_color(Color.GREEN)
                B_print("14 Intake Motor: ", Intake_Motor.temperature(PERCENT), Intake_Motor.power(PowerUnits.WATT), Intake_Motor.torque(TorqueUnits.NM), Intake_Motor.efficiency(PERCENT))
                B_new_line()
                if Left1.temperature(PERCENT)>50 and Left1.temperature(PERCENT)<80:
                    brain.screen.set_pen_color(Color.YELLOW)
                elif Left1.temperature(PERCENT) > 80:
                    brain.screen.set_pen_color(Color.RED)
                else:
                    brain.screen.set_pen_color(Color.GREEN)
                B_print("20       Left_1: ", Left1.temperature(PERCENT),  Left1.power(PowerUnits.WATT),  Left1.torque(TorqueUnits.NM),  Left1.efficiency(PERCENT))
                B_new_line()
                if Left2.temperature(PERCENT)>50 and Left2.temperature(PERCENT)<80:
                    brain.screen.set_pen_color(Color.YELLOW)
                elif Left2.temperature(PERCENT) > 80:
                    brain.screen.set_pen_color(Color.RED)
                else:
                    brain.screen.set_pen_color(Color.GREEN)
                B_print("19       Left_2: ", Left2.temperature(PERCENT), Left2.power(PowerUnits.WATT), Left2.torque(TorqueUnits.NM), Left2.efficiency(PERCENT))
                B_new_line()
                if Left3.temperature(PERCENT)>50 and Left3.temperature(PERCENT)<80:
                    brain.screen.set_pen_color(Color.YELLOW)
                elif Left3.temperature(PERCENT) > 80:
                    brain.screen.set_pen_color(Color.RED)
                else:
                    brain.screen.set_pen_color(Color.GREEN)
                B_print("18       Left_3: ", Left3.temperature(PERCENT), Left3.power(PowerUnits.WATT), Left3.torque(TorqueUnits.NM), Left3.efficiency(PERCENT))
                B_new_line()
                if Right1.temperature(PERCENT)>50 and Right1.temperature(PERCENT)<80:
                    brain.screen.set_pen_color(Color.YELLOW)
                elif Right1.temperature(PERCENT) > 80:
                    brain.screen.set_pen_color(Color.RED)
                else:
                    brain.screen.set_pen_color(Color.GREEN)
                B_print("11      Right_1: ", Right1.temperature(PERCENT), Right1.power(PowerUnits.WATT), Right1.torque(TorqueUnits.NM), Right1.efficiency(PERCENT))
                B_new_line()
                if Right2.temperature(PERCENT)>50 and Right2.temperature(PERCENT)<80:
                    brain.screen.set_pen_color(Color.YELLOW)
                elif Right2.temperature(PERCENT) > 80:
                    brain.screen.set_pen_color(Color.RED)
                else:
                    brain.screen.set_pen_color(Color.GREEN)
                B_print("13      Right_2: ", Right2.temperature(PERCENT), Right2.power(PowerUnits.WATT), Right2.torque(TorqueUnits.NM), Right2.efficiency(PERCENT))
                B_new_line()
                if Right3.temperature(PERCENT)>50 and Right3.temperature(PERCENT)<80:
                    brain.screen.set_pen_color(Color.YELLOW)
                elif Right3.temperature(PERCENT) > 80:
                    brain.screen.set_pen_color(Color.RED)
                else:
                    brain.screen.set_pen_color(Color.GREEN)
                B_print("12      Right_3: ", Right3.temperature(PERCENT), Right3.power(PowerUnits.WATT), Right3.torque(TorqueUnits.NM), Right3.efficiency(PERCENT))
                B_new_line()
                if colorsorting.temperature(PERCENT)>50 and colorsorting.temperature(PERCENT)<80:
                    brain.screen.set_pen_color(Color.YELLOW)
                elif colorsorting.temperature(PERCENT) > 80:
                    brain.screen.set_pen_color(Color.RED)
                else:
                    brain.screen.set_pen_color(Color.GREEN)
                B_print("15    Colorsort: ", colorsorting.temperature(PERCENT), colorsorting.power(PowerUnits.WATT), colorsorting.torque(TorqueUnits.NM), colorsorting.efficiency(PERCENT))
                B_new_line()
                if TopMotor.temperature(PERCENT)>50 and TopMotor.temperature(PERCENT)<80:
                    brain.screen.set_pen_color(Color.YELLOW)
                elif TopMotor.temperature(PERCENT) > 80:
                    brain.screen.set_pen_color(Color.RED)
                else:
                    brain.screen.set_pen_color(Color.GREEN)
                B_print("1     Top_motor: ", TopMotor.temperature(PERCENT), TopMotor.power(PowerUnits.WATT), TopMotor.torque(TorqueUnits.NM), TopMotor.efficiency(PERCENT))
                B_new_line()
                if inertial_for_auton.rotation(DEGREES)==0:
                    brain.screen.set_pen_color(Color.RED)
                else:
                    brain.screen.set_pen_color(Color.GREEN)
                B_print("inertal sensor rotation: ", inertial_for_auton.rotation(DEGREES))

                brain.screen.set_cursor(1,42)
                B_print("Battery Percent: ", brain.battery.capacity())
                brain.screen.set_cursor(2,42)
                B_print("Battery Voltage: ", brain.battery.voltage(VoltageUnits.VOLT))
                brain.screen.set_cursor(3,42)
                B_print("Battery Current: ", brain.battery.current(CurrentUnits.AMP))

                brain.screen.render()
                wait(100,MSEC)
                wait(5, MSEC)
            brain.screen.clear_screen()
            wait(5, MSEC)
            while screen_options==1:
                wait(5, MSEC)

def controller_1buttonB_pressed_callback_0():
    global my_event, Consle_output, Front_Down, Recording
    if Front_Down == 1:
        frontPiston.set(False)
        Front_Down = 2
        if Recording==1:
            brain.sdcard.appendfile("Left_Aton.txt", bytearray(", frontPiston.set(False)", "utf-8"))
        elif Recording==2:
            brain.sdcard.appendfile("Right_Aton.txt", bytearray(", frontPiston.set(False)", "utf-8"))
    else:
        frontPiston.set(True)
        Front_Down = 1
        if Recording==1:
            brain.sdcard.appendfile("Left_Aton.txt", bytearray(", frontPiston.set(True)", "utf-8"))   
        elif Recording==2:
            brain.sdcard.appendfile("Right_Aton.txt", bytearray(", frontPiston.set(True)", "utf-8"))

def onauton_autonomous_0():
    global my_event, Consle_output, Push, Aton_select, Front_Down
    Aton_init_setup()
    if Aton_select == 0:
        # Code for waiting until selection has been chosen.
        while not not Aton_select == 0:
            wait(5, MSEC)
    if Aton_select == 2:
        # Right Aton.

        # Load from SD Card if inserted.
        if brain.sdcard.is_inserted():
            #SD card reading
            Right_Aton_file = brain.sdcard.loadfile("Right_Aton.txt")
            exec(Right_Aton_file.decode("utf-8"))
            Logger("DA10", "Loaded Right Aton from SD Card")
        else:
            # Default Right Aton if no SD Card.
            print("No SD Card Inserted. Running Default Right Aton.")
            set_drivetrain_volosity_v(60)
            Intake_Motor.set_velocity(100, PERCENT)
            Intake_Motor.spin(FORWARD)
            TopMotor.spin(REVERSE)
            Drive_Forward_MM_mm(100)
            Turn_Degrees_Degrees(40)
            set_drivetrain_volosity_v(30)
            Drive_Forward_MM_mm(700)
            wait(0.4, SECONDS)
            Intake_Motor.stop()
            Drive_Forward_MM_mm(-140)
            set_drivetrain_volosity_v(60)
            Turn_Degrees_Degrees(-70)
            set_drivetrain_volosity_v(60)
            Drive_Forward_MM_mm(330)
            Intake_Motor.spin(REVERSE)
            wait(3, SECONDS)
            Intake_Motor.stop()
            TopMotor.stop()
            set_drivetrain_volosity_v(80)
            Drive_Forward_MM_mm(-900)
            Turn_to_rotation__degrees_degrees(270)
            set_drivetrain_volosity_v(80)
            Drive_Forward_MM_mm(-270)
            Turn_to_rotation__degrees_degrees(180)
            set_drivetrain_volosity_v(80)
            set_drivetrain_volosity_v(50)
            Drive_Forward_MM_mm(-310)
            TopMotor.spin(REVERSE)
            Intake_Motor.spin(REVERSE)
            wait(3, SECONDS)
            Intake_Motor.stop()
            TopMotor.stop()
    if Aton_select == 3:
        # Left Aton.

        # Load from SD Card if inserted.
        if brain.sdcard.is_inserted():
            #SD card reading
            Left_Aton_file = brain.sdcard.loadfile("Left_Aton.txt")
            exec(Left_Aton_file.decode("utf-8"))
            Logger("DA11", "Loaded Left Aton from SD Card")
        else:
            # Default Left Aton if no SD Card.
            print("No SD Card Inserted. Running Default Left Aton.")
            set_drivetrain_volosity_v(50)
            Drive_Forward_MM_mm(100)
            Turn_Degrees_Degrees(-40)
            set_drivetrain_volosity_v(30)
            Intake_Motor.spin(FORWARD)
            Drive_Forward_MM_mm(700)
            wait(0.2, SECONDS)
            Drive_Forward_MM_mm(-100)
            Turn_Degrees_Degrees(-100)
            Drive_Forward_MM_mm(-330)
            Intake_Motor.set_velocity(70, PERCENT)
            Intake_Motor.spin(FORWARD)
            TopMotor.spin(FORWARD)

    if Aton_select == 4:
        # None Aton.
        Drive_Forward_MM_mm(25)

def controller_1buttonL1_pressed_callback_0():
    global my_event, Consle_output, Recording
    TopMotor.spin(REVERSE)
    Intake_Motor.spin(FORWARD)
    if Recording==1:
        #Intake and Top Motor position recording for Left Aton
        brain.sdcard.appendfile("Left_Aton.txt", bytearray(", Intake_Motor.spin(FORWARD)", "utf-8"))
        brain.sdcard.appendfile("Left_Aton.txt", bytearray(", TopMotor.spin(REVERSE)", "utf-8"))
        print("Recorded Intake Motor Spin Forward")
        print("Recorded Top Motor Spin Reverse")
    elif Recording==2:
        #Intake and Top Motor position recording for Right Aton
        brain.sdcard.appendfile("Right_Aton.txt", bytearray(", Intake_Motor.spin(FORWARD)", "utf-8"))
        brain.sdcard.appendfile("Right_Aton.txt", bytearray(", TopMotor.spin(REVERSE)", "utf-8"))
        print("Recorded Intake Motor Spin Forward")
        print("Recorded Top Motor Spin Reverse")
    while controller_1.buttonL1.pressing():
        wait(5, MSEC)
    TopMotor.stop()
    Intake_Motor.stop()
    if Recording==1:
        #Intake and Top Motor position recording for Left Aton
        brain.sdcard.appendfile("Left_Aton.txt", bytearray(", Intake_Motor.stop()", "utf-8"))
        brain.sdcard.appendfile("Left_Aton.txt", bytearray(", TopMotor.stop()", "utf-8"))
        print("Recorded Intake Motor Spin Stop")
        print("Recorded Top Motor Spin Stop")
    elif Recording==2:
        #Intake and Top Motor position recording for Right Aton
        brain.sdcard.appendfile("Right_Aton.txt", bytearray(", Intake_Motor.stop()", "utf-8"))
        brain.sdcard.appendfile("Right_Aton.txt", bytearray(", TopMotor.stop()", "utf-8"))
        print("Recorded Intake Motor stop")
        print("Recorded Top Motor stop")

def controller_1buttonR1_pressed_callback_0():
    global my_event, Consle_output, Recording
    Intake_Motor.spin(FORWARD)
    if Recording==1:
        #Intake Motor position recording for Left Aton
        brain.sdcard.appendfile("Left_Aton.txt", bytearray(", Intake_Motor.spin(FORWARD)", "utf-8"))
        print("Recorded Intake Motor Spin Forward")
    elif Recording==2:
        #Intake Motor position recording for Right Aton
        brain.sdcard.appendfile("Right_Aton.txt", bytearray(", Intake_Motor.spin(FORWARD)", "utf-8"))
        print("Recorded Intake Motor Spin Forward")
    while controller_1.buttonR1.pressing():
        wait(5, MSEC)
    Intake_Motor.stop()
    if Recording==1:
        #Intake Motor position recording for Left Aton
        brain.sdcard.appendfile("Left_Aton.txt", bytearray(", Intake_Motor.stop()", "utf-8"))
        print("Recorded Intake Motor Stop")
    elif Recording==2:
        #Intake Motor position recording for Right Aton
        brain.sdcard.appendfile("Right_Aton.txt", bytearray(", Intake_Motor.stop()", "utf-8"))
        print("Recorded Intake Motor Stop")

def controller_1buttonDown_pressed_callback_0():
    global my_event, Consle_output, Recording, Push
    if Push == 1:
        Pusher.set(False)
        Push = 2
        if Recording==1:
            #Pusher position False recording for Left Aton
            brain.sdcard.appendfile("Left_Aton.txt", bytearray(", Pusher.set(False)", "utf-8"))
        elif Recording==2:
            #Pusher position False recording for Right Aton
            brain.sdcard.appendfile("Right_Aton.txt", bytearray(", Pusher.set(False)", "utf-8"))
    else:
        Pusher.set(True)
        Push = 1
        if Recording==1:
            #Pusher position True recording for Left Aton
            brain.sdcard.appendfile("Left_Aton.txt", bytearray(", Pusher.set(True)", "utf-8"))
        elif Recording==2:
            #Pusher position True recording for Right Aton
            brain.sdcard.appendfile("Right_Aton.txt", bytearray(", Pusher.set(True)", "utf-8"))

def controller_1buttonL2_pressed_callback_0():
    global my_event, Consle_output, Recording
    Intake_Motor.spin(REVERSE)
    TopMotor.spin(REVERSE)
    if Recording==1:
        #Intake and Top Motor position recording for Left Aton
        brain.sdcard.appendfile("Left_Aton.txt", bytearray(", Intake_Motor.spin(REVERSE)", "utf-8"))
        brain.sdcard.appendfile("Left_Aton.txt", bytearray(", TopMotor.spin(REVERSE)", "utf-8"))
        print("Recorded Intake Motor Spin Reverse")
        print("Recorded Top Motor Spin Reverse")
    elif Recording==2:
        #Intake and Top Motor position recording for Right Aton
        brain.sdcard.appendfile("Right_Aton.txt", bytearray(", Intake_Motor.spin(REVERSE)", "utf-8"))
        brain.sdcard.appendfile("Right_Aton.txt", bytearray(", TopMotor.spin(REVERSE)", "utf-8"))
        print("Recorded Intake Motor Spin Reverse")
        print("Recorded Top Motor Spin Reverse")
    while controller_1.buttonL2.pressing():
        wait(5, MSEC)
    TopMotor.stop()
    Intake_Motor.stop()
    if Recording==1:
        #Intake and Top Motor position recording for Left Aton
        brain.sdcard.appendfile("Left_Aton.txt", bytearray(", Intake_Motor.stop()", "utf-8"))
        brain.sdcard.appendfile("Left_Aton.txt", bytearray(", TopMotor.stop()", "utf-8"))
        print("Recorded Intake Motor Stop")
        print("Recorded Top Motor Stop")
    elif Recording==2:
        #Intake and Top Motor position recording for Right Aton
        brain.sdcard.appendfile("Right_Aton.txt", bytearray(", Intake_Motor.stop()", "utf-8"))
        brain.sdcard.appendfile("Right_Aton.txt", bytearray(", TopMotor.stop()", "utf-8"))
        print("Recorded Intake Motor stop")
        print("Recorded Top Motor stop")
    
def controller_1buttonR2_pressed_callback_0():
    global my_event, Consle_output, Recording
    Intake_Motor.spin(REVERSE)
    if Recording==1:
        #Intake Motor position recording for Left Aton
        brain.sdcard.appendfile("Left_Aton.txt", bytearray(", Intake_Motor.spin(REVERSE)", "utf-8"))
        print("Recorded Intake Motor Spin Forward")
    elif Recording==2:
        #Intake Motor position recording for Right Aton
        brain.sdcard.appendfile("Right_Aton.txt", bytearray(", Intake_Motor.spin(REVERSE)", "utf-8"))
        print("Recorded Intake Motor Spin Forward")
    while controller_1.buttonR2.pressing():
        wait(5, MSEC)
    Intake_Motor.stop()
    if Recording==1:
        #Intake Motor position recording for Left Aton
        brain.sdcard.appendfile("Left_Aton.txt", bytearray(", Intake_Motor.stop()", "utf-8"))
        print("Recorded Intake Motor Stop")
    elif Recording==2:
        #Intake Motor position recording for Right Aton
        brain.sdcard.appendfile("Right_Aton.txt", bytearray(", Intake_Motor.stop()", "utf-8"))
        print("Recorded Intake Motor Stop")
    

def controller_1buttonRight_pressed_callback_0():
    global my_event, Consle_output
    TopMotor.spin(REVERSE)
    if Recording==1:
        #Top Motor position recording for Left Aton
        brain.sdcard.appendfile("Left_Aton.txt", bytearray(", TopMotor.spin(REVERSE)", "utf-8"))
        print("Recorded Top Motor Spin Reverse")
    elif Recording==2:
        #Top Motor position recording for Right Aton
        brain.sdcard.appendfile("Right_Aton.txt", bytearray(", TopMotor.spin(REVERSE)", "utf-8"))
        print("Recorded Top Motor Spin Reverse")
    while controller_1.buttonRight.pressing():
        wait(5, MSEC)
    TopMotor.stop()
    if Recording==1:
        #Top Motor position recording for Left Aton
        brain.sdcard.appendfile("Left_Aton.txt", bytearray(", TopMotor.stop()", "utf-8"))
        print("Recorded Top Motor Stop")
    elif Recording==2:
        #Top Motor position recording for Right Aton
        brain.sdcard.appendfile("Right_Aton.txt", bytearray(", TopMotor.stop()", "utf-8"))
        print("Recorded Top Motor Stop")

def controller_1axis2Changed_callback_0():
    global my_event, Consle_output
    Right_speed = controller_1.axis2.position() / 8.33
    Right1.spin(FORWARD, Right_speed, VOLT)
    Right2.spin(FORWARD, Right_speed, VOLT)
    Right3.spin(FORWARD, Right_speed, VOLT)
    wait(5, MSEC)
    print("Right drive: ", str(controller_1.axis2.position()))

def controller_1buttonUp_pressed_callback_0():
    global my_event, Consle_output
    colorsorting.stop()

def Deny():
    global Recording, No
    Recording= 0
    No=1
    controller_1.screen.clear_row(3)
    controller_1.screen.set_cursor(3,1)
    controller_1.screen.print("Recording Cancelled")
    print ("Recording Cancelled")

def Yes_left():
    global Recording
    Recording= 1
    controller_1.screen.clear_row(3)
    controller_1.screen.set_cursor(3,1)
    controller_1.screen.print("Recording Left Aton")
    print ("Started Left Aton Recording")

def Yes_right():
    global Recording
    Recording= 2
    controller_1.screen.clear_row(3)
    controller_1.screen.set_cursor(3,1)
    controller_1.screen.print("Recording Right Aton")
    print ("Started Right Aton Recording")

def controller_1buttonA_pressed_callback_0():
    global my_event, Consle_output, Recording, No
    # Left Aton Recording Toggle
    if Recording==0:
        Recording=1
        
    elif Recording==1:
        Recording= 0
        controller_1.screen.clear_row(3)
        controller_1.screen.set_cursor(3,1)
        controller_1.screen.print("Recording Stopped")
        print ("Stopped Left Aton Recording")

def controller_1buttonX_pressed_callback_0():
    global my_event, Consle_output, Recording,  No
    # Right Aton Recording Toggle
    if Recording==0:
        controller_1.screen.clear_row(3)
        controller_1.screen.set_cursor(3,1)
        controller_1.screen.print("Record Right Aton? A/B")
        controller_1.buttonA.pressed(Yes_right)
        controller_1.buttonB.pressed(Deny)
        while Recording==0 and No==0:
            wait(5,MSEC)
        controller_1.buttonA.pressed(controller_1buttonA_pressed_callback_0)
        controller_1.buttonB.pressed(controller_1buttonB_pressed_callback_0)
        No=0
    elif Recording==2:
        Recording= 0
        controller_1.screen.clear_row(3)
        controller_1.screen.set_cursor(3,1)
        controller_1.screen.print("Recording Stopped")
        print ("Stopped Right Aton Recording")

def controller_1axis3Changed_callback_0():
    global my_event, Consle_output
    left_speed = controller_1.axis3.position() / 8.333
    Left1.spin(FORWARD, left_speed, VOLT)
    Left2.spin(FORWARD, left_speed, VOLT)
    Left3.spin(FORWARD, left_speed, VOLT)
    wait(5, MSEC)
    print("Left drive: ", str(controller_1.axis3.position()))

def optical_9_detects_object_callback_0():
    global my_event, Consle_output, color_select
    if color_select == 2:
        # Red mode.
        for repeat_count in range(5):
            Color_sorting_Color(optical_9.color() == Color.BLUE)
            wait(5, MSEC)
        colorsorting.stop()
    if color_select == 3:
        # Blue mode.
        for repeat_count2 in range(5):
            Color_sorting_Color(optical_9.color() == Color.RED)
            wait(5, MSEC)
        colorsorting.stop()

def Velosity_setup_up():
    global PreVolosity
    PreVolosity+=10

def Velosity_setup_down():
    global PreVolosity
    PreVolosity-=10

def Velosity_yes():
    global PreVolosity, Volosity_Aton
    Volosity_Aton=PreVolosity

def velosity_no():
    global Recording
    Recording=0

def ondriver_drivercontrol_0():
    global my_event, Consle_output, Recording
    Driver_init_setup()

    #Aton Drive Recording Code
    if Recording==1 or Recording==2 or Recording==0:
        #wait for command to start recording
        while Recording == 0:
            wait(5, MSEC)
        # Left Aton Recording Code
        if Recording==1:
            # Create or Overwrite Left Aton file on SD Card
            controller_1.screen.clear_row(3)
            controller_1.buttonUp.pressed(Velosity_setup_up)
            controller_1.buttonDown.pressed(Velosity_setup_down)
            controller_1.buttonA.pressed(Velosity_yes)
            controller_1.buttonB.pressed(velosity_no)

            while Recording==1 and Volosity_Aton==0:
                controller_1.screen.clear_row(3)
                controller_1.screen.print("Select velosity: ", PreVolosity)
            
            controller_1.screen.clear_row(3)
            controller_1.buttonA.pressed(controller_1buttonA_pressed_callback_0)
            controller_1.buttonB.pressed(controller_1buttonB_pressed_callback_0)
            controller_1.buttonUp.pressed(controller_1buttonUp_pressed_callback_0)
            controller_1.buttonDown.pressed(controller_1buttonDown_pressed_callback_0)
            

            brain.sdcard.savefile("Left_Aton.txt",  bytearray("set_drivetrain_volosity_v(%f)"%(Volosity_Aton), "utf-8"))

            #Initial position reset for Left and Right drive motors and inertial sensor
            Right1.set_position(0, DEGREES)
            Left1.set_position(0, DEGREES)
            while Recording==1:
                inertial_for_auton.set_rotation(0, DEGREES)
                # Driving and Turning Recording for Left Aton

                #Moving forward
                if controller_1.axis2.position() != 0 and controller_1.axis3.position() != 0:
                    while controller_1.axis2.position() != 0 and controller_1.axis3.position() != 0:
                        controller_1_Velosity_Left.append(controller_1.axis2.position())
                        controller_1_Velosity_Right.append(controller_1.axis3.position())
                        wait(5, MSEC)
                        if controller_1.axis2.position() == 0 or controller_1.axis3.position() == 0:
                            break
                    
                    for Velosity_count in range(len(controller_1_Velosity_Left)):
                        n1=Left_Velosity
                        n2=controller_1_Velosity_Left[Velosity_count]
                        Left_Velosity=Left_Velosity+n1+n2/3
                        print("Left Velosity Sum: ", Left_Velosity)
                    for Velosity_count2 in range(len(controller_1_Velosity_Right)):
                        m1=Right_Velosity
                        m2=controller_1_Velosity_Right[Velosity_count2]
                        Right_Velosity=Right_Velosity+m1+m2/3
                        print("Right Velosity Sum: ", Right_Velosity)
                        
                    brain.sdcard.appendfile("Left_Aton.txt", bytearray(", Curved_move(%s, %s)" %(Right1.position(DEGREES), Left1.position(DEGREES)), "utf-8"))
                    print("Recorded Drive F: ", Right1.position(DEGREES), Left1.position(DEGREES))
                    Right1.set_position(0, DEGREES)
                    Left1.set_position(0, DEGREES)
                
                #Turning right
                if controller_1.axis2.position() < 0 and controller_1.axis3.position() > 0:
                    while controller_1.axis2.position() < 0 and controller_1.axis3.position() > 0:
                        wait(5, MSEC)
                        if controller_1.axis2.position() == 0 or controller_1.axis3.position() == 0:
                            break
                    brain.sdcard.appendfile("Left_Aton.txt", bytearray(", Turn_Degrees_Degrees(%f)" %(inertial_for_auton.rotation(DEGREES)), "utf-8"))
                    print("Recorded Turn R: ", str(inertial_for_auton.rotation(DEGREES)))
                    Right1.set_position(0, DEGREES)
                    Left1.set_position(0, DEGREES)

                #Turning left
                if controller_1.axis2.position() > 0 and controller_1.axis3.position() < 0:
                    while controller_1.axis2.position() > 0 and controller_1.axis3.position() < 0:
                        wait(5, MSEC)
                        if controller_1.axis2.position() == 0 or controller_1.axis3.position() == 0:
                            break
                    brain.sdcard.appendfile("Left_Aton.txt", bytearray(", Turn_Degrees_Degrees(-%f)" %(inertial_for_auton.rotation(DEGREES)), "utf-8"))
                    print("Recorded Turn R: ", str(-inertial_for_auton.rotation(DEGREES)))
                    Right1.set_position(0, DEGREES)
                    Left1.set_position(0, DEGREES)
                
                #Right side drive only
                if controller_1.axis3.position() != 0:
                    while controller_1.axis3.position() != 0:
                        wait(5, MSEC)
                        if controller_1.axis2.position() != 0:
                            break
                    brain.sdcard.appendfile("Left_Aton.txt", bytearray(", Drive_Right_degrees_F_R(%f, 'F')" %Right1.position(DEGREES), "utf-8"))
                    print("Recorded Drive R: ", str(Right1.position(DEGREES)))
                    Right1.set_position(0, DEGREES)
                    Left1.set_position(0, DEGREES)
                
                #Left side drive only
                if controller_1.axis2.position() != 0:
                    while controller_1.axis2.position() != 0:
                        wait(5, MSEC)
                        if controller_1.axis3.position() != 0:
                            break
                    brain.sdcard.appendfile("Left_Aton.txt", bytearray(", Drive_left_degrees_F_R(%f, 'F')" %Left1.position(DEGREES), "utf-8"))
                    print("Recorded Drive L: ", str(Left1.position(DEGREES)))
                    Right1.set_position(0, DEGREES)
                    Left1.set_position(0, DEGREES)
                
                #Wait time recording
                if controller_1.axis2.position() == 0 and controller_1.axis3.position() == 0 and not controller_1.buttonA.pressing() and not controller_1.buttonB.pressing() and not controller_1.buttonUp.pressing() and not controller_1.buttonDown.pressing() and not controller_1.buttonLeft.pressing():
                    brain.timer.reset()
                    while controller_1.axis2.position() == 0 and controller_1.axis3.position() == 0 and not controller_1.buttonA.pressing() and not controller_1.buttonB.pressing() and not controller_1.buttonUp.pressing() and not controller_1.buttonDown.pressing() and not controller_1.buttonLeft.pressing():
                        wait(5, MSEC)
                        if controller_1.buttonL1.pressing() or controller_1.buttonR1.pressing() or controller_1.buttonL2.pressing() or controller_1.buttonR2.pressing() or controller_1.buttonRight.pressing():
                            while Intake_Motor.is_spinning() or TopMotor.is_spinning():
                                wait(5, MSEC)
                            break
                    brain.sdcard.appendfile("Left_Aton.txt", bytearray(", wait(%f, SECONDS)" %(brain.timer.time(SECONDS)), "utf-8"))
                    print("Recorded Wait Time: ", str(brain.timer.time(SECONDS))) 
        # Right Aton Recording Code    
        elif Recording==2:
            # Create or Overwrite Right Aton file on SD Card
            controller_1.screen.clear_row(3)
            controller_1.buttonUp.pressed(Velosity_setup_up)
            controller_1.buttonDown.pressed(Velosity_setup_down)
            controller_1.buttonA.pressed(Velosity_yes)
            controller_1.buttonB.pressed(velosity_no)

            while Recording==1 and Volosity_Aton==0:
                controller_1.screen.clear_row(3)
                controller_1.screen.print("Select velosity: ", PreVolosity)
            
            controller_1.screen.clear_row(3)
            controller_1.buttonA.pressed(controller_1buttonA_pressed_callback_0)
            controller_1.buttonB.pressed(controller_1buttonB_pressed_callback_0)
            controller_1.buttonUp.pressed(controller_1buttonUp_pressed_callback_0)
            controller_1.buttonDown.pressed(controller_1buttonDown_pressed_callback_0)

            brain.sdcard.savefile("Right_Aton.txt", bytearray("set_drivetrain_volosity_v(%f)"%(Volosity_Aton), "utf-8"))

            #Initial position reset for Left and Right drive motors and inertial sensor
            Right1.set_position(0, DEGREES)
            Left1.set_position(0, DEGREES)
            while Recording==2:
                inertial_for_auton.set_rotation(0, DEGREES)
                # Driving and Turning Recording for Right Aton

                #Moving forward
                if controller_1.axis2.position() > 0 and controller_1.axis3.position() > 0:
                    while controller_1.axis2.position() > 0 and controller_1.axis3.position() > 0:
                        wait(5, MSEC)
                        if controller_1.axis2.position() == 0 or controller_1.axis3.position() == 0:
                            break
                    brain.sdcard.appendfile("Right_Aton.txt", bytearray(", Drive_Forward_MM_mm(%f)" %((Right1.position(DEGREES)+Left1.position(DEGREES))/2), "utf-8"))
                    print("Recorded Drive F: ", str((Right1.position(DEGREES)+Left1.position(DEGREES))/2))
                    Right1.set_position(0, DEGREES)
                    Left1.set_position(0, DEGREES)
                
                #Turning right
                if controller_1.axis2.position() < 0 and controller_1.axis3.position() > 0:
                    while controller_1.axis2.position() < 0 and controller_1.axis3.position() > 0:
                        wait(5, MSEC)
                        if controller_1.axis2.position() == 0 or controller_1.axis3.position() == 0:
                            break
                    brain.sdcard.appendfile("Right_Aton.txt", bytearray(", Turn_Degrees_Degrees(%f)" %(inertial_for_auton.rotation(DEGREES)), "utf-8"))
                    print("Recorded Turn R: ", str(inertial_for_auton.rotation(DEGREES)))
                    Right1.set_position(0, DEGREES)
                    Left1.set_position(0, DEGREES)

                #Turning left
                if controller_1.axis2.position() > 0 and controller_1.axis3.position() < 0:
                    while controller_1.axis2.position() > 0 and controller_1.axis3.position() < 0:
                        wait(5, MSEC)
                        if controller_1.axis2.position() == 0 or controller_1.axis3.position() == 0:
                            break
                    brain.sdcard.appendfile("Right_Aton.txt", bytearray(", Turn_Degrees_Degrees(-%f)" %(inertial_for_auton.rotation(DEGREES)), "utf-8"))
                    print("Recorded Turn R: ", str(-inertial_for_auton.rotation(DEGREES)))
                    Right1.set_position(0, DEGREES)
                    Left1.set_position(0, DEGREES)
                
                #Right side drive only
                if controller_1.axis2.position() != 0:
                    while controller_1.axis2.position() != 0:
                        wait(5, MSEC)
                        if controller_1.axis3.position() != 0:
                            break
                    brain.sdcard.appendfile("Right_Aton.txt", bytearray(", Drive_Right_degrees_F_R(%f, 'F')" %Right1.position(DEGREES), "utf-8"))
                    print("Recorded Drive R: ", str(Right1.position(DEGREES)))
                    Right1.set_position(0, DEGREES)
                    Left1.set_position(0, DEGREES)

                #Left side drive only
                if controller_1.axis3.position() != 0:
                    while controller_1.axis3.position() != 0:
                        wait(5, MSEC)
                        if controller_1.axis2.position() != 0:
                            break
                    brain.sdcard.appendfile("Right_Aton.txt", bytearray(", Drive_left_degrees_F_R(%f, 'F')" %Left1.position(DEGREES), "utf-8"))
                    print("Recorded Drive L: ", str(Left1.position(DEGREES)))
                    Right1.set_position(0, DEGREES)
                    Left1.set_position(0, DEGREES)
                
                #Wait time recording
                if controller_1.axis2.position() == 0 and controller_1.axis3.position() == 0 and not controller_1.buttonL1.pressing() and not controller_1.buttonL2.pressing() and not controller_1.buttonR1.pressing() and not controller_1.buttonR2.pressing() and not controller_1.buttonA.pressing() and not controller_1.buttonB.pressing() and not controller_1.buttonUp.pressing() and not controller_1.buttonDown.pressing() and not controller_1.buttonLeft.pressing() and not controller_1.buttonRight.pressing():
                    brain.timer.reset()
                    while controller_1.axis2.position() == 0 and controller_1.axis3.position() == 0 and not controller_1.buttonL1.pressing() and not controller_1.buttonL2.pressing() and not controller_1.buttonR1.pressing() and not controller_1.buttonR2.pressing() and not controller_1.buttonA.pressing() and not controller_1.buttonB.pressing() and not controller_1.buttonUp.pressing() and not controller_1.buttonDown.pressing() and not controller_1.buttonLeft.pressing() and not controller_1.buttonRight.pressing(): 
                        wait(5, MSEC)
                    brain.sdcard.appendfile("Right_Aton.txt", bytearray(", wait(%f, SECONDS)" %(brain.timer.time(SECONDS)), "utf-8"))
                    print("Recorded Wait Time: ", str(brain.timer.time(SECONDS)))

# create a function for handling the starting and stopping of all autonomous tasks
def vexcode_auton_function():
    # Start the autonomous control tasks
    auton_task_0 = Thread( onauton_autonomous_0 )
    # wait for the driver control period to end
    while( competition.is_autonomous() and competition.is_enabled() ):
        # wait 10 milliseconds before checking again
        wait( 10, MSEC )
    # Stop the autonomous control tasks
    auton_task_0.stop()

def vexcode_driver_function():
    # Start the driver control tasks
    driver_control_task_0 = Thread( ondriver_drivercontrol_0 )

    # wait for the driver control period to end
    while( competition.is_driver_control() and competition.is_enabled() ):
        # wait 10 milliseconds before checking again
        wait( 10, MSEC )
    # Stop the driver control tasks
    driver_control_task_0.stop()

def Dinostics():
    global my_event, Consle_output
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

def Options():
    global my_event, Consle_output, color_select, Aton_select, Left_Aton_file, Right_Aton_file, screen_options
    screen_options=1
    brain.screen.clear_screen()
    brain.screen.set_cursor(1,1)
    brain.screen.set_pen_color(Color.WHITE)
    brain.screen.set_font(FontType.MONO15)
    brain.screen.print("Options Mode:")
    while screen_options==1:
        brain.screen.draw_rectangle(10, 10, 460, 222, Color.WHITE)
        brain.screen.set_cursor(2,2)
        brain.screen.print("Dinostics")
        brain.screen.set_cursor(4,2)
        brain.screen.print("Edit Color")
        brain.screen.set_cursor(6,2)
        brain.screen.print("Edit Aton")
        brain.screen.set_cursor(8,2)
        brain.screen.print("Read Left Aton")
        brain.screen.set_cursor(10,2)
        brain.screen.print("Read Right Aton")
        brain.screen.set_cursor(12,2)
        brain.screen.print("Exit Options")
        brain.screen.render()
        if brain.screen.x_position()>10 and brain.screen.x_position()<470 and brain.screen.y_position()>10 and brain.screen.y_position()<40 and brain.screen.pressing():
            Dinostics()
        if brain.screen.x_position()>10 and brain.screen.x_position()<470 and brain.screen.y_position()>50 and brain.screen.y_position()<80 and brain.screen.pressing():
            color_select=0
            screen_options=0
        if brain.screen.x_position()>10 and brain.screen.x_position()<470 and brain.screen.y_position()>90 and brain.screen.y_position()<120 and brain.screen.pressing():
            Aton_select=0
            screen_options=0
        if brain.screen.x_position()>10 and brain.screen.x_position()<470 and brain.screen.y_position()>130 and brain.screen.y_position()<160 and brain.screen.pressing():
            Left_Aton_file = brain.sdcard.loadfile("Left_Aton.txt")
            brain.screen.set_cursor(1,1)
            brain.screen.print("Left Aton Reading...")
            brain.screen.new_line()
            brain.screen.print(Left_Aton_file.decode("utf-8"))
            if brain.screen.pressing():
                screen_options=0
        if brain.screen.x_position()>10 and brain.screen.x_position()<470 and brain.screen.y_position()>170 and brain.screen.y_position()<200 and brain.screen.pressing():
            Right_Aton_file = brain.sdcard.loadfile("Right_Aton.txt")
            brain.screen.set_cursor(1,1)
            brain.screen.print("Right Aton Reading...")
            brain.screen.new_line()
            brain.screen.print(Right_Aton_file.decode("utf-8"))
            if brain.screen.pressing():
                screen_options=0
        if brain.screen.x_position()>10 and brain.screen.x_position()<470 and brain.screen.y_position()>210 and brain.screen.y_position()<240 and brain.screen.pressing():
            screen_options=0
            


# register the competition functions
competition = Competition( vexcode_driver_function, vexcode_auton_function )

# system event handlers
controller_1.buttonX.pressed(controller_1buttonX_pressed_callback_0)
controller_1.buttonA.pressed(controller_1buttonA_pressed_callback_0)
controller_1.buttonB.pressed(controller_1buttonB_pressed_callback_0)
controller_1.buttonL2.pressed(controller_1buttonL2_pressed_callback_0)
controller_1.buttonR1.pressed(controller_1buttonR1_pressed_callback_0)
controller_1.buttonDown.pressed(controller_1buttonDown_pressed_callback_0)
controller_1.buttonL1.pressed(controller_1buttonL1_pressed_callback_0)
controller_1.buttonR2.pressed(controller_1buttonR2_pressed_callback_0)
controller_1.buttonRight.pressed(controller_1buttonRight_pressed_callback_0)
controller_1.axis2.changed(controller_1axis2Changed_callback_0)
controller_1.buttonUp.pressed(controller_1buttonUp_pressed_callback_0)
controller_1.axis3.changed(controller_1axis3Changed_callback_0)
optical_9.object_detected(optical_9_detects_object_callback_0)
# add 15ms delay to make sure events are registered correctly.
wait(15, MSEC)

when_started1()