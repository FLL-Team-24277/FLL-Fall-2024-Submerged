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
    br.moveRightAttachmentMotorForDegrees(20)
    br.moveRightAttachmentMotorForDegrees(-160, wait=False)
    br.driveForDistance(700)
    br.turnInPlace(25)
    br.driveForDistance(35)
    br.moveRightAttachmentMotorForDegrees(-140)
    br.driveForDistance(25)
    br.driveForDistance(-50, wait=False)
    br.moveRightAttachmentMotorForDegrees(140)
    br.turnInPlace(-95)
    # shark
    br.driveForDistance(-50)
    br.moveRightAttachmentMotorForDegrees(-195)
    br.driveForDistance(-25)
    br.moveRightAttachmentMotorForDegrees(-30)
    br.moveRightAttachmentMotorForDegrees(225)
    # coral reef
    br.turnInPlace(-25)
    br.driveForDistance(130)
    br.moveRightAttachmentMotorForDegrees(100)
    br.driveForDistance(-100)
    br.turnInPlace(-65)
    br.driveForDistance(600)


# If running this program directly (not from the master program), this is
# how we know it is running directly. In which case, this method will
# create a BaseRobot and run the Run(br) method above.
# In other words, keep these three lines at the bottom of your code and
# everything will be fine.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
