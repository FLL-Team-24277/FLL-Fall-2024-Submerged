from base_robot import *

# Add good comments, such as what the mission is supposed to do,
# how to align the robot in home, any initial starting instructions,
# such as how it should be loaded with anything, arm positions, etc.


# When we run this program from the master program, we will call this
# "Run(br)" method.
def Run(br: BaseRobot):
    # Your mission code goes here, step-by-step
    # It MUST be indented just like the lines below
    # br.driveArcDist(radius=-250, dist=-150, speedPct=80)
    # br.moveLeftAttachmentMotorUntilStalled(speedPct=50, stallPct=95)
    # br.moveLeftAttachmentMotorForDegrees(degrees=360, speedPct=100, wait=False)
    # br.moveRightAttachmentMotorForDegrees(degrees=-360, speedPct=100)

    medMotPair = DriveBase(
        br.leftAttachmentMotor, br.rightAttachmentMotor, 100, 100
    )
    medMotPair.curve(0, -360)
    wait(1001)
    medMotPair.stop()
    # br.leftAttachmentMotor.reset_angle(0)
    # br.leftAttachmentMotor.run_target(speed=300, target_angle=90)
    # br.moveRightAttachmentMotorForDegrees(250)


# If running this program directly (not from the master program), this is
# how we know it is running directly. In which case, this method will
# create a BaseRobot and run the Run(br) method above.
# In other words, keep these three lines at the bottom of your code and
# everything will be fine.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
