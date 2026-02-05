def if_visual_color_detected__sort_block(if_visual_color_detected__sort_block__color):
    global my_event, fake_auto, sd_is_in, Accuracy, Front_Down, right_temp, left_temp, Descoring, turn_mod, DegreesToTurn, TurnData, driveMod, auto_side, Auto_color, leftData, RightData, IntakeData, iteration, LeftDriveData, RightDriveData, IntakeDriveData, Left_Iter, Right_Iter, Intake_Iter, textReadout, LeftVP, RightVP, BreakParsing, AuBP_MaxVP, colortoggle, skillsRun, recording, MatchLoadData, TopMotorDATA, TopMotorDriveDATA, MatchLoadDriveDATA, matchload_iter, top_iter, use_turningInertial, LastFront_down, turn_to_h_dif, Kp, Ki, Kd, error, loop_delay, last_error, integral, position, integral_limit, error_threshhold, derivative, POWER, intake_speed, screen_precision, console_precision, ai_vision_2_index, ai_vision_2_objects, controller_1_precision
    if if_visual_color_detected__sort_block__color:
        Intake.stop()
        colorsorting.spin(REVERSE)
    else:
        colorsorting.stop()
