from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Espectrum:
	"""Espectrum commands group definition. 8 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("espectrum", core, parent)

	@property
	def mode(self):
		"""mode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mode'):
			from .Mode import Mode
			self._mode = Mode(self._core, self._cmd_group)
		return self._mode

	@property
	def check(self):
		"""check commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_check'):
			from .Check import Check
			self._check = Check(self._core, self._cmd_group)
		return self._check

	@property
	def value(self):
		"""value commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_value'):
			from .Value import Value
			self._value = Value(self._core, self._cmd_group)
		return self._value

	@property
	def pclass(self):
		"""pclass commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_pclass'):
			from .Pclass import Pclass
			self._pclass = Pclass(self._core, self._cmd_group)
		return self._pclass

	@property
	def limits(self):
		"""limits commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_limits'):
			from .Limits import Limits
			self._limits = Limits(self._core, self._cmd_group)
		return self._limits

	def clone(self) -> 'Espectrum':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Espectrum(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
