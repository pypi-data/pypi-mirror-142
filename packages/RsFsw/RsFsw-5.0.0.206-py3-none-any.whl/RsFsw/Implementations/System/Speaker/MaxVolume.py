from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MaxVolume:
	"""MaxVolume commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("maxVolume", core, parent)

	def set(self, volume: float) -> None:
		"""SCPI: SYSTem:SPEaker:MAXVolume \n
		Snippet: driver.system.speaker.maxVolume.set(volume = 1.0) \n
		No command help available \n
			:param volume: No help available
		"""
		param = Conversions.decimal_value_to_str(volume)
		self._core.io.write(f'SYSTem:SPEaker:MAXVolume {param}')

	def get(self) -> float:
		"""SCPI: SYSTem:SPEaker:MAXVolume \n
		Snippet: value: float = driver.system.speaker.maxVolume.get() \n
		No command help available \n
			:return: volume: No help available"""
		response = self._core.io.query_str(f'SYSTem:SPEaker:MAXVolume?')
		return Conversions.str_to_float(response)
