from pybricks.pupdevices import Motor

from pybricks.parameters import (
    Port,
    Direction,
    Stop,
)
from pybricks.robotics import DriveBase
from pybricks import version
import utils

print(version)

leftMedMot = Motor(Port.B)
rightMedmot = Motor(Port.D)
leftSpeed = utils.RescaleMedMotSpeed(100)
rightSpeed = utils.RescaleMedMotSpeed(100)
leftMedMot.run_angle(speed=leftSpeed, rotation_angle=360, wait=False)
rightMedmot.run_angle(speed=rightSpeed, rotation_angle=-360)