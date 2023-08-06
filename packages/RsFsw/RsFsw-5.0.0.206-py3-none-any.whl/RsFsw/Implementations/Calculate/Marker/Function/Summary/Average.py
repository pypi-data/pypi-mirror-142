from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Average:
	"""Average commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("average", core, parent)

	def set(self, state: bool, window=repcap.Window.Default, marker=repcap.Marker.Default) -> None:
		"""SCPI: CALCulate<n>:MARKer<m>:FUNCtion:SUMMary:AVERage \n
		Snippet: driver.calculate.marker.function.summary.average.set(state = False, window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		This command switches on or off averaging for the active power measurement in zero span in the window specified by the
		suffix <n>. If activated, a time domain value is calculated from the trace after each sweep; in the end, all values are
		averaged to calculate the final result. The number of results required for the calculation of average is defined with
		[SENSe:]AVERage<n>:COUNt . Averaging is reset by switching it off and on again. Synchronization to the end of averaging
		is only possible in single sweep mode. \n
			:param state: ON | OFF | 1 | 0
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
		"""
		param = Conversions.bool_to_str(state)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		self._core.io.write(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:FUNCtion:SUMMary:AVERage {param}')

	def get(self, window=repcap.Window.Default, marker=repcap.Marker.Default) -> bool:
		"""SCPI: CALCulate<n>:MARKer<m>:FUNCtion:SUMMary:AVERage \n
		Snippet: value: bool = driver.calculate.marker.function.summary.average.get(window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		This command switches on or off averaging for the active power measurement in zero span in the window specified by the
		suffix <n>. If activated, a time domain value is calculated from the trace after each sweep; in the end, all values are
		averaged to calculate the final result. The number of results required for the calculation of average is defined with
		[SENSe:]AVERage<n>:COUNt . Averaging is reset by switching it off and on again. Synchronization to the end of averaging
		is only possible in single sweep mode. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
			:return: state: ON | OFF | 1 | 0"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:FUNCtion:SUMMary:AVERage?')
		return Conversions.str_to_bool(response)
