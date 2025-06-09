from base_robot import *

# Import missions
import noah2, noahsdice, shaila, shaila2, noah4, Carovanni, carternoah, GiosToast


br: BaseRobot = BaseRobot()

pressed = []
col: Color = br.colorSensor.color()

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
            br.driveForMillis(millis=30000, speedPct=100, gyro=False)

    # It will now launch the mission coresponding to the color
    if col == Color.SENSOR_YELLOW:
        print("Launching Yellow")
        noah2.Run(br)
        br.waitForForwardButton()

        shaila.Run(br)

    if col == Color.SENSOR_GREEN:
        print("Launching Green")
        GiosToast.Run(br)

    if col == Color.SENSOR_LIME:
        print("Launching Lime")
        noahsdice.Run(br)

    # if col == Color.SENSOR_MAGENTA:
    #     print("Launching Magenta")
    #     shaila.Run(br)

    if col == Color.SENSOR_WHITE:
        print("Launching White")
        shaila2.Run(br)

    if col == Color.SENSOR_ORANGE:
        print("Launching Orange")
        noah4.Run(br)

    if col == Color.SENSOR_RED or col == Color.SENSOR_MAGENTA:
        print("Launching Red/Magenta")
        carternoah.Run(br)

    if col == Color.SENSOR_BLUE:
        print("Launching Blue")
        Carovanni.Run(br)
