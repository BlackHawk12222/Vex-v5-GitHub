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

def stop_l_r_drive_l_r(stop_l_r_drive_l_r__l_r):
    global my_event, fake_auto, sd_is_in, Accuracy, Front_Down, right_temp, left_temp, Descoring, turn_mod, DegreesToTurn, TurnData, driveMod, auto_side, Auto_color, leftData, RightData, IntakeData, iteration, LeftDriveData, RightDriveData, IntakeDriveData, Left_Iter, Right_Iter, Intake_Iter, textReadout, LeftVP, RightVP, BreakParsing, AuBP_MaxVP, colortoggle, skillsRun, recording, MatchLoadData, TopMotorDATA, TopMotorDriveDATA, MatchLoadDriveDATA, matchload_iter, top_iter, use_turningInertial, LastFront_down, turn_to_h_dif, Kp, Ki, Kd, error, loop_delay, last_error, integral, position, integral_limit, error_threshhold, derivative, POWER, intake_speed, screen_precision, console_precision, ai_vision_2_index, ai_vision_2_objects, controller_1_precision
    if stop_l_r_drive_l_r__l_r == "l":
        left1.stop()
        left3.stop()
        left2.stop()
    else:
        if stop_l_r_drive_l_r__l_r == "r":
            Right1.stop()
            Right2.stop()
            Right3.stop()
        else:
            pass

def Drive_reverse_dist_milinmeters(Drive_reverse_dist_milinmeters__dist):
    global my_event, fake_auto, sd_is_in, Accuracy, Front_Down, right_temp, left_temp, Descoring, turn_mod, DegreesToTurn, TurnData, driveMod, auto_side, Auto_color, leftData, RightData, IntakeData, iteration, LeftDriveData, RightDriveData, IntakeDriveData, Left_Iter, Right_Iter, Intake_Iter, textReadout, LeftVP, RightVP, BreakParsing, AuBP_MaxVP, colortoggle, skillsRun, recording, MatchLoadData, TopMotorDATA, TopMotorDriveDATA, MatchLoadDriveDATA, matchload_iter, top_iter, use_turningInertial, LastFront_down, turn_to_h_dif, Kp, Ki, Kd, error, loop_delay, last_error, integral, position, integral_limit, error_threshhold, derivative, POWER, intake_speed, screen_precision, console_precision, ai_vision_2_index, ai_vision_2_objects, controller_1_precision
    driveMod = (Drive_reverse_dist_milinmeters__dist / ((69.85 * 3.14) / 360)) / 0.76
    Raw__Drive_f_r_f_r_for_d_degrees("r", driveMod)
    wait(0.1, SECONDS)

def turn_r_l_r_l_for_seconds_seconds_at_speed(turn_r_l_r_l_for_seconds_seconds_at_speed__r_l, turn_r_l_r_l_for_seconds_seconds_at_speed__seconds, turn_r_l_r_l_for_seconds_seconds_at_speed__speed):
    global my_event, fake_auto, sd_is_in, Accuracy, Front_Down, right_temp, left_temp, Descoring, turn_mod, DegreesToTurn, TurnData, driveMod, auto_side, Auto_color, leftData, RightData, IntakeData, iteration, LeftDriveData, RightDriveData, IntakeDriveData, Left_Iter, Right_Iter, Intake_Iter, textReadout, LeftVP, RightVP, BreakParsing, AuBP_MaxVP, colortoggle, skillsRun, recording, MatchLoadData, TopMotorDATA, TopMotorDriveDATA, MatchLoadDriveDATA, matchload_iter, top_iter, use_turningInertial, LastFront_down, turn_to_h_dif, Kp, Ki, Kd, error, loop_delay, last_error, integral, position, integral_limit, error_threshhold, derivative, POWER, intake_speed, screen_precision, console_precision, ai_vision_2_index, ai_vision_2_objects, controller_1_precision
    if turn_r_l_r_l_for_seconds_seconds_at_speed__r_l == "r":
        drive_forward_true_right__R_L_at_velocity_v(False, turn_r_l_r_l_for_seconds_seconds_at_speed__speed)
        drive_reverse_true_right__R_l_at_velocity_v(True, turn_r_l_r_l_for_seconds_seconds_at_speed__speed)
    else:
        drive_forward_true_right__R_L_at_velocity_v(True, turn_r_l_r_l_for_seconds_seconds_at_speed__speed)
        drive_reverse_true_right__R_l_at_velocity_v(False, turn_r_l_r_l_for_seconds_seconds_at_speed__speed)
    wait(turn_r_l_r_l_for_seconds_seconds_at_speed__seconds, SECONDS)
    stop_l_r_drive_l_r("r")
    stop_l_r_drive_l_r("l")

def Turn_To_Heading_heading_input_from_0_359_9(Turn_To_Heading_heading_input_from_0_359_9__heading):
    global my_event, fake_auto, sd_is_in, Accuracy, Front_Down, right_temp, left_temp, Descoring, turn_mod, DegreesToTurn, TurnData, driveMod, auto_side, Auto_color, leftData, RightData, IntakeData, iteration, LeftDriveData, RightDriveData, IntakeDriveData, Left_Iter, Right_Iter, Intake_Iter, textReadout, LeftVP, RightVP, BreakParsing, AuBP_MaxVP, colortoggle, skillsRun, recording, MatchLoadData, TopMotorDATA, TopMotorDriveDATA, MatchLoadDriveDATA, matchload_iter, top_iter, use_turningInertial, LastFront_down, turn_to_h_dif, Kp, Ki, Kd, error, loop_delay, last_error, integral, position, integral_limit, error_threshhold, derivative, POWER, intake_speed, screen_precision, console_precision, ai_vision_2_index, ai_vision_2_objects, controller_1_precision
    turn_to_h_dif = Turn_To_Heading_heading_input_from_0_359_9__heading - inertial_for_auton.heading(DEGREES)
    if turn_to_h_dif > 180:
        Turn_target_Degrees_With_Inertial_Helping(0 - (360 - turn_to_h_dif))
    else:
        Turn_target_Degrees_With_Inertial_Helping(turn_to_h_dif)

def drive_forwards_dist_milimeters(drive_forwards_dist_milimeters__dist):
    global my_event, fake_auto, sd_is_in, Accuracy, Front_Down, right_temp, left_temp, Descoring, turn_mod, DegreesToTurn, TurnData, driveMod, auto_side, Auto_color, leftData, RightData, IntakeData, iteration, LeftDriveData, RightDriveData, IntakeDriveData, Left_Iter, Right_Iter, Intake_Iter, textReadout, LeftVP, RightVP, BreakParsing, AuBP_MaxVP, colortoggle, skillsRun, recording, MatchLoadData, TopMotorDATA, TopMotorDriveDATA, MatchLoadDriveDATA, matchload_iter, top_iter, use_turningInertial, LastFront_down, turn_to_h_dif, Kp, Ki, Kd, error, loop_delay, last_error, integral, position, integral_limit, error_threshhold, derivative, POWER, intake_speed, screen_precision, console_precision, ai_vision_2_index, ai_vision_2_objects, controller_1_precision
    driveMod = (drive_forwards_dist_milimeters__dist / ((69.85 * 3.14) / 360)) / 0.76
    Raw__Drive_f_r_f_r_for_d_degrees("f", driveMod)
    wait(0.1, SECONDS)

def Turn_target_Degrees_With_Inertial_Helping(Turn_target_Degrees_With_Inertial_Helping__target):
    global my_event, fake_auto, sd_is_in, Accuracy, Front_Down, right_temp, left_temp, Descoring, turn_mod, DegreesToTurn, TurnData, driveMod, auto_side, Auto_color, leftData, RightData, IntakeData, iteration, LeftDriveData, RightDriveData, IntakeDriveData, Left_Iter, Right_Iter, Intake_Iter, textReadout, LeftVP, RightVP, BreakParsing, AuBP_MaxVP, colortoggle, skillsRun, recording, MatchLoadData, TopMotorDATA, TopMotorDriveDATA, MatchLoadDriveDATA, matchload_iter, top_iter, use_turningInertial, LastFront_down, turn_to_h_dif, Kp, Ki, Kd, error, loop_delay, last_error, integral, position, integral_limit, error_threshhold, derivative, POWER, intake_speed, screen_precision, console_precision, ai_vision_2_index, ai_vision_2_objects, controller_1_precision
    inertial_for_auton.set_rotation(0, DEGREES)
    raw__turn_d_degrees(Turn_target_Degrees_With_Inertial_Helping__target)
    for repeat_count in range(3):
        raw__turn_d_degrees((Turn_target_Degrees_With_Inertial_Helping__target - inertial_for_auton.rotation(DEGREES)) * 0.5)
        wait(5, MSEC)
    wait(0.1, SECONDS)

def drive_for_seconds_seconds_at_velocity_f_b_f_b(drive_for_seconds_seconds_at_velocity_f_b_f_b__seconds, drive_for_seconds_seconds_at_velocity_f_b_f_b__velocity, drive_for_seconds_seconds_at_velocity_f_b_f_b__f_b):
    global my_event, fake_auto, sd_is_in, Accuracy, Front_Down, right_temp, left_temp, Descoring, turn_mod, DegreesToTurn, TurnData, driveMod, auto_side, Auto_color, leftData, RightData, IntakeData, iteration, LeftDriveData, RightDriveData, IntakeDriveData, Left_Iter, Right_Iter, Intake_Iter, textReadout, LeftVP, RightVP, BreakParsing, AuBP_MaxVP, colortoggle, skillsRun, recording, MatchLoadData, TopMotorDATA, TopMotorDriveDATA, MatchLoadDriveDATA, matchload_iter, top_iter, use_turningInertial, LastFront_down, turn_to_h_dif, Kp, Ki, Kd, error, loop_delay, last_error, integral, position, integral_limit, error_threshhold, derivative, POWER, intake_speed, screen_precision, console_precision, ai_vision_2_index, ai_vision_2_objects, controller_1_precision
    if drive_for_seconds_seconds_at_velocity_f_b_f_b__f_b == "f":
        drive_forward_true_right__R_L_at_velocity_v(True, drive_for_seconds_seconds_at_velocity_f_b_f_b__velocity)
        drive_forward_true_right__R_L_at_velocity_v(False, drive_for_seconds_seconds_at_velocity_f_b_f_b__velocity)
    else:
        if drive_for_seconds_seconds_at_velocity_f_b_f_b__f_b == "b":
            drive_reverse_true_right__R_l_at_velocity_v(True, drive_for_seconds_seconds_at_velocity_f_b_f_b__velocity)
            drive_reverse_true_right__R_l_at_velocity_v(False, drive_for_seconds_seconds_at_velocity_f_b_f_b__velocity)
        else:
            pass
    wait(drive_for_seconds_seconds_at_velocity_f_b_f_b__seconds, SECONDS)
    stop_l_r_drive_l_r("l")
    stop_l_r_drive_l_r("r")

def raw__turn_d_degrees(raw__turn_d_degrees__d):
    global my_event, fake_auto, sd_is_in, Accuracy, Front_Down, right_temp, left_temp, Descoring, turn_mod, DegreesToTurn, TurnData, driveMod, auto_side, Auto_color, leftData, RightData, IntakeData, iteration, LeftDriveData, RightDriveData, IntakeDriveData, Left_Iter, Right_Iter, Intake_Iter, textReadout, LeftVP, RightVP, BreakParsing, AuBP_MaxVP, colortoggle, skillsRun, recording, MatchLoadData, TopMotorDATA, TopMotorDriveDATA, MatchLoadDriveDATA, matchload_iter, top_iter, use_turningInertial, LastFront_down, turn_to_h_dif, Kp, Ki, Kd, error, loop_delay, last_error, integral, position, integral_limit, error_threshhold, derivative, POWER, intake_speed, screen_precision, console_precision, ai_vision_2_index, ai_vision_2_objects, controller_1_precision
    turn_mod = ((((355.6 * 3.14) / 360) * raw__turn_d_degrees__d) / 0.76) * 2
    Right1.spin_for(REVERSE, turn_mod, DEGREES, wait=False)
    Right2.spin_for(REVERSE, turn_mod, DEGREES, wait=False)
    Right3.spin_for(REVERSE, turn_mod, DEGREES, wait=False)
    left1.spin_for(FORWARD, turn_mod, DEGREES, wait=False)
    left2.spin_for(FORWARD, turn_mod, DEGREES, wait=False)
    left3.spin_for(FORWARD, turn_mod, DEGREES)

