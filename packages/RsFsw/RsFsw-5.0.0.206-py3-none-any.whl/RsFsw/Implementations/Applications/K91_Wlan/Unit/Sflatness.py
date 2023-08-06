from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sflatness:
	"""Sflatness commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sflatness", core, parent)

	def set(self, unit: enums.FlatnessUnit) -> None:
		"""SCPI: UNIT:SFLatness \n
		Snippet: driver.applications.k91Wlan.unit.sflatness.set(unit = enums.FlatnessUnit.DB) \n
		This command switches between relative (dB) and absolute (dBm) results for Spectrum Flatness results (see 'Spectrum
		Flatness') . \n
			:param unit: DB | DBM
		"""
		param = Conversions.enum_scalar_to_str(unit, enums.FlatnessUnit)
		self._core.io.write(f'UNIT:SFLatness {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.FlatnessUnit:
		"""SCPI: UNIT:SFLatness \n
		Snippet: value: enums.FlatnessUnit = driver.applications.k91Wlan.unit.sflatness.get() \n
		This command switches between relative (dB) and absolute (dBm) results for Spectrum Flatness results (see 'Spectrum
		Flatness') . \n
			:return: unit: DB | DBM"""
		response = self._core.io.query_str(f'UNIT:SFLatness?')
		return Conversions.str_to_scalar_enum(response, enums.FlatnessUnit)
