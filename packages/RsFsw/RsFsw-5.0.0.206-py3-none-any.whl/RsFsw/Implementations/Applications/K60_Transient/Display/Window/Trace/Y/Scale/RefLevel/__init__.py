from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RefLevel:
	"""RefLevel commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("refLevel", core, parent)

	@property
	def offset(self):
		"""offset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_offset'):
			from .Offset import Offset
			self._offset = Offset(self._core, self._cmd_group)
		return self._offset

	def set(self, reference_level: float, window=repcap.Window.Default) -> None:
		"""SCPI: DISPlay[:WINDow<n>]:TRACe:Y[:SCALe]:RLEVel \n
		Snippet: driver.applications.k60Transient.display.window.trace.y.scale.refLevel.set(reference_level = 1.0, window = repcap.Window.Default) \n
		This command defines the reference level (for all traces in all windows) . With a reference level offset ≠ 0, the value
		range of the reference level is modified by the offset. \n
			:param reference_level: The unit is variable. Range: see datasheet , Unit: DBM
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
		"""
		param = Conversions.decimal_value_to_str(reference_level)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'DISPlay:WINDow{window_cmd_val}:TRACe:Y:SCALe:RLEVel {param}')

	def get(self, window=repcap.Window.Default) -> float:
		"""SCPI: DISPlay[:WINDow<n>]:TRACe:Y[:SCALe]:RLEVel \n
		Snippet: value: float = driver.applications.k60Transient.display.window.trace.y.scale.refLevel.get(window = repcap.Window.Default) \n
		This command defines the reference level (for all traces in all windows) . With a reference level offset ≠ 0, the value
		range of the reference level is modified by the offset. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:return: reference_level: The unit is variable. Range: see datasheet , Unit: DBM"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'DISPlay:WINDow{window_cmd_val}:TRACe:Y:SCALe:RLEVel?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'RefLevel':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RefLevel(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
