from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Y:
	"""Y commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("y", core, parent)

	@property
	def percent(self):
		"""percent commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_percent'):
			from .Percent import Percent
			self._percent = Percent(self._core, self._cmd_group)
		return self._percent

	def get(self, window=repcap.Window.Default, marker=repcap.Marker.Default) -> float:
		"""SCPI: CALCulate<n>:MARKer<m>:Y \n
		Snippet: value: float = driver.applications.k91Wlan.calculate.marker.y.get(window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		Queries the result at the position of the specified marker. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
			:return: yposition: No help available"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		response = self._core.io.query_str_with_opc(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:Y?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Y':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Y(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