def init_setup():
    global my_event, fake_auto, sd_is_in, Accuracy, Front_Down, right_temp, left_temp, Descoring, turn_mod, DegreesToTurn, TurnData, driveMod, auto_side, Auto_color, leftData, RightData, IntakeData, iteration, LeftDriveData, RightDriveData, IntakeDriveData, Left_Iter, Right_Iter, Intake_Iter, textReadout, LeftVP, RightVP, BreakParsing, AuBP_MaxVP, colortoggle, skillsRun, recording, MatchLoadData, TopMotorDATA, TopMotorDriveDATA, MatchLoadDriveDATA, matchload_iter, top_iter, use_turningInertial, LastFront_down, turn_to_h_dif, Kp, Ki, Kd, error, loop_delay, last_error, integral, position, integral_limit, error_threshhold, derivative, POWER, intake_speed, screen_precision, console_precision, ai_vision_2_index, ai_vision_2_objects, controller_1_precision
    colorsorting.set_velocity(100, PERCENT)
    Right1.set_velocity(50, PERCENT)
    Right2.set_velocity(50, PERCENT)
    Right3.set_velocity(50, PERCENT)
    left1.set_velocity(50, PERCENT)
    left2.set_velocity(50, PERCENT)
    left3.set_velocity(50, PERCENT)
    Intake.set_velocity(100, PERCENT)
    TopMotor.set_velocity(100, PERCENT)
    TopMotor.set_stopping(BRAKE)
    optical_9.set_light(LedStateType.ON)
    optical_9.set_light_power(100, PERCENT)
    Accuracy = 1
    Front_Down = 0
    Descoring = 0
    leftData = 0
    RightData = 0
    textReadout = 0
    colortoggle = 3
    Right1.set_stopping(BRAKE)
    Right2.set_stopping(BRAKE)
    Right3.set_stopping(BRAKE)
    left1.set_stopping(BRAKE)
    left2.set_stopping(BRAKE)
    left3.set_stopping(BRAKE)

def if_visual_color_detected__sort_block(if_visual_color_detected__sort_block__color):
    global my_event, fake_auto, sd_is_in, Accuracy, Front_Down, right_temp, left_temp, Descoring, turn_mod, DegreesToTurn, TurnData, driveMod, auto_side, Auto_color, leftData, RightData, IntakeData, iteration, LeftDriveData, RightDriveData, IntakeDriveData, Left_Iter, Right_Iter, Intake_Iter, textReadout, LeftVP, RightVP, BreakParsing, AuBP_MaxVP, colortoggle, skillsRun, recording, MatchLoadData, TopMotorDATA, TopMotorDriveDATA, MatchLoadDriveDATA, matchload_iter, top_iter, use_turningInertial, LastFront_down, turn_to_h_dif, Kp, Ki, Kd, error, loop_delay, last_error, integral, position, integral_limit, error_threshhold, derivative, POWER, intake_speed, screen_precision, console_precision, ai_vision_2_index, ai_vision_2_objects, controller_1_precision
    if if_visual_color_detected__sort_block__color:
        Intake.stop()
        colorsorting.spin(REVERSE)
    else:
        colorsorting.stop()

def PID_move_mm_mm(PID_move_mm_mm__mm):
    global my_event, fake_auto, sd_is_in, Accuracy, Front_Down, right_temp, left_temp, Descoring, turn_mod, DegreesToTurn, TurnData, driveMod, auto_side, Auto_color, leftData, RightData, IntakeData, iteration, LeftDriveData, RightDriveData, IntakeDriveData, Left_Iter, Right_Iter, Intake_Iter, textReadout, LeftVP, RightVP, BreakParsing, AuBP_MaxVP, colortoggle, skillsRun, recording, MatchLoadData, TopMotorDATA, TopMotorDriveDATA, MatchLoadDriveDATA, matchload_iter, top_iter, use_turningInertial, LastFront_down, turn_to_h_dif, Kp, Ki, Kd, error, loop_delay, last_error, integral, position, integral_limit, error_threshhold, derivative, POWER, intake_speed, screen_precision, console_precision, ai_vision_2_index, ai_vision_2_objects, controller_1_precision
    driveMod = (PID_move_mm_mm__mm / ((69.85 * 3.14) / 360)) / 0.76
    Right1.set_position(0, DEGREES)
    left1.set_position(0, DEGREES)
    Kp = 0.25
    Ki = 0
    Kd = 2
    error = 0
    last_error = 0
    integral = 0
    loop_delay = 0.015
    error_threshhold = 5
    integral_limit = 300
    while True:
        # AVG motor positions
        position = (Right1.position(DEGREES) + left1.position(DEGREES)) / 2
        # PID math
        error = driveMod - position
        integral = integral + error
        # Anti-windup
        if math.fabs(error) > integral_limit:
            integral = 0
        derivative = error - last_error
        last_error = error
        POWER = Kp * error + (Ki * integral + Kd * derivative)
        # Driving
        Set_Drivetrain_Velocity_to__25(POWER)
        Right1.spin(FORWARD)
        Right2.spin(FORWARD)
        Right3.spin(FORWARD)
        left1.spin(FORWARD)
        left2.spin(FORWARD)
        left3.spin(FORWARD)
        if math.fabs(error) < error_threshhold:
            break
        wait(loop_delay, SECONDS)
        wait(5, MSEC)
    stop_l_r_drive_l_r("l")
    stop_l_r_drive_l_r("r")

def PID_turn_to_head_angle(PID_turn_to_head_angle__head):
    global my_event, fake_auto, sd_is_in, Accuracy, Front_Down, right_temp, left_temp, Descoring, turn_mod, DegreesToTurn, TurnData, driveMod, auto_side, Auto_color, leftData, RightData, IntakeData, iteration, LeftDriveData, RightDriveData, IntakeDriveData, Left_Iter, Right_Iter, Intake_Iter, textReadout, LeftVP, RightVP, BreakParsing, AuBP_MaxVP, colortoggle, skillsRun, recording, MatchLoadData, TopMotorDATA, TopMotorDriveDATA, MatchLoadDriveDATA, matchload_iter, top_iter, use_turningInertial, LastFront_down, turn_to_h_dif, Kp, Ki, Kd, error, loop_delay, last_error, integral, position, integral_limit, error_threshhold, derivative, POWER, intake_speed, screen_precision, console_precision, ai_vision_2_index, ai_vision_2_objects, controller_1_precision
    Kp = 0.2
    Ki = 0
    Kd = 2
    integral_limit = 200
    error_threshhold = 5
    loop_delay = 0.015
    inertial_for_auton.set_heading(0, DEGREES)
    error = 0
    last_error = 0
    integral = 0
    while True:
        # PID math
        error = PID_turn_to_head_angle__head - inertial_for_auton.heading(DEGREES)
        integral = integral + error
        # Anti-windup
        if math.fabs(error) > integral_limit:
            integral = 0
        derivative = error - last_error
        last_error = error
        POWER = Kp * error + (Ki * integral + Kd * derivative)
        # Driving
        Set_Drivetrain_Velocity_to__25(POWER)
        Right1.spin(REVERSE)
        Right2.spin(REVERSE)
        Right3.spin(REVERSE)
        left1.spin(FORWARD)
        left2.spin(FORWARD)
        left3.spin(FORWARD)
        if math.fabs(error) < error_threshhold:
            break
        wait(loop_delay, SECONDS)
        wait(5, MSEC)
    stop_l_r_drive_l_r("l")
    stop_l_r_drive_l_r("r")

def Raw__Drive_f_r_f_r_for_d_degrees(Raw__Drive_f_r_f_r_for_d_degrees__f_r, Raw__Drive_f_r_f_r_for_d_degrees__d):
    global my_event, fake_auto, sd_is_in, Accuracy, Front_Down, right_temp, left_temp, Descoring, turn_mod, DegreesToTurn, TurnData, driveMod, auto_side, Auto_color, leftData, RightData, IntakeData, iteration, LeftDriveData, RightDriveData, IntakeDriveData, Left_Iter, Right_Iter, Intake_Iter, textReadout, LeftVP, RightVP, BreakParsing, AuBP_MaxVP, colortoggle, skillsRun, recording, MatchLoadData, TopMotorDATA, TopMotorDriveDATA, MatchLoadDriveDATA, matchload_iter, top_iter, use_turningInertial, LastFront_down, turn_to_h_dif, Kp, Ki, Kd, error, loop_delay, last_error, integral, position, integral_limit, error_threshhold, derivative, POWER, intake_speed, screen_precision, console_precision, ai_vision_2_index, ai_vision_2_objects, controller_1_precision
    if Raw__Drive_f_r_f_r_for_d_degrees__f_r == "f" or Raw__Drive_f_r_f_r_for_d_degrees__f_r == "F":
        left1.spin_for(FORWARD, Raw__Drive_f_r_f_r_for_d_degrees__d, DEGREES, wait=False)
        left2.spin_for(FORWARD, Raw__Drive_f_r_f_r_for_d_degrees__d, DEGREES, wait=False)
        left3.spin_for(FORWARD, Raw__Drive_f_r_f_r_for_d_degrees__d, DEGREES, wait=False)
        Right1.spin_for(FORWARD, Raw__Drive_f_r_f_r_for_d_degrees__d, DEGREES, wait=False)
        Right2.spin_for(FORWARD, Raw__Drive_f_r_f_r_for_d_degrees__d, DEGREES, wait=False)
        Right3.spin_for(FORWARD, Raw__Drive_f_r_f_r_for_d_degrees__d, DEGREES)
    else:
        if Raw__Drive_f_r_f_r_for_d_degrees__f_r == "r" or Raw__Drive_f_r_f_r_for_d_degrees__f_r == "R":
            left1.spin_for(REVERSE, Raw__Drive_f_r_f_r_for_d_degrees__d, DEGREES, wait=False)
            left2.spin_for(REVERSE, Raw__Drive_f_r_f_r_for_d_degrees__d, DEGREES, wait=False)
            left3.spin_for(REVERSE, Raw__Drive_f_r_f_r_for_d_degrees__d, DEGREES, wait=False)
            Right1.spin_for(REVERSE, Raw__Drive_f_r_f_r_for_d_degrees__d, DEGREES, wait=False)
            Right2.spin_for(REVERSE, Raw__Drive_f_r_f_r_for_d_degrees__d, DEGREES, wait=False)
            Right3.spin_for(REVERSE, Raw__Drive_f_r_f_r_for_d_degrees__d, DEGREES)
        else:
            pass

def drive_forward_true_right__R_L_at_velocity_v(drive_forward_true_right__R_L_at_velocity_v__R_L, drive_forward_true_right__R_L_at_velocity_v__v):
    global my_event, fake_auto, sd_is_in, Accuracy, Front_Down, right_temp, left_temp, Descoring, turn_mod, DegreesToTurn, TurnData, driveMod, auto_side, Auto_color, leftData, RightData, IntakeData, iteration, LeftDriveData, RightDriveData, IntakeDriveData, Left_Iter, Right_Iter, Intake_Iter, textReadout, LeftVP, RightVP, BreakParsing, AuBP_MaxVP, colortoggle, skillsRun, recording, MatchLoadData, TopMotorDATA, TopMotorDriveDATA, MatchLoadDriveDATA, matchload_iter, top_iter, use_turningInertial, LastFront_down, turn_to_h_dif, Kp, Ki, Kd, error, loop_delay, last_error, integral, position, integral_limit, error_threshhold, derivative, POWER, intake_speed, screen_precision, console_precision, ai_vision_2_index, ai_vision_2_objects, controller_1_precision
    if drive_forward_true_right__R_L_at_velocity_v__R_L:
        Right1.set_velocity((drive_forward_true_right__R_L_at_velocity_v__v / Accuracy), PERCENT)
        Right2.set_velocity((drive_forward_true_right__R_L_at_velocity_v__v / Accuracy), PERCENT)
        Right3.set_velocity((drive_forward_true_right__R_L_at_velocity_v__v / Accuracy), PERCENT)
        Right1.spin(FORWARD)
        Right2.spin(FORWARD)
        Right3.spin(FORWARD)
    else:
        left1.set_velocity((drive_forward_true_right__R_L_at_velocity_v__v / Accuracy), PERCENT)
        left2.set_velocity((drive_forward_true_right__R_L_at_velocity_v__v / Accuracy), PERCENT)
        left3.set_velocity((drive_forward_true_right__R_L_at_velocity_v__v / Accuracy), PERCENT)
        left1.spin(FORWARD)
        left2.spin(FORWARD)
        left3.spin(FORWARD)

def raw__spin_right_for_d_degrees_f_r_f_b(raw__spin_right_for_d_degrees_f_r_f_b__d, raw__spin_right_for_d_degrees_f_r_f_b__f_b):
    global my_event, fake_auto, sd_is_in, Accuracy, Front_Down, right_temp, left_temp, Descoring, turn_mod, DegreesToTurn, TurnData, driveMod, auto_side, Auto_color, leftData, RightData, IntakeData, iteration, LeftDriveData, RightDriveData, IntakeDriveData, Left_Iter, Right_Iter, Intake_Iter, textReadout, LeftVP, RightVP, BreakParsing, AuBP_MaxVP, colortoggle, skillsRun, recording, MatchLoadData, TopMotorDATA, TopMotorDriveDATA, MatchLoadDriveDATA, matchload_iter, top_iter, use_turningInertial, LastFront_down, turn_to_h_dif, Kp, Ki, Kd, error, loop_delay, last_error, integral, position, integral_limit, error_threshhold, derivative, POWER, intake_speed, screen_precision, console_precision, ai_vision_2_index, ai_vision_2_objects, controller_1_precision
    if raw__spin_right_for_d_degrees_f_r_f_b__f_b == "f" or raw__spin_right_for_d_degrees_f_r_f_b__f_b == "F":
        Right1.spin_for(FORWARD, raw__spin_right_for_d_degrees_f_r_f_b__d, DEGREES, wait=False)
        Right2.spin_for(FORWARD, raw__spin_right_for_d_degrees_f_r_f_b__d, DEGREES, wait=False)
        Right3.spin_for(FORWARD, raw__spin_right_for_d_degrees_f_r_f_b__d, DEGREES, wait=False)
    else:
        if raw__spin_right_for_d_degrees_f_r_f_b__f_b == "r" or raw__spin_right_for_d_degrees_f_r_f_b__f_b == "R":
            Right1.spin_for(REVERSE, raw__spin_right_for_d_degrees_f_r_f_b__d, DEGREES, wait=False)
            Right2.spin_for(REVERSE, raw__spin_right_for_d_degrees_f_r_f_b__d, DEGREES, wait=False)
            Right3.spin_for(REVERSE, raw__spin_right_for_d_degrees_f_r_f_b__d, DEGREES, wait=False)
        else:
            pass

