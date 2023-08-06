from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Icomponent:
	"""Icomponent commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("icomponent", core, parent)

	@property
	def inverted(self):
		"""inverted commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_inverted'):
			from .Inverted import Inverted
			self._inverted = Inverted(self._core, self._cmd_group)
		return self._inverted

	def set(self, value: float, inputIx=repcap.InputIx.Default) -> None:
		"""SCPI: INPut<ip>:IQ:OSC:SKEW:I \n
		Snippet: driver.inputPy.iq.osc.skew.icomponent.set(value = 1.0, inputIx = repcap.InputIx.Default) \n
		Compensates for skewed values in the positive I path, e.g. due to different input cables. \n
			:param value: Unit: S
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
		"""
		param = Conversions.decimal_value_to_str(value)
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		self._core.io.write(f'INPut{inputIx_cmd_val}:IQ:OSC:SKEW:I {param}')

	def get(self, inputIx=repcap.InputIx.Default) -> float:
		"""SCPI: INPut<ip>:IQ:OSC:SKEW:I \n
		Snippet: value: float = driver.inputPy.iq.osc.skew.icomponent.get(inputIx = repcap.InputIx.Default) \n
		Compensates for skewed values in the positive I path, e.g. due to different input cables. \n
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
			:return: value: Unit: S"""
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		response = self._core.io.query_str(f'INPut{inputIx_cmd_val}:IQ:OSC:SKEW:I?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Icomponent':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Icomponent(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
