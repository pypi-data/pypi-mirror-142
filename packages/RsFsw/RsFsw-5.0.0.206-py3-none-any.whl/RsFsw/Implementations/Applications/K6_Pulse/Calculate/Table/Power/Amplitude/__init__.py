from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Amplitude:
	"""Amplitude commands group definition. 9 total commands, 3 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("amplitude", core, parent)

	@property
	def icomponent(self):
		"""icomponent commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_icomponent'):
			from .Icomponent import Icomponent
			self._icomponent = Icomponent(self._core, self._cmd_group)
		return self._icomponent

	@property
	def qcomponent(self):
		"""qcomponent commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_qcomponent'):
			from .Qcomponent import Qcomponent
			self._qcomponent = Qcomponent(self._core, self._cmd_group)
		return self._qcomponent

	@property
	def limit(self):
		"""limit commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_limit'):
			from .Limit import Limit
			self._limit = Limit(self._core, self._cmd_group)
		return self._limit

	def set(self, state: bool, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:TABLe:POWer:AMPLitude \n
		Snippet: driver.applications.k6Pulse.calculate.table.power.amplitude.set(state = False, window = repcap.Window.Default) \n
		If enabled, the pulse amplitude is included in the result tables. \n
			:param state: ON | OFF | 1 | 0
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.bool_to_str(state)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:TABLe:POWer:AMPLitude {param}')

	def get(self, window=repcap.Window.Default) -> bool:
		"""SCPI: CALCulate<n>:TABLe:POWer:AMPLitude \n
		Snippet: value: bool = driver.applications.k6Pulse.calculate.table.power.amplitude.get(window = repcap.Window.Default) \n
		If enabled, the pulse amplitude is included in the result tables. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: state: ON | OFF | 1 | 0"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:TABLe:POWer:AMPLitude?')
		return Conversions.str_to_bool(response)

	def clone(self) -> 'Amplitude':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Amplitude(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