def drive_reverse_true_right__R_l_at_velocity_v(drive_reverse_true_right__R_l_at_velocity_v__R_l, drive_reverse_true_right__R_l_at_velocity_v__v):
    global my_event, fake_auto, sd_is_in, Accuracy, Front_Down, right_temp, left_temp, Descoring, turn_mod, DegreesToTurn, TurnData, driveMod, auto_side, Auto_color, leftData, RightData, IntakeData, iteration, LeftDriveData, RightDriveData, IntakeDriveData, Left_Iter, Right_Iter, Intake_Iter, textReadout, LeftVP, RightVP, BreakParsing, AuBP_MaxVP, colortoggle, skillsRun, recording, MatchLoadData, TopMotorDATA, TopMotorDriveDATA, MatchLoadDriveDATA, matchload_iter, top_iter, use_turningInertial, LastFront_down, turn_to_h_dif, Kp, Ki, Kd, error, loop_delay, last_error, integral, position, integral_limit, error_threshhold, derivative, POWER, intake_speed, screen_precision, console_precision, ai_vision_2_index, ai_vision_2_objects, controller_1_precision
    if drive_reverse_true_right__R_l_at_velocity_v__R_l:
        Right1.set_velocity((drive_reverse_true_right__R_l_at_velocity_v__v / Accuracy), PERCENT)
        Right2.set_velocity((drive_reverse_true_right__R_l_at_velocity_v__v / Accuracy), PERCENT)
        Right3.set_velocity((drive_reverse_true_right__R_l_at_velocity_v__v / Accuracy), PERCENT)
        Right1.spin(REVERSE)
        Right2.spin(REVERSE)
        Right3.spin(REVERSE)
    else:
        left1.set_velocity((drive_reverse_true_right__R_l_at_velocity_v__v / Accuracy), PERCENT)
        left2.set_velocity((drive_reverse_true_right__R_l_at_velocity_v__v / Accuracy), PERCENT)
        left3.set_velocity((drive_reverse_true_right__R_l_at_velocity_v__v / Accuracy), PERCENT)
        left1.spin(REVERSE)
        left2.spin(REVERSE)
        left3.spin(REVERSE)

def raw__spin_left_degrees_degrees_f_r_f_r(raw__spin_left_degrees_degrees_f_r_f_r__degrees, raw__spin_left_degrees_degrees_f_r_f_r__f_r):
    global my_event, fake_auto, sd_is_in, Accuracy, Front_Down, right_temp, left_temp, Descoring, turn_mod, DegreesToTurn, TurnData, driveMod, auto_side, Auto_color, leftData, RightData, IntakeData, iteration, LeftDriveData, RightDriveData, IntakeDriveData, Left_Iter, Right_Iter, Intake_Iter, textReadout, LeftVP, RightVP, BreakParsing, AuBP_MaxVP, colortoggle, skillsRun, recording, MatchLoadData, TopMotorDATA, TopMotorDriveDATA, MatchLoadDriveDATA, matchload_iter, top_iter, use_turningInertial, LastFront_down, turn_to_h_dif, Kp, Ki, Kd, error, loop_delay, last_error, integral, position, integral_limit, error_threshhold, derivative, POWER, intake_speed, screen_precision, console_precision, ai_vision_2_index, ai_vision_2_objects, controller_1_precision
    if raw__spin_left_degrees_degrees_f_r_f_r__f_r == "f" or raw__spin_left_degrees_degrees_f_r_f_r__f_r == "F":
        left1.spin_for(FORWARD, raw__spin_left_degrees_degrees_f_r_f_r__degrees, DEGREES, wait=False)
        left2.spin_for(FORWARD, raw__spin_left_degrees_degrees_f_r_f_r__degrees, DEGREES, wait=False)
        left3.spin_for(FORWARD, raw__spin_left_degrees_degrees_f_r_f_r__degrees, DEGREES, wait=False)
    else:
        if raw__spin_left_degrees_degrees_f_r_f_r__f_r == "r" or raw__spin_left_degrees_degrees_f_r_f_r__f_r == "R":
            left1.spin_for(REVERSE, raw__spin_left_degrees_degrees_f_r_f_r__degrees, DEGREES, wait=False)
            left2.spin_for(REVERSE, raw__spin_left_degrees_degrees_f_r_f_r__degrees, DEGREES, wait=False)
            left3.spin_for(REVERSE, raw__spin_left_degrees_degrees_f_r_f_r__degrees, DEGREES, wait=False)
        else:
            pass

def Record_Auto():
    global my_event, fake_auto, sd_is_in, Accuracy, Front_Down, right_temp, left_temp, Descoring, turn_mod, DegreesToTurn, TurnData, driveMod, auto_side, Auto_color, leftData, RightData, IntakeData, iteration, LeftDriveData, RightDriveData, IntakeDriveData, Left_Iter, Right_Iter, Intake_Iter, textReadout, LeftVP, RightVP, BreakParsing, AuBP_MaxVP, colortoggle, skillsRun, recording, MatchLoadData, TopMotorDATA, TopMotorDriveDATA, MatchLoadDriveDATA, matchload_iter, top_iter, use_turningInertial, LastFront_down, turn_to_h_dif, Kp, Ki, Kd, error, loop_delay, last_error, integral, position, integral_limit, error_threshhold, derivative, POWER, intake_speed, screen_precision, console_precision, ai_vision_2_index, ai_vision_2_objects, controller_1_precision
    controller_1.rumble("....")
    leftData = 0
    RightData = 0
    MatchLoadData = 0
    TopMotorDATA = 0
    IntakeDriveData = ""
    MatchLoadDriveDATA = ""
    TopMotorDriveDATA = ""
    LeftDriveData = ""
    RightDriveData = ""
    AuBP_MaxVP = 60
    controller_1.screen.print("press A")
    while not controller_1.buttonA.pressing():
        wait(5, MSEC)
    while not not controller_1.buttonA.pressing():
        wait(5, MSEC)
    controller_1.screen.clear_row(3)
    controller_1.screen.set_cursor(controller_1.screen.row(), 1)
    while True:
        textReadout = "///Paused\\\\\\"
        while not controller_1.buttonA.pressing():
            wait(5, MSEC)
        while not not controller_1.buttonA.pressing():
            wait(5, MSEC)
        while not controller_1.buttonA.pressing():
            textReadout = str(str("Max Velocity: ") + str(str(AuBP_MaxVP))) + str(str(" & ") + str(str("Speed: ") + str(str(str(((68.95 * 3.14) * (450 * (AuBP_MaxVP / 100))) / 60)) + str(" MM/S"))))
            if controller_1.buttonUp.pressing():
                AuBP_MaxVP = AuBP_MaxVP + 5
                if AuBP_MaxVP > 100:
                    AuBP_MaxVP = 100
                if AuBP_MaxVP < 10:
                    AuBP_MaxVP = 5
                while not not controller_1.buttonUp.pressing():
                    wait(5, MSEC)
            if controller_1.buttonRight.pressing():
                AuBP_MaxVP = AuBP_MaxVP + -5
                if AuBP_MaxVP < 1:
                    AuBP_MaxVP = 1
                while not not controller_1.buttonRight.pressing():
                    wait(5, MSEC)
            wait(5, MSEC)
        if controller_1.buttonLeft.pressing():
            break
        while not not controller_1.buttonA.pressing():
            wait(5, MSEC)
        textReadout = "Recording..."
        IntakeData = 0
        MatchLoadData = 0
        TopMotorDATA = 0
        Right1.set_position(0, DEGREES)
        left1.set_position(0, DEGREES)
        inertial_for_auton.set_rotation(0, DEGREES)
        print("\033[31m")
        print("RECORDING...")
        TopMotor.set_position(0, DEGREES)
        Intake.set_position(0, DEGREES)
        while not controller_1.buttonA.pressing():
            wait(5, MSEC)
        if math.fabs(Intake.position(DEGREES)) > 0:
            IntakeData = 1
        MatchLoadData = Front_Down
        if math.fabs(TopMotor.position(DEGREES)) > 0:
            TopMotorDATA = 1
        print("intake data")
        print(console_format(IntakeData))
        print(console_format(left1.position(DEGREES)))
        print(console_format(Right1.position(DEGREES)))
        if left1.position(DEGREES) > 0 and Right1.position(DEGREES) < 0 or left1.position(DEGREES) < 0 and Right1.position(DEGREES) > 0:
            IntakeDriveData = str(IntakeDriveData) + str(str("{") + str(str(inertial_for_auton.rotation(DEGREES)) + str("}")))
        else:
            if IntakeData == 1:
                IntakeDriveData = str(IntakeDriveData) + str("1!")
            else:
                IntakeDriveData = str(IntakeDriveData) + str("0!")
            if MatchLoadData == 1:
                MatchLoadDriveDATA = str(MatchLoadDriveDATA) + str("1!")
            else:
                MatchLoadDriveDATA = str(MatchLoadDriveDATA) + str("0!")
            if TopMotorDATA == 1:
                TopMotorDriveDATA = str(TopMotorDriveDATA) + str("1!")
            else:
                TopMotorDriveDATA = str(TopMotorDriveDATA) + str("0!")
            textReadout = "drive compensate"
            if math.fabs(left1.position(DEGREES)) < 1 and math.fabs(Right1.position(DEGREES)) < 1:
                leftData = 1
                RightData = 1
            else:
                if math.fabs(left1.position(DEGREES)) > math.fabs(Right1.position(DEGREES)):
                    leftData = AuBP_MaxVP
                    RightData = AuBP_MaxVP / (left1.position(DEGREES) / (Right1.position(DEGREES) + 1))
                else:
                    RightData = AuBP_MaxVP
                    leftData = AuBP_MaxVP / (Right1.position(DEGREES) / (left1.position(DEGREES) + 1))
            LeftDriveData = str(str(LeftDriveData) + str(str(str(leftData)) + str(":"))) + str(str(str(left1.position(DEGREES))) + str("!"))
            RightDriveData = str(str(RightDriveData) + str(str(str(RightData)) + str(":"))) + str(str(str(Right1.position(DEGREES))) + str("!"))
        wait(5, MSEC)
    print("\033[2J")
    LeftDriveData = str(str(LeftDriveData) + str("0:0!")) + str("/")
    RightDriveData = str(str(RightDriveData) + str("0:0!")) + str("/")
    TopMotorDriveDATA = str(str(TopMotorDriveDATA) + str("0!")) + str("/")
    MatchLoadDriveDATA = str(str(MatchLoadDriveDATA) + str("0!")) + str("/")
    IntakeDriveData = str(str(IntakeDriveData) + str("0!")) + str("#")
    controller_1.rumble("-.-.")
    controller_1.screen.print("Press A to retrieve data")
    while not not controller_1.buttonA.pressing():
        wait(5, MSEC)
    while not controller_1.buttonA.pressing():
        wait(5, MSEC)
    controller_1.screen.clear_row(3)
    controller_1.screen.set_cursor(controller_1.screen.row(), 1)
    textReadout = "Check the console for data"
    print("\033[30m")
    # fix
    print(str(LeftDriveData) + str(str(RightDriveData) + str(str(TopMotorDriveDATA) + str(str(MatchLoadDriveDATA) + str(IntakeDriveData)))))
    print("Copy this value and paste it into the read auto block")

def Set_Drivetrain_Velocity_to__25(Set_Drivetrain_Velocity_to__25___25):
    global my_event, fake_auto, sd_is_in, Accuracy, Front_Down, right_temp, left_temp, Descoring, turn_mod, DegreesToTurn, TurnData, driveMod, auto_side, Auto_color, leftData, RightData, IntakeData, iteration, LeftDriveData, RightDriveData, IntakeDriveData, Left_Iter, Right_Iter, Intake_Iter, textReadout, LeftVP, RightVP, BreakParsing, AuBP_MaxVP, colortoggle, skillsRun, recording, MatchLoadData, TopMotorDATA, TopMotorDriveDATA, MatchLoadDriveDATA, matchload_iter, top_iter, use_turningInertial, LastFront_down, turn_to_h_dif, Kp, Ki, Kd, error, loop_delay, last_error, integral, position, integral_limit, error_threshhold, derivative, POWER, intake_speed, screen_precision, console_precision, ai_vision_2_index, ai_vision_2_objects, controller_1_precision
    set_Left_drive_velocity_to_velocity(Set_Drivetrain_Velocity_to__25___25)
    Set_Right_Drive_Velocity_To_v(Set_Drivetrain_Velocity_to__25___25)

