def leftAttachmentMoterForDegrees(
    self, degrees, speed=DEFAULT_MOT_SPEED, then=Stop.BRAKE, wait=TRUE
):
    self.leftAttachmentMotor.run_angle(
        speed, degrees, then=Stop.HOLD, wait=True
    )
