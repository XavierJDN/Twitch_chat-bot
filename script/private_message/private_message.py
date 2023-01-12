import script.message.message as Message

@dataclass
class PrivateMessage:
	"""
	The main purpose of the IRC protocol is to provide a base for clients to communicate with each other. Messages with the PRIVMSG command are the main messages which actually perform delivery of a text message from one client to another. This is how users chat with each other.

	A PRIVMSG typically has the form `<prefix> PRIVMSG <#|&><channel> :<text>` (https://tools.ietf.org/html/rfc1459#section-4.4.1)

	:ivar orig_str: The original full string of the message
	:ivar prefix: The prefix, can be None. Clients usually do not need to add a prefix when sending messages.
	:ivar channel: The channel name, without the # or & character.
	:ivar text: The message text, without the beginning colon.
	"""

	orig_str: str
	prefix: str = None
	channel: str = None
	text: str = None

	@classmethod
	def from_str(cls, msg_str):
		return cls.from_irc_msg(Message.from_str(msg_str))

	@classmethod
	def from_irc_msg(cls, irc_msg):
		privmsg = cls(irc_msg.orig_str)
		channel_str, text_str = irc_msg.params.split(None, 1)
		privmsg.prefix = irc_msg.prefix
		privmsg.channel = channel_str[1:]
		privmsg.text = text_str[1:] if text_str[0] == ":" else text_str
		return privmsg