def set_Left_drive_velocity_to_velocity(set_Left_drive_velocity_to_velocity__velocity):
    global my_event, fake_auto, sd_is_in, Accuracy, Front_Down, right_temp, left_temp, Descoring, turn_mod, DegreesToTurn, TurnData, driveMod, auto_side, Auto_color, leftData, RightData, IntakeData, iteration, LeftDriveData, RightDriveData, IntakeDriveData, Left_Iter, Right_Iter, Intake_Iter, textReadout, LeftVP, RightVP, BreakParsing, AuBP_MaxVP, colortoggle, skillsRun, recording, MatchLoadData, TopMotorDATA, TopMotorDriveDATA, MatchLoadDriveDATA, matchload_iter, top_iter, use_turningInertial, LastFront_down, turn_to_h_dif, Kp, Ki, Kd, error, loop_delay, last_error, integral, position, integral_limit, error_threshhold, derivative, POWER, intake_speed, screen_precision, console_precision, ai_vision_2_index, ai_vision_2_objects, controller_1_precision
    left1.set_velocity(set_Left_drive_velocity_to_velocity__velocity, PERCENT)
    left2.set_velocity(set_Left_drive_velocity_to_velocity__velocity, PERCENT)
    left3.set_velocity(set_Left_drive_velocity_to_velocity__velocity, PERCENT)

def get_next_value_for_drive():
    global my_event, fake_auto, sd_is_in, Accuracy, Front_Down, right_temp, left_temp, Descoring, turn_mod, DegreesToTurn, TurnData, driveMod, auto_side, Auto_color, leftData, RightData, IntakeData, iteration, LeftDriveData, RightDriveData, IntakeDriveData, Left_Iter, Right_Iter, Intake_Iter, textReadout, LeftVP, RightVP, BreakParsing, AuBP_MaxVP, colortoggle, skillsRun, recording, MatchLoadData, TopMotorDATA, TopMotorDriveDATA, MatchLoadDriveDATA, matchload_iter, top_iter, use_turningInertial, LastFront_down, turn_to_h_dif, Kp, Ki, Kd, error, loop_delay, last_error, integral, position, integral_limit, error_threshhold, derivative, POWER, intake_speed, screen_precision, console_precision, ai_vision_2_index, ai_vision_2_objects, controller_1_precision
    IntakeDriveData = ""
    LeftDriveData = ""
    RightDriveData = ""
    TopMotorDriveDATA = ""
    MatchLoadDriveDATA = ""
    LeftVP = ""
    RightVP = ""
    use_turningInertial = 0
    while not (IntakeData[Intake_Iter - 1]) == "!":
        textReadout = str("finding intake data...") + str(Intake_Iter)
        print("\033[91m")
        print(str("finding intake data...") + str(Intake_Iter))
        if (IntakeData[Intake_Iter - 1]) == "#":
            print("limit reached! Commencing breaking...")
            Intake_Iter = Intake_Iter + -1
            BreakParsing = 1
            break
        if (IntakeData[Intake_Iter - 1]) == "{":
            Intake_Iter = Intake_Iter + 1
            while not (IntakeData[Intake_Iter - 1]) == "}":
                IntakeDriveData = str(IntakeDriveData) + str(IntakeData[Intake_Iter - 1])
                Intake_Iter = Intake_Iter + 1
                wait(5, MSEC)
            Intake_Iter = Intake_Iter + 1
            use_turningInertial = 1
            break
        IntakeDriveData = str(IntakeDriveData) + str(IntakeData[Intake_Iter - 1])
        Intake_Iter = Intake_Iter + 1
        wait(5, MSEC)
    if use_turningInertial == 0:
        Intake_Iter = Intake_Iter + 1
        while not (leftData[Left_Iter - 1]) == ":":
            textReadout = str("finding left vp...") + str(Left_Iter)
            print("\033[32m")
            print(str("finding left vp...") + str(Left_Iter))
            if BreakParsing == 1:
                print("Breaking left...")
                break
            LeftVP = str(LeftVP) + str(leftData[Left_Iter - 1])
            Left_Iter = Left_Iter + 1
            wait(5, MSEC)
        Left_Iter = Left_Iter + 1
        while not (leftData[Left_Iter - 1]) == "!":
            textReadout = str("finding left dist...") + str(Left_Iter)
            print("\033[31m")
            print(str("finding left dist...") + str(Left_Iter))
            if BreakParsing == 1:
                print("Breaking left...")
                break
            LeftDriveData = str(LeftDriveData) + str(leftData[Left_Iter - 1])
            Left_Iter = Left_Iter + 1
            wait(5, MSEC)
        Left_Iter = Left_Iter + 1
        while not (RightData[Right_Iter - 1]) == ":":
            textReadout = str("finding right vp...") + str(Right_Iter)
            print("\033[34m")
            print(str("finding right vp...") + str(Right_Iter))
            if BreakParsing == 1:
                print("Breaking right...")
                break
            RightVP = str(RightVP) + str(RightData[Right_Iter - 1])
            Right_Iter = Right_Iter + 1
            wait(5, MSEC)
        Right_Iter = Right_Iter + 1
        while not (RightData[Right_Iter - 1]) == "!":
            textReadout = str("finding right dist...") + str(Right_Iter)
            print("\033[36m")
            print(str("finding right dist...") + str(Right_Iter))
            if BreakParsing == 1:
                print("Breaking right...")
                break
            RightDriveData = str(RightDriveData) + str(RightData[Right_Iter - 1])
            Right_Iter = Right_Iter + 1
            wait(5, MSEC)
        Right_Iter = Right_Iter + 1
        print(str("finding scoring data...") + str(top_iter))
        while not (TopMotorDATA[top_iter - 1]) == "!":
            textReadout = str("finding scoring data...") + str(top_iter)
            print("\033[91m")
            print(str("finding scoring data...") + str(top_iter))
            if BreakParsing == 1:
                print("Breaking scoring...")
                break
            TopMotorDriveDATA = str(TopMotorDriveDATA) + str(TopMotorDATA[top_iter - 1])
            top_iter = top_iter + 1
            wait(5, MSEC)
        top_iter = top_iter + 1
        while not (MatchLoadData[matchload_iter - 1]) == "!":
            textReadout = str("finding matchload data...") + str(matchload_iter)
            print("\033[91m")
            print(str("finding matchload data...") + str(matchload_iter))
            if BreakParsing == 1:
                print("Breaking matchload...")
                break
            MatchLoadDriveDATA = str(MatchLoadDriveDATA) + str(MatchLoadData[matchload_iter - 1])
            matchload_iter = matchload_iter + 1
            wait(5, MSEC)
        matchload_iter = matchload_iter + 1

def Read_Auto_String__auto_code(Read_Auto_String__auto_code__auto_code):
    global my_event, fake_auto, sd_is_in, Accuracy, Front_Down, right_temp, left_temp, Descoring, turn_mod, DegreesToTurn, TurnData, driveMod, auto_side, Auto_color, leftData, RightData, IntakeData, iteration, LeftDriveData, RightDriveData, IntakeDriveData, Left_Iter, Right_Iter, Intake_Iter, textReadout, LeftVP, RightVP, BreakParsing, AuBP_MaxVP, colortoggle, skillsRun, recording, MatchLoadData, TopMotorDATA, TopMotorDriveDATA, MatchLoadDriveDATA, matchload_iter, top_iter, use_turningInertial, LastFront_down, turn_to_h_dif, Kp, Ki, Kd, error, loop_delay, last_error, integral, position, integral_limit, error_threshhold, derivative, POWER, intake_speed, screen_precision, console_precision, ai_vision_2_index, ai_vision_2_objects, controller_1_precision
    BreakParsing = 0
    leftData = ""
    RightData = ""
    IntakeData = ""
    Right_Iter = 1
    Left_Iter = 1
    iteration = 1
    while not (Read_Auto_String__auto_code__auto_code[iteration - 1]) == "/":
        leftData = str(leftData) + str(Read_Auto_String__auto_code__auto_code[iteration - 1])
        iteration = iteration + 1
        wait(5, MSEC)
    iteration = iteration + 1
    while not (Read_Auto_String__auto_code__auto_code[iteration - 1]) == "/":
        RightData = str(RightData) + str(Read_Auto_String__auto_code__auto_code[iteration - 1])
        iteration = iteration + 1
        wait(5, MSEC)
    iteration = iteration + 1
    while not (Read_Auto_String__auto_code__auto_code[iteration - 1]) == "/":
        TopMotorDATA = str(TopMotorDATA) + str(Read_Auto_String__auto_code__auto_code[iteration - 1])
        iteration = iteration + 1
        wait(5, MSEC)
    iteration = iteration + 1
    while not (Read_Auto_String__auto_code__auto_code[iteration - 1]) == "/":
        MatchLoadData = str(MatchLoadData) + str(Read_Auto_String__auto_code__auto_code[iteration - 1])
        iteration = iteration + 1
        wait(5, MSEC)
    iteration = iteration + 1
    while not (Read_Auto_String__auto_code__auto_code[iteration - 1]) == "#":
        IntakeData = str(IntakeData) + str(Read_Auto_String__auto_code__auto_code[iteration - 1])
        iteration = iteration + 1
        wait(5, MSEC)
    IntakeData = str(IntakeData) + str(Read_Auto_String__auto_code__auto_code[iteration - 1])
    iteration = iteration + 1
    controller_1.rumble("....")
    controller_1.screen.print("Press a to view data")
    print("\033[30m")
    print(str("Left Data: ") + str(leftData))
    print(str("Right Data: ") + str(RightData))
    print(str("intake Data: ") + str(IntakeData))
    print(str("Match Load data: ") + str(MatchLoadData))
    print(str("scoring Data: ") + str(TopMotorDATA))
    if not ("!" in IntakeData):
        print("\033[31m")
        print("ERROR ON INTAKE; NO DELINEATOR:STOPPING")
        while not ("!" in IntakeData):
            wait(5, MSEC)
    controller_1.rumble("....")
    controller_1.screen.clear_row(3)
    controller_1.screen.set_cursor(controller_1.screen.row(), 1)
    controller_1.screen.print("X to confirm")
    controller_1.screen.clear_row(3)
    controller_1.screen.set_cursor(controller_1.screen.row(), 1)
    Intake_Iter = 1
    Right_Iter = 1
    Left_Iter = 1
    top_iter = 1
    matchload_iter = 1
    while True:
        get_next_value_for_drive()
        print("\033[30m")
        if use_turningInertial == 1:
            print(console_format(IntakeDriveData))
            Turn_target_Degrees_With_Inertial_Helping(float(IntakeDriveData))
            use_turningInertial = 0
        else:
            print(console_format(IntakeDriveData))
            if (float(IntakeDriveData)) == 1:
                Intake.spin(FORWARD)
            else:
                Intake.stop()
            print(console_format(TopMotorDriveDATA))
            if (float(TopMotorDriveDATA)) == 1:
                TopMotor.spin(REVERSE)
            else:
                TopMotor.stop()
            print(console_format(MatchLoadDriveDATA))
            if (float(MatchLoadDriveDATA)) == 1:
                Front_Down = 1
            else:
                Front_Down = 0
            print(console_format(LeftVP))
            set_Left_drive_velocity_to_velocity(float(LeftVP))
            print(console_format(RightVP))
            Set_Right_Drive_Velocity_To_v(float(RightVP))
            print(console_format(LeftDriveData))
            raw__spin_left_degrees_degrees_f_r_f_r(float(LeftDriveData), "f")
            print(console_format(RightDriveData))
            raw__spin_right_for_d_degrees_f_r_f_b(float(RightDriveData), "f")
        while not (not left1.is_spinning() and not Right1.is_spinning()):
            wait(5, MSEC)
        while not (inertial_for_auton.orientation(PITCH, DEGREES) > -5 and inertial_for_auton.orientation(PITCH, DEGREES) < 5 and inertial_for_auton.orientation(ROLL, DEGREES) > -5 and inertial_for_auton.orientation(ROLL, DEGREES) < 5):
            wait(5, MSEC)
        if (IntakeData[Intake_Iter - 1]) == "b" or (IntakeData[Intake_Iter - 1]) == "#":
            break
        if BreakParsing == 1:
            break
        wait(5, MSEC)
    textReadout = "done!"
    print("Done!")
    print("Done!")

def Set_Right_Drive_Velocity_To_v(Set_Right_Drive_Velocity_To_v__v):
    global my_event, fake_auto, sd_is_in, Accuracy, Front_Down, right_temp, left_temp, Descoring, turn_mod, DegreesToTurn, TurnData, driveMod, auto_side, Auto_color, leftData, RightData, IntakeData, iteration, LeftDriveData, RightDriveData, IntakeDriveData, Left_Iter, Right_Iter, Intake_Iter, textReadout, LeftVP, RightVP, BreakParsing, AuBP_MaxVP, colortoggle, skillsRun, recording, MatchLoadData, TopMotorDATA, TopMotorDriveDATA, MatchLoadDriveDATA, matchload_iter, top_iter, use_turningInertial, LastFront_down, turn_to_h_dif, Kp, Ki, Kd, error, loop_delay, last_error, integral, position, integral_limit, error_threshhold, derivative, POWER, intake_speed, screen_precision, console_precision, ai_vision_2_index, ai_vision_2_objects, controller_1_precision
    Right1.set_velocity(Set_Right_Drive_Velocity_To_v__v, PERCENT)
    Right2.set_velocity(Set_Right_Drive_Velocity_To_v__v, PERCENT)
    Right3.set_velocity(Set_Right_Drive_Velocity_To_v__v, PERCENT)

