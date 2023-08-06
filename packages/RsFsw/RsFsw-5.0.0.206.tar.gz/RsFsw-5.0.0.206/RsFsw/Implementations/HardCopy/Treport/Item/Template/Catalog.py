from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Catalog:
	"""Catalog commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("catalog", core, parent)

	def get(self) -> List[str]:
		"""SCPI: HCOPy:TREPort:ITEM:TEMPlate:CATalog \n
		Snippet: value: List[str] = driver.hardCopy.treport.item.template.catalog.get() \n
		This command queries the test report templates available in the default report directory (and its subdirectories) . \n
			:return: result: String containing the name of the templates as a comma-separated list."""
		response = self._core.io.query_str(f'HCOPy:TREPort:ITEM:TEMPlate:CATalog?')
		return Conversions.str_to_str_list(response)
