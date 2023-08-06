from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: TRACe:IQ:EGATe[:STATe] \n
		Snippet: driver.trace.iq.egate.state.set(state = False) \n
		This command turns gated measurements with the I/Q analyzer on and off. Before you can use the command you have to turn
		on the I/Q analyzer and select an external or IF power trigger source. \n
			:param state: ON | OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'TRACe:IQ:EGATe:STATe {param}')

	def get(self) -> bool:
		"""SCPI: TRACe:IQ:EGATe[:STATe] \n
		Snippet: value: bool = driver.trace.iq.egate.state.get() \n
		This command turns gated measurements with the I/Q analyzer on and off. Before you can use the command you have to turn
		on the I/Q analyzer and select an external or IF power trigger source. \n
			:return: state: ON | OFF"""
		response = self._core.io.query_str(f'TRACe:IQ:EGATe:STATe?')
		return Conversions.str_to_bool(response)
