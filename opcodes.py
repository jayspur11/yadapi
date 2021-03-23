""" Discord Gateway opcodes.

All gateway events in Discord are tagged with an opcode that denotes the payload
type.
"""

key = "op"

""" INCOMING OPCODES """
# An event was dispatched.
DISPATCH = 0
# Client should attempt to reconnect and resume immediately.
RECONNECT = 7
# The session has been invalidated. Client should reconnect and identify or
# resume accordingly.
INVALID_SESSION = 9
# Sent immediately after connecting. Contains `heartbeat_interval` to use.
HELLO = 10
# Sent in response to a heartbeat, to acknowledge receipt.
# NOTE: If the client does not receive ack between heartbeats, it should
#       terminate the connection with a non-1000 code, reconnect, and attempt to
#       resume.
HEARTBEAT_ACK = 11

""" OUTGOING OPCODES """
# Fired periodically by the client to keep the connection alive.
# NOTE: The gateway can use this to request a heartbeat, and the client should
#       send a heartbeat back as normal.
HEARTBEAT = 1
# Starts a new session during the initial handshake.
IDENTIFY = 2
# Update the client's presence.
PRESENCE_UPDATE = 3
# Used to join, leave, or move between voice channels.
VOICE_STATE_UPDATE = 4
# Resume a previous session that was disconnected.
RESUME = 6
# Request information about offline guild members in a large guild.
REQUEST_GUILD_MEMBERS = 8
