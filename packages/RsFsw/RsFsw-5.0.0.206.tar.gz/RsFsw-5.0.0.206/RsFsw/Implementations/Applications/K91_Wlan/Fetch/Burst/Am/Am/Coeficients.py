from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Coeficients:
	"""Coeficients commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("coeficients", core, parent)

	def get(self) -> int:
		"""SCPI: FETCh:BURSt:AM:AM:COEFicients \n
		Snippet: value: int = driver.applications.k91Wlan.fetch.burst.am.am.coeficients.get() \n
		This remote control returns the coefficients of the polynomial regression model used to determine the AM/AM result
		display. See 'AM/AM' for details. \n
			:return: coefficients: No help available"""
		response = self._core.io.query_str(f'FETCh:BURSt:AM:AM:COEFicients?')
		return Conversions.str_to_int(response)
