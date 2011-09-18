import logging
import crazyhorse.utils.logging

_logger = None


def get_logger():
    global _logger

    if _logger == None:
        _logger = logging.getLogger("CrazyHorse")
        filter  = crazyhorse.utils.logging.CrazyHorseStatusFilter()
        handler = logging.StreamHandler()
        _logger.setLevel(logging.DEBUG)
        _logger.addHandler(handler)
        _logger.addFilter(filter)

    return _logger