from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Link:
	"""Link commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("link", core, parent)

	def set(self, display_type: enums.DisplayType, window=repcap.Window.Default, marker=repcap.Marker.Default) -> None:
		"""SCPI: CALCulate<n>:MARKer<m>:LINK \n
		Snippet: driver.calculate.marker.link.set(display_type = enums.DisplayType.BOTH, window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		Links the specified marker in all displays of the specified type. \n
			:param display_type: TIME | SPECtrum | BOTH | NONE TIME Links the markers in all time domain diagrams SPECtrum Links the markers in all AF Spectrum displays BOTH Links the markers both in the time domain diagrams and in the AF Spectrum displays NONE Markers are not linked.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
		"""
		param = Conversions.enum_scalar_to_str(display_type, enums.DisplayType)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		self._core.io.write_with_opc(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:LINK {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default, marker=repcap.Marker.Default) -> enums.DisplayType:
		"""SCPI: CALCulate<n>:MARKer<m>:LINK \n
		Snippet: value: enums.DisplayType = driver.calculate.marker.link.get(window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		Links the specified marker in all displays of the specified type. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
			:return: display_type: TIME | SPECtrum | BOTH | NONE TIME Links the markers in all time domain diagrams SPECtrum Links the markers in all AF Spectrum displays BOTH Links the markers both in the time domain diagrams and in the AF Spectrum displays NONE Markers are not linked."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		response = self._core.io.query_str_with_opc(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:LINK?')
		return Conversions.str_to_scalar_enum(response, enums.DisplayType)
