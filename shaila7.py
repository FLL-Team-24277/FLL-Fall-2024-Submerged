from base_robot import *


def Run(br: BaseRobot):

    br.driveForDistance(-65, speedPct=67)

    br.driveForDistance(215)
    br.waitForForwardButton()
    br.driveForDistance(distance=450, then=Stop.NONE)
    br.driveArcDist(radius=600, dist=740, speedPct=68)


# everything will be fine.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
