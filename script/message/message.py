"""
Wrapper for IRC protocol

RFC: https://tools.ietf.org/html/rfc1459
"""


import socket
import ssl
from dataclasses import dataclass


@dataclass
class Message:
	"""
	An IRC message. It is at its core made of a prefix, a command and parameters to that command, all space-separated. Messages in a stream are delimited by CR-LF.

	:ivar orig_str: The original full string of the message.
	:ivar prefix: The prefix, can be None.
	:ivar command: The command name.
	:ivar params: The command parameters, can be None.
	"""

	orig_str: str
	prefix: str = None
	command: str = None
	params: str = None

	@classmethod
	def from_str(cls, msg_str):
		msg = msg_str.strip()
		if len(msg) == 0:
			return cls(msg_str)
		if msg.startswith(":"):
			parts = msg.split(None, 2)
			return cls(msg_str, parts[0][1:], parts[1], parts[2] if len(parts) == 3 else None)
		else:
			parts = msg.split(None, 1)
			return cls(msg_str, None, parts[0], parts[1] if len(parts) == 2 else None)
