from base_robot import *

# Add good comments, such as what the mission is supposed to do,
# how to align the robot in home, any initial starting instructions,
# such as how it should be loaded with anything, arm positions, etc.
# When we run this program from the master program, we will call this
# "Run(br)" method.

def Run(br: BaseRobot):
<<<<<<< HEAD
    Your mission code goes here, step-by-step
    It MUST be indented just like the lines below
    br.driveForDistance(distance=250)
    br.turnInPlace(-50)
    br.moveRightAttachmentMotorForDegrees(degrees=-115)
    br.driveForDistance(200)
    br.turnInPlace(-60)
    br.driveForDistance(185)
    br.turnInPlace(73)
    br.driveForDistance(310 )
    br.moveRightAttachmentMotorForDegrees(degrees=150)
    br.turnInPlace(-35)
    br.driveForDistance(500)
    br.moveRightAttachmentMotorForDegrees(-100)
    br.turnInPlace(125)
    br.driveForDistance(170)
    br.moveRightAttachmentMotorForDegrees(150)

=======
    # Your mission code goes here, step-by-step
    # It MUST be indented just like the lines below

    br.driveForDistance(distance=250)
    br.turnInPlace(-50)
    br.moveRightAttachmentMotorForDegrees(degrees=-150, speedPct=45)
    br.driveForDistance(200)
    br.turnInPlace(-60)
    br.driveForDistance(185)
    br.turnInPlace(70)
    br.driveForDistance(300)
    br.moveRightAttachmentMotorForDegrees(degrees=150)
    br.turnInPlace(-20)
    br.driveForDistance(500)
    br.turnInPlace(120)
    br.driveForDistance(750)
    # br.driveForDistance(distance=250)
    # br.turnInPlace(-50)
    # br.moveRightAttachmentMotorForDegrees(degrees=-115)
    # br.driveForDistance(200)
    # br.turnInPlace(-60)
    # br.driveForDistance(185)
    # br.turnInPlace(73)
    # br.driveForDistance(310 )
    # br.moveRightAttachmentMotorForDegrees(degrees=150)
    # br.turnInPlace(-35)
    # br.driveForDistance(500)
    # br.moveRightAttachmentMotorForDegrees(-100)
    # br.turnInPlace(125)
    # br.driveForDistance(170)
>>>>>>> a2581a00605db56de3761fc4045068437ed59f43
# If running this program directly (not from the master program), this is
# how we know it is running directly. In which case, this method will
# create a BaseRobot and run the Run(br) method above.
# In other words, keep these three lines at the bottom of your code and
# everything will be fine.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
