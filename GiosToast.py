from base_robot import *

# Add    good comments, such as what the mission is supposed to do,
# how to align the robot in home, any initial starting instructions,
# such as how it should be loaded with anything, arm positions, etc.
# When we run this program from the master program, we will call this
    #"Run(br)" method.
def Run(br: BaseRobot):
    # Your mission code goes here, step-by-step
 
    # It MUST be indented just like the lines below
    
    br.driveForDistance(345, speedPct=50, then=Stop.NONE)
    br.driveArcDist(radius=750, dist=150, speedPct=50, then=Stop.NONE)
    br.driveArcDist(radius=-800, dist=180, speedPct=50, then=Stop.NONE)
    br.driveForDistance(300, speedPct=50)
    br.moveRightAttachmentMotorForDegrees(-70)  
    br.driveForDistance(-180)
    br.moveRightAttachmentMotorForDegrees(200)
    br.moveRightAttachmentMotorForDegrees(-200)   
    br.turnInPlace(-40)
    br.driveForDistance(325)
    br.turnInPlace(-15)
    br.driveForDistance(275)
    br.moveRightAttachmentMotorForDegrees(150)
    br.driveForDistance(-240)
    br.moveLeftAttachmentMotorForDegrees(-150)
    br.driveForDistance(-400)
    br.driveArcDist(radius=-200, dist=550, then=Stop.NONE)
    br.driveForDistance(600,100)




    # If running this pogram directly (not from the master program), this is
# how we know it is running directly. In which case, this method will
# create a BaseRobot and run the Run(br) method above.
# In other words, keep these three lines at the bottom of your code and
# everything will be fine-.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
