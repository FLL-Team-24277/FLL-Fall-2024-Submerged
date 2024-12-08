from base_robot import *


def Run(br: BaseRobot):

    br.driveForDistance(-65, speedPct=67)
    br.driveForDistance(115)
    br.waitForForwardButton()
    br.driveForDistance(distance=450, then=Stop.NONE)
    br.driveArcDist(radius=650, dist=740, speedPct=68, gyro=False)
    br.driveForDistance(-100)


if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
