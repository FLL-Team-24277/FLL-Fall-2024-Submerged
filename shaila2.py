from base_robot import *


def Run(br: BaseRobot):

    br.driveForDistance(-65, speedPct=67)
    br.driveForDistance(115)
    br.waitForForwardButton()
    br.driveForDistance(distance=350, speedPct=25, then=Stop.NONE)
    br.driveArcDist(radius=650, dist=780, speedPct=45, gyro=False)
    br.driveForDistance(-150, speedPct=100, accelerationPct=100)


if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
