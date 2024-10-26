from base_robot import *

# Add good comments, such as what the mission is supposed to do,
# how to align the robot in home, any initial starting instructions,
# such as how it should be loaded with anything, arm positions, etc.


# When we run this program from the master program, we will call this
# "Run(br)" method.
def Run(br: BaseRobot):
    # Your mission code goes here, step-by-step
 
    # It MUST be indented just like the lines below
    
    #br.driveForDistance(600)
    br.driveForDistance(400, then=Stop.NONE)
    br.driveArcDist(radius=800, dist=180, then=Stop.NONE)
    br.driveArcDist(radius=-800, dist=180, then=Stop.NONE)
    br.driveForDistance(300)
    br.moveRightAttachmentMotorForDegrees(-75)
    br.driveForDistance(-180)
    br.moveRightAttachmentMotorForDegrees(95)
    br.driveForDistance(-100)
    br.moveRightAttachmentMotorForDegrees(75)
    br.driveForDistance(50)
    br.moveRightAttachmentMotorForDegrees(90)
    br.turnInPlace(-40)
    br.driveForDistance(350)
    br.turnInPlace(35)
    br.driveForDistance(200)

    # If running this pogram directly (not from the master program), this is
# how we know it is running directly. In which case, this method will
# create a BaseRobot and run the Run(br) method above.
# In other words, keep these three lines at the bottom of your code and
# everything will be fine-.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
