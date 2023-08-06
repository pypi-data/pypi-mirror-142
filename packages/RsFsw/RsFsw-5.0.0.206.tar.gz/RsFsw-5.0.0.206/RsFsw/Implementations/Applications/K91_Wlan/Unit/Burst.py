from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Burst:
	"""Burst commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("burst", core, parent)

	def set(self, unit: enums.BurstUnit) -> None:
		"""SCPI: UNIT:BURSt \n
		Snippet: driver.applications.k91Wlan.unit.burst.set(unit = enums.BurstUnit.SAMPle) \n
		This command specifies the units for PPDU length results (see method RsFsw.Applications.K91_Wlan.Fetch.Burst.Lengths.
		get_) . \n
			:param unit: SYMBol | SAMPle SYMBol Number of OFDM data symbols for each analyzed PPDU. Preamble symbols are NOT included. SAMPle Number of samples each analyzed PPDU contains. Tip: To obtain the result in seconds, divide the number of samples by the input sample rate. This value is indicated as 'Sample Rate Fs' in the channel bar.
		"""
		param = Conversions.enum_scalar_to_str(unit, enums.BurstUnit)
		self._core.io.write(f'UNIT:BURSt {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.BurstUnit:
		"""SCPI: UNIT:BURSt \n
		Snippet: value: enums.BurstUnit = driver.applications.k91Wlan.unit.burst.get() \n
		This command specifies the units for PPDU length results (see method RsFsw.Applications.K91_Wlan.Fetch.Burst.Lengths.
		get_) . \n
			:return: unit: SYMBol | SAMPle SYMBol Number of OFDM data symbols for each analyzed PPDU. Preamble symbols are NOT included. SAMPle Number of samples each analyzed PPDU contains. Tip: To obtain the result in seconds, divide the number of samples by the input sample rate. This value is indicated as 'Sample Rate Fs' in the channel bar."""
		response = self._core.io.query_str(f'UNIT:BURSt?')
		return Conversions.str_to_scalar_enum(response, enums.BurstUnit)
