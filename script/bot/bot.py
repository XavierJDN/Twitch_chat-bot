import json
from script.twitch_bot.twitch_bot import TwitchBot


class Bot:
    def __init__(self):
        self._bot = TwitchBot("twitch_bot")
        self.set_up_commands()
        self.set_up_join()
        self._bot.run()

    def set_up_commands(self):
        commands = self.fetch_commands()
        for command in commands:
            self._bot.register_command(command['exec'], lambda cmd: self.bot.send_privmsg(command['message']))
        self.set_up_help_command(commands)

    def set_up_join(self):
        bot_settings = self.fetch_bot_settings()
        self._bot.connect_and_join(bot_settings['password'], bot_settings['nickname'], bot_settings['channel'])

    def fetch_commands(self):
        with open(file="./data/commands.json") as commands:
            return json.loads(commands.read())

    def fetch_bot_settings(self):
        with open(file="./data/settings.json") as settings:
            return json.loads(settings.read())

    def set_up_help_command(self, commands):
        response = "You can exec all this commands: " + ", ".join([message for key, message in commands if key =="exec"])
        self._bot.register_command("help", lambda cmd: self.bot.send_privmsg(response))

    @property
    def bot(self):
         return self._bot
