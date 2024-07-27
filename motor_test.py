from pybricks.pupdevices import Motor
from pybricks.parameters import (
    Port,
    Direction,
)
from pybricks.tools import wait

leftAttachmentMotor = Motor(Port.B)
 # default is accel=1000, torque = 199
print(leftAttachmentMotor.control.limits())
leftAttachmentMotor.run(speed=1000)
loads = [0] * 10
while(True):
    load = abs(leftAttachmentMotor.load())
    loads.append(load)
    loads.pop(0)
    print(load, sum(loads) / len(loads))
    wait(100)