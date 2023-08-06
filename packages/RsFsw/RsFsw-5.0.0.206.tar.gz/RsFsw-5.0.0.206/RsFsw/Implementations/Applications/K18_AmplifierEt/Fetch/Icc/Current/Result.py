from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Result:
	"""Result commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("result", core, parent)

	def get(self) -> float:
		"""SCPI: FETCh:ICC:CURRent[:RESult] \n
		Snippet: value: float = driver.applications.k18AmplifierEt.fetch.icc.current.result.get() \n
		This command queries the measured baseband current (I_cc) as shown in the Result Summary. \n
			:return: current: Minimum, maximum or current I_cc, depending on the command syntax. Unit: A"""
		response = self._core.io.query_str(f'FETCh:ICC:CURRent:RESult?')
		return Conversions.str_to_float(response)
