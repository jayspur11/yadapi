from restapi import _core

def get_region_list():
    return _core.make_get_request("/voice/regions")
