import json
from script.command.command import HelpCommand, HiCommand
from script.twitch_bot.twitch_bot import TwitchBot


class Bot:
    def __init__(self):
        self._bot = TwitchBot("twitch_bot")
        self.set_up_commands()
        self.set_up_join()
        self._bot.run()

    def set_up_commands(self):
        commands = [HiCommand(self.bot)] # build all commands here
        commands.append(HelpCommand(self._bot, commands))

    def set_up_join(self):
        bot_settings = self.fetch_bot_settings()
        self._bot.connect_and_join(bot_settings['password'], bot_settings['nickname'], bot_settings['channel'])


    def fetch_bot_settings(self):
        with open(file="./data/settings.json") as settings:
            return json.loads(settings.read())


    @property
    def bot(self):
         return self._bot
