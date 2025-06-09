TIRE_DIAMETER: int = 56  # mm
AXLE_TRACK: int = 103  # distance between the wheels, mm

# Drivebase parameters. None of these should ever be changed by users
if TIRE_DIAMETER == 56:
    DB_MAX_SPEED_MMSEC: int = 488
if TIRE_DIAMETER == 88:
    DB_MAX_SPEED_MMSEC: int = 768

# Straight Acceleration constants
# Anything above 800 mm/sec^2 causes wheel slippage, regardless of the
# tire size. The mass of the 56 and 88mm robots is about the same, so the
# force to maintain that acceleration is the same
# For 56mm, the maximum that can be set in the settings() command is 9775.
# For 88mm, the maximum that can be set in the settings() command is 15360.
DB_MAX_ACCEL_MMSEC2: int = 800

# For turn rates, the best speed and acceleration was determined by testing
# It did not matter if it was on 56mm or 88mm tires, the values were the
# same for both. 180 deg/sec for speed and 360 deg/sec^2 for acceleration
# For 56mm, the maximum speed that can be set in the settings() command is 543
# For 88mm, the maximum speed that can be set in the settings() command is 854.
# For 88mm, the maximum accel that can be set in the settings() command is 17094.
DB_MAX_TURN_RATE_DEGSEC: int = 180
DB_MAX_TURN_ACCEL_DEGSEC2: int = 360

AXLE_TRACK: int = 103  # distance between the wheels, mm

# The drivebase can accept speeds down to zero, but is not very efficient and
# quite erratic. Realistically, 30 is a good minimum speed
DB_MIN_SPEED_MMSEC: int = 30

# Lowest usable accelleration, determined by testing
DB_MIN_ACCEL_MMSEC2: int = 5

# Max and min turning speeds, determined by testing
# These are not affected by the tire size
DB_MIN_TURN_RATE_DEGSEC: int = 20
DB_MIN_TURN_ACCEL_DEGSEC2: int = 10

# Not sure how these are used
DB_ABS_MAX_TORQUE_MNM: int = 700  # milli-newton-meters
DB_ABS_MIN_TORQUE_MNM: int = 20  # milli-newton-meters

# Large Motor usable parameters
LG_MOT_MAX_VOLTAGE: int = 9000  # mV
LG_MOT_MIN_VOLTAGE: int = 3000  # mV
LG_MOT_MAX_TORQUE: int = 560

# Medium Motor usable parameters
MED_MOT_MAX_SPEED_DEGSEC: int = 1000
# MED_MOT_MAX_ACCEL_DEGSEC2 = 20000
# MED_MOT_MIN_ACCEL_DEGSEC2 = 50
MED_MOT_MIN_SPEED_DEGSEC: int = 100
MED_MOT_MAX_TORQUE: int = 195  # milli-newton-meters
MED_MOT_MIN_TORQUE: int = 50  # milli-newton-meters


def Rescale(
    val: int, in_min: int, in_max: int, out_min: int, out_max: int
) -> int:
    neg: int = int(val / abs(val))  # will either be 1 or -1
    val = abs(val)
    if in_max == in_min:
        return 0
    if val < in_min:
        val = in_min
    if val > in_max:
        val = in_max
    retVal: int = out_min + (val - in_min) * int(
        (out_max - out_min) / (in_max - in_min)
    )
    if retVal > out_max:
        retVal = out_max
    if retVal < out_min:
        retVal = out_min
    return retVal * neg


def RescaleStraightSpeed(speedPct) -> int:
    return Rescale(
        speedPct,
        1,
        100,
        DB_MIN_SPEED_MMSEC,
        DB_MAX_SPEED_MMSEC,
    )


def RescaleStraightAccel(accelPct) -> int:
    return Rescale(
        accelPct,
        1,
        100,
        DB_MIN_ACCEL_MMSEC2,
        DB_MAX_ACCEL_MMSEC2,
    )


def RescaleTurnSpeed(turnSpeedPct) -> int:
    # print(turnSpeedPct)
    return Rescale(
        turnSpeedPct,
        1,
        100,
        DB_MIN_TURN_RATE_DEGSEC,
        DB_MAX_TURN_RATE_DEGSEC,
    )


def RescaleTurnAccel(turnAccelPct) -> int:
    return Rescale(
        turnAccelPct,
        1,
        100,
        DB_MIN_TURN_ACCEL_DEGSEC2,
        DB_MAX_TURN_ACCEL_DEGSEC2,
    )


def RescaleMedMotSpeed(medMotSpeedPct) -> int:
    return Rescale(
        medMotSpeedPct,
        1,
        100,
        MED_MOT_MIN_SPEED_DEGSEC,
        MED_MOT_MAX_SPEED_DEGSEC,
    )


def RescaleMedMotTorque(medMotTorquePct) -> int:
    return Rescale(
        medMotTorquePct,
        1,
        100,
        MED_MOT_MIN_TORQUE,
        MED_MOT_MAX_TORQUE,
    )


def RescaleDbTorque(dbTorquePct) -> int:
    return Rescale(
        dbTorquePct,
        1,
        100,
        DB_ABS_MIN_TORQUE_MNM,
        DB_ABS_MAX_TORQUE_MNM,
    )


def RescaleConvertFarToCel(DegF) -> int:
    return Rescale(DegF, 0, 212, -18, 100)


def RescaleMedMotDutyLimit(medMotDutyLimitPct) -> int:
    return Rescale(
        medMotDutyLimitPct,
        1,
        100,
        5,
        195,
    )


def RescaleSensitivity(sens) -> int:
    return Rescale(
        sens,
        1,
        100,
        1,
        12,
    )


def RescaleBatteryVoltage(volts) -> int:
    return Rescale(volts, 7000, 8000, 0, 100)
