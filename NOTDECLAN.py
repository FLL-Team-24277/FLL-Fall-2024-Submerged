def MoveRightAttachmentMotorForDegrees(self, degrees, speed=DEFAULT_MOT_SPEED, then=Stop.BRAKE, wait=True):
    self.RightAttachmentMotor.run_angle(speed, degrees, then=Stop.HOLD, wait=True)
