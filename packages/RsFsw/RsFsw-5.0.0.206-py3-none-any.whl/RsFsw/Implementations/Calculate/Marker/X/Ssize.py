from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ssize:
	"""Ssize commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ssize", core, parent)

	def set(self, stepsize: enums.Stepsize, window=repcap.Window.Default, marker=repcap.Marker.Default) -> None:
		"""SCPI: CALCulate<n>:MARKer<m>:X:SSIZe \n
		Snippet: driver.calculate.marker.x.ssize.set(stepsize = enums.Stepsize.POINts, window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		This command selects the marker step size mode for all markers in all windows. The step size defines the distance the
		marker moves when you move it with the rotary knob. It therefore takes effect in manual operation only. \n
			:param stepsize: STANdard the marker moves from one pixel to the next POINts the marker moves from one sweep point to the next
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
		"""
		param = Conversions.enum_scalar_to_str(stepsize, enums.Stepsize)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		self._core.io.write(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:X:SSIZe {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default, marker=repcap.Marker.Default) -> enums.Stepsize:
		"""SCPI: CALCulate<n>:MARKer<m>:X:SSIZe \n
		Snippet: value: enums.Stepsize = driver.calculate.marker.x.ssize.get(window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		This command selects the marker step size mode for all markers in all windows. The step size defines the distance the
		marker moves when you move it with the rotary knob. It therefore takes effect in manual operation only. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
			:return: stepsize: STANdard the marker moves from one pixel to the next POINts the marker moves from one sweep point to the next"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:X:SSIZe?')
		return Conversions.str_to_scalar_enum(response, enums.Stepsize)
