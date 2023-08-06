from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Gain:
	"""Gain commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("gain", core, parent)

	def set(self, gain: float) -> None:
		"""SCPI: SYSTem:CONFigure:DUT:GAIN \n
		Snippet: driver.applications.k30NoiseFigure.system.configure.dut.gain.set(gain = 1.0) \n
		This command defines the expected gain of the DUT. The application uses the gain for automatic reference level detection. \n
			:param gain: Range: 10 to 1000, Unit: DB
		"""
		param = Conversions.decimal_value_to_str(gain)
		self._core.io.write(f'SYSTem:CONFigure:DUT:GAIN {param}')

	def get(self) -> float:
		"""SCPI: SYSTem:CONFigure:DUT:GAIN \n
		Snippet: value: float = driver.applications.k30NoiseFigure.system.configure.dut.gain.get() \n
		This command defines the expected gain of the DUT. The application uses the gain for automatic reference level detection. \n
			:return: gain: Range: 10 to 1000, Unit: DB"""
		response = self._core.io.query_str(f'SYSTem:CONFigure:DUT:GAIN?')
		return Conversions.str_to_float(response)
