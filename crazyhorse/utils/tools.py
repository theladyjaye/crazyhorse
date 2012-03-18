import collections
import importlib
import crazyhorse

def import_class(pkg, cls=None):
    module = None

    if "/" in pkg:
        pkg = pkg.replace("/", ".")

    if cls is None:
        parts = collections.deque(pkg.split("."))
        cls = parts.pop()
        pkg = ".".join(parts)

    try:
        module = importlib.import_module(pkg)
    except ImportError as e:
        crazyhorse.get_logger().error("Unable to import {0} from {1}: {2}".format(cls, pkg, e.message))
        return None

    try:
        return getattr(module, cls)
    except AttributeError as e:
        crazyhorse.get_logger().error("Unable to import {0} from {1}: {2}".format(cls, pkg, e.message))

def import_module(pkg):

    module = None

    if "/" in pkg:
        pkg = pkg.replace("/", ".")

    try:
        module  = importlib.import_module(pkg)
    except ImportError as e:
        crazyhorse.get_logger().warning("Unable to import module {0}: {1}".format(pkg, e.message))
        return None

    return module