import socket
import ssl
from dataclasses import dataclass

class Client:
	def __init__(self, channel_char="#"):
		self.ssl_context = ssl.create_default_context()
		self.sock = None
		self.channel_char = "#"

	def connect(self, host, port, use_ssl=False):
		self.sock = socket.create_connection((host, port))
		if use_ssl:
			self.sock = self.ssl_context.wrap_socket(self.sock, server_hostname=host)
		self.sock.settimeout(0)

	def disconnect(self):
		if self.sock is not None:
			self.sock.close()
			self.sock = None

	def send_join(self, channel):
		return self.send(None, "JOIN", self.channel_char + channel)

	def send_part(self, channel):
		return self.send(None, "PART", self.channel_char + channel)

	def send_privmsg(self, channel, msg):
		return self.send(None, "PRIVMSG", f"{self.channel_char}{channel} :{msg}")

	def receive_and_parse(self):
		msgs = self.receive()
		return [Message.from_str(msg) for msg in msgs]

	def send(self, msg_prefix, msg_command, command_params, newline_replacement = " "):
		msg_str = self.format_msg(msg_prefix, msg_command, command_params, newline_replacement)
		num_sent_bytes = self.sock.send(bytes("\r\n" + msg_str + "\r\n", "UTF-8"))
		return msg_str, num_sent_bytes

	def format_msg(self, msg_prefix, msg_command, command_params, newline_replacement = " "):
		command_params = newline_replacement.join(command_params.split())
		msg_str = ""
		if msg_prefix is not None:
			msg_str += f":{msg_prefix} "
		msg_str = f"{msg_command} {command_params}"
		return msg_str

	def receive(self):
		msg_list = []
		data = b""
		while True:
			try:
				rec_bytes = self.sock.recv(4096)
			except ssl.SSLWantReadError:
				rec_bytes = b""
			if len(rec_bytes) == 0:
				break
			data += rec_bytes
			lines = data.split(b"\r\n")
			if lines[-1] != b"":
				lines = lines[:-1]
				data = lines[-1]
			else:
				data = b""
			for l in lines:
				if l != b"":
					msg_list.append(l.decode("UTF-8"))
		return msg_list