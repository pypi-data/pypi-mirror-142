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
		"""SCPI: DIAGnostic:HUMS[:STATe] \n
		Snippet: driver.diagnostic.hums.state.set(state = False) \n
		This command turns the HUMS service and data collection on and off. \n
			:param state: ON | OFF | 1 | 0
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'DIAGnostic:HUMS:STATe {param}')

	def get(self) -> bool:
		"""SCPI: DIAGnostic:HUMS[:STATe] \n
		Snippet: value: bool = driver.diagnostic.hums.state.get() \n
		This command turns the HUMS service and data collection on and off. \n
			:return: state: ON | OFF | 1 | 0"""
		response = self._core.io.query_str(f'DIAGnostic:HUMS:STATe?')
		return Conversions.str_to_bool(response)
