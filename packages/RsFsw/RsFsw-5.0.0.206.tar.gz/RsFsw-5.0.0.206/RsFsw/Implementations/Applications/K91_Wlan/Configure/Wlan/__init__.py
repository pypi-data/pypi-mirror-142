from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Wlan:
	"""Wlan commands group definition. 48 total commands, 11 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("wlan", core, parent)

	@property
	def mimo(self):
		"""mimo commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_mimo'):
			from .Mimo import Mimo
			self._mimo = Mimo(self._core, self._cmd_group)
		return self._mimo

	@property
	def dutConfig(self):
		"""dutConfig commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dutConfig'):
			from .DutConfig import DutConfig
			self._dutConfig = DutConfig(self._core, self._cmd_group)
		return self._dutConfig

	@property
	def antMatrix(self):
		"""antMatrix commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_antMatrix'):
			from .AntMatrix import AntMatrix
			self._antMatrix = AntMatrix(self._core, self._cmd_group)
		return self._antMatrix

	@property
	def gtime(self):
		"""gtime commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_gtime'):
			from .Gtime import Gtime
			self._gtime = Gtime(self._core, self._cmd_group)
		return self._gtime

	@property
	def ruConfig(self):
		"""ruConfig commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_ruConfig'):
			from .RuConfig import RuConfig
			self._ruConfig = RuConfig(self._core, self._cmd_group)
		return self._ruConfig

	@property
	def rsync(self):
		"""rsync commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_rsync'):
			from .Rsync import Rsync
			self._rsync = Rsync(self._core, self._cmd_group)
		return self._rsync

	@property
	def stbc(self):
		"""stbc commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_stbc'):
			from .Stbc import Stbc
			self._stbc = Stbc(self._core, self._cmd_group)
		return self._stbc

	@property
	def extension(self):
		"""extension commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_extension'):
			from .Extension import Extension
			self._extension = Extension(self._core, self._cmd_group)
		return self._extension

	@property
	def smapping(self):
		"""smapping commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_smapping'):
			from .Smapping import Smapping
			self._smapping = Smapping(self._core, self._cmd_group)
		return self._smapping

	@property
	def payload(self):
		"""payload commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_payload'):
			from .Payload import Payload
			self._payload = Payload(self._core, self._cmd_group)
		return self._payload

	@property
	def pvError(self):
		"""pvError commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_pvError'):
			from .PvError import PvError
			self._pvError = PvError(self._core, self._cmd_group)
		return self._pvError

	def clone(self) -> 'Wlan':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Wlan(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
