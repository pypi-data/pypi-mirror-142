from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Icomponent:
	"""Icomponent commands group definition. 3 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("icomponent", core, parent)

	@property
	def limit(self):
		"""limit commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_limit'):
			from .Limit import Limit
			self._limit = Limit(self._core, self._cmd_group)
		return self._limit

	def set(self, state: bool, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:TABLe:POWer:AMPLitude:I \n
		Snippet: driver.applications.k6Pulse.calculate.table.power.amplitude.icomponent.set(state = False, window = repcap.Window.Default) \n
		If enabled, the in-phase amplitude is included in the result tables. \n
			:param state: ON | OFF | 1 | 0
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.bool_to_str(state)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:TABLe:POWer:AMPLitude:I {param}')

	def get(self, window=repcap.Window.Default) -> bool:
		"""SCPI: CALCulate<n>:TABLe:POWer:AMPLitude:I \n
		Snippet: value: bool = driver.applications.k6Pulse.calculate.table.power.amplitude.icomponent.get(window = repcap.Window.Default) \n
		If enabled, the in-phase amplitude is included in the result tables. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: state: ON | OFF | 1 | 0"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:TABLe:POWer:AMPLitude:I?')
		return Conversions.str_to_bool(response)

	def clone(self) -> 'Icomponent':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Icomponent(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
