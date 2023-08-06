from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Stime:
	"""Stime commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("stime", core, parent)

	def set(self, settling_time: float) -> None:
		"""SCPI: SYSTem:CONFigure:DUT:STIMe \n
		Snippet: driver.applications.k30NoiseFigure.system.configure.dut.stime.set(settling_time = 1.0) \n
		This command defines the settling time of the noise source. \n
			:param settling_time: Range: 0 s to 20 s, Unit: S
		"""
		param = Conversions.decimal_value_to_str(settling_time)
		self._core.io.write(f'SYSTem:CONFigure:DUT:STIMe {param}')

	def get(self) -> float:
		"""SCPI: SYSTem:CONFigure:DUT:STIMe \n
		Snippet: value: float = driver.applications.k30NoiseFigure.system.configure.dut.stime.get() \n
		This command defines the settling time of the noise source. \n
			:return: settling_time: Range: 0 s to 20 s, Unit: S"""
		response = self._core.io.query_str(f'SYSTem:CONFigure:DUT:STIMe?')
		return Conversions.str_to_float(response)
