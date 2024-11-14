from base_robot import *

def Run ( br: BaseRobot ) :  
    #   Your mission code goes here, step-by-step
    # It MUST be indented just like the lines below

    br.robot.drive(900, 0)
    br.leftAttachmentMotor.run(900)
    br.rightAttachmentMotor.run(900)

    while(True):
        v = br.hub.battery.voltage()
        print(str(v))
        wait(60000)



# If running this program directly (not from the master program), this is
# how we know it is running directly. In which case, this method will
# create a BaseRobot and run the Run(br) method above.
# In other words, keep these three lines at the bottom of your code and
# everything will be fine.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
