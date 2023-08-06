from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tables:
	"""Tables commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tables", core, parent)

	def set(self, channel_name: str) -> None:
		"""SCPI: SYSTem:COMMunicate:INTernal[:COMMand]:TABLes \n
		Snippet: driver.system.communicate.internal.command.tables.set(channel_name = '1') \n
		No command help available \n
			:param channel_name: No help available
		"""
		param = Conversions.value_to_quoted_str(channel_name)
		self._core.io.write(f'SYSTem:COMMunicate:INTernal:COMMand:TABLes {param}')

	def get(self) -> str:
		"""SCPI: SYSTem:COMMunicate:INTernal[:COMMand]:TABLes \n
		Snippet: value: str = driver.system.communicate.internal.command.tables.get() \n
		No command help available \n
			:return: channel_name: No help available"""
		response = self._core.io.query_str(f'SYSTem:COMMunicate:INTernal:COMMand:TABLes?')
		return trim_str_response(response)
