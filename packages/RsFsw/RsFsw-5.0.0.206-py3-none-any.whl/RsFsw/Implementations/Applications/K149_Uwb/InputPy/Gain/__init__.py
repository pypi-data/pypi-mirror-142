from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Gain:
	"""Gain commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("gain", core, parent)

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	def set(self, level: float, inputIx=repcap.InputIx.Default) -> None:
		"""SCPI: INPut<Undef>:GAIN \n
		Snippet: driver.applications.k149Uwb.inputPy.gain.set(level = 1.0, inputIx = repcap.InputIx.Default) \n
		No command help available \n
			:param level: No help available
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
		"""
		param = Conversions.decimal_value_to_str(level)
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		self._core.io.write(f'INPut{inputIx_cmd_val}:GAIN {param}')

	def get(self, inputIx=repcap.InputIx.Default) -> float:
		"""SCPI: INPut<Undef>:GAIN \n
		Snippet: value: float = driver.applications.k149Uwb.inputPy.gain.get(inputIx = repcap.InputIx.Default) \n
		No command help available \n
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
			:return: level: No help available"""
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		response = self._core.io.query_str(f'INPut{inputIx_cmd_val}:GAIN?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Gain':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Gain(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