def when_started1():
    global my_event, fake_auto, sd_is_in, Accuracy, Front_Down, right_temp, left_temp, Descoring, turn_mod, DegreesToTurn, TurnData, driveMod, auto_side, Auto_color, leftData, RightData, IntakeData, iteration, LeftDriveData, RightDriveData, IntakeDriveData, Left_Iter, Right_Iter, Intake_Iter, textReadout, LeftVP, RightVP, BreakParsing, AuBP_MaxVP, colortoggle, skillsRun, recording, MatchLoadData, TopMotorDATA, TopMotorDriveDATA, MatchLoadDriveDATA, matchload_iter, top_iter, use_turningInertial, LastFront_down, turn_to_h_dif, Kp, Ki, Kd, error, loop_delay, last_error, integral, position, integral_limit, error_threshhold, derivative, POWER, intake_speed, screen_precision, console_precision, ai_vision_2_index, ai_vision_2_objects, controller_1_precision
    # DO NOT INTERMIX PID TURN & [TURN FOR__] OR [TURN TO HEADING__]
    controller_1.rumble("----")
    controller_1.screen.print("Don't forget to setup!")
    inertial_for_auton.calibrate()
    while inertial_for_auton.is_calibrating():
        sleep(50)
    while not (not Auto_color == "bl" and not auto_side == "bl"):
        wait(5, MSEC)
    controller_1.screen.clear_row(3)
    controller_1.screen.set_cursor(controller_1.screen.row(), 1)
    if auto_side == "m":
        if IntakeData == 0:
            recording = 1
            Record_Auto()
        else:
            pass
    else:
        pass

def onauton_autonomous_0():
    global my_event, fake_auto, sd_is_in, Accuracy, Front_Down, right_temp, left_temp, Descoring, turn_mod, DegreesToTurn, TurnData, driveMod, auto_side, Auto_color, leftData, RightData, IntakeData, iteration, LeftDriveData, RightDriveData, IntakeDriveData, Left_Iter, Right_Iter, Intake_Iter, textReadout, LeftVP, RightVP, BreakParsing, AuBP_MaxVP, colortoggle, skillsRun, recording, MatchLoadData, TopMotorDATA, TopMotorDriveDATA, MatchLoadDriveDATA, matchload_iter, top_iter, use_turningInertial, LastFront_down, turn_to_h_dif, Kp, Ki, Kd, error, loop_delay, last_error, integral, position, integral_limit, error_threshhold, derivative, POWER, intake_speed, screen_precision, console_precision, ai_vision_2_index, ai_vision_2_objects, controller_1_precision
    # Auto
    init_setup()
    turn_mod = 1
    inertial_for_auton.calibrate()
    while inertial_for_auton.is_calibrating():
        sleep(50)
    Intake.set_max_torque(100, PERCENT)
    Intake.set_velocity(100, PERCENT)
    while not (not Auto_color == "bl" and not auto_side == "bl"):
        print(console_format(Auto_color))
        print("VEXcode", end="")
        print(console_format(auto_side))
        wait(5, MSEC)
    if auto_side == "r":
        Set_Drivetrain_Velocity_to__25(60)
        drive_forwards_dist_milimeters(300)
        Turn_target_Degrees_With_Inertial_Helping(20)
        Intake.spin(FORWARD)
        Set_Drivetrain_Velocity_to__25(40)
        drive_forwards_dist_milimeters(800)
        wait(0.5, SECONDS)
        drive_forwards_dist_milimeters(-800)
        Set_Drivetrain_Velocity_to__25(50)
        Turn_To_Heading_heading_input_from_0_359_9(270)
        drive_forwards_dist_milimeters(-834)
        Turn_To_Heading_heading_input_from_0_359_9(180)
        drive_forwards_dist_milimeters(-300)
        Intake.spin(FORWARD)
        TopMotor.spin(REVERSE)
        for repeat_count2 in range(4):
            wait(1, SECONDS)
            TopMotor.spin(FORWARD)
            wait(0.2, SECONDS)
            TopMotor.spin(REVERSE)
            wait(5, MSEC)
    elif auto_side == "l":
        PID_move_mm_mm(200)
        PID_turn_to_head_angle(-90)
    elif auto_side == "n":
        PID_move_mm_mm(50)
    else:
        if IntakeData == 0:
            pass
        else:
            Read_Auto_String__auto_code("60:837.5999!40:1772.4!50:-2119.2!48.88086:-2193.6!47.23186:-980.4!0.9401041:-73.2!1:129.6!0:0!/57.40688:800.4!38.91221:1723.2!47.39997:-2010.0!50:-2242.8!50:-1036.8!1:-76.8!0.9984568:128.4!0:0!/0!1!0!0!0!1!1!0!/0!0!0!0!0!0!0!0!/0!{26.70579}1!0!{-109.1027}0!{-97.49892}0!1!1!0!#")

