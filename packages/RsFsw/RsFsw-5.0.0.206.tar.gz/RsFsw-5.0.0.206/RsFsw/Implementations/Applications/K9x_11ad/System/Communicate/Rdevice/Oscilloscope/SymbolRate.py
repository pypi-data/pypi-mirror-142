from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SymbolRate:
	"""SymbolRate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("symbolRate", core, parent)

	def set(self, sample_rate: float) -> None:
		"""SCPI: SYSTem:COMMunicate:RDEVice:OSCilloscope:SRATe \n
		Snippet: driver.applications.k9X11Ad.system.communicate.rdevice.oscilloscope.symbolRate.set(sample_rate = 1.0) \n
		Determines whether the 10 GHz mode (default) or 20 GHz mode of the connected oscilloscope is used. The 20 GHZ mode
		achieves a higher decimation gain, but reduces the record length by half. \n
			:param sample_rate: 10 GHz | 20 GHz No other sample rate values are allowed. Unit: HZ
		"""
		param = Conversions.decimal_value_to_str(sample_rate)
		self._core.io.write(f'SYSTem:COMMunicate:RDEVice:OSCilloscope:SRATe {param}')

	def get(self) -> float:
		"""SCPI: SYSTem:COMMunicate:RDEVice:OSCilloscope:SRATe \n
		Snippet: value: float = driver.applications.k9X11Ad.system.communicate.rdevice.oscilloscope.symbolRate.get() \n
		Determines whether the 10 GHz mode (default) or 20 GHz mode of the connected oscilloscope is used. The 20 GHZ mode
		achieves a higher decimation gain, but reduces the record length by half. \n
			:return: sample_rate: No help available"""
		response = self._core.io.query_str(f'SYSTem:COMMunicate:RDEVice:OSCilloscope:SRATe?')
		return Conversions.str_to_float(response)
