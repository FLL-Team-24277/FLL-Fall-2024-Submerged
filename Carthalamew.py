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
    br.driveArcDist(radius=-450, dist=-450)
    br.waitForForwardButton()
    br.moveLeftAttachmentMotorForDegrees(-500)
    br.driveArcDist(radius=-1000, dist=300, then=Stop.NONE)
    br.driveArcDist(radius=400, dist=350)
    br.moveLeftAttachmentMotorForDegrees(800)
    br.driveArcDist(radius=200, dist=-200, then=Stop.NONE)
    br.driveForDistance(-450)
    # NOM NOM NOM
    br.waitForForwardButton()

    br.driveArcDist(radius=-240, dist=300, then=Stop.NONE)
    br.driveForDistance(170, then=Stop.NONE)
    br.driveArcDist(radius=400, dist=300, then=Stop.NONE)
    br.driveArcDist(radius=-500, dist=280)
    br.driveForDistance(250)
    br.turnInPlace(-40)
    br.driveForDistance(-150)
    br.moveRightAttachmentMotorForDegrees(800)
    br.driveForDistance(300)
    br.moveLeftAttachmentMotorForDegrees(-500)
    br.driveArcDist(radius=-500, dist=500)
    br.driveForDistance(600)


if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
