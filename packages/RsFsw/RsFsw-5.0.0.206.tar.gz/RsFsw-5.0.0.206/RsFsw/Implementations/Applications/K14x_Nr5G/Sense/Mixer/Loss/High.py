from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class High:
	"""High commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("high", core, parent)

	def set(self, average: float) -> None:
		"""SCPI: [SENSe]:MIXer:LOSS:HIGH \n
		Snippet: driver.applications.k14Xnr5G.sense.mixer.loss.high.set(average = 1.0) \n
		No command help available \n
			:param average: No help available
		"""
		param = Conversions.decimal_value_to_str(average)
		self._core.io.write(f'SENSe:MIXer:LOSS:HIGH {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:MIXer:LOSS:HIGH \n
		Snippet: value: float = driver.applications.k14Xnr5G.sense.mixer.loss.high.get() \n
		No command help available \n
			:return: average: No help available"""
		response = self._core.io.query_str(f'SENSe:MIXer:LOSS:HIGH?')
		return Conversions.str_to_float(response)
