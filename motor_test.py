from pybricks.pupdevices import Motor
from pybricks.parameters import (
    Port,
    Direction,
)

leftAttachmentMotor = Motor(Port.B)
leftAttachmentMotor.control.limits(acceleration=10000)
leftAttachmentMotor.run_angle(speed=1000, rotation_angle=10000)
