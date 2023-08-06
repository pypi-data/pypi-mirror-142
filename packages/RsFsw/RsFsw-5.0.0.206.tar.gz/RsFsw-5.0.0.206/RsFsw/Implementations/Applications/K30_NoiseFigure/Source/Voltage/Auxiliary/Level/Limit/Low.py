from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Low:
	"""Low commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("low", core, parent)

	def set(self, voltage: float) -> None:
		"""SCPI: SOURce:VOLTage:AUX:LEVel:LIMit:LOW \n
		Snippet: driver.applications.k30NoiseFigure.source.voltage.auxiliary.level.limit.low.set(voltage = 1.0) \n
		No command help available \n
			:param voltage: No help available
		"""
		param = Conversions.decimal_value_to_str(voltage)
		self._core.io.write(f'SOURce:VOLTage:AUX:LEVel:LIMit:LOW {param}')

	def get(self) -> float:
		"""SCPI: SOURce:VOLTage:AUX:LEVel:LIMit:LOW \n
		Snippet: value: float = driver.applications.k30NoiseFigure.source.voltage.auxiliary.level.limit.low.get() \n
		No command help available \n
			:return: voltage: No help available"""
		response = self._core.io.query_str(f'SOURce:VOLTage:AUX:LEVel:LIMit:LOW?')
		return Conversions.str_to_float(response)
