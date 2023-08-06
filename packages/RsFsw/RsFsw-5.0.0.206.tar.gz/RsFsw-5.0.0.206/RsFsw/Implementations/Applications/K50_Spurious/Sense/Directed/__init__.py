from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Directed:
	"""Directed commands group definition. 11 total commands, 7 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("directed", core, parent)

	@property
	def settings(self):
		"""settings commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_settings'):
			from .Settings import Settings
			self._settings = Settings(self._core, self._cmd_group)
		return self._settings

	@property
	def nfft(self):
		"""nfft commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nfft'):
			from .Nfft import Nfft
			self._nfft = Nfft(self._core, self._cmd_group)
		return self._nfft

	@property
	def refLevel(self):
		"""refLevel commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_refLevel'):
			from .RefLevel import RefLevel
			self._refLevel = RefLevel(self._core, self._cmd_group)
		return self._refLevel

	@property
	def inputPy(self):
		"""inputPy commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_inputPy'):
			from .InputPy import InputPy
			self._inputPy = InputPy(self._core, self._cmd_group)
		return self._inputPy

	@property
	def loffset(self):
		"""loffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_loffset'):
			from .Loffset import Loffset
			self._loffset = Loffset(self._core, self._cmd_group)
		return self._loffset

	@property
	def mfRbw(self):
		"""mfRbw commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mfRbw'):
			from .MfRbw import MfRbw
			self._mfRbw = MfRbw(self._core, self._cmd_group)
		return self._mfRbw

	@property
	def pexcursion(self):
		"""pexcursion commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pexcursion'):
			from .Pexcursion import Pexcursion
			self._pexcursion = Pexcursion(self._core, self._cmd_group)
		return self._pexcursion

	def save(self, filename: str) -> None:
		"""SCPI: [SENSe]:DIRected:SAVE \n
		Snippet: driver.applications.k50Spurious.sense.directed.save(filename = '1') \n
		Saves the current directed search configuration to a user-defined .csv file for later use.
		The result is a comma-separated list of values with the following syntax for each span: <No>,<Frequency>,<SearchSpan>,
		<DetThreshold>,<SNR>,<DetectMode> For details on the parameters see 'Directed Search Measurement settings') . \n
			:param filename: No help available
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SENSe:DIRected:SAVE {param}')

	def load(self, filename: str) -> None:
		"""SCPI: [SENSe]:DIRected:LOAD \n
		Snippet: driver.applications.k50Spurious.sense.directed.load(filename = '1') \n
		Loads a stored search configuration from a .csv file. The current settings in the table are overwritten by the settings
		in the file! \n
			:param filename: No help available
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SENSe:DIRected:LOAD {param}')

	def clone(self) -> 'Directed':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Directed(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
