from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Frequency:
	"""Frequency commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frequency", core, parent)

	def set(self, frequency: float) -> None:
		"""SCPI: [SENSe]:CONFigure:MODE:SYSTem:IF:FREQuency \n
		Snippet: driver.applications.k30NoiseFigure.sense.configure.mode.system.ifreq.frequency.set(frequency = 1.0) \n
		This command defines the frequency for DUTs with a fixed IF. \n
			:param frequency: Range: 0 Hz to 100 GHz, Unit: HZ
		"""
		param = Conversions.decimal_value_to_str(frequency)
		self._core.io.write(f'SENSe:CONFigure:MODE:SYSTem:IF:FREQuency {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:CONFigure:MODE:SYSTem:IF:FREQuency \n
		Snippet: value: float = driver.applications.k30NoiseFigure.sense.configure.mode.system.ifreq.frequency.get() \n
		This command defines the frequency for DUTs with a fixed IF. \n
			:return: frequency: Range: 0 Hz to 100 GHz, Unit: HZ"""
		response = self._core.io.query_str(f'SENSe:CONFigure:MODE:SYSTem:IF:FREQuency?')
		return Conversions.str_to_float(response)