def when_started2():
    global my_event, fake_auto, sd_is_in, Accuracy, Front_Down, right_temp, left_temp, Descoring, turn_mod, DegreesToTurn, TurnData, driveMod, auto_side, Auto_color, leftData, RightData, IntakeData, iteration, LeftDriveData, RightDriveData, IntakeDriveData, Left_Iter, Right_Iter, Intake_Iter, textReadout, LeftVP, RightVP, BreakParsing, AuBP_MaxVP, colortoggle, skillsRun, recording, MatchLoadData, TopMotorDATA, TopMotorDriveDATA, MatchLoadDriveDATA, matchload_iter, top_iter, use_turningInertial, LastFront_down, turn_to_h_dif, Kp, Ki, Kd, error, loop_delay, last_error, integral, position, integral_limit, error_threshhold, derivative, POWER, intake_speed, screen_precision, console_precision, ai_vision_2_index, ai_vision_2_objects, controller_1_precision
    # readout
    recording = 0
    skillsRun = 0
    Auto_color = "bl"
    auto_side = "bl"
    while True:
        if Auto_color == "r":
            brain.screen.set_fill_color(Color.RED)
        else:
            brain.screen.set_fill_color(Color.WHITE)
        brain.screen.draw_rectangle(50, 25, 100, 50)
        brain.screen.set_pen_color(Color.BLACK)
        brain.screen.set_cursor(3, 9)
        brain.screen.print("RED")
        if Auto_color == "b":
            brain.screen.set_fill_color(Color.BLUE)
        else:
            brain.screen.set_fill_color(Color.WHITE)
        brain.screen.draw_rectangle(150, 25, 100, 50)
        brain.screen.set_pen_color(Color.BLACK)
        brain.screen.set_cursor(3, 20)
        brain.screen.print("BLUE")
        if Auto_color == "n":
            brain.screen.set_fill_color(Color.ORANGE)
        else:
            brain.screen.set_fill_color(Color.WHITE)
        brain.screen.draw_rectangle(250, 25, 100, 50)
        brain.screen.set_pen_color(Color.BLACK)
        brain.screen.set_cursor(3, 25)
        brain.screen.print("No C-Sort")
        if skillsRun == 1:
            brain.screen.set_fill_color(Color.YELLOW)
        else:
            brain.screen.set_fill_color(Color.WHITE)
        brain.screen.draw_rectangle(350, 25, 100, 50)
        brain.screen.set_pen_color(Color.BLACK)
        brain.screen.set_cursor(3, 37)
        brain.screen.print("Skills?")
        if brain.screen.pressing():
            if brain.screen.y_position() > 25 and brain.screen.y_position() < 70:
                if brain.screen.x_position() > 50 and brain.screen.x_position() < 150:
                    Auto_color = "r"
                if brain.screen.x_position() > 155 and brain.screen.x_position() < 250:
                    Auto_color = "b"
                if brain.screen.x_position() > 255 and brain.screen.x_position() < 350:
                    Auto_color = "n"
                if brain.screen.x_position() > 355 and brain.screen.x_position() < 455:
                    if skillsRun == 1:
                        skillsRun = 0
                    else:
                        skillsRun = 1
                    while not not brain.screen.pressing():
                        wait(5, MSEC)
            if brain.screen.y_position() > 95 and brain.screen.y_position() < 140:
                if brain.screen.x_position() > 50 and brain.screen.x_position() < 150:
                    auto_side = "r"
                if brain.screen.x_position() > 155 and brain.screen.x_position() < 250:
                    auto_side = "l"
                if brain.screen.x_position() > 255 and brain.screen.x_position() < 350:
                    auto_side = "n"
                if brain.screen.x_position() > 355 and brain.screen.x_position() < 450:
                    auto_side = "m"
                    IntakeData = 0
        if brain.screen.y_position() > 135 and brain.screen.y_position() < 210:
            if brain.screen.x_position() > 355 and brain.screen.x_position() < 450:
                auto_side = "m"
                IntakeData = 1
        print(console_format(brain.screen.x_position()), end="")
        print(" , ", end="")
        print(console_format(brain.screen.y_position()))
        print("///", end="")
        print(console_format(IntakeData), end="")
        print("///", end="")
        if auto_side == "r":
            brain.screen.set_fill_color(Color.GREEN)
        else:
            brain.screen.set_fill_color(Color.WHITE)
        brain.screen.draw_rectangle(50, 100, 100, 50)
        brain.screen.set_pen_color(Color.BLACK)
        brain.screen.set_cursor(7, 9)
        brain.screen.print("RIGHT")
        if auto_side == "l":
            brain.screen.set_fill_color(Color.GREEN)
        else:
            brain.screen.set_fill_color(Color.WHITE)
        brain.screen.draw_rectangle(150, 100, 100, 50)
        brain.screen.set_pen_color(Color.BLACK)
        brain.screen.set_cursor(7, 20)
        brain.screen.print("LEFT")
        if auto_side == "n":
            brain.screen.set_fill_color(Color.CYAN)
        else:
            brain.screen.set_fill_color(Color.WHITE)
        brain.screen.draw_rectangle(250, 100, 100, 50)
        brain.screen.set_pen_color(Color.BLACK)
        brain.screen.set_cursor(7, 28)
        brain.screen.print("NoSolo")
        if auto_side == "m" and IntakeData == 0:
            brain.screen.set_fill_color(Color.RED)
        else:
            brain.screen.set_fill_color(Color.WHITE)
        brain.screen.draw_rectangle(350, 100, 100, 50)
        brain.screen.set_pen_color(Color.BLACK)
        brain.screen.set_cursor(6, 36)
        brain.screen.print("AuBP")
        brain.screen.set_cursor(7, 36)
        brain.screen.print("RECORD")
        if auto_side == "m" and IntakeData == 1:
            brain.screen.set_fill_color(Color.PURPLE)
        else:
            brain.screen.set_fill_color(Color.WHITE)
        brain.screen.draw_rectangle(350, 150, 100, 50)
        brain.screen.set_pen_color(Color.BLACK)
        brain.screen.set_cursor(9, 36)
        brain.screen.print("AuBP")
        brain.screen.set_cursor(10, 36)
        brain.screen.print("RUN")
        if not Auto_color == "bl" and not auto_side == "bl":
            break
        wait(5, MSEC)
    brain.screen.clear_screen()
    if Auto_color == "r":
        brain.screen.set_fill_color(Color.RED)
    else:
        brain.screen.set_fill_color(Color.WHITE)
    brain.screen.draw_rectangle(50, 25, 100, 50)
    brain.screen.set_pen_color(Color.BLACK)
    brain.screen.set_cursor(3, 9)
    brain.screen.print("RED")
    if Auto_color == "b":
        brain.screen.set_fill_color(Color.BLUE)
    else:
        brain.screen.set_fill_color(Color.WHITE)
    brain.screen.draw_rectangle(150, 25, 100, 50)
    brain.screen.set_pen_color(Color.BLACK)
    brain.screen.set_cursor(3, 20)
    brain.screen.print("BLUE")
    if Auto_color == "n":
        brain.screen.set_fill_color(Color.ORANGE)
    else:
        brain.screen.set_fill_color(Color.WHITE)
    brain.screen.draw_rectangle(250, 25, 100, 50)
    brain.screen.set_pen_color(Color.BLACK)
    brain.screen.set_cursor(3, 25)
    brain.screen.print("No C-Sort")
    if auto_side == "r":
        brain.screen.set_fill_color(Color.GREEN)
    else:
        brain.screen.set_fill_color(Color.WHITE)
    brain.screen.draw_rectangle(50, 100, 100, 50)
    brain.screen.set_pen_color(Color.BLACK)
    brain.screen.set_cursor(7, 9)
    brain.screen.print("RIGHT")
    if auto_side == "l":
        brain.screen.set_fill_color(Color.GREEN)
    else:
        brain.screen.set_fill_color(Color.WHITE)
    brain.screen.draw_rectangle(150, 100, 100, 50)
    brain.screen.set_pen_color(Color.BLACK)
    brain.screen.set_cursor(7, 20)
    brain.screen.print("LEFT")
    if auto_side == "n":
        brain.screen.set_fill_color(Color.CYAN)
    else:
        brain.screen.set_fill_color(Color.WHITE)
    brain.screen.draw_rectangle(250, 100, 100, 50)
    brain.screen.set_pen_color(Color.BLACK)
    brain.screen.set_cursor(7, 26)
    brain.screen.print("NoSolo")
    if auto_side == "m":
        brain.screen.set_fill_color(Color.PURPLE)
    else:
        brain.screen.set_fill_color(Color.WHITE)
    brain.screen.draw_rectangle(350, 100, 100, 50)
    brain.screen.set_pen_color(Color.BLACK)
    brain.screen.set_cursor(6, 36)
    brain.screen.print("AuBP")
    brain.screen.set_cursor(7, 36)
    if IntakeData == 0:
        brain.screen.print("RECORD")
    else:
        brain.screen.print("RUN")
    wait(1.2, SECONDS)
    print("\033[2J")
    brain.screen.clear_screen()
    brain.screen.set_fill_color(Color.TRANSPARENT)
    brain.screen.set_font(FontType.MONO15)
    brain.screen.set_pen_color(Color.GREEN)
    screen_precision = 2
    while True:
        brain.screen.clear_screen()
        brain.screen.set_cursor(1, 1)
        brain.screen.print("Program: ")
        brain.screen.next_row()
        brain.screen.set_cursor(1, 28)
        brain.screen.set_pen_color(Color.YELLOW)
        if brain.battery.capacity() < 40:
            brain.screen.set_fill_color(Color.RED)
        brain.screen.print(str("Battery status: Level: ") + str(str(str(brain.battery.capacity())) + str(" percent")))
        brain.screen.next_row()
        brain.screen.set_pen_color(Color.GREEN)
        brain.screen.set_fill_color(Color.TRANSPARENT)
        if auto_side == "l":
            brain.screen.print("Left ")
        elif auto_side == "r":
            brain.screen.print("Right ")
        elif auto_side == "m":
            brain.screen.set_pen_color(Color.RED)
            brain.screen.print("AuBP ")
        else:
            brain.screen.set_pen_color(Color.CYAN)
            brain.screen.print("One Inch ")
        brain.screen.set_cursor(2, 28)
        brain.screen.set_pen_color(Color.YELLOW)
        brain.screen.print(str("current: ") + str(str(str(brain.battery.current(CurrentUnits.AMP))) + str(str(" amps & voltage: ") + str(str(brain.battery.voltage(VoltageUnits.VOLT)) + str(" volts")))))
        brain.screen.next_row()
        if Auto_color == "r":
            brain.screen.set_pen_color(Color.RED)
            brain.screen.print("Red ")
            brain.screen.next_row()
        elif Auto_color == "b":
            brain.screen.set_pen_color(Color.BLUE)
            brain.screen.print("Blue ")
            brain.screen.next_row()
        else:
            brain.screen.set_pen_color(Color.ORANGE)
            brain.screen.print("No Color Sorting")
            brain.screen.next_row()
        brain.screen.next_row()
        brain.screen.set_pen_color(Color.GREEN)
        brain.screen.print("port    Name    temp power torque effeciency")
        brain.screen.next_row()
        if Right1.temperature(PERCENT) > 2:
            if Right1.temperature(PERCENT) > 70:
                brain.screen.set_fill_color(Color.RED)
            brain.screen.print(str("P11     Right1: ") + str(str(Right1.temperature(PERCENT))))
            brain.screen.print(" ")
            brain.screen.print(Right1.power(PowerUnits.WATT), precision=screen_precision)
            brain.screen.print(" ")
            brain.screen.print(Right1.torque(TorqueUnits.NM), precision=screen_precision)
            brain.screen.print(" ")
            brain.screen.print(Right1.efficiency(PERCENT), precision=screen_precision)
            brain.screen.next_row()
            brain.screen.set_fill_color(Color.TRANSPARENT)
        if Right2.temperature(PERCENT) > 2:
            if Right2.temperature(PERCENT) > 70:
                brain.screen.set_fill_color(Color.RED)
            brain.screen.print(str("P13     Right2: ") + str(str(Right2.temperature(PERCENT))))
            brain.screen.print(" ")
            brain.screen.print(Right2.power(PowerUnits.WATT), precision=screen_precision)
            brain.screen.print(" ")
            brain.screen.print(Right2.torque(TorqueUnits.NM), precision=screen_precision)
            brain.screen.print(" ")
            brain.screen.print(Right2.efficiency(PERCENT), precision=screen_precision)
            brain.screen.next_row()
            brain.screen.set_fill_color(Color.TRANSPARENT)
        if Right3.temperature(PERCENT) > 2:
            if Right3.temperature(PERCENT) > 70:
                brain.screen.set_fill_color(Color.RED)
            brain.screen.print(str("P12     Right3: ") + str(str(Right3.temperature(PERCENT))))
            brain.screen.print(" ")
            brain.screen.print(Right3.power(PowerUnits.WATT), precision=screen_precision)
            brain.screen.print(" ")
            brain.screen.print(Right3.torque(TorqueUnits.NM), precision=screen_precision)
            brain.screen.print(" ")
            brain.screen.print(Right3.efficiency(PERCENT), precision=screen_precision)
            brain.screen.next_row()
            brain.screen.set_fill_color(Color.TRANSPARENT)
        if left1.temperature(PERCENT) > 2:
            if left1.temperature(PERCENT) > 70:
                brain.screen.set_fill_color(Color.RED)
            brain.screen.print(str("P20      Left1: ") + str(str(left1.temperature(PERCENT))))
            brain.screen.print(" ")
            brain.screen.print(left1.power(PowerUnits.WATT), precision=screen_precision)
            brain.screen.print(" ")
            brain.screen.print(left1.torque(TorqueUnits.NM), precision=screen_precision)
            brain.screen.print(" ")
            brain.screen.print(left1.efficiency(PERCENT), precision=screen_precision)
            brain.screen.next_row()
            brain.screen.set_fill_color(Color.TRANSPARENT)
        if left2.temperature(PERCENT) > 2:
            if left2.temperature(PERCENT) > 70:
                brain.screen.set_fill_color(Color.RED)
            brain.screen.print(str("P19      Left2: ") + str(str(left2.temperature(PERCENT))))
            brain.screen.print(" ")
            brain.screen.print(left2.power(PowerUnits.WATT), precision=screen_precision)
            brain.screen.print(" ")
            brain.screen.print(left2.torque(TorqueUnits.NM), precision=screen_precision)
            brain.screen.print(" ")
            brain.screen.print(left2.efficiency(PERCENT), precision=screen_precision)
            brain.screen.next_row()
            brain.screen.set_fill_color(Color.TRANSPARENT)
        if left3.temperature(PERCENT) > 2:
            if left3.temperature(PERCENT) > 70:
                brain.screen.set_fill_color(Color.RED)
            brain.screen.print(str("P18      Left3: ") + str(str(left3.temperature(PERCENT))))
            brain.screen.print(" ")
            brain.screen.print(left3.power(PowerUnits.WATT), precision=screen_precision)
            brain.screen.print(" ")
            brain.screen.print(left3.torque(TorqueUnits.NM), precision=screen_precision)
            brain.screen.print(" ")
            brain.screen.print(left3.efficiency(PERCENT), precision=screen_precision)
            brain.screen.next_row()
            brain.screen.set_fill_color(Color.TRANSPARENT)
        if colorsorting.temperature(PERCENT) > 0:
            if colorsorting.temperature(PERCENT) > 70:
                brain.screen.set_fill_color(Color.RED)
            brain.screen.print(str("P15 colorsorting:") + str(str(colorsorting.temperature(PERCENT))))
            brain.screen.print(" ")
            brain.screen.print(colorsorting.power(PowerUnits.WATT), precision=screen_precision)
            brain.screen.print(" ")
            brain.screen.print(colorsorting.torque(TorqueUnits.NM), precision=screen_precision)
            brain.screen.print(" ")
            brain.screen.print(colorsorting.efficiency(PERCENT), precision=screen_precision)
            brain.screen.next_row()
            brain.screen.set_fill_color(Color.TRANSPARENT)
        brain.screen.print(str("P15 colorsorting:") + str(str(colorsorting.temperature(PERCENT))))
        brain.screen.print(" ")
        brain.screen.print(colorsorting.power(PowerUnits.WATT), precision=screen_precision)
        brain.screen.print(" ")
        brain.screen.print(colorsorting.torque(TorqueUnits.NM), precision=screen_precision)
        brain.screen.print(" ")
        brain.screen.print(colorsorting.efficiency(PERCENT), precision=screen_precision)
        brain.screen.next_row()
        brain.screen.set_fill_color(Color.TRANSPARENT)
        if TopMotor.temperature(PERCENT) > 2:
            if TopMotor.temperature(PERCENT) > 70:
                brain.screen.set_fill_color(Color.RED)
            brain.screen.print(str("P1    TopMotor: ") + str(str(TopMotor.temperature(PERCENT))))
            brain.screen.print(" ")
            brain.screen.print(TopMotor.power(PowerUnits.WATT), precision=screen_precision)
            brain.screen.print(" ")
            brain.screen.print(TopMotor.torque(TorqueUnits.NM), precision=screen_precision)
            brain.screen.print(" ")
            brain.screen.print(TopMotor.efficiency(PERCENT), precision=screen_precision)
            brain.screen.next_row()
            brain.screen.set_fill_color(Color.TRANSPARENT)
        if Intake.temperature(PERCENT) > 2:
            if Intake.temperature(PERCENT) > 70:
                brain.screen.set_fill_color(Color.RED)
            brain.screen.print(str("P14     Intake: ") + str(str(Intake.temperature(PERCENT))))
            brain.screen.print(" ")
            brain.screen.print(Intake.power(PowerUnits.WATT), precision=screen_precision)
            brain.screen.print(" ")
            brain.screen.print(Intake.torque(TorqueUnits.NM), precision=screen_precision)
            brain.screen.print(" ")
            brain.screen.print(Intake.efficiency(PERCENT), precision=screen_precision)
            brain.screen.next_row()
            brain.screen.set_fill_color(Color.TRANSPARENT)
        if inertial_for_auton.acceleration(XAXIS) > 0:
            brain.screen.print(str("P6 Inertial:") + str(str("Acceleration in Gs(x,y,z): ") + str(str(str(round(inertial_for_auton.acceleration(XAXIS), 1))) + str(str(" , ") + str(str(str(round(inertial_for_auton.acceleration(YAXIS), 1))) + str(str(" , ") + str(str(round(inertial_for_auton.acceleration(ZAXIS), 1)))))))))
            brain.screen.next_row()
            brain.screen.print(str("Orientation (R,P,Y): ") + str(str(str(round(inertial_for_auton.orientation(ROLL, DEGREES), 1))) + str(str(" , ") + str(str(str(round(inertial_for_auton.orientation(PITCH, DEGREES), 1))) + str(str(" , ") + str(str(round(inertial_for_auton.orientation(YAW, DEGREES), 1))))))))
            brain.screen.next_row()
            brain.screen.print(str(str("Rotation: ") + str(str(round(inertial_for_auton.rotation(DEGREES), 1)))) + str(str("Heading: ") + str(str(round(inertial_for_auton.heading(DEGREES), 1)))))
            brain.screen.next_row()
        if auto_side == "m" and auto_side == "m":
            break
        brain.screen.render()
        wait(5, MSEC)
    while True:
        brain.screen.clear_screen()
        brain.screen.set_cursor(1, 1)
        brain.screen.set_font(FontType.MONO20)
        brain.screen.set_pen_color(Color.PURPLE)
        brain.screen.print(textReadout, precision=screen_precision)
        brain.screen.render()
        if textReadout == "done!":
            break
        wait(5, MSEC)
    wait(1.2, SECONDS)
    brain.screen.clear_screen()
    brain.screen.set_fill_color(Color.TRANSPARENT)
    brain.screen.set_font(FontType.MONO15)
    brain.screen.set_pen_color(Color.GREEN)
    screen_precision = 2
    while True:
        brain.screen.clear_screen()
        brain.screen.set_cursor(1, 1)
        brain.screen.print("Program: ")
        if auto_side == "l":
            brain.screen.print("Left ")
        elif auto_side == "r":
            brain.screen.print("Right ")
        elif auto_side == "m":
            brain.screen.set_pen_color(Color.RED)
            brain.screen.print("AuBP ")
        else:
            brain.screen.set_pen_color(Color.CYAN)
            brain.screen.print("One Inch ")
        if Auto_color == "r":
            brain.screen.set_pen_color(Color.RED)
            brain.screen.print("Red ")
            brain.screen.next_row()
        elif Auto_color == "b":
            brain.screen.set_pen_color(Color.BLUE)
            brain.screen.print("Blue ")
            brain.screen.next_row()
        else:
            brain.screen.set_pen_color(Color.ORANGE)
            brain.screen.print("No Color Sorting")
            brain.screen.next_row()
        brain.screen.set_pen_color(Color.GREEN)
        brain.screen.print("port  Name      temp  power   effeciency torque(Nm)")
        brain.screen.next_row()
        if Right1.temperature(PERCENT) > 2:
            if Right1.temperature(PERCENT) > 70:
                brain.screen.set_fill_color(Color.RED)
            brain.screen.print(str("P11 Right1: ") + str(str(Right1.temperature(PERCENT))))
            brain.screen.print("    ")
            brain.screen.print(Right1.power(PowerUnits.WATT), precision=screen_precision)
            brain.screen.print("    ")
            brain.screen.print(Right1.efficiency(PERCENT), precision=screen_precision)
            brain.screen.print("    ")
            brain.screen.print(Right1.torque(TorqueUnits.NM), precision=screen_precision)
            brain.screen.next_row()
            brain.screen.set_fill_color(Color.TRANSPARENT)
        if Right2.temperature(PERCENT) > 2:
            if Right2.temperature(PERCENT) > 70:
                brain.screen.set_fill_color(Color.RED)
            brain.screen.print(str("P13 Right2: ") + str(str(Right2.temperature(PERCENT))))
            brain.screen.print("    ")
            brain.screen.print(Right2.power(PowerUnits.WATT), precision=screen_precision)
            brain.screen.print("    ")
            brain.screen.print(Right2.efficiency(PERCENT), precision=screen_precision)
            brain.screen.print("    ")
            brain.screen.print(Right2.torque(TorqueUnits.NM), precision=screen_precision)
            brain.screen.next_row()
            brain.screen.set_fill_color(Color.TRANSPARENT)
        if Right3.temperature(PERCENT) > 2:
            if Right3.temperature(PERCENT) > 70:
                brain.screen.set_fill_color(Color.RED)
            brain.screen.print(str("P12 Right3: ") + str(str(Right3.temperature(PERCENT))))
            brain.screen.print(Right3.power(PowerUnits.WATT), precision=screen_precision)
            brain.screen.print("    ")
            brain.screen.print(Right3.efficiency(PERCENT), precision=screen_precision)
            brain.screen.print("    ")
            brain.screen.print(Right3.torque(TorqueUnits.NM), precision=screen_precision)
            brain.screen.next_row()
            brain.screen.set_fill_color(Color.TRANSPARENT)
        if left1.temperature(PERCENT) > 2:
            if left1.temperature(PERCENT) > 70:
                brain.screen.set_fill_color(Color.RED)
            brain.screen.print(str("P20 Left1: ") + str(str(left1.temperature(PERCENT))))
            brain.screen.print("    ")
            brain.screen.print(left1.power(PowerUnits.WATT), precision=screen_precision)
            brain.screen.print("    ")
            brain.screen.print(left1.efficiency(PERCENT), precision=screen_precision)
            brain.screen.print("    ")
            brain.screen.print(left1.torque(TorqueUnits.NM), precision=screen_precision)
            brain.screen.next_row()
            brain.screen.set_fill_color(Color.TRANSPARENT)
        if left2.temperature(PERCENT) > 2:
            if left2.temperature(PERCENT) > 70:
                brain.screen.set_fill_color(Color.RED)
            brain.screen.print(str("P19 Left2: ") + str(str(left2.temperature(PERCENT))))
            brain.screen.print("    ")
            brain.screen.print(left2.power(PowerUnits.WATT), precision=screen_precision)
            brain.screen.print("    ")
            brain.screen.print(left2.efficiency(PERCENT), precision=screen_precision)
            brain.screen.print("    ")
            brain.screen.print(left2.torque(TorqueUnits.NM), precision=screen_precision)
            brain.screen.next_row()
            brain.screen.set_fill_color(Color.TRANSPARENT)
        if left3.temperature(PERCENT) > 2:
            if left3.temperature(PERCENT) > 70:
                brain.screen.set_fill_color(Color.RED)
            brain.screen.print(str("P18 Left3: ") + str(str(left3.temperature(PERCENT))))
            brain.screen.print("    ")
            brain.screen.print(left3.power(PowerUnits.WATT), precision=screen_precision)
            brain.screen.print("    ")
            brain.screen.print(left3.efficiency(PERCENT), precision=screen_precision)
            brain.screen.print("    ")
            brain.screen.print(left3.torque(TorqueUnits.NM), precision=screen_precision)
            brain.screen.next_row()
            brain.screen.set_fill_color(Color.TRANSPARENT)
        if colorsorting.temperature(PERCENT) > 2:
            if colorsorting.temperature(PERCENT) > 70:
                brain.screen.set_fill_color(Color.RED)
            brain.screen.print(str("P15 colorsorting:") + str(str(colorsorting.temperature(PERCENT))))
            brain.screen.print("    ")
            brain.screen.print(colorsorting.power(PowerUnits.WATT), precision=screen_precision)
            brain.screen.print("    ")
            brain.screen.print(colorsorting.efficiency(PERCENT), precision=screen_precision)
            brain.screen.print("    ")
            brain.screen.print(colorsorting.torque(TorqueUnits.NM), precision=screen_precision)
            brain.screen.next_row()
            brain.screen.set_fill_color(Color.TRANSPARENT)
        if TopMotor.temperature(PERCENT) > 2:
            if TopMotor.temperature(PERCENT) > 70:
                brain.screen.set_fill_color(Color.RED)
            brain.screen.print(str("P1 TopMotor: ") + str(str(TopMotor.temperature(PERCENT))))
            brain.screen.print("    ")
            brain.screen.print(TopMotor.power(PowerUnits.WATT), precision=screen_precision)
            brain.screen.print("    ")
            brain.screen.print(TopMotor.efficiency(PERCENT), precision=screen_precision)
            brain.screen.print("    ")
            brain.screen.print(TopMotor.torque(TorqueUnits.NM), precision=screen_precision)
            brain.screen.next_row()
            brain.screen.set_fill_color(Color.TRANSPARENT)
        if Intake.temperature(PERCENT) > 2:
            if Intake.temperature(PERCENT) > 70:
                brain.screen.set_fill_color(Color.RED)
            brain.screen.print(str("P14 Intake: ") + str(str(Intake.temperature(PERCENT))))
            brain.screen.print("    ")
            brain.screen.print(Intake.power(PowerUnits.WATT), precision=screen_precision)
            brain.screen.print("    ")
            brain.screen.print(Intake.efficiency(PERCENT), precision=screen_precision)
            brain.screen.print("    ")
            brain.screen.print(Intake.torque(TorqueUnits.NM), precision=screen_precision)
            brain.screen.next_row()
            brain.screen.set_fill_color(Color.TRANSPARENT)
        if inertial_for_auton.acceleration(XAXIS) > 0:
            brain.screen.print(str("P6 Inertial:") + str(str("Acceleration in Gs(x,y,z): ") + str(str(str(round(inertial_for_auton.acceleration(XAXIS), 1))) + str(str(" , ") + str(str(str(round(inertial_for_auton.acceleration(YAXIS), 1))) + str(str(" , ") + str(str(round(inertial_for_auton.acceleration(ZAXIS), 1)))))))))
            brain.screen.next_row()
            brain.screen.print(str("Orientation (R,P,Y): ") + str(str(str(round(inertial_for_auton.orientation(ROLL, DEGREES), 1))) + str(str(" , ") + str(str(str(round(inertial_for_auton.orientation(PITCH, DEGREES), 1))) + str(str(" , ") + str(str(round(inertial_for_auton.orientation(YAW, DEGREES), 1))))))))
            brain.screen.next_row()
            brain.screen.print(str("Heading: ") + str(str(round(inertial_for_auton.heading(DEGREES), 1))))
            brain.screen.next_row()
            brain.screen.print(str("Rotation: ") + str(str(round(inertial_for_auton.rotation(DEGREES), 1))))
            brain.screen.next_row()
            brain.screen.render()
        wait(5, MSEC)

