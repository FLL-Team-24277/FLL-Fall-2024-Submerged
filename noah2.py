from base_robot import *

# Add good comments, such as what the mission is supposed to do,
# how to align the robot in home, any initial starting instructions,
# such as how it should be loaded with anything, arm positions, etc.


# When we run this program from the master program, we will cal(l this
# "Run(br)" method.
def Run(br: BaseRobot):
    # Your mission code goes here, step-by-step
    # It MUST be indented just like the lines below

    br.driveForDistance(480, speedPct=100, then=Stop.NONE)
    br.driveArcDist(radius=255, dist=280)
    # br.driveForDistance(30)
    # br.moveLeftAttachmentMotorForMillis(millis=1000, speedPct=-100, wait=False)
    # br.moveLeftAttachmentMotorForDegrees(400)
    # br.moveRightAttachmentMotorForMillis(millis=750, speedPct=-75)
    # br.moveRightAttachmentMotorForMillis(millis=250, speedPct=10)
    # WIGGLE WIGGLE

    # br.moveLeftAttachmentMotorForMillis(millis=250, speedPct=-100)
    # br.moveLeftAttachmentMotorForMillis(millis=250, speedPct=100)
    # br.moveLeftAttachmentMotorForMillis(millis=250, speedPct=-100)
    # br.moveLeftAttachmentMotorForMillis(millis=500, speedPct=-100, wait=False)
    # END OF WIGGLE WIGGLE

    # br.waitForMillis(500)
    # br.driveForDistance(-300)
    # br.turnInPlace(-80)
    # br.driveForDistance(-750)


# If running this program directly (not from the master program), this is
# how we know it is running directly. In which case, this method will
# create a BaseRobot and run the Run(br) method above.
# In other words, keep these three lines at the bottom of your code and
# everything will be fine.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
