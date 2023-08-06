from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sense:
	"""Sense commands group definition. 117 total commands, 11 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sense", core, parent)

	@property
	def adjust(self):
		"""adjust commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_adjust'):
			from .Adjust import Adjust
			self._adjust = Adjust(self._core, self._cmd_group)
		return self._adjust

	@property
	def correction(self):
		"""correction commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_correction'):
			from .Correction import Correction
			self._correction = Correction(self._core, self._cmd_group)
		return self._correction

	@property
	def mixer(self):
		"""mixer commands group. 8 Sub-classes, 0 commands."""
		if not hasattr(self, '_mixer'):
			from .Mixer import Mixer
			self._mixer = Mixer(self._core, self._cmd_group)
		return self._mixer

	@property
	def probe(self):
		"""probe commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_probe'):
			from .Probe import Probe
			self._probe = Probe(self._core, self._cmd_group)
		return self._probe

	@property
	def directed(self):
		"""directed commands group. 7 Sub-classes, 2 commands."""
		if not hasattr(self, '_directed'):
			from .Directed import Directed
			self._directed = Directed(self._core, self._cmd_group)
		return self._directed

	@property
	def fplan(self):
		"""fplan commands group. 3 Sub-classes, 2 commands."""
		if not hasattr(self, '_fplan'):
			from .Fplan import Fplan
			self._fplan = Fplan(self._core, self._cmd_group)
		return self._fplan

	@property
	def listPy(self):
		"""listPy commands group. 1 Sub-classes, 3 commands."""
		if not hasattr(self, '_listPy'):
			from .ListPy import ListPy
			self._listPy = ListPy(self._core, self._cmd_group)
		return self._listPy

	@property
	def pmeter(self):
		"""pmeter commands group. 8 Sub-classes, 0 commands."""
		if not hasattr(self, '_pmeter'):
			from .Pmeter import Pmeter
			self._pmeter = Pmeter(self._core, self._cmd_group)
		return self._pmeter

	@property
	def creference(self):
		"""creference commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_creference'):
			from .Creference import Creference
			self._creference = Creference(self._core, self._cmd_group)
		return self._creference

	@property
	def ssearch(self):
		"""ssearch commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_ssearch'):
			from .Ssearch import Ssearch
			self._ssearch = Ssearch(self._core, self._cmd_group)
		return self._ssearch

	@property
	def transfer(self):
		"""transfer commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_transfer'):
			from .Transfer import Transfer
			self._transfer = Transfer(self._core, self._cmd_group)
		return self._transfer

	def clone(self) -> 'Sense':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Sense(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
