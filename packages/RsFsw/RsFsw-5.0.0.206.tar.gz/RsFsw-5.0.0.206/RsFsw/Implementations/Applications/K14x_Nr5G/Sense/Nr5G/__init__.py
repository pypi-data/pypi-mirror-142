from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Nr5G:
	"""Nr5G commands group definition. 48 total commands, 14 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nr5G", core, parent)

	@property
	def acPower(self):
		"""acPower commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_acPower'):
			from .AcPower import AcPower
			self._acPower = AcPower(self._core, self._cmd_group)
		return self._acPower

	@property
	def cc(self):
		"""cc commands group. 11 Sub-classes, 0 commands."""
		if not hasattr(self, '_cc'):
			from .Cc import Cc
			self._cc = Cc(self._core, self._cmd_group)
		return self._cc

	@property
	def demod(self):
		"""demod commands group. 10 Sub-classes, 0 commands."""
		if not hasattr(self, '_demod'):
			from .Demod import Demod
			self._demod = Demod(self._core, self._cmd_group)
		return self._demod

	@property
	def emHold(self):
		"""emHold commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_emHold'):
			from .EmHold import EmHold
			self._emHold = EmHold(self._core, self._cmd_group)
		return self._emHold

	@property
	def tdView(self):
		"""tdView commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tdView'):
			from .TdView import TdView
			self._tdView = TdView(self._core, self._cmd_group)
		return self._tdView

	@property
	def efilter(self):
		"""efilter commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_efilter'):
			from .Efilter import Efilter
			self._efilter = Efilter(self._core, self._cmd_group)
		return self._efilter

	@property
	def fevents(self):
		"""fevents commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_fevents'):
			from .Fevents import Fevents
			self._fevents = Fevents(self._core, self._cmd_group)
		return self._fevents

	@property
	def frame(self):
		"""frame commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_frame'):
			from .Frame import Frame
			self._frame = Frame(self._core, self._cmd_group)
		return self._frame

	@property
	def iq(self):
		"""iq commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_iq'):
			from .Iq import Iq
			self._iq = Iq(self._core, self._cmd_group)
		return self._iq

	@property
	def ooPower(self):
		"""ooPower commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ooPower'):
			from .OoPower import OoPower
			self._ooPower = OoPower(self._core, self._cmd_group)
		return self._ooPower

	@property
	def rantenna(self):
		"""rantenna commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rantenna'):
			from .Rantenna import Rantenna
			self._rantenna = Rantenna(self._core, self._cmd_group)
		return self._rantenna

	@property
	def rsummary(self):
		"""rsummary commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_rsummary'):
			from .Rsummary import Rsummary
			self._rsummary = Rsummary(self._core, self._cmd_group)
		return self._rsummary

	@property
	def segment(self):
		"""segment commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_segment'):
			from .Segment import Segment
			self._segment = Segment(self._core, self._cmd_group)
		return self._segment

	@property
	def tracking(self):
		"""tracking commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_tracking'):
			from .Tracking import Tracking
			self._tracking = Tracking(self._core, self._cmd_group)
		return self._tracking

	def clone(self) -> 'Nr5G':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Nr5G(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
