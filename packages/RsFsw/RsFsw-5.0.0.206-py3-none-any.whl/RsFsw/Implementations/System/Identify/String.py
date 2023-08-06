from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class String:
	"""String commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("string", core, parent)

	def set(self, string: str) -> None:
		"""SCPI: SYSTem:IDENtify[:STRing] \n
		Snippet: driver.system.identify.string.set(string = '1') \n
		This command defines the response to *IDN?. \n
			:param string: String containing the description of the instrument.
		"""
		param = Conversions.value_to_quoted_str(string)
		self._core.io.write(f'SYSTem:IDENtify:STRing {param}')

	def get(self) -> str:
		"""SCPI: SYSTem:IDENtify[:STRing] \n
		Snippet: value: str = driver.system.identify.string.get() \n
		This command defines the response to *IDN?. \n
			:return: string: String containing the description of the instrument."""
		response = self._core.io.query_str(f'SYSTem:IDENtify:STRing?')
		return trim_str_response(response)
