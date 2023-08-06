from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Result:
	"""Result commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("result", core, parent)

	def get(self) -> float:
		"""SCPI: FETCh:STABle:MERRor:SELected[:RESult] \n
		Snippet: value: float = driver.applications.k18AmplifierEt.fetch.stable.merror.selected.result.get() \n
		No command help available \n
			:return: power: No help available"""
		response = self._core.io.query_str(f'FETCh:STABle:MERRor:SELected:RESult?')
		return Conversions.str_to_float(response)
