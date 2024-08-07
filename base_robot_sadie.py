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
from utils import *
from pybricks.robotics import DriveBase
from pybricks.hubs import PrimeHub
from pybricks.tools import wait

# All constents will be defined here
TIRE_DIAMETER = 56  # mm
AXLE_TRACK = 103  # distance between the wheels, mm
DEFAULT_STALL = 120
STRAIGHT_SPEED = 400  # normal straight speed for driving, mm/sec
DEFAULT_MED_MOT_SPEED_PCT = 100  # normal attachment moter speed, % value
DEFAULT_BIG_MOT_SPEED_PCT = 80  # normal wheels moter speed, % value
STRAIGHT_ACCEL = 600  # normal acceleration, mm/sec^2
TURN_RATE = 150  # normal turning rate, deg/sec
TURN_ACCEL = 360  # normal turning acceleration, deg/sec^2
DEF_ROBOT_ACCELERATION = 75  # normal acceleration
DEFAULT_STALL_PCT = 50  #normal
DEFAULT_TURN_SPEED_PCT = 45 #
DEFAULT_TURN_ACCEL_PCT = 45 #


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
        self.robot = DriveBase(
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
        speed = RescaleMedMotSpeed(speedPct)
        self.leftAttachmentMotor.run_angle(speed, degrees, then, wait)

    def moveLeftAttachmentMotorForMillis(
        self,
        millis,
        speedPct=DEFAULT_MED_MOT_SPEED_PCT,
        then=Stop.HOLD,
        wait=True,
    ):
        speed = RescaleMedMotSpeed(speedPct)
        self.leftAttachmentMotor.run_angle(speed, millis, then, wait)

    def moveLeftAttachmentMotorUntilStalled(
        self,
        duty_limit_pct,
        speedPct=DEFAULT_MED_MOT_SPEED_PCT,
        then=Stop.HOLD,
    ):
        speed = RescaleMedMotSpeed(speedPct)
        duty_limit_pct = RescaleMedMotDutyLimit(duty_limit_pct)
        self.leftAttachmentMotor.run_until_stalled(speed, then, duty_limit_pct)

    def driveForDistance(
        self,
        distance,
        speedPct=DEFAULT_BIG_MOT_SPEED_PCT,
        then=Stop.BRAKE,
        wait=True,
        gyro=True,
        accelerationPct=DEF_ROBOT_ACCELERATION,
    ):
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
        degrees,
        speedPct=DEFAULT_TURN_SPEED_PCT,
        gyro=True,
        wait=True,
        then=Stop.BRAKE,
        accelerationPct=DEFAULT_TURN_ACCEL_PCT
    ):
        speed = RescaleMedMotSpeed(speedPct)
        acceleration = RescaleTurnAccel(accelerationPct)
        self.robot.use_gyro(gyro)
        self.robot.settings(acceleration, speed)
        self.robot.straight(degrees, then, wait)

# Finish this if you can ^
#also start doing comments like  this