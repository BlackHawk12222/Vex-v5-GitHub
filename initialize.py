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
