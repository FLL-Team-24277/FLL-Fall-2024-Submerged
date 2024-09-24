from base_robot import *

# Add good comments, such as what the mission is supposed to do,
# how to align the robot in home, any initial starting instructions,
# such as how it should be loaded with anything, arm positions, etc.


# When we run this program from the master program, we will call this
# "Run(br)" method.
def Run(br: BaseRobot):
    # Your mission code goes here, step-by-step
    # It MUST be indented just like the lines below
    br.driveForDistance(520)
    br.turnInPlace(90)
    br.driveForDistance(128)
    br.moveRightAttachmentMotorForDegrees(degrees=550, speedPct=65)
    br.moveLeftAttachmentMotorForDegrees(degrees=35, speedPct=45)
    br.driveForDistance(-80)
    br.turnInPlace(90)
    br.driveForDistance(200)
    br.turnInPlace(90)
    br.moveRightAttachmentMotorForDegrees(degrees=325, wait=False)
    #br.driveForDistance(950)
    #br.turnInPlace(-135)
    #br.driveForDistance(159)
    #br.moveLeftAttachmentMotorForDegrees(degrees=-125, speedPct=50, wait=2500)
    #br.turnInPlace(-10)
    #br.driveForDistance(-975)
# If running this program directly 
# t from the master program), this is
# how we know it is running directly. In which case, this method will
# create a BaseRobot and run the Run(br) method above.
# In other words, keep these three lines at the bottom of your code and
# everything will be fine.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
