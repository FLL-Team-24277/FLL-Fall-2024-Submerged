from base_robot import *

# Add good comments, such as what the mission is supposed to do,
# how to align the robot in home, any initial starting instructions,
# such as how it should be loaded with anything, arm positions, etc.

###             this is the shark/coral reef


# When we run this program from the master program, we will call this
# "Run(br)" method.
def Run(br: BaseRobot):
    # Your mission code goes here, step-by-step
    # It MUST be indented just like the lines below

    # Shark

    br.driveForDistance(200, wait=False)
    br.curve(150, 40)
    br.curve(150, -40)
    br.driveForDistance(470)
    br.moveRightAttachmentMotorForDegrees(-250, wait=False)
    br.driveForDistance(50)
    br.driveForDistance(-50)
    br.moveLeftAttachmentMotorUntilStalled(90)
    br.waitForMillis(300)
    br.moveLeftAttachmentMotorForDegrees(degrees=-640, wait=False)
    br.moveRightAttachmentMotorForDegrees(250)
    br.turnInPlace(-90)

    # coral nursery
    br.moveLeftAttachmentMotorForDegrees(550)
    br.waitForMillis(300)
    br.waitForMillis(300)
    br.driveForDistance(110,35)
    br.turnInPlace(10)
    br.driveForDistance(-70)
    br.moveLeftAttachmentMotorForDegrees(-480)
    br.moveLeftAttachmentMotorForDegrees(50)
    br.moveLeftAttachmentMotorForDegrees(-50)
    br.turnInPlace(30)

    # to coral reef and scuba diver
    br.turnInPlace(-100)
    br.driveForDistance(-20, wait=False)
    br.driveForDistance(700)
  
    # br.driveForDistance(-100, wait=False)
    # br.turnInPlace(120)
    # br.driveForDistance(40)
    # br.moveRightAttachmentMotorForDegrees(-250)
    # br.waitForMillis(300)
    # br.driveForDistance(20)
    # br.driveArcDist(-700,-730)
  


 

# If running this program directly (not from the master program), this is
# how we know it is running directly. In which case, this method will
# create a BaseRobot and run the Run(br) method above.
# In other words, keep these three lines at the bottom of your code and
# everything will be fine.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
