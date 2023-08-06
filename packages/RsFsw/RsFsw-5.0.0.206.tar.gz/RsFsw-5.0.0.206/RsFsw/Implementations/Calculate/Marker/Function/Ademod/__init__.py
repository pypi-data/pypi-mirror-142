from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ademod:
	"""Ademod commands group definition. 14 total commands, 10 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ademod", core, parent)

	@property
	def am(self):
		"""am commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_am'):
			from .Am import Am
			self._am = Am(self._core, self._cmd_group)
		return self._am

	@property
	def acv(self):
		"""acv commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_acv'):
			from .Acv import Acv
			self._acv = Acv(self._core, self._cmd_group)
		return self._acv

	@property
	def fm(self):
		"""fm commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_fm'):
			from .Fm import Fm
			self._fm = Fm(self._core, self._cmd_group)
		return self._fm

	@property
	def pm(self):
		"""pm commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_pm'):
			from .Pm import Pm
			self._pm = Pm(self._core, self._cmd_group)
		return self._pm

	@property
	def afrequency(self):
		"""afrequency commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_afrequency'):
			from .Afrequency import Afrequency
			self._afrequency = Afrequency(self._core, self._cmd_group)
		return self._afrequency

	@property
	def freqError(self):
		"""freqError commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_freqError'):
			from .FreqError import FreqError
			self._freqError = FreqError(self._core, self._cmd_group)
		return self._freqError

	@property
	def sinad(self):
		"""sinad commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_sinad'):
			from .Sinad import Sinad
			self._sinad = Sinad(self._core, self._cmd_group)
		return self._sinad

	@property
	def distortion(self):
		"""distortion commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_distortion'):
			from .Distortion import Distortion
			self._distortion = Distortion(self._core, self._cmd_group)
		return self._distortion

	@property
	def thd(self):
		"""thd commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_thd'):
			from .Thd import Thd
			self._thd = Thd(self._core, self._cmd_group)
		return self._thd

	@property
	def carrier(self):
		"""carrier commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_carrier'):
			from .Carrier import Carrier
			self._carrier = Carrier(self._core, self._cmd_group)
		return self._carrier

	def clone(self) -> 'Ademod':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ademod(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
