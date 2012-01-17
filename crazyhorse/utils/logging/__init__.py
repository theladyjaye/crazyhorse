import logging
import sys
import traceback
from crazyhorse.utils.logging import colors

class CrazyHorseStatusFilter(logging.Filter):

    def filter(self, record):
        color = None
        extra = ""

        if record.levelno == logging.INFO:
           color = colors.foreground.green
        if record.levelno == logging.DEBUG:
           color = colors.foreground.cyan
        elif record.levelno == logging.WARNING:
            color = colors.foreground.yellow
        elif record.levelno == logging.ERROR:
            color = colors.foreground.red
            extra = "\n" + traceback.format_exc(5)
        elif record.levelno == logging.CRITICAL:
            color = colors.foreground.red
            extra = "\n" + traceback.format_exc(5)
        elif record.levelno == logging.FATAL:
            color = colors.foreground.red
            extra = "\n" + traceback.format_exc(5)

        if color is not None:
            record.msg = color + "["+record.levelname+"] " + colors.foreground.reset + record.msg + extra

        return True
