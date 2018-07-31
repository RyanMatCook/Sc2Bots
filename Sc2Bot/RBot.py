
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
		self.generals = [
				GeneralResourceGatherer(),
				GeneralMilitaryBuilder(),
				GeneralBattle(),
				GeneralIntelligence()
			]
		self.master_queue = []

	def import_queues(self, iteration):
		for general in generals:
			 self.master_queue.append(general.get_new_requisitions(iteration))

	async def act(self, iteration):
		for general in self.generals:
			general.act();
		self.import_queues(iteration)

class Requisition():
	def __init__(self, iteration, lifespan=10, priority=0):
		self.created_iteration = iteration
		self.lifespan = lifespan
		self.priority = priority

	def is_new(self, iteration):
		# New requisitions are those created in this iteration as creation happens before import
		return self.created_iteration == iteration

	def is_expired(self, iteration):
		return iteration - self.created_iteration > self.lifespan

class General():
	def __init__(self):
		self.units = []
		self.structures = []
		self.max_requisitions = 10
		self.requisitionQueue = []

	def get_new_requisitions(self, iteration):
		to_return = []
		for requisition in self.requisitionQueue:
			if not requisition.is_new(iteration):
				to_return.append(requisition)
		return to_return

	def remove_expired_requisitions(self, iteration):
		to_remove = []
		for requisition in self.requisitionQueue:
			if requisition.is_expired(iteration):
				to_remove.append(requisition)
		for requsition in to_remove:
			self.requisitionQueue.remove(requisition)

	def act(self, iteration):
		self.remove_expired_requisitions(iteration)
		if len(self.requisitionQueue) == self.max_requisitions: 
			# This could increment priorities to force closure of requisitions
			return
		

# General responsible for gathering resources and building workers
class GeneralResourceGatherer(General):
	def __init__(self):
		super.__init__(self)
		self.minerals = 0
		self.vespene_gas = 0

# General responsible for building military structures and units
class GeneralMilitaryBuilder(General):
	def __init__(self):
		super.__init__(self)

# General responsible for managing battle plans
class GeneralBattle(General):
	def __init__(self):
		super.__init__(self)

# General responsible for gathering intelligence
class GeneralIntelligence(General):
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
