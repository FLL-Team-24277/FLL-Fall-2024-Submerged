from base_robot import BaseRobot


def Run(br: BaseRobot):

    br.driveForDistance(-65, speedPct=67)

    br.driveForDistance(215)
    br.waitForForwardButton()
    br.driveForDistance(distance=450)
    br.driveArcDist(radius=600, dist=822, speedPct=68, gyro=False)


# everything will be fine.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
