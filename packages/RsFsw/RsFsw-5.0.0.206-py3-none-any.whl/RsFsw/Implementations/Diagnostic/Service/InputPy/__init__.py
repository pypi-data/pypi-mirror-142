from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class InputPy:
	"""InputPy commands group definition. 11 total commands, 7 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("inputPy", core, parent)

	@property
	def emi(self):
		"""emi commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_emi'):
			from .Emi import Emi
			self._emi = Emi(self._core, self._cmd_group)
		return self._emi

	@property
	def rf(self):
		"""rf commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_rf'):
			from .Rf import Rf
			self._rf = Rf(self._core, self._cmd_group)
		return self._rf

	@property
	def mc(self):
		"""mc commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_mc'):
			from .Mc import Mc
			self._mc = Mc(self._core, self._cmd_group)
		return self._mc

	@property
	def aiq(self):
		"""aiq commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_aiq'):
			from .Aiq import Aiq
			self._aiq = Aiq(self._core, self._cmd_group)
		return self._aiq

	@property
	def select(self):
		"""select commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_select'):
			from .Select import Select
			self._select = Select(self._core, self._cmd_group)
		return self._select

	@property
	def pulsed(self):
		"""pulsed commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_pulsed'):
			from .Pulsed import Pulsed
			self._pulsed = Pulsed(self._core, self._cmd_group)
		return self._pulsed

	@property
	def synthTwo(self):
		"""synthTwo commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_synthTwo'):
			from .SynthTwo import SynthTwo
			self._synthTwo = SynthTwo(self._core, self._cmd_group)
		return self._synthTwo

	def clone(self) -> 'InputPy':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = InputPy(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
