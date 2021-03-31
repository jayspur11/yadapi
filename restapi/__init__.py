from restapi import _core

def initialize(app_name, bot_token):
    _core.app_name = app_name
    _core.bot_token = bot_token