from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Uncertainty:
	"""Uncertainty commands group definition. 29 total commands, 7 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("uncertainty", core, parent)

	@property
	def sanalyzer(self):
		"""sanalyzer commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_sanalyzer'):
			from .Sanalyzer import Sanalyzer
			self._sanalyzer = Sanalyzer(self._core, self._cmd_group)
		return self._sanalyzer

	@property
	def result(self):
		"""result commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_result'):
			from .Result import Result
			self._result = Result(self._core, self._cmd_group)
		return self._result

	@property
	def common(self):
		"""common commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_common'):
			from .Common import Common
			self._common = Common(self._core, self._cmd_group)
		return self._common

	@property
	def preamp(self):
		"""preamp commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_preamp'):
			from .Preamp import Preamp
			self._preamp = Preamp(self._core, self._cmd_group)
		return self._preamp

	@property
	def enr(self):
		"""enr commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_enr'):
			from .Enr import Enr
			self._enr = Enr(self._core, self._cmd_group)
		return self._enr

	@property
	def data(self):
		"""data commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_data'):
			from .Data import Data
			self._data = Data(self._core, self._cmd_group)
		return self._data

	@property
	def match(self):
		"""match commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_match'):
			from .Match import Match
			self._match = Match(self._core, self._cmd_group)
		return self._match

	def clone(self) -> 'Uncertainty':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Uncertainty(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
