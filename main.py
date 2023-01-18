"""
Fonction principale qui roule les exemples par chapitre.
"""


import sys
import os
import argparse
import configparser
import json
import random
from collections import namedtuple
from dataclasses import dataclass

from script.chat_bot.chatbot import *
from script.twitch_bot.twitch_bot import *
from script.bot.bot import Bot


def main():
	# set up the bot
	Bot()
	
if __name__ == "__main__":
	main()
