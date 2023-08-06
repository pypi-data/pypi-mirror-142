from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Value:
	"""Value commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("value", core, parent)

	def set(self, stimulus: float, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:MSRA:ALINe[:VALue] \n
		Snippet: driver.applications.k6Pulse.calculate.msra.aline.value.set(stimulus = 1.0, window = repcap.Window.Default) \n
		This command defines the position of the analysis line for all time-based windows in all MSRA secondary applications and
		the MSRA primary application. \n
			:param stimulus: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.decimal_value_to_str(stimulus)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:MSRA:ALINe:VALue {param}')

	def get(self, window=repcap.Window.Default) -> float:
		"""SCPI: CALCulate<n>:MSRA:ALINe[:VALue] \n
		Snippet: value: float = driver.applications.k6Pulse.calculate.msra.aline.value.get(window = repcap.Window.Default) \n
		This command defines the position of the analysis line for all time-based windows in all MSRA secondary applications and
		the MSRA primary application. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: stimulus: No help available"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:MSRA:ALINe:VALue?')
		return Conversions.str_to_float(response)
