from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Fline:
	"""Fline commands group definition. 2 total commands, 1 Subgroups, 1 group commands
	Repeated Capability: FreqLine, default value after init: FreqLine.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fline", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_freqLine_get', 'repcap_freqLine_set', repcap.FreqLine.Nr1)

	def repcap_freqLine_set(self, freqLine: repcap.FreqLine) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to FreqLine.Default
		Default value after init: FreqLine.Nr1"""
		self._cmd_group.set_repcap_enum_value(freqLine)

	def repcap_freqLine_get(self) -> repcap.FreqLine:
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

	def set(self, position: float, window=repcap.Window.Default, freqLine=repcap.FreqLine.Default) -> None:
		"""SCPI: CALCulate<n>:FLINe<dl> \n
		Snippet: driver.applications.k10Xlte.calculate.fline.set(position = 1.0, window = repcap.Window.Default, freqLine = repcap.FreqLine.Default) \n
		No command help available \n
			:param position: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param freqLine: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fline')
		"""
		param = Conversions.decimal_value_to_str(position)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		freqLine_cmd_val = self._cmd_group.get_repcap_cmd_value(freqLine, repcap.FreqLine)
		self._core.io.write(f'CALCulate{window_cmd_val}:FLINe{freqLine_cmd_val} {param}')

	def get(self, window=repcap.Window.Default, freqLine=repcap.FreqLine.Default) -> float:
		"""SCPI: CALCulate<n>:FLINe<dl> \n
		Snippet: value: float = driver.applications.k10Xlte.calculate.fline.get(window = repcap.Window.Default, freqLine = repcap.FreqLine.Default) \n
		No command help available \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param freqLine: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fline')
			:return: position: No help available"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		freqLine_cmd_val = self._cmd_group.get_repcap_cmd_value(freqLine, repcap.FreqLine)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:FLINe{freqLine_cmd_val}?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Fline':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Fline(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
