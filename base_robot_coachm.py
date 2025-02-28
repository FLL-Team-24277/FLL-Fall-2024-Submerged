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
from pybricks.robotics import DriveBase
from pybricks.hubs import PrimeHub
from pybricks.tools import wait
from utils import *

# All default constant percentages will be defined here
DEFAULT_MED_MOT_SPEED_PCT = 100  # normal attachment moter speed, % value
DEFAULT_MED_MOT_ACCEL_PCT = 80
DEFAULT_BIG_MOT_SPEED_PCT = 80  # normal wheels moter speed, % value
DEFAULT_BIG_MOT_ACCEL_PCT = 80
DEFAULT_TURN_SPEED_PCT = 45  #
DEFAULT_TURN_ACCEL_PCT = 45  #
DEFAULT_DB_STALL_PCT = 50
DEFAULT_MED_MOT_STALL_PCT = 50


class BaseRobot:
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
            RescaleStraightSpeed(DEFAULT_BIG_MOT_SPEED_PCT),
            RescaleStraightAccel(DEFAULT_BIG_MOT_ACCEL_PCT),
            RescaleTurnSpeed(DEFAULT_TURN_SPEED_PCT),
            RescaleTurnAccel(DEFAULT_TURN_ACCEL_PCT),
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
        self.SENSOR_WHITE: Color = Color(h=0, s=0, v=100)  # h=0,s=0,v=100
        self.SENSOR_RED: Color = Color(h=353, s=82, v=92)  # h=0,s=100,v=100
        self.SENSOR_YELLOW: Color = Color(
            h=60, s=60, v=100
        )  # h=60,s=100,v=100
        self.SENSOR_GREEN: Color = Color(
            h=156, s=66, v=66
        )  # h=120,s=100,v=100
        self.SENSOR_BLUE: Color = Color(h=216, s=84, v=83)  # h=240,s=100,v=100
        self.SENSOR_MAGENTA: Color = Color(
            h=333, s=75, v=78
        )  # h=300,s=100,v=100
        self.SENSOR_ORANGE: Color = Color(h=8, s=75, v=100)  # h=30,s=100,v=100
        self.SENSOR_DARKGRAY: Color = Color(h=192, s=21, v=64)  # h=0,s=0,v=50
        self.SENSOR_NONE: Color = Color(h=170, s=26, v=15)  # h=0,s=0,v=0
        self.SENSOR_LIME: Color = Color(h=92, s=55, v=93)  # h=92, s=57, v=93

        # Put the custom colors in a list. Best practice is to only use
        # colors that we are using for actual missions.
        self.sensorColors = [
            self.SENSOR_WHITE,
            self.SENSOR_RED,
            self.SENSOR_YELLOW,
            self.SENSOR_GREEN,
            self.SENSOR_BLUE,
            self.SENSOR_MAGENTA,
            self.SENSOR_ORANGE,
            self.SENSOR_DARKGRAY,
            self.SENSOR_NONE,  # must have SENSOR_NONE. Do not comment
            self.SENSOR_LIME,
        ]

        # Set the detectable colors usisng our list
        self.colorSensor.detectable_colors(self.sensorColors)

        # Translates our costom colors into the default pybricks colors
        # Used to set the hub light to the correct color. It dodesn't
        # matter if there are extra colors in here that won't be detected
        self.myColor2DefaultColorDict = {
            self.SENSOR_GREEN: Color.GREEN,
            self.SENSOR_RED: Color.RED,
            self.SENSOR_YELLOW: Color.YELLOW,
            self.SENSOR_BLUE: Color.BLUE,
            self.SENSOR_MAGENTA: Color.MAGENTA,
            self.SENSOR_WHITE: Color.WHITE,
            self.SENSOR_ORANGE: Color.ORANGE,
            self.SENSOR_DARKGRAY: Color.GRAY,
            self.SENSOR_NONE: Color.NONE,
            self.SENSOR_LIME: Color.CYAN,
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
        speedPct=DEFAULT_MED_MOT_SPEED_PCT,
        stallPct=DEFAULT_MED_MOT_STALL_PCT,
    ):
        speed = RescaleMedMotSpeed(speedPct)
        load = RescaleMedMotTorque(stallPct)
        self.leftAttachmentMotor.run(speed)
        while abs(self.leftAttachmentMotor.load()) < load:
            wait(25)
        self.leftAttachmentMotor.hold()

    def moveRightAttachmentMotorForDegrees(
        self,
        degrees,
        speedPct=DEFAULT_MED_MOT_SPEED_PCT,
        then=Stop.HOLD,
        wait=True,
    ):
        speed = RescaleMedMotSpeed(speedPct)
        self.rightAttachmentMotor.run_angle(speed, degrees, then, wait)

    def moveRightAttachmentMotorForMillis(
        self,
        millis,
        speedPct=DEFAULT_MED_MOT_SPEED_PCT,
        then=Stop.HOLD,
        wait=True,
    ):
        speed = RescaleMedMotSpeed(speedPct)
        self.rightAttachmentMotor.run_angle(speed, millis, then, wait)

    def moveRightAttachmentMotorUntilStalled(
        self,
        speedPct=DEFAULT_MED_MOT_SPEED_PCT,
        stallPct=DEFAULT_MED_MOT_STALL_PCT,
    ):
        speed = RescaleMedMotSpeed(speedPct)
        load = RescaleMedMotTorque(stallPct)
        self.rightAttachmentMotor.run(speed)
        while abs(self.rightAttachmentMotor.load()) < load:
            wait(25)
        self.rightAttachmentMotor.hold()

    def driveForDistance(
        self,
        distance,
        speedPct=DEFAULT_BIG_MOT_SPEED_PCT,
        then=Stop.BRAKE,
        wait=True,
        gyro=True,
        accelerationPct=DEFAULT_BIG_MOT_ACCEL_PCT,
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
        accelerationPct=DEFAULT_BIG_MOT_ACCEL_PCT,
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
        stallPct=DEFAULT_DB_STALL_PCT,
        speedPct=DEFAULT_BIG_MOT_SPEED_PCT,
        gyro=True,
        accelerationPct=DEFAULT_BIG_MOT_ACCEL_PCT,
    ):
        spd = RescaleMedMotSpeed(speedPct)
        # print(spd)
        acceleration = RescaleStraightAccel(accelerationPct)
        load = RescaleDbTorque(stallPct)
        self.robot.use_gyro(gyro)
        # self.robot.settings(straight_speed=-999)
        self.robot.settings(straight_acceleration=acceleration)
        self.robot.drive(spd, 0)
        # while not self.robot.stalled():
        while (
            abs(self.leftDriveMotor.load()) < load
            and abs(self.rightDriveMotor.load()) < load
        ):
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
        accelerationPct=DEFAULT_BIG_MOT_ACCEL_PCT,
    ):
        speed = RescaleStraightSpeed(speedPct)
        acceleration = RescaleStraightAccel(accelerationPct)
        self.robot.use_gyro(gyro)
        # self.robot.settings(acceleration, speed, 150, 360)
        self.robot.settings(turn_acceleration=acceleration, turn_rate=speed)
        self.robot.curve(radius, angle, then, wait)
