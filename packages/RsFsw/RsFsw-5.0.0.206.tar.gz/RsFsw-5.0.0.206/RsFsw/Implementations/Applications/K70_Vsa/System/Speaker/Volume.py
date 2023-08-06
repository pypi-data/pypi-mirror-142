from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Volume:
	"""Volume commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("volume", core, parent)

	def set(self, volume: float) -> None:
		"""SCPI: SYSTem:SPEaker:VOLume \n
		Snippet: driver.applications.k70Vsa.system.speaker.volume.set(volume = 1.0) \n
		No command help available \n
			:param volume: No help available
		"""
		param = Conversions.decimal_value_to_str(volume)
		self._core.io.write(f'SYSTem:SPEaker:VOLume {param}')

	def get(self) -> float:
		"""SCPI: SYSTem:SPEaker:VOLume \n
		Snippet: value: float = driver.applications.k70Vsa.system.speaker.volume.get() \n
		No command help available \n
			:return: volume: No help available"""
		response = self._core.io.query_str(f'SYSTem:SPEaker:VOLume?')
		return Conversions.str_to_float(response)
