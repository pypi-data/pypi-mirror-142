from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Iq:
	"""Iq commands group definition. 19 total commands, 9 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("iq", core, parent)

	@property
	def data(self):
		"""data commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_data'):
			from .Data import Data
			self._data = Data(self._core, self._cmd_group)
		return self._data

	@property
	def egate(self):
		"""egate commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_egate'):
			from .Egate import Egate
			self._egate = Egate(self._core, self._cmd_group)
		return self._egate

	@property
	def bandwidth(self):
		"""bandwidth commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bandwidth'):
			from .Bandwidth import Bandwidth
			self._bandwidth = Bandwidth(self._core, self._cmd_group)
		return self._bandwidth

	@property
	def eval(self):
		"""eval commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_eval'):
			from .Eval import Eval
			self._eval = Eval(self._core, self._cmd_group)
		return self._eval

	@property
	def diqFilter(self):
		"""diqFilter commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_diqFilter'):
			from .DiqFilter import DiqFilter
			self._diqFilter = DiqFilter(self._core, self._cmd_group)
		return self._diqFilter

	@property
	def apcon(self):
		"""apcon commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_apcon'):
			from .Apcon import Apcon
			self._apcon = Apcon(self._core, self._cmd_group)
		return self._apcon

	@property
	def file(self):
		"""file commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_file'):
			from .File import File
			self._file = File(self._core, self._cmd_group)
		return self._file

	@property
	def lcapture(self):
		"""lcapture commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_lcapture'):
			from .Lcapture import Lcapture
			self._lcapture = Lcapture(self._core, self._cmd_group)
		return self._lcapture

	@property
	def scapture(self):
		"""scapture commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_scapture'):
			from .Scapture import Scapture
			self._scapture = Scapture(self._core, self._cmd_group)
		return self._scapture

	def clone(self) -> 'Iq':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Iq(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
