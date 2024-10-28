from base_robot import *

# Import missions
import noah2, Gio, Sadie, noah3, shaila


br = BaseRobot()

pressed = []
col = br.colorSensor.color()

while True:
    while True:
        col = br.colorSensor.color()
        # The first thing this program does is it detects what color is
        # being help up to the robot color sensor.
        # If no color is detected, then it will display a sad face
        if col == Color.SENSOR_NONE:
            br.hub.display.icon(Icon.SAD)
            br.hub.light.on(Color.RED)
        else:  #  If a color is detected, then it will display a happy face
            br.hub.display.icon(Icon.HAPPY)
            br.hub.light.on(br.myColor2DefaultColorDict[col])

        wait(50)
        pressed = br.hub.buttons.pressed()
        #  When the left button is pressed, it will break out of the loop
        if Button.LEFT in pressed:
            break
        if Button.BLUETOOTH in pressed:
            # If the Bluetooth button is pressed, it will run the motors fast for
            # cleaning
            br.leftDriveMotor.run(1000)
            br.rightDriveMotor.run(1000)
            wait(25000)
            br.leftDriveMotor.brake()
            br.rightDriveMotor.brake()

    # It will now launch the mission coresponding to the color
    if col == Color.SENSOR_YELLOW:
        noah2.Run(br)

    if col == Color.SENSOR_GREEN:
        Gio.Run(br)

    if col == Color.SENSOR_BLUE:
        Sadie.Run(br)

    if col == Color.SENSOR_LIME:
        noah3.Run(br)

    if col == Color.SENSOR_MAGENTA:
        shaila.Run(br)

    # if col == Color.SENSOR_BLUE:
        # shaila2.run(br)