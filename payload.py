import json

_OPCODE_KEY = "op"
_DATA_KEY = "d"
_SEQNO_KEY = "s"
_EVENT_KEY = "t"


class Payload:
    # Class methods
    @classmethod
    def receive(cls, payload_string):
        payload = json.loads(payload_string)
        return cls(payload.get(_OPCODE_KEY), payload.get(_DATA_KEY),
                   payload.get(_SEQNO_KEY), payload.get(_EVENT_KEY))

    # Instance methods
    def __init__(self,
                 opcode,
                 data=None,
                 sequence_number=None,
                 event_name=None):
        self.opcode = opcode
        self.data = data
        self.sequence_number = sequence_number
        self.event_name = event_name

    def dumps(self):
        json.dumps({
            _OPCODE_KEY: self.opcode,
            _DATA_KEY: self.data,
            _SEQNO_KEY: self.sequence_number,
            _EVENT_KEY: self.event_name
        })
