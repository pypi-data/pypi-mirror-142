from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class X:
	"""X commands group definition. 6 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("x", core, parent)

	@property
	def slimits(self):
		"""slimits commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_slimits'):
			from .Slimits import Slimits
			self._slimits = Slimits(self._core, self._cmd_group)
		return self._slimits

	@property
	def ssize(self):
		"""ssize commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ssize'):
			from .Ssize import Ssize
			self._ssize = Ssize(self._core, self._cmd_group)
		return self._ssize

	def set(self, position: float, window=repcap.Window.Default, marker=repcap.Marker.Default) -> None:
		"""SCPI: CALCulate<n>:MARKer<m>:X \n
		Snippet: driver.applications.k10Xlte.calculate.marker.x.set(position = 1.0, window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		This command moves a marker to a specific coordinate on the x-axis. If necessary, the command activates the marker.
		If the marker has been used as a delta marker, the command turns it into a normal marker. \n
			:param position: Numeric value that defines the marker position on the x-axis. The unit depends on the result display. Range: The range depends on the current x-axis range. , Unit: Hz
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
		"""
		param = Conversions.decimal_value_to_str(position)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		self._core.io.write(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:X {param}')

	def get(self, window=repcap.Window.Default, marker=repcap.Marker.Default) -> float:
		"""SCPI: CALCulate<n>:MARKer<m>:X \n
		Snippet: value: float = driver.applications.k10Xlte.calculate.marker.x.get(window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		This command moves a marker to a specific coordinate on the x-axis. If necessary, the command activates the marker.
		If the marker has been used as a delta marker, the command turns it into a normal marker. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
			:return: position: Numeric value that defines the marker position on the x-axis. The unit depends on the result display. Range: The range depends on the current x-axis range. , Unit: Hz"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:X?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'X':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = X(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
