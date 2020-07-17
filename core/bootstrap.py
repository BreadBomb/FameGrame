from typing import Type

from core import Application


def bootstrap_application(app_type: Type[Application]):
    application = None
    try:
        application = app_type()
        application.start()
    except KeyboardInterrupt:
        application.close()
