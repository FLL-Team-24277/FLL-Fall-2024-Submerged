""" program to show the battery voltage and current consumed over time
    Simplified arithmetic so this can also run on the movehub
    Updates: 2025-02-12 /BL
    Report a status change each 10 seconds but keep reporting each 30 seconds
    Show on ech message if there was an error status before
"""

from pybricks import version
from pybricks.hubs import ThisHub

# from pybricks.pupdevices import Motor, Light
from pybricks.tools import wait, StopWatch
from pybricks.parameters import Color  # Port
from my_functions_battery import report_git_hash

print(f"version {version}")
hw_type = version[0]
hub = ThisHub()

if hw_type in ["cityhub", "essentialhub", "movehub", "technichub"]:
    pass
elif hw_type in ["inventorhub", "primehub"]:  # aliases == the same firmware
    hub.display.off()
else:
    raise Exception(
        "Unknown hub " + hw_type
    )  # pylint: disable=E0602  # Undefined variable
print(hw_type, "loaded\n \t Battery voltage:", hub.battery.voltage(), "mV")
githash_report = report_git_hash()
parts = githash_report.split("'")  # Split on apostrophes
git_hash = parts[1].split()[
    0
]  # Take the first word from the second part; split on blank space
print("\t", githash_report)

DEBUG = False
# DEBUG = True
INTERVAL_MS = 30 * 1000  # 30 seconds in mSec
charger = None

if hw_type in ["technichub", "cityhub", "movehub"]:
    # max 6 * 1.2 Volt?
    BAT_HI = 8000  # mVolt
    BAT_MED = 7000  # mVolt
    BAT_LOW = 6000  # mVolt
    BAT_OUT = 5500  # mVolt
else:
    # Prime hub complains sooner?
    BAT_HI = 8400  # mVolt
    BAT_MED = 8000  # mVolt
    BAT_LOW = 7000  # mVolt
    BAT_OUT = 6250  # mVolt

# try:
#     std_dc = 90
#     ma = Motor(Port.A)
#     ma.dc(std_dc)
#     mb = Motor(Port.B)
#     mb.dc(std_dc)
#     mc = Motor(Port.C)
#     mc.dc(std_dc)
#     md = Motor(Port.D)
#     md.dc(std_dc)
#     me = Motor(Port.E)
#     me.dc(std_dc)
#     mf = Motor(Port.F)
#     mf.dc(std_dc)
# except Exception as exc:
#     pass

HEADER = "\033[95m"
OKBLUE = "\033[94m"
OKCYAN = "\033[96m"
OKGREEN = "\033[92m"
WARNING = "\033[93m"
FAIL = "\033[91m"
ENDC = "\033[0m"
BOLD = "\033[1m"
UNDERLINE = "\033[4m"


# Movehub does not have math functions, so no float() just shift-in the decimal point
def format_ms_to_time(ms):
    # Constants representing the number of milliseconds in one second, minute, and hour
    ms_per_second = 1000
    ms_per_minute = 60 * ms_per_second
    ms_per_hour = 60 * ms_per_minute

    # Calculate the hours, minutes, and seconds
    hours = ms // ms_per_hour
    ms %= ms_per_hour

    minutes = ms // ms_per_minute
    ms %= ms_per_minute

    seconds = ms // ms_per_second
    ms %= ms_per_second
    return hours, minutes, seconds, ms


def format_msec_as_time(clock):
    # use decimal math not float, so movehub can also do it.
    hour, minute, sec, ms = format_ms_to_time(clock)
    return f"{hour:>2}:{minute:>02}:{sec:02}.{ms:03} - "


def set_voltage_color(volt):
    if volt >= BAT_MED:
        textcolor = OKGREEN + BOLD
        light_color = Color.GREEN
    elif volt >= BAT_LOW:
        textcolor = WARNING + BOLD
        light_color = Color.YELLOW
    else:
        textcolor = FAIL + BOLD
        light_color = Color.RED

    return textcolor, light_color


