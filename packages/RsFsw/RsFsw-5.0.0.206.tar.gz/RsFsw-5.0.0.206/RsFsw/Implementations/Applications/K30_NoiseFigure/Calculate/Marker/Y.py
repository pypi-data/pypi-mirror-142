from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Y:
	"""Y commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("y", core, parent)

	def get(self, trace: enums.NoiseFigureResultCustom, window=repcap.Window.Default, marker=repcap.Marker.Default) -> float:
		"""SCPI: CALCulate<n>:MARKer<m>:Y \n
		Snippet: value: float = driver.applications.k30NoiseFigure.calculate.marker.y.get(trace = enums.NoiseFigureResultCustom.CPCold, window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		Queries the result at the position of the specified marker. \n
			:param trace: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
			:return: result: Selects the result. CPCold Queries calibration power (cold) results. CPHot Queries calibration power (hot) results. CYFactor Queries calibration y-factor results. GAIN Queries gain results. NOISe Queries noise figure results. NUNCertainty Queries the noise figure uncertainty results. PCOLd Queries power (cold) results. PHOT Queries power (hot) results. TEMPerature Queries noise temperature results. YFACtor Queries y-factor results."""
		param = Conversions.enum_scalar_to_str(trace, enums.NoiseFigureResultCustom)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		response = self._core.io.query_str_with_opc(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:Y? {param}')
		return Conversions.str_to_float(response)
