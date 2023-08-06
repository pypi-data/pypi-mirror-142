from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Relative:
	"""Relative commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("relative", core, parent)

	def get(self, meas_type: enums.AdemMeasType, window=repcap.Window.Default, marker=repcap.Marker.Default, trace=repcap.Trace.Default) -> float:
		"""SCPI: CALCulate<n>:MARKer<m>:FUNCtion:ADEMod:AM[:RESult<t>]:RELative \n
		Snippet: value: float = driver.calculate.marker.function.ademod.am.result.relative.get(meas_type = enums.AdemMeasType.MIDDle, window = repcap.Window.Default, marker = repcap.Marker.Default, trace = repcap.Trace.Default) \n
		This command queries the current relative value of the demodulated signal for the specified trace (as displayed in the
		Result Summary in manual operation) . Note that all windows with the same evaluation method have the same traces.
		The unit of the results depends on the method RsFsw.Configure.Ademod.Results.Unit.set setting. \n
			:param meas_type: PPEak Postive peak (+PK) MPEak | NPEak Negative peak (-PK) MIDDle Average of positive and negative peaks ±PK/2 RMS Root mean square value
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Result')
			:return: meas_type_result: No help available"""
		param = Conversions.enum_scalar_to_str(meas_type, enums.AdemMeasType)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:FUNCtion:ADEMod:AM:RESult{trace_cmd_val}:RELative? {param}')
		return Conversions.str_to_float(response)
