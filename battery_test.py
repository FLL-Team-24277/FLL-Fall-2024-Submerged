""" program to show the battery voltage and current consumed over time
    Simplified arithmetic so this can also run on the movehub """

from pybricks import version
from pybricks.tools import wait
from pybricks.tools import StopWatch
from pybricks.parameters import Color

print(f"version {version}")

hw_type = version[0]

if hw_type in ["inventorhub", "primehub"]:  # aliases == the same firmware
    from pybricks.hubs import InventorHub

    hub = InventorHub()
elif hw_type == "technichub":
    from pybricks.hubs import TechnicHub

    hub = TechnicHub()
elif hw_type == "cityhub":
    from pybricks.hubs import CityHub

    hub = CityHub()
elif hw_type == "movehub":
    from pybricks.hubs import MoveHub

    hub = MoveHub()
# else:
#     raise RuntimeException("Unknown hub " + hw_type)
print(hw_type, "loaded\n\tBattery voltage:", hub.battery.voltage(), "mV")

DEBUG = False
# DEBUG = True
INTERVAL_MS = 30 * 1000  # 30 seconds in mSec

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
    BAT_OUT = 5500  # mVolt

HEADER = "\033[95m"
OKBLUE = "\033[94m"
OKCYAN = "\033[96m"
OKGREEN = "\033[92m"
WARNING = "\033[93m"
FAIL = "\033[91m"
ENDC = "\033[0m"
BOLD = "\033[1m"
UNDERLINE = "\033[4m"


hw_type = version[0]

# import and define the HUB object
if str(hw_type) == "technichub":
    from pybricks.hubs import TechnicHub

    HUB = TechnicHub()
elif hw_type == "movehub":
    from pybricks.hubs import MoveHub

    HUB = MoveHub()
elif hw_type == "inventorhub":
    from pybricks.hubs import InventorHub

    HUB = InventorHub()
    HUB.display.off()
elif hw_type == "primehub":
    from pybricks.hubs import PrimeHub

    HUB = PrimeHub()
    HUB.display.off()
elif hw_type == "cityhub":
    from pybricks.hubs import CityHub

    HUB = CityHub()
    # HUB.display.off() ## No display on cityhub
else:
    print("Unknown HUB:", hw_type)


# Movehub does not have math functions, so no float() just shift the decimal point in
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
    # use decimal math not float, so movehub can do it too.
    hour, minute, sec, ms = format_ms_to_time(clock)
    return f"{hour:>2}:{minute:>02}:{sec:02}.{ms:03} - "


def print_time_and_voltage():

    # if BAT_HI > HUB.battery.voltage() > BAT_MED:
    if HUB.battery.voltage() > BAT_MED:
        textcolor = OKGREEN + BOLD
        HUB.light.on(Color.GREEN)
    elif BAT_MED > HUB.battery.voltage() > BAT_LOW:
        textcolor = WARNING + BOLD
        HUB.light.on(Color.YELLOW)
    else:
        textcolor = FAIL + BOLD
        HUB.light.on(Color.RED)

    print(format_msec_as_time(watch.time()), end=" ")
    cur_voltage = format_like_decimal(HUB.battery.voltage())
    print(
        f"{hw_type:<12} {textcolor}voltage: {cur_voltage:>6} V{ENDC}", end=" "
    )


def print_amperes():
    # print(f"{hw_type:<12} current: {format_like_decimal(HUB.battery.current()):>6} A", end=" ")
    print(
        f"current: {format_like_decimal(HUB.battery.current()):>6} A", end=" "
    )
    # print(f'Charger Connected:\t {HUB.charger.connected()}')
    try:
        charger = HUB.charger
    except:
        charger = None
    if charger:
        print(f"| Charger:{HUB.charger.current():>5} mA", end=" ")
        charger_status = HUB.charger.status()
        if charger_status == 0:
            charge_text = f"{OKCYAN}Not charging (light off){ENDC}"
        elif charger_status == 1:
            charge_text = (
                f"{OKGREEN + BOLD}Charging {ENDC}{FAIL}(light red){ENDC}"
            )
        elif charger_status == 2:
            charge_text = (
                f"{OKGREEN}Complete (light {BOLD}green{ENDC}{OKGREEN}){ENDC}"
            )
        else:
            charge_text = f"{WARNING + BOLD}Problem (light yellow){ENDC}"
        print(charge_text)
    else:
        print()


def format_like_decimal(mynum):
    sign = "-" if mynum < 0 else ""
    num_str = str(abs(mynum))
    num_len = len(num_str)
    result = ""
    if num_len == 1:
        result = sign + "0.00" + num_str
    elif num_len == 2:
        result = sign + "0.0" + num_str
    elif num_len == 3:
        result = sign + "0." + num_str
    else:
        for i in range(num_len):
            if i == num_len - 3:  # was 4
                result += "."
            result += num_str[i]
    return result


# tests
if DEBUG:
    print(format_like_decimal(-1000))
    print(format_like_decimal(-100))
    print(format_like_decimal(-10))
    print(format_like_decimal(-1))
    print(format_like_decimal(0))
    print(format_like_decimal(1))
    print(format_like_decimal(10))
    print(format_like_decimal(999))
    print(format_like_decimal(1000))
    print(format_like_decimal(10000))
    print(format_like_decimal(100000))


watch = StopWatch()
watch.reset()
while True:
    # determine the time it took to deliver our payload and subtract that from waittime
    start_time = watch.time()  # get the current time
    print_time_and_voltage()
    print_amperes()
    end_time = watch.time()  # get the time after the action

    processing_time = (
        end_time - start_time
    )  # calculate the time taken for the action
    # wait for the remaining time
    wait(max(INTERVAL_MS - processing_time, 0))
