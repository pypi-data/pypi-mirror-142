from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Low:
	"""Low commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("low", core, parent)

	def set(self, bias_low: float) -> None:
		"""SCPI: [SENSe]:MIXer:BIAS[:LOW] \n
		Snippet: driver.applications.k50Spurious.sense.mixer.bias.low.set(bias_low = 1.0) \n
		This command defines the bias current for the low (first) range. . This command is only available if the external mixer
		is active (see [SENSe:]MIXer<x>[:STATe]) . \n
			:param bias_low: No help available
		"""
		param = Conversions.decimal_value_to_str(bias_low)
		self._core.io.write(f'SENSe:MIXer:BIAS:LOW {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:MIXer:BIAS[:LOW] \n
		Snippet: value: float = driver.applications.k50Spurious.sense.mixer.bias.low.get() \n
		This command defines the bias current for the low (first) range. . This command is only available if the external mixer
		is active (see [SENSe:]MIXer<x>[:STATe]) . \n
			:return: bias_low: No help available"""
		response = self._core.io.query_str(f'SENSe:MIXer:BIAS:LOW?')
		return Conversions.str_to_float(response)
