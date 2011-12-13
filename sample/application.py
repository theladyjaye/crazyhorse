import crazyhorse.application.wsgi
from myapp.application import MyApp
application = crazyhorse.application.wsgi.Application(MyApp());