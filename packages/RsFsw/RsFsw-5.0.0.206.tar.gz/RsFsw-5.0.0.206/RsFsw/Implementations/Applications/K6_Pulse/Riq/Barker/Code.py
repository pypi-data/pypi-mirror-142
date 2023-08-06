from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Code:
	"""Code commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("code", core, parent)

	def set(self, code_length: int) -> None:
		"""SCPI: RIQ:BARKer:CODE \n
		Snippet: driver.applications.k6Pulse.riq.barker.code.set(code_length = 1) \n
		This command selects the reference IQ barker code length for time sidelobe measurements. \n
			:param code_length: No help available
		"""
		param = Conversions.decimal_value_to_str(code_length)
		self._core.io.write(f'RIQ:BARKer:CODE {param}')

	def get(self) -> int:
		"""SCPI: RIQ:BARKer:CODE \n
		Snippet: value: int = driver.applications.k6Pulse.riq.barker.code.get() \n
		This command selects the reference IQ barker code length for time sidelobe measurements. \n
			:return: code_length: No help available"""
		response = self._core.io.query_str(f'RIQ:BARKer:CODE?')
		return Conversions.str_to_int(response)
