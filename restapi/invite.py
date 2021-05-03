from restapi import _core


def get_invite(invite_code):
    return _core.make_get_request(f"/invites/{invite_code}")
