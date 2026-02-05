def if_visual_color_detected__sort_block(if_visual_color_detected__sort_block__color):
    global my_event, fake_auto, sd_is_in, Accuracy, Front_Down, right_temp, left_temp, Descoring, turn_mod, DegreesToTurn, TurnData, driveMod, auto_side, Auto_color, leftData, RightData, IntakeData, iteration, LeftDriveData, RightDriveData, IntakeDriveData, Left_Iter, Right_Iter, Intake_Iter, textReadout, LeftVP, RightVP, BreakParsing, AuBP_MaxVP, colortoggle, skillsRun, recording, MatchLoadData, TopMotorDATA, TopMotorDriveDATA, MatchLoadDriveDATA, matchload_iter, top_iter, use_turningInertial, LastFront_down, turn_to_h_dif, Kp, Ki, Kd, error, loop_delay, last_error, integral, position, integral_limit, error_threshhold, derivative, POWER, intake_speed, screen_precision, console_precision, ai_vision_2_index, ai_vision_2_objects, controller_1_precision
    if if_visual_color_detected__sort_block__color:
        Intake.stop()
        colorsorting.spin(REVERSE)
    else:
        colorsorting.stop()

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
