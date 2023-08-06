from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Result:
	"""Result commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("result", core, parent)

	def get(self) -> str:
		"""SCPI: CALibration:RESult \n
		Snippet: value: str = driver.calibration.result.get() \n
		This command returns the results collected during calibration. \n
			:return: calibration_data: String containing the calibration data."""
		response = self._core.io.query_str(f'CALibration:RESult?')
		return trim_str_response(response)
