from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import enums
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Derror:
	"""Derror commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("derror", core, parent)

	def get(self, result_type: enums.ResultTypeStat, window=repcap.Window.Default, marker=repcap.Marker.Default) -> float:
		"""SCPI: CALCulate<n>:MARKer<m>:FUNCtion:DDEMod:STATistic:FSK:DERRor \n
		Snippet: value: float = driver.applications.k70Vsa.calculate.marker.function.ddemod.statistic.fsk.derror.get(result_type = enums.ResultTypeStat.AVG, window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		This command queries the results of the frequency error of FSK modulated signals. \n
			:param result_type: none RMS frequency error of display points of current sweep AVG Average of frequency errors over several sweeps PAVG Average of maximum frequency errors over several sweeps PCTL 95% percentile of frequency error over several sweeps PEAK Maximum frequency error over all symbols of current sweep PPCT 95% percentile of maximum frequency errors over several sweeps PSD Standard deviation of maximum frequency errors over several sweeps RPE Maximum value of frequency error over several sweeps SDEV Standard deviation of frequency errors over several sweeps TPE Maximum frequency error over all display points over several sweeps
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
			:return: result: No help available"""
		param = Conversions.enum_scalar_to_str(result_type, enums.ResultTypeStat)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:FUNCtion:DDEMod:STATistic:FSK:DERRor? {param}')
		return Conversions.str_to_float(response)
