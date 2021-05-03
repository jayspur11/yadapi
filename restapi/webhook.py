from restapi import _core


def get_webhook(webhook_id):
    return _core.make_get_request(f"/webhooks/{webhook_id}")


def get_webhook_with_token(webhook_id, webhook_token):
    return _core.make_get_request(f"/webhooks/{webhook_id}/{webhook_token}")


def get_message(webhook_id, webhook_token, message_id):
    return _core.make_get_request(
        f"/webhooks/{webhook_id}/{webhook_token}/messages/{message_id}")
