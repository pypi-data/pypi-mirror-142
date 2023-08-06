from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Condition:
	"""Condition commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("condition", core, parent)

	def get(self) -> int:
		"""SCPI: STATus:OPERation:CONDition \n
		Snippet: value: int = driver.status.operation.condition.get() \n
		These commands read out the CONDition section of the status register. The commands do not delete the contents of the
		CONDition section. \n
			:return: register_value: No help available"""
		response = self._core.io.query_str(f'STATus:OPERation:CONDition?')
		return Conversions.str_to_int(response)
