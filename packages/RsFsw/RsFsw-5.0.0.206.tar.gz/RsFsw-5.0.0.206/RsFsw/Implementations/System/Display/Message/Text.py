from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Text:
	"""Text commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("text", core, parent)

	def set(self, message: str) -> None:
		"""SCPI: SYSTem:DISPlay:MESSage[:TEXT] \n
		Snippet: driver.system.display.message.text.set(message = '1') \n
		No command help available \n
			:param message: No help available
		"""
		param = Conversions.value_to_quoted_str(message)
		self._core.io.write(f'SYSTem:DISPlay:MESSage:TEXT {param}')

	def get(self) -> str:
		"""SCPI: SYSTem:DISPlay:MESSage[:TEXT] \n
		Snippet: value: str = driver.system.display.message.text.get() \n
		No command help available \n
			:return: message: No help available"""
		response = self._core.io.query_str(f'SYSTem:DISPlay:MESSage:TEXT?')
		return trim_str_response(response)
