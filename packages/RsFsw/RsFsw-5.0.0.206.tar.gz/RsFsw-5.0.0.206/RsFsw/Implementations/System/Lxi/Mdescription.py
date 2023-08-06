from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mdescription:
	"""Mdescription commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mdescription", core, parent)

	def set(self, description: str) -> None:
		"""SCPI: SYSTem:LXI:MDEScription \n
		Snippet: driver.system.lxi.mdescription.set(description = '1') \n
		This command defines the 'LAN' instrument description. \n
			:param description: String containing the instrument description.
		"""
		param = Conversions.value_to_quoted_str(description)
		self._core.io.write(f'SYSTem:LXI:MDEScription {param}')

	def get(self) -> str:
		"""SCPI: SYSTem:LXI:MDEScription \n
		Snippet: value: str = driver.system.lxi.mdescription.get() \n
		This command defines the 'LAN' instrument description. \n
			:return: description: String containing the instrument description."""
		response = self._core.io.query_str(f'SYSTem:LXI:MDEScription?')
		return trim_str_response(response)
