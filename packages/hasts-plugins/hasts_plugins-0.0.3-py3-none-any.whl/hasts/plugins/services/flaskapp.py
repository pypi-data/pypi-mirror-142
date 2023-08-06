#!/usr/bin/env python3

# Disable some rules in pylint because they're not valid for this file:
#  - R0903 (too-few-public-methods)
# pylint: disable=R0903

### IMPORTS ###
import abc
import logging

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class AppService(metaclass = abc.ABCMeta):
    def __init__(self):
        self.logger = logging.getLogger(type(self).__name__)

    @abc.abstractmethod
    def get_app(self):
        raise NotImplementedError

class FlaskAppService(AppService):
    def __init__(self, flask_app):
        super().__init__()
        self.logger.debug("Inputs - flask_app: %s", flask_app)
        # FIXME: Put some checks in here to make sure that the input is a flask app object.
        self._flask_app = flask_app

    def get_app(self):
        self.logger.debug("Getting app:%s", self._flask_app)
        return self._flask_app
