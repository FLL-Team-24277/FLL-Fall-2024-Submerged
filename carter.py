from base_robot import *


def Run(br: BaseRobot):

    br.driveForDistance(100)
    br.turnInPlace(-40)
    br.driveForDistance(400)


if __name__ == "__main__":
    br: BaseRobot = BaseRobot()
    Run(br)
