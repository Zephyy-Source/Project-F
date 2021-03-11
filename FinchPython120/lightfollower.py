from finch import Finch



finch = Finch()



while True:
    try:
        # light – returns the left and right light sensor readings, values range from 0.0 (dark) to 1.0 (bright)
        lls, rls = finch.light()
        finch.wheels(lls, rls)

    except Exception:
        print('Error')