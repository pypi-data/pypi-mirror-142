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
		"""SCPI: [SENSe]:NPRatio:STATe \n
		Snippet: driver.sense.npratio.state.set(state = False) \n
		Activates or deactivates the noise power ratio (NPR) measurement. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Deactivates the NPR measurement (returns to common frequency sweep) ON | 1 Activates the NPR measurement
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:NPRatio:STATe {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:NPRatio:STATe \n
		Snippet: value: bool = driver.sense.npratio.state.get() \n
		Activates or deactivates the noise power ratio (NPR) measurement. \n
			:return: state: ON | OFF | 0 | 1 OFF | 0 Deactivates the NPR measurement (returns to common frequency sweep) ON | 1 Activates the NPR measurement"""
		response = self._core.io.query_str(f'SENSe:NPRatio:STATe?')
		return Conversions.str_to_bool(response)
