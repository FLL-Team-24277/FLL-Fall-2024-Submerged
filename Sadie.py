from base_robot import *

# Add good comments, such as what the mission is supposed to do,
# how to align the robot in home, any initial starting instructions,
# such as how it should be loaded with anything, arm positions, etc.

###             this is the shark/coral reef


# When we run this program from the master program, we will call this
# "Run(br)" method.
def Run(br: BaseRobot):
    # Your mission code goes here, step-by-step
    # It MUST be indented just like the lines below

    # Coral nursery

    br.driveForDistance(200, wait=False)
    br.curve(150, 40)
    br.curve(150, -40)
    br.driveForDistance(450)
    br.moveRightAttachmentMotorForDegrees(-145, wait=False)
    br.moveLeftAttachmentMotorForDegrees(350)
    br.waitForMillis(300)
    br.moveLeftAttachmentMotorForDegrees(-300)
    br.turnInPlace(-90)
    br.moveLeftAttachmentMotorForDegrees(320)


# If running this program directly (not from the master program), this is
# how we know it is running directly. In which case, this method will
# create a BaseRobot and run the Run(br) method above.
# In other words, keep these three lines at the bottom of your code and
# everything will be fine.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
