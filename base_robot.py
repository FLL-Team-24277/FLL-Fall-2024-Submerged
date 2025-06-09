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
from pybricks import version
from utils import *

# All default constant percentages will be defined here
DEFAULT_MED_MOT_SPEED_PCT = 100  # normal attachment moter speed, % value
DEFAULT_MED_MOT_ACCEL_PCT = 80
DEFAULT_BIG_MOT_SPEED_PCT = 80  # normal wheels moter speed, % value
DEFAULT_BIG_MOT_ACCEL_PCT = 80
DEFAULT_TURN_SPEED_PCT = 45  #
DEFAULT_TURN_ACCEL_PCT = 45  #
DEFAULT_STALL_PCT = 50
# DEFAULT_STALL_PCT = 50  # not currently used


class BaseRobot:
    """
    A collection of methods and Spike Prime for FLL Team 24277. \
    Uses pybricks for most functionality.

    Example:

    >>> from base_robot import *
    >>> br = BaseRobot()
    >>> br.driveForDistance(400) #400mm at default speed
    >>> br.turnInPlace(90) #90 deg to the right
    """

    def __init__(self):
        self.hub: PrimeHub = PrimeHub(top_side=Axis.Z, front_side=-Axis.Y)
        print(version)
        v: int = self.hub.battery.voltage()
        vPct: int = RescaleBatteryVoltage(v)
        print(str(v))
        print(f"Battery voltage %: {vPct / 100 :.2%}")
        self._version: str = "1.0 09/11/2024"
        self.leftDriveMotor: Motor = Motor(Port.E, Direction.COUNTERCLOCKWISE)
        self.rightDriveMotor: Motor = Motor(Port.A)
        self.robot: DriveBase = DriveBase(
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

        self.leftAttachmentMotor: Motor = Motor(Port.B)
        self.rightAttachmentMotor: Motor = Motor(Port.D)
        self.leftAttachmentMotor.control.limits(acceleration=20000)
        self.leftAttachmentMotor.control.limits(acceleration=20000)

        self.colorSensor: ColorSensor = ColorSensor(Port.F)

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
        self.sensorColors: list[Color] = [
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
        self.myColor2DefaultColorDict: dict[Color, Color] = {
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
        degrees: int,
        speedPct: int = DEFAULT_MED_MOT_SPEED_PCT,
        then: Stop = Stop.HOLD,
        wait: bool = True,
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
        millis: int,
        speedPct: int = DEFAULT_MED_MOT_SPEED_PCT,
        then: Stop = Stop.HOLD,
        wait: bool = True,
    ):
        """
        Moves the left attachment motor for a set amount of time

        Snippet: lamt

        Example:

        >>> moveLeftAttachmentMotorForMillis(millis=500, speedPct=50)
        >>> moveLeftAttachmentMotorForMillis(millis=500, then=STOP.BRAKE)
        >>> moveLeftAttachmentMotorForMillis(millis=500, wait=False)

        Args:

        millis (REQUIRED integer, > 0): how many miliseconds the left \
        attachment motor will turn for. A millisecond is 0.001 of a second, \
        so 5000 is 5 seconds.

        speedPct (OPTIONAL integer, -100 to 100, except 0): Controls how fast \
        the motor/motors will move. Positive numbers move the motor right, \
        negative numbers turn it to the left.

        then (OPTIONAL Stop): the then function tells the robot what to do \
        next. Our default is stop.HOLD, which tells the motor that when it \
        stops to hold that position as much as it can.

        wait (OPTIONAL bool): this tells the robot if it should wait for the \
        next line of code or run both lines of code at the same time. \
        Default is True, which means wait on this line until it is \
        complete.

        """
        speed: int = RescaleMedMotSpeed(speedPct)
        self.leftAttachmentMotor.run_time(speed, millis, then, wait)

    def moveLeftAttachmentMotorUntilStalled(
        self,
        speedPct: int = DEFAULT_MED_MOT_SPEED_PCT,
        stallPct: int = DEFAULT_STALL_PCT,
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
        Moves the right attachment motor for a set amount of time

        Example:

        >>> moveRightAttachmentMotorForMillis(millis=500, speedPct=50)
        >>> moveRightAttachmentMotorForMillis(millis=500, then=STOP.BRAKE)
        >>> moveRightAttachmentMotorForMillis(millis=500, wait=False)

        Snippet: ramt

        Args:

        millis (REQUIRED integer, > 0): how many miliseconds the right \
        attachment motor will turn for. A millisecond is 0.001 of a second, \
        so 5000 is 5 seconds.

        speedPct (OPTIONAL integer, -100 to 100, except 0): Controls how fast \
        the motor/motors will move. Positive numbers move the motor right, \
        negative numbers turn it to the left.

        then (OPTIONAL Stop): the then function tells the robot what to do \
        next. Our default is stop.HOLD, which tells the motor that when it \
        stops to hold that position as much as it can.

        wait (OPTIONAL bool): this tells the robot if it should wait for the \
        next line of code or run both lines of code at the same time. \
        Default is True, which means wait on this line until it is \
        complete.

        """
        speed = RescaleMedMotSpeed(speedPct)
        self.rightAttachmentMotor.run_time(speed, millis, then, wait)

    def moveRightAttachmentMotorUntilStalled(
        self, speedPct=DEFAULT_MED_MOT_SPEED_PCT, stallPct=DEFAULT_STALL_PCT
    ):
        """
        Moves the right attachment motor untill it is stalled

        Example:

        >>> moveRightAttachmentMotorUntilStalled() # uses defaults
        >>> moveRightAttachmentMotorUntilStalled(speedPct=20)
        >>> moveRightAttachmentMotorUntilStalled(speedPct=30, stallPct=75)

        Args:

        speedPct (OPTIONAL integer, -100 to 100, except 0): Sets how fast the \
        motor/motors will move.

        stallPct (OPTIONAL integer, 1 to 100): How much torque before \
        stalling. Lower numbers means stalls with less torque.

        """
        speed: int = RescaleMedMotSpeed(speedPct)
        load: int = RescaleMedMotTorque(stallPct)
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
        speed = RescaleStraightSpeed(
            speedPct
        )  # TODO: Ensure speed is positive
        acceleration = RescaleStraightAccel(accelerationPct)
        self.robot.use_gyro(gyro)
        self.robot.settings(acceleration, speed)
        self.robot.straight(distance, then, wait)

    def driveForMillis(
        self,
        millis: int,
        speedPct: int = DEFAULT_BIG_MOT_SPEED_PCT,
        gyro: bool = True,
        accelerationPct: int = DEFAULT_BIG_MOT_ACCEL_PCT,
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
        speed = RescaleStraightSpeed(speedPct)
        acceleration = RescaleStraightAccel(accelerationPct)
        self.robot.use_gyro(gyro)
        self.robot.settings(straight_acceleration=acceleration)
        self.robot.drive(speed, 0)
        wait(millis)
        self.robot.brake()

    # TODO driveUntilStalled() needs comments
    def driveUntilStalled(  # TODO add stall parameter
        self,
        # stallPct=DEFAULT_STALL_PCT,
        # think about above line later
        speedPct=DEFAULT_BIG_MOT_SPEED_PCT,
        gyro=True,
        accelerationPct=DEFAULT_BIG_MOT_ACCEL_PCT,
    ):
        spd = RescaleStraightSpeed(speedPct)
        # print(spd)
        acceleration = RescaleStraightAccel(accelerationPct)
        self.robot.use_gyro(gyro)
        # self.robot.settings(straight_speed=-999)
        self.robot.settings(straight_acceleration=acceleration)
        self.robot.drive(spd, 0)
        while not self.robot.stalled():  # TODO: Change to use stall parameter
            wait(50)
        self.robot.brake()

    # TODO waitForMillis needs comments
    def waitForMillis(self, millis):
        wait(millis)

    # TODO waitForForwardButton() needs comments
    def waitForForwardButton(
        self,
    ):
        while True:
            pressed = self.hub.buttons.pressed()
            if Button.LEFT in pressed:
                break
            wait(10)

    # TODO waitForBackButton() needs comments
    def waitForBackButton(
        self,
    ):
        while True:
            pressed = self.hub.buttons.pressed()
            if Button.RIGHT in pressed:
                break
            wait(10)

    # TODO turnInPlace() needs comments
    def turnInPlace(
        self,
        angle,
        speedPct=DEFAULT_TURN_SPEED_PCT,
        gyro=True,
        wait=True,
        then=Stop.BRAKE,
        accelerationPct=DEFAULT_TURN_ACCEL_PCT,
    ):
        speed = RescaleTurnSpeed(speedPct)  # TODO: Ensure speed is positive
        acceleration = RescaleTurnAccel(accelerationPct)
        self.robot.use_gyro(gyro)
        self.robot.settings(acceleration, speed)
        self.robot.turn(angle, then, wait)

    # TODO curve() needs comments
    def curve(
        self,
        radius,
        angle,
        speedPct=DEFAULT_BIG_MOT_SPEED_PCT,
        then=Stop.BRAKE,
        wait=True,
        gyro=True,
        accelerationPct=DEFAULT_TURN_ACCEL_PCT,  # FIXME: Wrong default
    ):
        """Drive the robot in a curve

        Example:

        >>> curve(radius=350, angle=-60) # curve forward to the left
        >>> curve(radius=170, angle=60, speedPct=40)
        >>> curve(radius=-200, angle=45, wait=False)

        Args:

        radius (REQUIRED, integer): How tight of a curve. POS = Forward; \
        NEG = Reverse

        angle (REQUIRED, integer): Number of degrees to drive along the curve. \
        POS = right; NEG = left

        speedPct (pos integer, optional): How fast to drive. Defaults to \
        DEFAULT_BIG_MOT_SPEED_PCT.

        then (Stop(), optional): What kind of Stop. Defaults to Stop.BRAKE.

        wait (bool, optional): Control whether execution stays on this line \
        until finished or not. Defaults to True, which means stay on this \
        line. wait = False means exection can move on to the next line \
        immediately and not have to wait for it to finish. We often use this \
        to run attachment motors while the robot is driving.

        gyro (bool, optional): Use the gyro. Defaults to True.

        accelerationPct (pos integer, optional): How fast to change speed. \
        Defaults to DEFAULT_TURN_ACCEL_PCT.

        """
        speed = RescaleStraightSpeed(
            speedPct
        )  # TODO: Ensure speed is positive
        acceleration = RescaleTurnAccel(
            accelerationPct
        )  # FIXME: Wrong rescale
        self.robot.use_gyro(gyro)
        self.robot.settings(
            acceleration, speed
        )  # FIXME: Need to set turn_rate & turn_acceleration only
        self.robot.curve(radius, angle, then, wait)

    def driveArcDist(
        self,
        radius,
        dist,
        speedPct=DEFAULT_BIG_MOT_SPEED_PCT,
        accelPct=DEFAULT_BIG_MOT_ACCEL_PCT,
        gyro=True,
        then=Stop.BRAKE,
        wait=True,
    ):
        """Drive the robot in an arc

        Example:

        >>> driveArcDist(radius=350, dist=60) # curve forward to the right
        >>> driveArcDist(radius=170, dist=-160, speedPct=40)
        >>> driveArcDist(radius=-200, dist=45, wait=False, then=Stop.NONE)

        Snippet: dad

        Args:

        radius (REQUIRED, integer): How tight of a curve in mm. POS = curve \
        right; NEG = curve left. Smaller numbers means tighter curve.

        dist (REQUIRED, integer): Number of mm to drive along the curve. \
        POS = forward; NEG = reverse

        speedPct (OPTIONAL, pos integer): How fast to drive. Defaults to \
        DEFAULT_BIG_MOT_SPEED_PCT.

        then (OPTIONAL, Stop()): What kind of Stop. Defaults to Stop.BRAKE. \
        Stop.NONE works great when chaining multiple movements together.

        wait (OPTIONAL, bool): Control whether execution stays on this line \
        until finished or not. Defaults to True, which means stay on this \
        line. wait = False means exection can move on to the next line \
        immediately and not have to wait for it to finish. We often use this \
        to run attachment motors while the robot is driving.

        gyro (OPTIONAL, bool): Use the gyro or not. Defaults to True, which \
        means use the gyro.

        accelPct (OPTIONAL, pos integer): How fast to change speed. \
        Defaults to DEFAULT_TURN_ACCEL_PCT.

        """
        speed = RescaleStraightSpeed(speedPct)
        accel = RescaleStraightAccel(accelPct)
        self.robot.use_gyro(gyro)
        self.robot.settings(straight_speed=speed, straight_acceleration=accel)
        self.robot.arc(radius=radius, distance=dist, then=then, wait=wait)


# This BaseRobot class file is not meant to be run like the mission files.
# But if someone does try (accidentally probably) to run it, show this
# error message.
if __name__ == "__main__":
    print("Don't run the BaseRobot class file. Nothing to do here.")
    print("You probably meant to run one of the mission files.")
