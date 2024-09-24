from pybricks.pupdevices import Motor

from pybricks.parameters import (
    Port,
    Direction,
    Stop,
)
from pybricks.robotics import DriveBase

TIRE_DIAMETER = 56  # mm
AXLE_TRACK = 103  # distance between the wheels, mm

leftDriveMotor = Motor(Port.E, Direction.COUNTERCLOCKWISE)
rightDriveMotor = Motor(Port.A)
robot = DriveBase(
    leftDriveMotor,
    rightDriveMotor,
    TIRE_DIAMETER,
    AXLE_TRACK,
)

robot.settings(straight_speed=400, straight_acceleration=300)
robot.straight(distance=700, then=Stop.NONE)
robot.curve(radius=600, angle=90)
