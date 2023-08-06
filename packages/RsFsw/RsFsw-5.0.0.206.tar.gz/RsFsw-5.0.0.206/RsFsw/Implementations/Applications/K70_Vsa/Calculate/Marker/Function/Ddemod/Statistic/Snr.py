from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Snr:
	"""Snr commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("snr", core, parent)

	def get(self, result_type: enums.ResultTypeStat, window=repcap.Window.Default, marker=repcap.Marker.Default) -> float:
		"""SCPI: CALCulate<n>:MARKer<m>:FUNCtion:DDEMod:STATistic:SNR \n
		Snippet: value: float = driver.applications.k70Vsa.calculate.marker.function.ddemod.statistic.snr.get(result_type = enums.ResultTypeStat.AVG, window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		This command queries the results of the SNR error measurement performed for digital demodulation. \n
			:param result_type: none SNR value of display points of current sweep AVG Average of SNR values over several sweeps PAVG Average of maximum SNR values over several sweeps PCTL 95% percentile of SNR value over several sweeps PEAK Maximum SNR over all symbols of current sweep PPCT 95% percentile of maximum SNR values over several sweeps PSD Standard deviation of maximum SNR values over several sweeps RPE Maximum value of SNR over several sweeps SDEV Standard deviation of SNR values over several sweeps TPE Maximum SNR over all display points over several sweeps
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
			:return: result: No help available"""
		param = Conversions.enum_scalar_to_str(result_type, enums.ResultTypeStat)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:FUNCtion:DDEMod:STATistic:SNR? {param}')
		return Conversions.str_to_float(response)
