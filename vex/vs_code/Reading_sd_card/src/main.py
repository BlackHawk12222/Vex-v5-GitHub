# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       MicaS                                                        #
# 	Created:      1/24/2026, 2:21:04 PM                                        #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *

brain = Brain()

controller_1 = Controller()

List_Left = []
List_Right = []

if brain.sdcard.is_inserted():
    brain.screen.print("SD Card Inserted. Prees A for Left, X for Right.")
    brain.screen.set_font(FontType.MONO12)

    if controller_1.buttonA.pressing():
        Left_Aton_file = brain.sdcard.loadfile("Left_Aton.txt")
        Right_Aton_file = brain.sdcard.loadfile("Right_Aton.txt")
        List_Left = [Left_Aton_file.decode("utf-8")]
        print(List_Left)
        for Left in List_Left:
            brain.screen.print(Left)
    elif controller_1.buttonX.pressing():
        Right_Aton_file = brain.sdcard.loadfile("Right_Aton.txt")
        List_Right = [Right_Aton_file.decode("utf-8")]
        print(List_Right)
        for Right in List_Right:
            brain.screen.print(Right)
else:
    brain.screen.print("No SD Card Inserted")
