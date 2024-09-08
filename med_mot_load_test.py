from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait
from pybricks.hubs import PrimeHub

myMotor = Motor(Port.B)
myHub = PrimeHub()

myMotor.run(speed=1000)

while True:
    print(myMotor.load())
    wait(100)