def print_time_and_voltage():
    print(format_msec_as_time(watch.time()), end="")

    voltage_ma = hub.battery.voltage()
    textcolor, light_color = set_voltage_color(voltage_ma)
    hub.light.on(light_color)
    # print(f"{hw_type} Hub:{textcolor}{voltage_ma:>6} mV{ENDC}", end=" ")
    print(f"{git_hash} Hub:{textcolor}{voltage_ma:>6} mV{ENDC}", end=" ")


def print_amperes():
    global got_error_status, charger
    print(f"{hub.battery.current():>4} mA", end=" ")

    # 0. Not charging (light is off).
    # 1. Charging (light is red).
    # 2. Charging is complete (light is green).
    # 3. There is a problem with the charger (light is yellow).

    try:
        charger = hub.charger
    except:  # noqa
        charger = None
        print()

    if charger:
        charger_status = hub.charger.status()
        print(
            "|"
            + f" Ch conn:{hub.charger.connected()} stat:{charger_status} {hub.charger.current():>5} mA",
            end=" ",
        )
        if charger_status == 0:
            charge_text = f"{OKCYAN}Not charging (light off){ENDC}"
        elif charger_status == 1:
            charge_text = f"{OKGREEN + BOLD}Charging {ENDC}{FAIL + BOLD}(light red){ENDC}"
        elif charger_status == 2:
            charge_text = (
                f"{OKGREEN}Complete (light {BOLD}green{ENDC}{OKGREEN}){ENDC}"
            )
        else:
            charge_text = f"stat {charger_status} {WARNING + BOLD}Problem (light yellow){ENDC}"
            got_error_status = True
        error_status = (
            f" | {WARNING + BOLD}Got error{ENDC}" if got_error_status else ""
        )
        print(f"{charge_text:<20} {error_status}")


watch = StopWatch()
watch.reset()
got_error_status = False
prev_conn = 0
prev_stat = 0
first_wait_needed = True
while True:
    # Do the reporting 3 times in 30 seconds and report once unless charger connected or status changes
    # The First reporting step needs an extra 10 second wait
    if first_wait_needed:
        wait(INTERVAL_MS / 3)
        first_wait_needed = False
    # determine the time it took to deliver our payload and subtract that from waittime
    start_time = watch.time()  # get the current time
    if charger and (
        prev_conn != hub.charger.connected()
        or prev_stat != hub.charger.status()
    ):
        print_time_and_voltage()
        print_amperes()
        prev_conn = hub.charger.connected()
        prev_stat = hub.charger.status()
    end_time = watch.time()  # get the time after the action
    processing_time = (
        end_time - start_time
    )  # calculate the time taken for the action
    # wait for the remaining time
    wait(max(INTERVAL_MS / 3 - processing_time, 0))

    # determine the time it took to deliver our payload and subtract that from waittime
    start_time = watch.time()  # get the current time
    if charger and (
        prev_conn != hub.charger.connected()
        or prev_stat != hub.charger.status()
    ):
        print_time_and_voltage()
        print_amperes()
        prev_conn = hub.charger.connected()
        prev_stat = hub.charger.status()
    end_time = watch.time()  # get the time after the action
    processing_time = (
        end_time - start_time
    )  # calculate the time taken for the action
    # wait for the remaining time
    wait(max(INTERVAL_MS / 3 - processing_time, 0))

    # determine the time it took to deliver our payload and subtract that from waittime
    start_time = watch.time()  # get the current time
    # always report at the 30 seconds mark
    print_time_and_voltage()
    print_amperes()
    end_time = watch.time()  # get the time after the action
    if charger:
        prev_conn = hub.charger.connected()  # Might have changed this interval
        prev_stat = hub.charger.status()
    processing_time = (
        end_time - start_time
    )  # calculate the time taken for the action
    # wait for the remaining time
    wait(max(INTERVAL_MS / 3 - processing_time, 0))
