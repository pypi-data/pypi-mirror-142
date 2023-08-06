from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ListPy:
	"""ListPy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("listPy", core, parent)

	def get(self, window=repcap.Window.Default, marker=repcap.Marker.Default) -> float:
		"""SCPI: CALCulate<n>:MARKer<m>:FUNCtion:HARMonics:LIST \n
		Snippet: value: float = driver.calculate.marker.function.harmonics.listPy.get(window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		This command queries the position of the harmonics. To get a valid result, you have to perform a complete measurement
		with synchronization to the end of the measurement before reading out the result. This is only possible for single sweep
		mode. See also method RsFsw.Applications.K10x_Lte.Initiate.Continuous.set. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
			:return: harmonics: Returns one value for every harmonic. The first value is the absolute power of the first harmonic. The unit is variable. The other values are power levels relative to the first harmonic. The unit for these is dB."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:FUNCtion:HARMonics:LIST?')
		return Conversions.str_to_float(response)
