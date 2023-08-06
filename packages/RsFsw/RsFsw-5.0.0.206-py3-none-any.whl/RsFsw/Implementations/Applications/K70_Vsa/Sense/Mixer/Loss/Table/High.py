from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class High:
	"""High commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("high", core, parent)

	def set(self, value: str) -> None:
		"""SCPI: [SENSe]:MIXer:LOSS:TABLe:HIGH \n
		Snippet: driver.applications.k70Vsa.sense.mixer.loss.table.high.set(value = '1') \n
		This command defines the conversion loss table to be used for the high (second) range. \n
			:param value: No help available
		"""
		param = Conversions.value_to_quoted_str(value)
		self._core.io.write(f'SENSe:MIXer:LOSS:TABLe:HIGH {param}')

	def get(self) -> str:
		"""SCPI: [SENSe]:MIXer:LOSS:TABLe:HIGH \n
		Snippet: value: str = driver.applications.k70Vsa.sense.mixer.loss.table.high.get() \n
		This command defines the conversion loss table to be used for the high (second) range. \n
			:return: value: No help available"""
		response = self._core.io.query_str(f'SENSe:MIXer:LOSS:TABLe:HIGH?')
		return trim_str_response(response)
