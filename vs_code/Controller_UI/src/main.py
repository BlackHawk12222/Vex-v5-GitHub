# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       MicaS                                                        #
# 	Created:      4/6/2026, 3:34:40 PM                                         #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *

# Brain should be defined by default
brain=Brain()

motor1=Motor(Ports.PORT1)
run_time=Timer()
controller=Controller(PRIMARY)
def spin():
    motor1.spin(FORWARD, 12, VoltageUnits.VOLT)

def stop():
    motor1.stop()

controller.buttonA.pressed(spin)
controller.buttonB.pressed(stop)

controller.screen.clear_screen()
controller.screen.set_cursor(1,1)
controller.screen.print("%% %03d Cur: %04.1f /20.0"%(brain.battery.capacity(), brain.battery.current(CurrentUnits.AMP)))
controller.screen.new_line()
controller.screen.print("Time: %d"%(run_time.time(TimeUnits.SECONDS)))
controller.screen.new_line()
controller.screen.print("DAT: %02d%% IT: %02d%%"%(motor1.temperature(PERCENT), motor1.temperature(PERCENT)))

while True:
    controller.screen.set_cursor(1, 3)
    controller.screen.print("%03d"%(brain.battery.capacity()))
    controller.screen.set_cursor(1, 12)
    controller.screen.print("%04.1f"%(brain.battery.current(CurrentUnits.AMP)))
    controller.screen.set_cursor(2, 7)
    controller.screen.print("%d"%(run_time.time(TimeUnits.SECONDS)))
    controller.screen.set_cursor(3, 6)
    controller.screen.print("%02d%%"%(motor1.temperature(PERCENT)))
    controller.screen.set_cursor(3, 14)
    controller.screen.print("%02d%%"%(motor1.temperature(PERCENT)))
    wait(100, MSEC)
