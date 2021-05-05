import enum
import json


class Keys(enum.Enum):
    WEBHOOKS = "webhooks"
    USERS = "users"
    AUDIT_LOG_ENTRIES = "audit_log_entries"
    INTEGRATIONS = "integrations"


class AuditLog:
    @classmethod
    def receive(cls, audit_log_string):
        audit_log = json.loads(audit_log_string)
        # TODO process these into their respective objects -- should be arrays!
        return cls(audit_log.get(Keys.WEBHOOKS), audit_log.get(Keys.USERS),
                   audit_log.get(Keys.AUDIT_LOG_ENTRIES),
                   audit_log.get(Keys.INTEGRATIONS))

    def __init__(self, webhooks, users, audit_log_entries, integrations):
        self.webhooks = webhooks
        self.users = users
        self.audit_log_entries = audit_log_entries
        self.integrations = integrations
