from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Upper:
	"""Upper commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("upper", core, parent)

	def set(self, stop: float, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:STATistics:SCALe:Y:UPPer \n
		Snippet: driver.applications.k70Vsa.calculate.statistics.scale.y.upper.set(stop = 1.0, window = repcap.Window.Default) \n
		This command defines the upper vertical limit of the diagram. \n
			:param stop: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.decimal_value_to_str(stop)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:STATistics:SCALe:Y:UPPer {param}')

	def get(self, window=repcap.Window.Default) -> float:
		"""SCPI: CALCulate<n>:STATistics:SCALe:Y:UPPer \n
		Snippet: value: float = driver.applications.k70Vsa.calculate.statistics.scale.y.upper.get(window = repcap.Window.Default) \n
		This command defines the upper vertical limit of the diagram. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: stop: No help available"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:STATistics:SCALe:Y:UPPer?')
		return Conversions.str_to_float(response)
