from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Threshold:
	"""Threshold commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("threshold", core, parent)

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	def set(self, level: float, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:THReshold \n
		Snippet: driver.calculate.threshold.set(level = 1.0, window = repcap.Window.Default) \n
		This command defines a threshold level for the marker peak search (for all markers in all windows) . Note that you must
		enable the use of the threshold using method RsFsw.Calculate.Threshold.State.set. \n
			:param level: Numeric value. The value range and unit are variable. Unit: DBM
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.decimal_value_to_str(level)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:THReshold {param}')

	def get(self, window=repcap.Window.Default) -> float:
		"""SCPI: CALCulate<n>:THReshold \n
		Snippet: value: float = driver.calculate.threshold.get(window = repcap.Window.Default) \n
		This command defines a threshold level for the marker peak search (for all markers in all windows) . Note that you must
		enable the use of the threshold using method RsFsw.Calculate.Threshold.State.set. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: level: Numeric value. The value range and unit are variable. Unit: DBM"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:THReshold?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Threshold':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Threshold(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
