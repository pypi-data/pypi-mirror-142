from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def get(self) -> bool:
		"""SCPI: CALibration:MCGD:STATe \n
		Snippet: value: bool = driver.applications.k17Mcgd.calibration.mcgd.state.get() \n
		This command queries the calibration status of the Multi-Carrier Group Delay application. \n
			:return: state: ON | 1 Calibration has been performed, reference data is available. OFF | 0 Calibration has not yet been performed or is currently running, reference data is not yet available."""
		response = self._core.io.query_str(f'CALibration:MCGD:STATe?')
		return Conversions.str_to_bool(response)
