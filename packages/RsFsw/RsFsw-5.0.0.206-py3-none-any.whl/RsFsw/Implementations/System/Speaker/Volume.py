from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Volume:
	"""Volume commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("volume", core, parent)

	def set(self, volume: float) -> None:
		"""SCPI: SYSTem:SPEaker:VOLume \n
		Snippet: driver.system.speaker.volume.set(volume = 1.0) \n
		This command defines the volume of the built-in loudspeaker for demodulated signals. This setting is maintained for all
		applications. The command is available in the time domain in Spectrum mode and in Analog Modulation Analysis mode. \n
			:param volume: Percentage of the maximum possible volume. Range: 0 to 1
		"""
		param = Conversions.decimal_value_to_str(volume)
		self._core.io.write(f'SYSTem:SPEaker:VOLume {param}')

	def get(self) -> float:
		"""SCPI: SYSTem:SPEaker:VOLume \n
		Snippet: value: float = driver.system.speaker.volume.get() \n
		This command defines the volume of the built-in loudspeaker for demodulated signals. This setting is maintained for all
		applications. The command is available in the time domain in Spectrum mode and in Analog Modulation Analysis mode. \n
			:return: volume: Percentage of the maximum possible volume. Range: 0 to 1"""
		response = self._core.io.query_str(f'SYSTem:SPEaker:VOLume?')
		return Conversions.str_to_float(response)
