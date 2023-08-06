from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: CALibration:PADJust[:STATe] \n
		Snippet: driver.calibration.padjust.state.set(state = False) \n
		Activates or deactivates the preselector adjustment. This command is only available for instrument modelsR&S FSW43/50/67,
		for frequency sweeps in the Spectrum application. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'CALibration:PADJust:STATe {param}')

	def get(self) -> bool:
		"""SCPI: CALibration:PADJust[:STATe] \n
		Snippet: value: bool = driver.calibration.padjust.state.get() \n
		Activates or deactivates the preselector adjustment. This command is only available for instrument modelsR&S FSW43/50/67,
		for frequency sweeps in the Spectrum application. \n
			:return: state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on"""
		response = self._core.io.query_str(f'CALibration:PADJust:STATe?')
		return Conversions.str_to_bool(response)
