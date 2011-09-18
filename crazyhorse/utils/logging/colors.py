ESCAPE  = "\033["
RESET   = 0

class ForegroundColors(object):
    BLACK   = 30
    RED     = 31
    GREEN   = 32
    YELLOW  = 33
    BLUE    = 34
    MAGENTA = 35
    CYAN    = 36
    WHITE   = 37
    RESET   = 39

class Background(object):
    pass

class Foreground(object):

    @property
    def reset(self):
        return ESCAPE + "0;" + str(ForegroundColors.RESET) + 'm'

    def __getattr__(self, name):
            color = getattr(ForegroundColors, name.upper(), None)

            if color is None:
                color = ForegroundColors.RESET

            return ESCAPE + "0;" + str(color) + 'm'

foreground = Foreground()
