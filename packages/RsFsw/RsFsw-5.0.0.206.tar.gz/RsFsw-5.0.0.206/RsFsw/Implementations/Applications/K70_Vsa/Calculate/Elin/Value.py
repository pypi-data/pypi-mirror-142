from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Value:
	"""Value commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("value", core, parent)

	def set(self, left_disp: float, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:ELIN[:VALue] \n
		Snippet: driver.applications.k70Vsa.calculate.elin.value.set(left_disp = 1.0, window = repcap.Window.Default) \n
		Defines the start and stop values for the evaluation range (see method RsFsw.Applications.K70_Vsa.Calculate.Elin.State.
		set) . \n
			:param left_disp: Range: 0 to 1000000, Unit: SYM
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.decimal_value_to_str(left_disp)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:ELIN:VALue {param}')

	def get(self, window=repcap.Window.Default) -> float:
		"""SCPI: CALCulate<n>:ELIN[:VALue] \n
		Snippet: value: float = driver.applications.k70Vsa.calculate.elin.value.get(window = repcap.Window.Default) \n
		Defines the start and stop values for the evaluation range (see method RsFsw.Applications.K70_Vsa.Calculate.Elin.State.
		set) . \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: left_disp: Range: 0 to 1000000, Unit: SYM"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:ELIN:VALue?')
		return Conversions.str_to_float(response)
