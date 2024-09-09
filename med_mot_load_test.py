from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait
from pybricks import version

print(version)

myMotor = Motor(Port.B)

myMotor.run(speed=1000)

while True:
    print(myMotor.load())
    wait(100)