def when_started3():
    global my_event, fake_auto, sd_is_in, Accuracy, Front_Down, right_temp, left_temp, Descoring, turn_mod, DegreesToTurn, TurnData, driveMod, auto_side, Auto_color, leftData, RightData, IntakeData, iteration, LeftDriveData, RightDriveData, IntakeDriveData, Left_Iter, Right_Iter, Intake_Iter, textReadout, LeftVP, RightVP, BreakParsing, AuBP_MaxVP, colortoggle, skillsRun, recording, MatchLoadData, TopMotorDATA, TopMotorDriveDATA, MatchLoadDriveDATA, matchload_iter, top_iter, use_turningInertial, LastFront_down, turn_to_h_dif, Kp, Ki, Kd, error, loop_delay, last_error, integral, position, integral_limit, error_threshhold, derivative, POWER, intake_speed, screen_precision, console_precision, ai_vision_2_index, ai_vision_2_objects, controller_1_precision
    sd_is_in = False
    if brain.sdcard.is_inserted():

        print("sd card inserted!")
        sd_is_in = True
    init_setup()
    # right button - accuracy toggle
    while True:
        if controller_1.buttonUp.pressing():
            colorsorting.stop()
        if Front_Down == 1:
            frontPiston.set(True)
        else:
            frontPiston.set(False)
        if Descoring == 1:
            DeScorer.set(True)
        else:
            DeScorer.set(False)
        wait(5, MSEC)

def optical_9_detects_object_callback_0():
    global my_event, fake_auto, sd_is_in, Accuracy, Front_Down, right_temp, left_temp, Descoring, turn_mod, DegreesToTurn, TurnData, driveMod, auto_side, Auto_color, leftData, RightData, IntakeData, iteration, LeftDriveData, RightDriveData, IntakeDriveData, Left_Iter, Right_Iter, Intake_Iter, textReadout, LeftVP, RightVP, BreakParsing, AuBP_MaxVP, colortoggle, skillsRun, recording, MatchLoadData, TopMotorDATA, TopMotorDriveDATA, MatchLoadDriveDATA, matchload_iter, top_iter, use_turningInertial, LastFront_down, turn_to_h_dif, Kp, Ki, Kd, error, loop_delay, last_error, integral, position, integral_limit, error_threshhold, derivative, POWER, intake_speed, screen_precision, console_precision, ai_vision_2_index, ai_vision_2_objects, controller_1_precision
    if colortoggle == 3:
        if Auto_color == "b":
            for repeat_count3 in range(30):
                if_visual_color_detected__sort_block(optical_9.color() == Color.RED)
                wait(5, MSEC)
        elif Auto_color == "r":
            for repeat_count4 in range(30):
                if_visual_color_detected__sort_block(optical_9.color() == Color.BLUE)
                wait(5, MSEC)
        else:
            pass
    else:
        if colortoggle == 1:
            for repeat_count5 in range(30):
                if_visual_color_detected__sort_block(optical_9.color() == Color.RED)
                wait(5, MSEC)
        else:
            for repeat_count6 in range(30):
                if_visual_color_detected__sort_block(optical_9.color() == Color.BLUE)
                wait(5, MSEC)

def controller_1axis2Changed_callback_0():
    global my_event, fake_auto, sd_is_in, Accuracy, Front_Down, right_temp, left_temp, Descoring, turn_mod, DegreesToTurn, TurnData, driveMod, auto_side, Auto_color, leftData, RightData, IntakeData, iteration, LeftDriveData, RightDriveData, IntakeDriveData, Left_Iter, Right_Iter, Intake_Iter, textReadout, LeftVP, RightVP, BreakParsing, AuBP_MaxVP, colortoggle, skillsRun, recording, MatchLoadData, TopMotorDATA, TopMotorDriveDATA, MatchLoadDriveDATA, matchload_iter, top_iter, use_turningInertial, LastFront_down, turn_to_h_dif, Kp, Ki, Kd, error, loop_delay, last_error, integral, position, integral_limit, error_threshhold, derivative, POWER, intake_speed, screen_precision, console_precision, ai_vision_2_index, ai_vision_2_objects, controller_1_precision
    if controller_1.axis2.position() > -2 and controller_1.axis2.position() < 2:
        Right1.stop()
        Right2.stop()
        Right3.stop()
    else:
        if recording == 0:
            if controller_1.axis2.position() > 0:
                drive_forward_true_right__R_L_at_velocity_v(True, controller_1.axis2.position())
            else:
                drive_reverse_true_right__R_l_at_velocity_v(True, math.fabs(controller_1.axis2.position()))
        else:
            if controller_1.axis2.position() > 0:
                drive_forward_true_right__R_L_at_velocity_v(True, AuBP_MaxVP)
            else:
                drive_reverse_true_right__R_l_at_velocity_v(True, AuBP_MaxVP)

def controller_1axis3Changed_callback_0():
    global my_event, fake_auto, sd_is_in, Accuracy, Front_Down, right_temp, left_temp, Descoring, turn_mod, DegreesToTurn, TurnData, driveMod, auto_side, Auto_color, leftData, RightData, IntakeData, iteration, LeftDriveData, RightDriveData, IntakeDriveData, Left_Iter, Right_Iter, Intake_Iter, textReadout, LeftVP, RightVP, BreakParsing, AuBP_MaxVP, colortoggle, skillsRun, recording, MatchLoadData, TopMotorDATA, TopMotorDriveDATA, MatchLoadDriveDATA, matchload_iter, top_iter, use_turningInertial, LastFront_down, turn_to_h_dif, Kp, Ki, Kd, error, loop_delay, last_error, integral, position, integral_limit, error_threshhold, derivative, POWER, intake_speed, screen_precision, console_precision, ai_vision_2_index, ai_vision_2_objects, controller_1_precision
    if controller_1.axis3.position() > -2 and controller_1.axis3.position() < 2:
        left1.stop()
        left2.stop()
        left3.stop()
    else:
        if recording == 0:
            if controller_1.axis3.position() > 0:
                drive_forward_true_right__R_L_at_velocity_v(False, controller_1.axis3.position())
            else:
                drive_reverse_true_right__R_l_at_velocity_v(False, math.fabs(controller_1.axis3.position()))
        else:
            if controller_1.axis3.position() > 0:
                drive_forward_true_right__R_L_at_velocity_v(False, AuBP_MaxVP)
            else:
                drive_reverse_true_right__R_l_at_velocity_v(False, AuBP_MaxVP)

