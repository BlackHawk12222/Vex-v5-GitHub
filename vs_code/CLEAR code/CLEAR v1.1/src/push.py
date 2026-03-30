from vex import *

class Pushing():
    def __init__(self):
        self.stoped=False

    def impact_mode(self, *motors: Motor):
        self.stoped=False
        group=MotorGroup(*motors)
        
        group.set_max_torque(4, CurrentUnits.AMP)

        while not self.stoped:
            group.spin(FORWARD, 200, PERCENT)
            wait(100, MSEC)
            group.spin(REVERSE, 200, PERCENT)
            wait(50, MSEC)
    
    def stop(self):
        self.stoped=True
