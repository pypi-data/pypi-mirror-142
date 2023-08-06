from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:ELIN:STATe \n
		Snippet: driver.applications.k70Vsa.calculate.elin.state.set(state = False, window = repcap.Window.Default) \n
		This command restricts the evaluation range. The evaluation range is considered for the following display types:
			INTRO_CMD_HELP: The I/Q data file must be in one of the following supported formats: \n
			- eye diagrams
			- constellation diagrams
			- modulation accuracy
			- statistic displays
			- spectrum displays \n
			:param state: ON | 1 The evaluation range extends from the start value defined by CALC:ELIN1:VAL to the stop value defined by CALC:ELIN2:VAL (see method RsFsw.Applications.K70_Vsa.Calculate.Elin.Value.set) . OFF | 0 The complete result area is evaluated.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.bool_to_str(state)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:ELIN:STATe {param}')

	def get(self, window=repcap.Window.Default) -> bool:
		"""SCPI: CALCulate<n>:ELIN:STATe \n
		Snippet: value: bool = driver.applications.k70Vsa.calculate.elin.state.get(window = repcap.Window.Default) \n
		This command restricts the evaluation range. The evaluation range is considered for the following display types:
			INTRO_CMD_HELP: The I/Q data file must be in one of the following supported formats: \n
			- eye diagrams
			- constellation diagrams
			- modulation accuracy
			- statistic displays
			- spectrum displays \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: state: ON | 1 The evaluation range extends from the start value defined by CALC:ELIN1:VAL to the stop value defined by CALC:ELIN2:VAL (see method RsFsw.Applications.K70_Vsa.Calculate.Elin.Value.set) . OFF | 0 The complete result area is evaluated."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:ELIN:STATe?')
		return Conversions.str_to_bool(response)
