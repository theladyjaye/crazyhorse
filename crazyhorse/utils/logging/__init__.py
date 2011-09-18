import logging
from crazyhorse.utils.logging import colors

class CrazyHorseStatusFilter(logging.Filter):

    def filter(self, record):
        color = None
        if record.levelno == logging.INFO:
           color = colors.foreground.green
        if record.levelno == logging.DEBUG:
           color = colors.foreground.cyan
        elif record.levelno == logging.WARNING:
            color = colors.foreground.yellow
        elif record.levelno == logging.ERROR:
            color = colors.foreground.red
        elif record.levelno == logging.CRITICAL:
            color = colors.foreground.red
        elif record.levelno == logging.FATAL:
            color = colors.foreground.red

        if color is not None:
            record.msg = color + "["+record.levelname+"] " + colors.foreground.reset + record.msg

        return True
