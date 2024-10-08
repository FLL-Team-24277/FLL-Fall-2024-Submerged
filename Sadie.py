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

    # coral reef
    br.moveRightAttachmentMotorForDegrees(-170, wait=False)
    br.driveForDistance(700)
    br.turnInPlace(16)
    br.moveRightAttachmentMotorForDegrees(-120)
    br.driveForDistance(20)
    br.moveRightAttachmentMotorForDegrees(-20)
    br.waitForMillis(1000)
    br.driveForDistance(-20, wait=False)
    br.moveRightAttachmentMotorForDegrees(140)
    br.turnInPlace(-80)
    # shark
    br.driveForDistance(-60)
    br.moveRightAttachmentMotorForDegrees(-175)
    br.driveForDistance(-15)
    br.moveRightAttachmentMotorForDegrees(-30)
    br.moveRightAttachmentMotorForDegrees(215)
    # coral reef
    br.turnInPlace(-30)
    br.driveForDistance(100)
    br.moveRightAttachmentMotorForDegrees(90)
    br.driveForDistance(-100)


# If running this program directly (not from the master program), this is
# how we know it is running directly. In which case, this method will
# create a BaseRobot and run the Run(br) method above.
# In other words, keep these three lines at the bottom of your code and
# everything will be fine.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
