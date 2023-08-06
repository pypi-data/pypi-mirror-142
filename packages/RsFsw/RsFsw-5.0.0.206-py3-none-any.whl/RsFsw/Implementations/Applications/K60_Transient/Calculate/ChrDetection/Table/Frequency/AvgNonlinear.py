from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AvgNonlinear:
	"""AvgNonlinear commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("avgNonlinear", core, parent)

	def set(self, state: bool, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:CHRDetection:TABLe:FREQuency:AVGNonlinear \n
		Snippet: driver.applications.k60Transient.calculate.chrDetection.table.frequency.avgNonlinear.set(state = False, window = repcap.Window.Default) \n
		If enabled, the frequency nonlinearity parameter is included in the result tables (see 'Frequency Deviation (RMS) ') .
		Note that only the enabled columns are returned for the method RsFsw.Applications.K60_Transient.Calculate.ChrDetection.
		Table.Results.get_ query. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.bool_to_str(state)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:CHRDetection:TABLe:FREQuency:AVGNonlinear {param}')

	def get(self, window=repcap.Window.Default) -> bool:
		"""SCPI: CALCulate<n>:CHRDetection:TABLe:FREQuency:AVGNonlinear \n
		Snippet: value: bool = driver.applications.k60Transient.calculate.chrDetection.table.frequency.avgNonlinear.get(window = repcap.Window.Default) \n
		If enabled, the frequency nonlinearity parameter is included in the result tables (see 'Frequency Deviation (RMS) ') .
		Note that only the enabled columns are returned for the method RsFsw.Applications.K60_Transient.Calculate.ChrDetection.
		Table.Results.get_ query. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:CHRDetection:TABLe:FREQuency:AVGNonlinear?')
		return Conversions.str_to_bool(response)
