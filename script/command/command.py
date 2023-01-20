from script.private_message.private_message import PrivateMessage
from script.twitch_bot.twitch_bot import TwitchBot


class Command:
    message: str
    command: str
    def __init__(self, bot:TwitchBot):
        bot.register_command(self.command, lambda cmd: self._run(bot, cmd.privmsg))

    def _run(self, bot: TwitchBot, msg:PrivateMessage):
        bot.send_privmsg(self.message)
        self._execute()

    def _execute(self):
        pass

    def __str__(self) -> str:
        return self.command

class HelpCommand(Command):
    command = "help"
    message = "You can exec all this commands: "

    def __init__(self, bot:TwitchBot, commands:list):
        self.message += ", ".join(['!' + str(command) for command in commands])
        super().__init__(bot)

class HiCommand(Command):
    command = "hi"
    message = "Hi, Glad to have you here!"

    def __init__(self, bot:TwitchBot):
        super().__init__(bot)