from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Normalize:
	"""Normalize commands group definition. 8 total commands, 8 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("normalize", core, parent)

	@property
	def value(self):
		"""value commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_value'):
			from .Value import Value
			self._value = Value(self._core, self._cmd_group)
		return self._value

	@property
	def cfdrift(self):
		"""cfdrift commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cfdrift'):
			from .Cfdrift import Cfdrift
			self._cfdrift = Cfdrift(self._core, self._cmd_group)
		return self._cfdrift

	@property
	def fdError(self):
		"""fdError commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fdError'):
			from .FdError import FdError
			self._fdError = FdError(self._core, self._cmd_group)
		return self._fdError

	@property
	def iqOffset(self):
		"""iqOffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_iqOffset'):
			from .IqOffset import IqOffset
			self._iqOffset = IqOffset(self._core, self._cmd_group)
		return self._iqOffset

	@property
	def iqImbalance(self):
		"""iqImbalance commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_iqImbalance'):
			from .IqImbalance import IqImbalance
			self._iqImbalance = IqImbalance(self._core, self._cmd_group)
		return self._iqImbalance

	@property
	def adroop(self):
		"""adroop commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_adroop'):
			from .Adroop import Adroop
			self._adroop = Adroop(self._core, self._cmd_group)
		return self._adroop

	@property
	def channel(self):
		"""channel commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_channel'):
			from .Channel import Channel
			self._channel = Channel(self._core, self._cmd_group)
		return self._channel

	@property
	def srError(self):
		"""srError commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_srError'):
			from .SrError import SrError
			self._srError = SrError(self._core, self._cmd_group)
		return self._srError

	def clone(self) -> 'Normalize':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Normalize(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
