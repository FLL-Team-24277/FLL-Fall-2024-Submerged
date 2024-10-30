from base_robot import *

# Add good comments, such as what the mission is supposed to do,
# how to align the robot in home, any initial starting instructions,
# such as how it should be loaded with anything, arm positions, etc.


# When we run this program from the master program, we will cal(l this
# "Run(br)" method.
def Run(br: BaseRobot):
    # Your mission code goes here, step-by-step
    # It MUST be indented just like the lines below

    br.driveForDistance(400)
    # br.driveArcDist(radius=-400)
    br.driveArcDist(radius=-450,dist=-450)
    #negitive opens positive closes
    br.waitForForwardButton()
    br.moveLeftAttachmentMotorForDegrees(-500)
    # br.driveForDistance(400)
    br.driveArcDist(radius=-1000,dist=300, then=Stop.NONE)
    br.driveArcDist(radius=400, dist=350)
    br.moveLeftAttachmentMotorForDegrees(800)
    # br.turnInPlace(30)
    # br.driveForDistance(40, then=Stop.NONE)
    br.driveArcDist(radius=200,dist=-200, then=Stop.NONE)
    br.driveForDistance(-450)
    br.driveArcDist(radius=-800,dist=500)
    # br.driveArcDist(radius=100,dist=200)
    # br.moveLeftAttachmentMotorForDegrees(800)
# If running this program directly (not from the master program), this is
# how we know it is running directly. In which case, this method will
# create a BaseRobot and run the Run(br) method above.
# In other words, keep these three lines at the bottom of your code and
# everything will be fine.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
