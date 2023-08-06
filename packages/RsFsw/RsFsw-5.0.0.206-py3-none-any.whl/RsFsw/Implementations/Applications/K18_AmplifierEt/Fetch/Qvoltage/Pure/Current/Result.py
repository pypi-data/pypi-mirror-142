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
		"""SCPI: FETCh:QVOLtage:PURE:CURRent[:RESult] \n
		Snippet: value: float = driver.applications.k18AmplifierEt.fetch.qvoltage.pure.current.result.get() \n
		This command queries the measured at the baseband input Q as shown in the Result Summary. The returned value is a 'pure'
		voltage that does not contain any correction factors. \n
			:return: voltage: numeric value Minimum, maximum or current voltage, depending on the command syntax. Unit: V"""
		response = self._core.io.query_str(f'FETCh:QVOLtage:PURE:CURRent:RESult?')
		return Conversions.str_to_float(response)