def controller_1buttonLeft_pressed_callback_0():
    global my_event, fake_auto, sd_is_in, Accuracy, Front_Down, right_temp, left_temp, Descoring, turn_mod, DegreesToTurn, TurnData, driveMod, auto_side, Auto_color, leftData, RightData, IntakeData, iteration, LeftDriveData, RightDriveData, IntakeDriveData, Left_Iter, Right_Iter, Intake_Iter, textReadout, LeftVP, RightVP, BreakParsing, AuBP_MaxVP, colortoggle, skillsRun, recording, MatchLoadData, TopMotorDATA, TopMotorDriveDATA, MatchLoadDriveDATA, matchload_iter, top_iter, use_turningInertial, LastFront_down, turn_to_h_dif, Kp, Ki, Kd, error, loop_delay, last_error, integral, position, integral_limit, error_threshhold, derivative, POWER, intake_speed, screen_precision, console_precision, ai_vision_2_index, ai_vision_2_objects, controller_1_precision
    if skillsRun == 1:
        controller_1.screen.clear_row(3)
        controller_1.screen.set_cursor(controller_1.screen.row(), 1)
        if not colortoggle == 1:
            colortoggle = 1
            controller_1.screen.print("Sort RED")
        else:
            colortoggle = 3
            controller_1.screen.print("DEFAULT")

def controller_1buttonUp_pressed_callback_0():
    global my_event, fake_auto, sd_is_in, Accuracy, Front_Down, right_temp, left_temp, Descoring, turn_mod, DegreesToTurn, TurnData, driveMod, auto_side, Auto_color, leftData, RightData, IntakeData, iteration, LeftDriveData, RightDriveData, IntakeDriveData, Left_Iter, Right_Iter, Intake_Iter, textReadout, LeftVP, RightVP, BreakParsing, AuBP_MaxVP, colortoggle, skillsRun, recording, MatchLoadData, TopMotorDATA, TopMotorDriveDATA, MatchLoadDriveDATA, matchload_iter, top_iter, use_turningInertial, LastFront_down, turn_to_h_dif, Kp, Ki, Kd, error, loop_delay, last_error, integral, position, integral_limit, error_threshhold, derivative, POWER, intake_speed, screen_precision, console_precision, ai_vision_2_index, ai_vision_2_objects, controller_1_precision
    if skillsRun == 1:
        controller_1.screen.clear_row(3)
        controller_1.screen.set_cursor(controller_1.screen.row(), 1)
        if not colortoggle == 2:
            colortoggle = 2
            controller_1.screen.print("sort BLUE")
        else:
            colortoggle = 3
            controller_1.screen.print("DEFAULT")

def controller_1buttonRight_pressed_callback_0():
    global my_event, fake_auto, sd_is_in, Accuracy, Front_Down, right_temp, left_temp, Descoring, turn_mod, DegreesToTurn, TurnData, driveMod, auto_side, Auto_color, leftData, RightData, IntakeData, iteration, LeftDriveData, RightDriveData, IntakeDriveData, Left_Iter, Right_Iter, Intake_Iter, textReadout, LeftVP, RightVP, BreakParsing, AuBP_MaxVP, colortoggle, skillsRun, recording, MatchLoadData, TopMotorDATA, TopMotorDriveDATA, MatchLoadDriveDATA, matchload_iter, top_iter, use_turningInertial, LastFront_down, turn_to_h_dif, Kp, Ki, Kd, error, loop_delay, last_error, integral, position, integral_limit, error_threshhold, derivative, POWER, intake_speed, screen_precision, console_precision, ai_vision_2_index, ai_vision_2_objects, controller_1_precision
    TopMotor.spin(FORWARD)

def controller_1buttonL2_pressed_callback_0():
    global my_event, fake_auto, sd_is_in, Accuracy, Front_Down, right_temp, left_temp, Descoring, turn_mod, DegreesToTurn, TurnData, driveMod, auto_side, Auto_color, leftData, RightData, IntakeData, iteration, LeftDriveData, RightDriveData, IntakeDriveData, Left_Iter, Right_Iter, Intake_Iter, textReadout, LeftVP, RightVP, BreakParsing, AuBP_MaxVP, colortoggle, skillsRun, recording, MatchLoadData, TopMotorDATA, TopMotorDriveDATA, MatchLoadDriveDATA, matchload_iter, top_iter, use_turningInertial, LastFront_down, turn_to_h_dif, Kp, Ki, Kd, error, loop_delay, last_error, integral, position, integral_limit, error_threshhold, derivative, POWER, intake_speed, screen_precision, console_precision, ai_vision_2_index, ai_vision_2_objects, controller_1_precision
    TopMotor.spin(REVERSE)
    Intake.spin(REVERSE)

def controller_1buttonL1_pressed_callback_0():
    global my_event, fake_auto, sd_is_in, Accuracy, Front_Down, right_temp, left_temp, Descoring, turn_mod, DegreesToTurn, TurnData, driveMod, auto_side, Auto_color, leftData, RightData, IntakeData, iteration, LeftDriveData, RightDriveData, IntakeDriveData, Left_Iter, Right_Iter, Intake_Iter, textReadout, LeftVP, RightVP, BreakParsing, AuBP_MaxVP, colortoggle, skillsRun, recording, MatchLoadData, TopMotorDATA, TopMotorDriveDATA, MatchLoadDriveDATA, matchload_iter, top_iter, use_turningInertial, LastFront_down, turn_to_h_dif, Kp, Ki, Kd, error, loop_delay, last_error, integral, position, integral_limit, error_threshhold, derivative, POWER, intake_speed, screen_precision, console_precision, ai_vision_2_index, ai_vision_2_objects, controller_1_precision
    TopMotor.spin(REVERSE)
    Intake.spin(FORWARD)

def controller_1buttonRight_released_callback_0():
    global my_event, fake_auto, sd_is_in, Accuracy, Front_Down, right_temp, left_temp, Descoring, turn_mod, DegreesToTurn, TurnData, driveMod, auto_side, Auto_color, leftData, RightData, IntakeData, iteration, LeftDriveData, RightDriveData, IntakeDriveData, Left_Iter, Right_Iter, Intake_Iter, textReadout, LeftVP, RightVP, BreakParsing, AuBP_MaxVP, colortoggle, skillsRun, recording, MatchLoadData, TopMotorDATA, TopMotorDriveDATA, MatchLoadDriveDATA, matchload_iter, top_iter, use_turningInertial, LastFront_down, turn_to_h_dif, Kp, Ki, Kd, error, loop_delay, last_error, integral, position, integral_limit, error_threshhold, derivative, POWER, intake_speed, screen_precision, console_precision, ai_vision_2_index, ai_vision_2_objects, controller_1_precision
    TopMotor.stop()

def controller_1buttonL2_released_callback_0():
    global my_event, fake_auto, sd_is_in, Accuracy, Front_Down, right_temp, left_temp, Descoring, turn_mod, DegreesToTurn, TurnData, driveMod, auto_side, Auto_color, leftData, RightData, IntakeData, iteration, LeftDriveData, RightDriveData, IntakeDriveData, Left_Iter, Right_Iter, Intake_Iter, textReadout, LeftVP, RightVP, BreakParsing, AuBP_MaxVP, colortoggle, skillsRun, recording, MatchLoadData, TopMotorDATA, TopMotorDriveDATA, MatchLoadDriveDATA, matchload_iter, top_iter, use_turningInertial, LastFront_down, turn_to_h_dif, Kp, Ki, Kd, error, loop_delay, last_error, integral, position, integral_limit, error_threshhold, derivative, POWER, intake_speed, screen_precision, console_precision, ai_vision_2_index, ai_vision_2_objects, controller_1_precision
    Intake.stop()
    TopMotor.stop()

def controller_1buttonL1_released_callback_0():
    global my_event, fake_auto, sd_is_in, Accuracy, Front_Down, right_temp, left_temp, Descoring, turn_mod, DegreesToTurn, TurnData, driveMod, auto_side, Auto_color, leftData, RightData, IntakeData, iteration, LeftDriveData, RightDriveData, IntakeDriveData, Left_Iter, Right_Iter, Intake_Iter, textReadout, LeftVP, RightVP, BreakParsing, AuBP_MaxVP, colortoggle, skillsRun, recording, MatchLoadData, TopMotorDATA, TopMotorDriveDATA, MatchLoadDriveDATA, matchload_iter, top_iter, use_turningInertial, LastFront_down, turn_to_h_dif, Kp, Ki, Kd, error, loop_delay, last_error, integral, position, integral_limit, error_threshhold, derivative, POWER, intake_speed, screen_precision, console_precision, ai_vision_2_index, ai_vision_2_objects, controller_1_precision
    Intake.stop()
    TopMotor.stop()

def controller_1buttonDown_pressed_callback_0():
    global my_event, fake_auto, sd_is_in, Accuracy, Front_Down, right_temp, left_temp, Descoring, turn_mod, DegreesToTurn, TurnData, driveMod, auto_side, Auto_color, leftData, RightData, IntakeData, iteration, LeftDriveData, RightDriveData, IntakeDriveData, Left_Iter, Right_Iter, Intake_Iter, textReadout, LeftVP, RightVP, BreakParsing, AuBP_MaxVP, colortoggle, skillsRun, recording, MatchLoadData, TopMotorDATA, TopMotorDriveDATA, MatchLoadDriveDATA, matchload_iter, top_iter, use_turningInertial, LastFront_down, turn_to_h_dif, Kp, Ki, Kd, error, loop_delay, last_error, integral, position, integral_limit, error_threshhold, derivative, POWER, intake_speed, screen_precision, console_precision, ai_vision_2_index, ai_vision_2_objects, controller_1_precision
    Descoring = 1 - Descoring

def controller_1buttonB_pressed_callback_0():
    global my_event, fake_auto, sd_is_in, Accuracy, Front_Down, right_temp, left_temp, Descoring, turn_mod, DegreesToTurn, TurnData, driveMod, auto_side, Auto_color, leftData, RightData, IntakeData, iteration, LeftDriveData, RightDriveData, IntakeDriveData, Left_Iter, Right_Iter, Intake_Iter, textReadout, LeftVP, RightVP, BreakParsing, AuBP_MaxVP, colortoggle, skillsRun, recording, MatchLoadData, TopMotorDATA, TopMotorDriveDATA, MatchLoadDriveDATA, matchload_iter, top_iter, use_turningInertial, LastFront_down, turn_to_h_dif, Kp, Ki, Kd, error, loop_delay, last_error, integral, position, integral_limit, error_threshhold, derivative, POWER, intake_speed, screen_precision, console_precision, ai_vision_2_index, ai_vision_2_objects, controller_1_precision
    Front_Down = 1 - Front_Down

def controller_1buttonX_pressed_callback_0():
    global my_event, fake_auto, sd_is_in, Accuracy, Front_Down, right_temp, left_temp, Descoring, turn_mod, DegreesToTurn, TurnData, driveMod, auto_side, Auto_color, leftData, RightData, IntakeData, iteration, LeftDriveData, RightDriveData, IntakeDriveData, Left_Iter, Right_Iter, Intake_Iter, textReadout, LeftVP, RightVP, BreakParsing, AuBP_MaxVP, colortoggle, skillsRun, recording, MatchLoadData, TopMotorDATA, TopMotorDriveDATA, MatchLoadDriveDATA, matchload_iter, top_iter, use_turningInertial, LastFront_down, turn_to_h_dif, Kp, Ki, Kd, error, loop_delay, last_error, integral, position, integral_limit, error_threshhold, derivative, POWER, intake_speed, screen_precision, console_precision, ai_vision_2_index, ai_vision_2_objects, controller_1_precision
    if skillsRun == 1:
        if intake_speed == 100:
            Intake.set_velocity(40, PERCENT)
            intake_speed = 40
        else:
            Intake.set_velocity(100, PERCENT)
            intake_speed = 100

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

    # wait for the driver control period to end
    while( competition.is_driver_control() and competition.is_enabled() ):
        # wait 10 milliseconds before checking again
        wait( 10, MSEC )
    # Stop the driver control tasks


# register the competition functions
competition = Competition( vexcode_driver_function, vexcode_auton_function )

# system event handlers
optical_9.object_detected(optical_9_detects_object_callback_0)
controller_1.axis2.changed(controller_1axis2Changed_callback_0)
controller_1.axis3.changed(controller_1axis3Changed_callback_0)
controller_1.buttonLeft.pressed(controller_1buttonLeft_pressed_callback_0)
controller_1.buttonUp.pressed(controller_1buttonUp_pressed_callback_0)
controller_1.buttonRight.pressed(controller_1buttonRight_pressed_callback_0)
controller_1.buttonL2.pressed(controller_1buttonL2_pressed_callback_0)
controller_1.buttonL1.pressed(controller_1buttonL1_pressed_callback_0)
controller_1.buttonRight.released(controller_1buttonRight_released_callback_0)
controller_1.buttonL2.released(controller_1buttonL2_released_callback_0)
controller_1.buttonL1.released(controller_1buttonL1_released_callback_0)
controller_1.buttonDown.pressed(controller_1buttonDown_pressed_callback_0)
controller_1.buttonB.pressed(controller_1buttonB_pressed_callback_0)
controller_1.buttonX.pressed(controller_1buttonX_pressed_callback_0)
# add 15ms delay to make sure events are registered correctly.
wait(15, MSEC)

ws2 = Thread( when_started2 )
ws3 = Thread( when_started3 )
when_started1()
