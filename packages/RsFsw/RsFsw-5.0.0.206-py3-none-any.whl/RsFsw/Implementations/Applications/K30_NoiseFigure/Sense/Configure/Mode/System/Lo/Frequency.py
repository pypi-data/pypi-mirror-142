from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Frequency:
	"""Frequency commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frequency", core, parent)

	def set(self, lo_frequency: float) -> None:
		"""SCPI: [SENSe]:CONFigure:MODE:SYSTem:LO:FREQuency \n
		Snippet: driver.applications.k30NoiseFigure.sense.configure.mode.system.lo.frequency.set(lo_frequency = 1.0) \n
		This command defines the frequency for DUTs with a fixed LO. \n
			:param lo_frequency: Range: 0 Hz to 100 GHz, Unit: HZ
		"""
		param = Conversions.decimal_value_to_str(lo_frequency)
		self._core.io.write(f'SENSe:CONFigure:MODE:SYSTem:LO:FREQuency {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:CONFigure:MODE:SYSTem:LO:FREQuency \n
		Snippet: value: float = driver.applications.k30NoiseFigure.sense.configure.mode.system.lo.frequency.get() \n
		This command defines the frequency for DUTs with a fixed LO. \n
			:return: lo_frequency: Range: 0 Hz to 100 GHz, Unit: HZ"""
		response = self._core.io.query_str(f'SENSe:CONFigure:MODE:SYSTem:LO:FREQuency?')
		return Conversions.str_to_float(response)
