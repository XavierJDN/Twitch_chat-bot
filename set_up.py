import json
from script.twitch_bot.twitch_bot import TwitchBot


class SetUpBot:
    def __init__(self):
        self._bot = TwitchBot("twitch_bot")
        self.set_up_commands()
        self.set_up_join()
        self._bot.run()

    def set_up_commands(self):
        commands = self.fetch_commands()
        for command in commands:
            self._bot.register_command(command.ex, lambda cmd: self.bot.send_message(command.message))
        self.set_up_help_command(commands)

    def set_up_join(self):
        bot_settings = self.fetch_bot_settings()
        self._bot.connect_and_join(bot_settings.password, bot_settings.nickname, bot_settings.channel)

    def fetch_commands(self):
        with open(file="./data/commands.json") as commands:
            return json.load(commands)

    def fetch_bot_settings(self):
        with open(file="./data/settings.json") as settings:
            return json.load(settings)

    def set_up_help_command(self, commands):
        self._bot.register_command("help", "You can exec all this commands: " + ", ".join([message for key, message in commands if key =="ex"]))

    @property
    def bot(self):
         return self._bot
