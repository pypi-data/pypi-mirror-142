from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Lte:
	"""Lte commands group definition. 47 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lte", core, parent)

	@property
	def ooPower(self):
		"""ooPower commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ooPower'):
			from .OoPower import OoPower
			self._ooPower = OoPower(self._core, self._cmd_group)
		return self._ooPower

	@property
	def cc(self):
		"""cc commands group. 11 Sub-classes, 0 commands."""
		if not hasattr(self, '_cc'):
			from .Cc import Cc
			self._cc = Cc(self._core, self._cmd_group)
		return self._cc

	@property
	def downlink(self):
		"""downlink commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_downlink'):
			from .Downlink import Downlink
			self._downlink = Downlink(self._core, self._cmd_group)
		return self._downlink

	@property
	def frame(self):
		"""frame commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_frame'):
			from .Frame import Frame
			self._frame = Frame(self._core, self._cmd_group)
		return self._frame

	@property
	def uplink(self):
		"""uplink commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_uplink'):
			from .Uplink import Uplink
			self._uplink = Uplink(self._core, self._cmd_group)
		return self._uplink

	def clone(self) -> 'Lte':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Lte(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
