from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Event:
	"""Event commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("event", core, parent)

	def set(self, channel_name: str) -> None:
		"""SCPI: SYSTem:COMMunicate:INTernal[:COMPleted]:EVENt \n
		Snippet: driver.system.communicate.internal.completed.event.set(channel_name = '1') \n
		No command help available \n
			:param channel_name: No help available
		"""
		param = Conversions.value_to_quoted_str(channel_name)
		self._core.io.write(f'SYSTem:COMMunicate:INTernal:COMPleted:EVENt {param}')

	def get(self) -> str:
		"""SCPI: SYSTem:COMMunicate:INTernal[:COMPleted]:EVENt \n
		Snippet: value: str = driver.system.communicate.internal.completed.event.get() \n
		No command help available \n
			:return: channel_name: No help available"""
		response = self._core.io.query_str(f'SYSTem:COMMunicate:INTernal:COMPleted:EVENt?')
		return trim_str_response(response)
