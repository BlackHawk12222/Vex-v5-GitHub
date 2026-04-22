# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       MicaS                                                        #
# 	Created:      4/21/2026, 2:24:18 PM                                        #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *

# Brain should be defined by default
brain=Brain()

log_link=MessageLink(Ports.PORT21, "CLEAR32449", VexlinkType.WORKER)

brain.screen.set_cursor(1,1)
brain.screen.set_font(FontType.MONO12)
while True:
    if brain.screen.row() > 19:
        brain.screen.clear_screen()
        brain.screen.set_cursor(1,1)
    message=log_link.receive()
    if message != None:
        brain.screen.print(message)
        print(message)
        brain.screen.new_line()