from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Demod:
	"""Demod commands group definition. 30 total commands, 6 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("demod", core, parent)

	@property
	def cestimation(self):
		"""cestimation commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cestimation'):
			from .Cestimation import Cestimation
			self._cestimation = Cestimation(self._core, self._cmd_group)
		return self._cestimation

	@property
	def txArea(self):
		"""txArea commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_txArea'):
			from .TxArea import TxArea
			self._txArea = TxArea(self._core, self._cmd_group)
		return self._txArea

	@property
	def fft(self):
		"""fft commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_fft'):
			from .Fft import Fft
			self._fft = Fft(self._core, self._cmd_group)
		return self._fft

	@property
	def filterPy(self):
		"""filterPy commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_filterPy'):
			from .FilterPy import FilterPy
			self._filterPy = FilterPy(self._core, self._cmd_group)
		return self._filterPy

	@property
	def formatPy(self):
		"""formatPy commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_formatPy'):
			from .FormatPy import FormatPy
			self._formatPy = FormatPy(self._core, self._cmd_group)
		return self._formatPy

	@property
	def interpolate(self):
		"""interpolate commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_interpolate'):
			from .Interpolate import Interpolate
			self._interpolate = Interpolate(self._core, self._cmd_group)
		return self._interpolate

	def clone(self) -> 'Demod':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Demod(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
