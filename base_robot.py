from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import (
    Port,
    Direction,
    Axis,
    Side,
    Stop,
    Color,
    Button,
    Icon,
)
from pybricks.robotics import GyroDriveBase
from pybricks.hubs import PrimeHub
from pybricks.tools import wait
from utils import *

# All constents will be defined here

TIRE_DIAMETER = 56  # mm
AXLE_TRACK = 103  # distance between the wheels, mm
STRAIGHT_SPEED = 400  # normal straight speed for driving, mm/sec
DEFAULT_MED_MOT_SPEED_PCT = 100  # normal attachment moter speed, % value
DEFAULT_BIG_MOT_SPEED_PCT = 80  # normal wheels moter speed, % value
STRAIGHT_ACCEL = 600  # normal acceleration, mm/sec^2
TURN_RATE = 150  # normal turning rate, deg/sec
TURN_ACCEL = 360  # normal turning acceleration, deg/sec^2
DEF_ROBOT_ACCELERATION = 75  # normal acceleration
DEFAULT_STALL_PCT = 50  # normal
DEFAULT_TURN_SPEED_PCT = 45  #
DEFAULT_TURN_ACCEL_PCT = 45  #
DEFAULT_DUTY_LIMIT = 50


class BaseRobot:
    """
    A collection of methods and Spike Prime for FLL Team 24277. \
    Uses pybricks for most functionality.

    Example:

    >>> from base_robot import *
    >>> br = BaseRobot()
    >>> br.GyroDrive(400) #400mm at default speed
    >>> br.GyroTurn(90) #90 deg to the right
    """

    def __init__(self):
        self.hub = PrimeHub(top_side=Axis.Z, front_side=-Axis.Y)
        self._version = "0.1 05/19/2023"
        self.leftDriveMotor = Motor(Port.E, Direction.COUNTERCLOCKWISE)
        self.rightDriveMotor = Motor(Port.A)
        self.robot = GyroDriveBase(
            self.leftDriveMotor,
            self.rightDriveMotor,
            TIRE_DIAMETER,
            AXLE_TRACK,
        )
        # default speeds were determined by testing
        self.robot.settings(
            STRAIGHT_SPEED, STRAIGHT_ACCEL, TURN_RATE, TURN_ACCEL
        )
        self.leftAttachmentMotor = Motor(Port.B)
        self.rightAttachmentMotor = Motor(Port.D)
        self.leftAttachmentMotor.control.limits(acceleration=20000)
        self.leftAttachmentMotor.control.limits(acceleration=20000)

        self.colorSensor = ColorSensor(Port.F)

        # HSV values were found by testing. Default hsv-values are provided
        # in comments. Theoretically, the farther apart the hsv-values are,
        # the less likely two colors can get "confused"
        # Use the colorTest.py program to get the color sensor values
        Color.SENSOR_WHITE = Color(h=0, s=0, v=100)  # h=0,s=0,v=100
        Color.SENSOR_RED = Color(h=353, s=82, v=92)  # h=0,s=100,v=100
        Color.SENSOR_YELLOW = Color(h=60, s=60, v=100)  # h=60,s=100,v=100
        Color.SENSOR_GREEN = Color(h=156, s=66, v=66)  # h=120,s=100,v=100
        Color.SENSOR_BLUE = Color(h=216, s=84, v=83)  # h=240,s=100,v=100
        Color.SENSOR_MAGENTA = Color(h=333, s=75, v=78)  # h=300,s=100,v=100
        Color.SENSOR_ORANGE = Color(h=8, s=75, v=100)  # h=30,s=100,v=100
        Color.SENSOR_DARKGRAY = Color(h=192, s=21, v=64)  # h=0,s=0,v=50
        Color.SENSOR_NONE = Color(h=170, s=26, v=15)  # h=0,s=0,v=0
        Color.SENSOR_LIME = Color(h=92, s=55, v=93)  # h=92, s=57, v=93

        # Put the custom colors in a list. Best practice is to only use
        # colors that we are using for actual missions.
        self.sensorColors = [
            Color.SENSOR_WHITE,
            Color.SENSOR_RED,
            Color.SENSOR_YELLOW,
            Color.SENSOR_GREEN,
            Color.SENSOR_BLUE,
            Color.SENSOR_MAGENTA,
            Color.SENSOR_ORANGE,
            Color.SENSOR_DARKGRAY,
            Color.SENSOR_NONE,  # must have SENSOR_NONE. Do not comment
            Color.SENSOR_LIME,
        ]

        # Set the detectable colors usisng our list
        self.colorSensor.detectable_colors(self.sensorColors)

        # Translates our costom colors into the default pybricks colors
        # Used to set the hub light to the correct color. It dodesn't
        # matter if there are extra colors in here that won't be detected
        self.myColor2DefaultColorDict = {
            Color.SENSOR_GREEN: Color.GREEN,
            Color.SENSOR_RED: Color.RED,
            Color.SENSOR_YELLOW: Color.YELLOW,
            Color.SENSOR_BLUE: Color.BLUE,
            Color.SENSOR_MAGENTA: Color.MAGENTA,
            Color.SENSOR_WHITE: Color.WHITE,
            Color.SENSOR_ORANGE: Color.ORANGE,
            Color.SENSOR_DARKGRAY: Color.GRAY,
            Color.SENSOR_NONE: Color.NONE,
            Color.SENSOR_LIME: Color.CYAN,
        }

    def moveLeftAttachmentMotorForDegrees(
        self,
        degrees,
        speedPct=DEFAULT_MED_MOT_SPEED_PCT,
        then=Stop.HOLD,
        wait=True,
    ):
        """
        moveLeftAttachmentMotorForDegrees moves the left attachment motor. \
        to determine hoow much the motor moves you put in a number \
        positive numbers make it go right negative numbers left. \
        Paramaters:
        -------------
        degrees: how much the left attachment motor will turn \
        positive numbers move the motor right \
        negative numbers turn it to the left \
        -------------
        speedPct: this controls how fast the motors will move \
        the speed is from 1-100 \
        -------------
        then: the then function tells the robot what to do next \
        our default is stop.HOLD \
        stop.HOLD tells the robot that when it stops to hold that position \
        -------------
        wait: this tells the robot if it should wait for the next step \
        or run both lines of code at the same time
         """
        # now the real work begins!
        speed = RescaleMedMotSpeed(speedPct)
        self.leftAttachmentMotor.run_angle(speed, degrees, then, wait)

    def moveLeftAttachmentMotorForMillis(
        self,
        millis,
        speedPct=DEFAULT_MED_MOT_SPEED_PCT,
        then=Stop.HOLD,
        wait=True,
    ):
        """
        moveLeftAttachmentMotorForMillis moves the left attachment motor. \
        to determine how long the motor moves for you put in a number \
        that number is how many miliseconds it will run for \
        Paramaters:
        -------------
        millis: how many miliseconds the left attachment motor will turn for\
        a millisecond is 0.001 of a second \
        so 5000 is 5 seconds \
        -------------
        speedPct: this controls how fast the motor/motors will move \
        the speed percent is from -100 to 100 \
        you can not put in zero though \
        positive numbers move the motor right \
        negative numbers turn it to the left \
        -------------
        then: the then function tells the robot what to do next \
        our default is stop.HOLD \
        stop.HOLD tells the robot that when it stops \
        to hold that position as much as it can \
        -------------
        wait: this tells the robot if it should wait \
        for the next line of code or \
        run both lines of code at the same time
        """
        speed = RescaleMedMotSpeed(speedPct)
        self.leftAttachmentMotor.run_angle(speed, millis, then, wait)

    def moveLeftAttachmentMotorUntilStalled(
        self,
        speedPct=DEFAULT_MED_MOT_SPEED_PCT,
    ):
        """
        moveLeftAttachmentMotorUntillStalled moves \
        the left attachment motor untill it is stalled \
        Paramaters:
        -------------
        speedPct: this controls how fast the motor/motors will move \
        the speed percent is from -100 to 100 \
        you can not put in zero \
        positive numbers move the motor right \
        negative numbers turn it to the left \
        """

        speed = RescaleMedMotSpeed(speedPct)
        self.leftAttachmentMotor.run(speed)
        while not (self.leftAttachmentMotor.stalled()):
            wait(25)
        self.leftAttachmentMotor.hold()

    def moveRightAttachmentMotorForDegrees(
        self,
        degrees,
        speedPct=DEFAULT_MED_MOT_SPEED_PCT,
        then=Stop.HOLD,
        wait=True,
    ):
        """
        moveRightAttachmentMotorForDegrees moves the right attachment motor. \
        to determine hoow much the motor moves you put in a number \
        positive numbers make it go right negative numbers left. \
        Paramaters:
        -------------
        degrees: how much the right attachment motor will turn \
        positive numbers move the motor right \
        negative numbers turn it to the left \
        -------------
        speedPct: this controls how fast the motors will move \
        the speed is from 1-100 \
        -------------
        then: the then function tells the robot what to do next \
        our default is stop.HOLD \
        stop.HOLD tells the robot that when it stops to hold that position \
        -------------
        wait: this tells the robot if it should wait for the next step \
        or run both lines of code at the same time
         """
        # now the real work begins!
        speed = RescaleMedMotSpeed(speedPct)
        self.rightAttachmentMotor.run_angle(speed, degrees, then, wait)

    def moveRightAttachmentMotorForMillis(
        self,
        millis,
        speedPct=DEFAULT_MED_MOT_SPEED_PCT,
        then=Stop.HOLD,
        wait=True,
    ):
        """
        moveRightAttachmentMotorForMillis moves the right attachment motor. \
        to determine how long the motor moves for you put in a number \
        that number is how many miliseconds it will run for \
        Paramaters:
        -------------
        millis: how many miliseconds the right attachment motor will turn for\
        a millisecond is 0.001 of a second \
        so 5000 is 5 seconds \
        -------------
        speedPct: this controls how fast the motor/motors will move \
        the speed percent is from -100 to 100 \
        you can not put in zero though \
        positive numbers move the motor right \
        negative numbers turn it to the left \
        -------------
        then: the then function tells the robot what to do next \
        our default is stop.HOLD \
        stop.HOLD tells the robot that when it stops \
        to hold that position as much as it can \
        -------------
        wait: this tells the robot if it should wait \
        for the next line of code or \
        run both lines of code at the same time
        """
        speed = RescaleMedMotSpeed(speedPct)
        self.rightAttachmentMotor.run_angle(speed, millis, then, wait)

    def moveRightAttachmentMotorUntilStalled(
        self,
        speedPct=DEFAULT_MED_MOT_SPEED_PCT,
    ):
        """
        moveRightAttachmentMotorUntillStalled moves \
        the right attachment motor untill it is stalled \
        Paramaters:
        -------------
        speedPct: this controls how fast the motor/motors will move \
        the speed percent is from -100 to 100 \
        you can not put in zero \
        positive numbers move the motor right \
        negative numbers turn it to the left \
        """
        speed = RescaleMedMotSpeed(speedPct)
        self.rightAttachmentMotor.run(speed)
        while not (self.rightAttachmentMotor.stalled()):
            wait(25)
        self.rightAttachmentMotor.hold()

    def driveForDistance(
        self,
        distance,
        speedPct=DEFAULT_BIG_MOT_SPEED_PCT,
        then=Stop.BRAKE,
        wait=True,
        gyro=True,
        accelerationPct=DEF_ROBOT_ACCELERATION,
    ):
        """
        driveForDistance moves \
        the robot forward a certain amount \
        Paramaters:
        -------------
        distance: how far forward the robot will move \
        positive numbers move it forward \
        and negative numbers move the robot backward \
        -------------
        speedPct: this controls how fast the robot will move \
        the speed percent is from -100 to 100 \
        the code will not let you put in zero \
        positive numbers move the robot forward \
        negative numbers move the robot backward \
        -------------
        then: this function tells the robot what to do \
        after the current line of code is done running \
        our default for then is stop.BRAKE \
        stop.BRAKE tells the robot that when it stops \
        to stop and then dont do anything \
        untill the next line of code \
        -------------
        wait: this tells the robot if it should wait \
        for the next line of code or \
        run both lines of code at the same time
        -------------
        gyro: gyro is used most of the time during our code \
        this function gives us the option to turn off gyro \
        if we need to for some reason \
        gyro is a tool that looks at whats in front of it \
        and as the robot is moving gyro will make sure that \
        the robot is more acurate than before \
        -------------
        accelerationPct: this function tells the robot \
        how much acceleration the robot will have \
        while it is driving \
        the acceleration is on a 1-100 scale \
        """
        speed = RescaleMedMotSpeed(speedPct)
        acceleration = RescaleStraightAccel(accelerationPct)
        self.robot.use_gyro(gyro)
        self.robot.settings(acceleration, speed)
        self.robot.straight(distance, then, wait)

    def driveForMillis(
        self,
        millis,
        speedPct=DEFAULT_BIG_MOT_SPEED_PCT,
        gyro=True,
        accelerationPct=DEF_ROBOT_ACCELERATION,
    ):
        """
        driveForMillis moves \
        the robot forward for a certain amount of time \
        Paramaters:
        -------------
        Millis: how long the robot will move for \
        the time is measures in milliseconds \
        so 5000 would be 5 seconds
        -------------
        speedPct: this controls how fast the robot will move \
        the speed percent is from -100 to 100 \
        the code will not let you put in zero \
        positive numbers will move the robot forward \
        and negative numbers backward \
        -------------
        then: the function then lets the robot know \
        what to do after running the line of code \
        Our default for then is stop.BRAKE \
        stop.BRAKE tells the robot that when it stops \
        to stop and then dont do anything \
        untill the next line of code \
        -------------
        # waaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaait: this tells the robot if it should wait \
        for the next line of code or \
        run both lines of code at the same time
        -------------
        gyro: gyro is used most of the time during our code \
        this function gives us the option to turn off gyro \
        if we need to for some reason \
        gyro is  \
        -------------
        accelerationPct: this function tells the robot \
        how much acceleration the robot will have \
        while it is driving \
        the acceleration is on a 1-100 scale \
        """
        speed = RescaleMedMotSpeed(speedPct)
        acceleration = RescaleStraightAccel(accelerationPct)
        self.robot.use_gyro(gyro)
        self.robot.settings(straight_acceleration=acceleration)
        self.robot.drive(speed, 0)
        wait(millis)
        self.robot.brake()

    def driveUntilStalled(
        self,
        # stallPct=DEFAULT_STALL_PCT,
        # think about above line later
        speedPct=DEFAULT_BIG_MOT_SPEED_PCT,
        gyro=True,
        accelerationPct=DEF_ROBOT_ACCELERATION,
    ):
        spd = RescaleMedMotSpeed(speedPct)
        print(spd)
        acceleration = RescaleStraightAccel(accelerationPct)
        self.robot.use_gyro(gyro)
        # self.robot.settings(straight_speed=-999)
        self.robot.settings(straight_acceleration=acceleration)
        self.robot.drive(spd, 0)
        while not self.robot.stalled():
            wait(50)
        self.robot.brake()

    def waitForMillis(self, millis):
        wait(millis)

    def waitForForwardButton(
        self,
    ):
        while True:
            pressed = self.hub.buttons.pressed()
            if Button.LEFT in pressed:
                break
            wait(10)

    def waitForBackButton(
        self,
    ):
        while True:
            pressed = self.hub.buttons.pressed()
            if Button.RIGHT in pressed:
                break
            wait(10)

    def turnInPlace(
        self,
        angle,
        speedPct=DEFAULT_TURN_SPEED_PCT,
        gyro=True,
        wait=True,
        then=Stop.BRAKE,
        accelerationPct=DEFAULT_TURN_ACCEL_PCT,
    ):
        speed = RescaleTurnSpeed(speedPct)
        acceleration = RescaleTurnAccel(accelerationPct)
        self.robot.use_gyro(gyro)
        self.robot.settings(acceleration, speed)
        self.robot.turn(angle, then, wait)

    def curve(
        self,
        radius,
        angle,
        speedPct=DEFAULT_BIG_MOT_SPEED_PCT,
        then=Stop.BRAKE,
        wait=True,
        gyro=True,
        accelerationPct=DEFAULT_TURN_ACCEL_PCT,
    ):
        speed = RescaleTurnSpeed(speedPct)
        acceleration = RescaleTurnAccel(accelerationPct)
        self.robot.use_gyro(gyro)
        self.robot.settings(acceleration, speed)
        self.robot.curve(radius, angle, then, wait)
