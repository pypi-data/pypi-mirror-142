from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.RepeatedCapability import RepeatedCapability
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pline:
	"""Pline commands group definition. 2 total commands, 1 Subgroups, 1 group commands
	Repeated Capability: PowerLine, default value after init: PowerLine.Ix1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pline", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_powerLine_get', 'repcap_powerLine_set', repcap.PowerLine.Ix1)

	def repcap_powerLine_set(self, powerLine: repcap.PowerLine) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to PowerLine.Default
		Default value after init: PowerLine.Ix1"""
		self._cmd_group.set_repcap_enum_value(powerLine)

	def repcap_powerLine_get(self) -> repcap.PowerLine:
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

	def set(self, generator_level: float, window=repcap.Window.Default, powerLine=repcap.PowerLine.Default) -> None:
		"""SCPI: CALCulate<n>:PLINe<dl> \n
		Snippet: driver.calculate.pline.set(generator_level = 1.0, window = repcap.Window.Default, powerLine = repcap.PowerLine.Default) \n
		No command help available \n
			:param generator_level: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param powerLine: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Pline')
		"""
		param = Conversions.decimal_value_to_str(generator_level)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		powerLine_cmd_val = self._cmd_group.get_repcap_cmd_value(powerLine, repcap.PowerLine)
		self._core.io.write(f'CALCulate{window_cmd_val}:PLINe{powerLine_cmd_val} {param}')

	def get(self, window=repcap.Window.Default, powerLine=repcap.PowerLine.Default) -> float:
		"""SCPI: CALCulate<n>:PLINe<dl> \n
		Snippet: value: float = driver.calculate.pline.get(window = repcap.Window.Default, powerLine = repcap.PowerLine.Default) \n
		No command help available \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param powerLine: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Pline')
			:return: generator_level: No help available"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		powerLine_cmd_val = self._cmd_group.get_repcap_cmd_value(powerLine, repcap.PowerLine)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:PLINe{powerLine_cmd_val}?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Pline':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pline(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
