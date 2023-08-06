from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IfFrequency:
	"""IfFrequency commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ifFrequency", core, parent)

	def set(self, value: float) -> None:
		"""SCPI: OUTPut:IF:IFFRequency \n
		Snippet: driver.applications.k9X11Ad.output.ifreq.ifFrequency.set(value = 1.0) \n
		This command defines the frequency for the IF output of the R&S FSW. The IF frequency of the signal is converted
		accordingly. This command is available in the time domain and if the IF/VIDEO/DEMOD output is configured for IF. \n
			:param value: Unit: HZ
		"""
		param = Conversions.decimal_value_to_str(value)
		self._core.io.write(f'OUTPut:IF:IFFRequency {param}')

	def get(self) -> float:
		"""SCPI: OUTPut:IF:IFFRequency \n
		Snippet: value: float = driver.applications.k9X11Ad.output.ifreq.ifFrequency.get() \n
		This command defines the frequency for the IF output of the R&S FSW. The IF frequency of the signal is converted
		accordingly. This command is available in the time domain and if the IF/VIDEO/DEMOD output is configured for IF. \n
			:return: value: No help available"""
		response = self._core.io.query_str(f'OUTPut:IF:IFFRequency?')
		return Conversions.str_to_float(response)
