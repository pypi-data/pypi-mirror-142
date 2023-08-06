from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Average:
	"""Average commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("average", core, parent)

	def set(self, value: float) -> None:
		"""SCPI: CONFigure:BURSt:PVT:AVERage \n
		Snippet: driver.applications.k91Wlan.configure.burst.pvt.average.set(value = 1.0) \n
		Defines the number of samples used to adjust the length of the smoothing filter for PVT measurement. This command is only
		available for IEEE 802.11b, g (DSSS) standards. \n
			:param value: No help available
		"""
		param = Conversions.decimal_value_to_str(value)
		self._core.io.write(f'CONFigure:BURSt:PVT:AVERage {param}')

	def get(self) -> float:
		"""SCPI: CONFigure:BURSt:PVT:AVERage \n
		Snippet: value: float = driver.applications.k91Wlan.configure.burst.pvt.average.get() \n
		Defines the number of samples used to adjust the length of the smoothing filter for PVT measurement. This command is only
		available for IEEE 802.11b, g (DSSS) standards. \n
			:return: value: No help available"""
		response = self._core.io.query_str(f'CONFigure:BURSt:PVT:AVERage?')
		return Conversions.str_to_float(response)
