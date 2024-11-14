from pybricks.parameters import (
    Axis,
)
from pybricks.hubs import PrimeHub
from pybricks import version
from utils import *

hub = PrimeHub(top_side=Axis.Z, front_side=-Axis.Y)
print(version)
v = hub.battery.voltage()
print(str(v))
