from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Password:
	"""Password commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("password", core, parent)

	def set(self, password: str) -> None:
		"""SCPI: SYSTem:LXI:PASSword \n
		Snippet: driver.system.lxi.password.set(password = '1') \n
		This command defines the 'LAN' password. \n
			:param password: String containing the password.
		"""
		param = Conversions.value_to_quoted_str(password)
		self._core.io.write(f'SYSTem:LXI:PASSword {param}')

	def get(self) -> str:
		"""SCPI: SYSTem:LXI:PASSword \n
		Snippet: value: str = driver.system.lxi.password.get() \n
		This command defines the 'LAN' password. \n
			:return: password: String containing the password."""
		response = self._core.io.query_str(f'SYSTem:LXI:PASSword?')
		return trim_str_response(response)
