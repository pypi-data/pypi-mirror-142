from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Qcomponent:
	"""Qcomponent commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("qcomponent", core, parent)

	@property
	def inverted(self):
		"""inverted commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_inverted'):
			from .Inverted import Inverted
			self._inverted = Inverted(self._core, self._cmd_group)
		return self._inverted

	def set(self, value: float, inputIx=repcap.InputIx.Default) -> None:
		"""SCPI: INPut<ip>:IQ:OSC:SKEW:Q \n
		Snippet: driver.applications.k149Uwb.inputPy.iq.osc.skew.qcomponent.set(value = 1.0, inputIx = repcap.InputIx.Default) \n
		No command help available \n
			:param value: No help available
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
		"""
		param = Conversions.decimal_value_to_str(value)
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		self._core.io.write(f'INPut{inputIx_cmd_val}:IQ:OSC:SKEW:Q {param}')

	def get(self, inputIx=repcap.InputIx.Default) -> float:
		"""SCPI: INPut<ip>:IQ:OSC:SKEW:Q \n
		Snippet: value: float = driver.applications.k149Uwb.inputPy.iq.osc.skew.qcomponent.get(inputIx = repcap.InputIx.Default) \n
		No command help available \n
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
			:return: value: No help available"""
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		response = self._core.io.query_str(f'INPut{inputIx_cmd_val}:IQ:OSC:SKEW:Q?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Qcomponent':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Qcomponent(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
