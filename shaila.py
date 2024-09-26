from base_robot import *

# Add good comments, such as what the mission is supposed to do,
# how to align the robot in home, any initial starting instructions,
# such as how it should be loaded with anything, arm positions, etc.


# When we run this program from the master program, we will call this
# "Run(br)" method.
def Run(br: BaseRobot):
    # br.driveForDistance(distance=592, wait=None)
    # br.waitForMillis(1000)
    # br.curve(radius=300, angle=-90)
    # br.driveForDistance (754)
    # br.turnInPlace (-90.9021)
    # br.driveForDistance (200.1046)
    # br.turnInPlace (90.702501)
    # br.moveRightAttachmentMotorForDegrees(-900)

    br.curve(radius=1652, angle=-28.6)
    br.moveRightAttachmentMotorForDegrees(-600)
# sigh i do NOT know. what. is. going. on.
# If running this program directly (not from the master program), this is
# how we know it is running directly. In which case, this method will
# create a BaseRobot and run the Run(br) method above.
# In other words, keep these three lines at the bottom of your code and
# everything will be fine.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
