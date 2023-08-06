from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Info:
	"""Info commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("info", core, parent)

	def get(self) -> str:
		"""SCPI: SYSTem:LXI:INFO \n
		Snippet: value: str = driver.system.lxi.info.get() \n
		No command help available \n
			:return: lxi_info: No help available"""
		response = self._core.io.query_str(f'SYSTem:LXI:INFO?')
		return trim_str_response(response)
