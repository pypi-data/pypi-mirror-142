from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Upper:
	"""Upper commands group definition. 3 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("upper", core, parent)

	@property
	def auto(self):
		"""auto commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_auto'):
			from .Auto import Auto
			self._auto = Auto(self._core, self._cmd_group)
		return self._auto

	@property
	def unit(self):
		"""unit commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_unit'):
			from .Unit import Unit
			self._unit = Unit(self._core, self._cmd_group)
		return self._unit

	def set(self, level: float, inputIx=repcap.InputIx.Default) -> None:
		"""SCPI: INPut<ip>:DIQ:RANGe[:UPPer] \n
		Snippet: driver.applications.k10Xlte.inputPy.diq.range.upper.set(level = 1.0, inputIx = repcap.InputIx.Default) \n
		Defines or queries the 'Full Scale Level', i.e. the level that corresponds to an I/Q sample with the magnitude '1'. This
		command is only available if the optional Digital Baseband Interface is installed. \n
			:param level: Range: 1 μV to 7.071 V, Unit: DBM
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
		"""
		param = Conversions.decimal_value_to_str(level)
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		self._core.io.write(f'INPut{inputIx_cmd_val}:DIQ:RANGe:UPPer {param}')

	def get(self, inputIx=repcap.InputIx.Default) -> float:
		"""SCPI: INPut<ip>:DIQ:RANGe[:UPPer] \n
		Snippet: value: float = driver.applications.k10Xlte.inputPy.diq.range.upper.get(inputIx = repcap.InputIx.Default) \n
		Defines or queries the 'Full Scale Level', i.e. the level that corresponds to an I/Q sample with the magnitude '1'. This
		command is only available if the optional Digital Baseband Interface is installed. \n
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
			:return: level: Range: 1 μV to 7.071 V, Unit: DBM"""
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		response = self._core.io.query_str(f'INPut{inputIx_cmd_val}:DIQ:RANGe:UPPer?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Upper':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Upper(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
