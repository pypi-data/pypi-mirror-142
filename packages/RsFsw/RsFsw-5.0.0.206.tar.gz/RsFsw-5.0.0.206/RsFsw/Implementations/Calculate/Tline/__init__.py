from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.RepeatedCapability import RepeatedCapability
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tline:
	"""Tline commands group definition. 2 total commands, 1 Subgroups, 1 group commands
	Repeated Capability: TimeLine, default value after init: TimeLine.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tline", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_timeLine_get', 'repcap_timeLine_set', repcap.TimeLine.Nr1)

	def repcap_timeLine_set(self, timeLine: repcap.TimeLine) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to TimeLine.Default
		Default value after init: TimeLine.Nr1"""
		self._cmd_group.set_repcap_enum_value(timeLine)

	def repcap_timeLine_get(self) -> repcap.TimeLine:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	def set(self, time: float, window=repcap.Window.Default, timeLine=repcap.TimeLine.Default) -> None:
		"""SCPI: CALCulate<n>:TLINe<dl> \n
		Snippet: driver.calculate.tline.set(time = 1.0, window = repcap.Window.Default, timeLine = repcap.TimeLine.Default) \n
		This command defines the position of a time line. \n
			:param time: Note that you can not set a time line to a position that is higher than the current sweep time. Range: 0 s to 1600 s, Unit: S
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param timeLine: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tline')
		"""
		param = Conversions.decimal_value_to_str(time)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		timeLine_cmd_val = self._cmd_group.get_repcap_cmd_value(timeLine, repcap.TimeLine)
		self._core.io.write(f'CALCulate{window_cmd_val}:TLINe{timeLine_cmd_val} {param}')

	def get(self, window=repcap.Window.Default, timeLine=repcap.TimeLine.Default) -> float:
		"""SCPI: CALCulate<n>:TLINe<dl> \n
		Snippet: value: float = driver.calculate.tline.get(window = repcap.Window.Default, timeLine = repcap.TimeLine.Default) \n
		This command defines the position of a time line. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param timeLine: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tline')
			:return: time: Note that you can not set a time line to a position that is higher than the current sweep time. Range: 0 s to 1600 s, Unit: S"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		timeLine_cmd_val = self._cmd_group.get_repcap_cmd_value(timeLine, repcap.TimeLine)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:TLINe{timeLine_cmd_val}?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Tline':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Tline(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
