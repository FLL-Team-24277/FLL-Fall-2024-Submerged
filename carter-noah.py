from base_robot import *

import Sadie

# Add good comments, such as what the mission is supposed to do,
# how to align the robot in home, any initial starting instructions,
# such as how it should be loaded with anything, arm positions, etc.
# When we run this program from the master program, we will call this
# "Run(br)" method.


def Run(br: BaseRobot):
    br.driveForDistance(400)
    br.driveArcDist(radius=-600, dist=-450)
    br.waitForForwardButton()
    br.moveLeftAttachmentMotorForMillis(1000, speedPct=-100) # open claw
    br.driveArcDist(radius=-1000, dist=300, then=Stop.NONE)
    br.driveArcDist(radius=400, dist=350)
    br.moveLeftAttachmentMotorForMillis(1000, speedPct=100) # close claw
    br.driveArcDist(radius=200, dist=-200, then=Stop.NONE)
    br.driveForDistance(-450)
    # NOM NOM NOM
    br.waitForForwardButton()

    br.driveForDistance(200,then=Stop.NONE)
    br.driveArcDist(-535,800,then=Stop.NONE)
    br.driveForDistance(500)
    br.turnInPlace(-30)
    br.driveForDistance(-250)
    br.moveRightAttachmentMotorForDegrees(-900) # extend the arm
    br.moveLeftAttachmentMotorForMillis(1000, speedPct=-100) # open claw
    br.driveArcDist(1000,500)
    br.turnInPlace(-45)
    br.driveForDistance(800)
    # br.driveArcDist(radius=-535,dist=800)

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
