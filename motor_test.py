from pybricks.pupdevices import Motor
from pybricks.parameters import (
    Port,
    Direction,
)
from pybricks.tools import wait

leftAttachmentMotor = Motor(Port.B)
# default is accel=1000, torque = 199
print("First starting angle", leftAttachmentMotor.angle())

# keep a running average of the last four load readings

# run untill stalled
for i in range(1, 10):
    loads = [0] * 3
    leftAttachmentMotor.run(speed=250)
    while True:
        load = abs(leftAttachmentMotor.load())
        loads.append(load)
        loads.pop(0)
        if sum(loads) / len(loads) > 30:
            break
        wait(25)

    wait(1000)

    afterStall = leftAttachmentMotor.angle()
    leftAttachmentMotor.run_angle(rotation_angle=-680, speed=250)

    wait(500)
    stoppedAt = leftAttachmentMotor.angle()
    print("After stall =", afterStall, "Stopped at", stoppedAt)
    wait(1000)
