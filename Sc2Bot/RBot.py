
import sc2
from sc2 import run_game, maps, Race, Difficulty, position
from sc2.player import Bot, Computer
from sc2.constants import NEXUS, PROBE, PYLON, ASSIMILATOR, GATEWAY, \
	CYBERNETICSCORE, STALKER, STARGATE, VOIDRAY, OBSERVER, ROBOTICSFACILITY
import random
import cv2
import numpy as np
import keras

class Commander():
	def __init__(self):
		self.generals = []

	async def act(self):
		for general in self.generals:
			general.act();

class General():
	def __init__(self):
		self.units = []
		self.structures = []

	async def act(self):
		return

class GeneralResourceGatherer(General):
	def __init__(self):
		super.__init__(self)
		self.minerals = 0
		self.vespene_gas = 0

class GeneralMilitaryBuilder(General):
	def __init__(self):
		super.__init__(self)





class RBot(sc2.BotAI):
	def __init__(self, use_model=False):
		self.ITERATIONS_PER_MINUTE = 165
		self.MAX_WORKERS = 50
		self.commander = Commander()

	async def on_step(self, iteration):
		self.commander.act()
	
run_game(maps.get("AbyssalReefLE"), [
	Bot(Race.Protoss, RBot()),
	Computer(Race.Terran, Difficulty.Hard)
	], realtime=False)
