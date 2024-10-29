from base_robot import *

# Add good comments, such as what the mission is supposed to do,
# how to align the robot in home, any initial starting instructions,
# such as how it should be loaded with anything, arm positions, etc.


# When we run this program from the master program, we will call this
# "Run(br)" method.
def Run(br):
    br.driveForDistance (467, then=Stop.NONE)
    # br.curve(radius=1652, angle=-25, speedPct=120)
    br.driveArcDist (radius=-350, dist=350, speedPct=50)
    br.moveRightAttachmentMotorForDegrees(1800)

    # br.driveForDistance (distance=-20, speedPct=100, then=Stop.NONE)
    br.driveArcDist (radius=-340, dist=-150, speedPct=100, then=Stop.NONE)
    br.driveForDistance (distance=-670, speedPct=80)
    
    # If running this program directly (not from the master program), this is
# how we know it is running directly. In which case, this method will
# create a BaseRobot and run the Run(br) method above.
# In other words, keep these three lines at the bottom of your code and
# everything will be fine.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
