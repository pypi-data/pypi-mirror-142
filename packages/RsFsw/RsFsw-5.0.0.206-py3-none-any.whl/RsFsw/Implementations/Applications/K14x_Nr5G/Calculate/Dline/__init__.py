from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dline:
	"""Dline commands group definition. 2 total commands, 1 Subgroups, 1 group commands
	Repeated Capability: DisplayLine, default value after init: DisplayLine.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dline", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_displayLine_get', 'repcap_displayLine_set', repcap.DisplayLine.Nr1)

	def repcap_displayLine_set(self, displayLine: repcap.DisplayLine) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to DisplayLine.Default
		Default value after init: DisplayLine.Nr1"""
		self._cmd_group.set_repcap_enum_value(displayLine)

	def repcap_displayLine_get(self) -> repcap.DisplayLine:
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

	def set(self, position: float, window=repcap.Window.Default, displayLine=repcap.DisplayLine.Default) -> None:
		"""SCPI: CALCulate<n>:DLINe<li> \n
		Snippet: driver.applications.k14Xnr5G.calculate.dline.set(position = 1.0, window = repcap.Window.Default, displayLine = repcap.DisplayLine.Default) \n
		No command help available \n
			:param position: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param displayLine: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Dline')
		"""
		param = Conversions.decimal_value_to_str(position)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		displayLine_cmd_val = self._cmd_group.get_repcap_cmd_value(displayLine, repcap.DisplayLine)
		self._core.io.write(f'CALCulate{window_cmd_val}:DLINe{displayLine_cmd_val} {param}')

	def get(self, window=repcap.Window.Default, displayLine=repcap.DisplayLine.Default) -> float:
		"""SCPI: CALCulate<n>:DLINe<li> \n
		Snippet: value: float = driver.applications.k14Xnr5G.calculate.dline.get(window = repcap.Window.Default, displayLine = repcap.DisplayLine.Default) \n
		No command help available \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param displayLine: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Dline')
			:return: position: No help available"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		displayLine_cmd_val = self._cmd_group.get_repcap_cmd_value(displayLine, repcap.DisplayLine)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:DLINe{displayLine_cmd_val}?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Dline':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Dline(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
