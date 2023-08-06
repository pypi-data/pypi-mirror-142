from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class High:
	"""High commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("high", core, parent)

	def set(self, loss_high: float) -> None:
		"""SCPI: [SENSe]:MIXer:LOSS:HIGH \n
		Snippet: driver.sense.mixer.loss.high.set(loss_high = 1.0) \n
		This command defines the average conversion loss to be used for the entire high (second) range. \n
			:param loss_high: No help available
		"""
		param = Conversions.decimal_value_to_str(loss_high)
		self._core.io.write(f'SENSe:MIXer:LOSS:HIGH {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:MIXer:LOSS:HIGH \n
		Snippet: value: float = driver.sense.mixer.loss.high.get() \n
		This command defines the average conversion loss to be used for the entire high (second) range. \n
			:return: loss_high: No help available"""
		response = self._core.io.query_str(f'SENSe:MIXer:LOSS:HIGH?')
		return Conversions.str_to_float(response)
