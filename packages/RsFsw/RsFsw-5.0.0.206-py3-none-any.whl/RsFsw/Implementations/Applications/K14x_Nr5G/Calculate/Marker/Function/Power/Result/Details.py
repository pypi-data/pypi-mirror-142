from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Details:
	"""Details commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("details", core, parent)

	def set(self, measurement: enums.MarkerFunctionA, window=repcap.Window.Default, marker=repcap.Marker.Default) -> None:
		"""SCPI: CALCulate<n>:MARKer<m>:FUNCtion:POWer:RESult:DETails \n
		Snippet: driver.applications.k14Xnr5G.calculate.marker.function.power.result.details.set(measurement = enums.MarkerFunctionA.ACPower, window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		This command queries the results of the ACLR measurement. To get a valid result, you have to perform a complete
		measurement with synchronization to the end of the measurement before reading out the result. This is only possible for
		single sweeps.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Available for combined measurements only. \n
			:param measurement: ACPower
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
		"""
		param = Conversions.enum_scalar_to_str(measurement, enums.MarkerFunctionA)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		self._core.io.write(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:FUNCtion:POWer:RESult:DETails {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default, marker=repcap.Marker.Default) -> enums.MarkerFunctionA:
		"""SCPI: CALCulate<n>:MARKer<m>:FUNCtion:POWer:RESult:DETails \n
		Snippet: value: enums.MarkerFunctionA = driver.applications.k14Xnr5G.calculate.marker.function.power.result.details.get(window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		This command queries the results of the ACLR measurement. To get a valid result, you have to perform a complete
		measurement with synchronization to the end of the measurement before reading out the result. This is only possible for
		single sweeps.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Available for combined measurements only. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
			:return: measurement: ACPower"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:FUNCtion:POWer:RESult:DETails?')
		return Conversions.str_to_scalar_enum(response, enums.MarkerFunctionA)
