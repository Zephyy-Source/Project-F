from finch import Finch



finch = Finch()


# light – returns the left and right light sensor readings, values range from 0.0 (dark) to 1.0 (bright)
left_light_sensor, right_light_sensor = finch.light()
lls = left_light_sensor
rls = right_light_sensor
while True:
    try:
        finch.wheels(lls, rls)

    except Exception:
        print('Error')