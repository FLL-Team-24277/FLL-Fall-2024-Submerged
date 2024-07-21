from pybricks.parameters import Stop

DEFAULT_MOT_SPEED = 500
DEFAULT_STALL = 120


def leftAttachmentMoterForDegrees(
    self, degrees, speed=DEFAULT_MOT_SPEED, then=Stop.BRAKE, wait=True
):
    self.leftAttachmentMotor.run_angle(
        speed, degrees, then=Stop.HOLD, wait=True
    )


def leftAttachmentMotorForMillis(
    self, millis, speed=DEFAULT_MOT_SPEED, then=Stop.BRAKE, wait=True
):
    self.leftAttachmentMotor.run_angle(
        speed, millis, then=Stop.HOLD, wait=True
    )


def leftAttachmentMotorUntilStalled(
    self,
    StallPercent=DEFAULT_STALL,
    speed=DEFAULT_MOT_SPEED,
    then=Stop.BRAKE,
    wait=True,
):
    self.leftAttachmentMotor.run_angle(
        speed, StallPercent, then=Stop.HOLD, wait=True
    )
