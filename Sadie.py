from base_robot import *

# Add good comments, such as what the mission is supposed to do,
# how to align the robot in home, any initial starting instructions,
# such as how it should be loaded with anything, arm positions, etc.


# When we run this program from the master program, we will call this
# "Run(br)" method.
def Run(br: BaseRobot):
    # Your mission code goes here, step-by-step
    # It MUST be indented just like the lines below
    br.moveRightAttachmentMotorForDegrees(5, wait=False)
    br.driveForDistance(795)
    br.turnInPlace(-64)
    br.driveForDistance(220, speedPct=100)
    br.waitForMillis(450)
    br.driveForDistance(-330)
    br.turnInPlace(-35)
    br.moveRightAttachmentMotorForDegrees(-165)
    br.driveForDistance(350)
    br.moveRightAttachmentMotorForDegrees(145, speedPct=100)
    br.driveForDistance(-100, wait=False)
    br.moveRightAttachmentMotorForDegrees(100)


# If running this program directly (not from the master program), this is
# how we know it is running directly. In which case, this method will
# create a BaseRobot and run the Run(br) method above.
# In other words, keep these three lines at the bottom of your code and
# everything will be fine.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
