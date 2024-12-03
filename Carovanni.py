from base_robot import *

import Sadie2

# Add good comments, such as what the mission is supposed to do,
# how to align the robot in home, any initial starting instructions,
# such as how it should be loaded with anything, arm positions, etc.
# When we run this program from the master program, we will call this
# "Run(br)" method.


def Run(br: BaseRobot):
    br.driveForDistance(15, wait=False)
    br.moveRightAttachmentMotorForDegrees(-620)
    br.driveForDistance(-40)
    br.moveRightAttachmentMotorForDegrees(320, speedPct=50)
    br.driveForDistance(-40)
    br.moveRightAttachmentMotorForDegrees(-250, wait=False)
    br.driveForDistance(-500)

    br.waitForForwardButton()
    Sadie2.Run(br)

    # Your mission code goes here, step-by-step
    # It MUST be indented just like the lines below


# If running this program directly (not from the master program), this is
# how we know it is running directly. In which case, this method will
# create a BaseRobot and run the Run(br) method above.
# In other words, keep these three lines at the bottom of your code and
# everything will be fine.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
