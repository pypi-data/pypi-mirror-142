from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Immediate:
	"""Immediate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("immediate", core, parent)

	def set(self, peaks: float, window=repcap.Window.Default, marker=repcap.Marker.Default) -> None:
		"""SCPI: CALCulate<n>:MARKer<m>:FUNCtion:FPEaks[:IMMediate] \n
		Snippet: driver.calculate.marker.function.fpeaks.immediate.set(peaks = 1.0, window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		This command initiates a peak search. \n
			:param peaks: This parameter defines the number of peaks to find during the search. Note that the actual number of peaks found during the search also depends on the peak excursion you have set with method RsFsw.Applications.K10x_Lte.Calculate.Marker.Pexcursion.set. Range: 1 to 200
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
		"""
		param = Conversions.decimal_value_to_str(peaks)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		self._core.io.write(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:FUNCtion:FPEaks:IMMediate {param}')
