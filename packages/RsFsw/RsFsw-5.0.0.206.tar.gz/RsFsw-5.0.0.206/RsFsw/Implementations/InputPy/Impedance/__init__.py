from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Impedance:
	"""Impedance commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("impedance", core, parent)

	@property
	def ptype(self):
		"""ptype commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ptype'):
			from .Ptype import Ptype
			self._ptype = Ptype(self._core, self._cmd_group)
		return self._ptype

	def set(self, impedance: int) -> None:
		"""SCPI: INPut:IMPedance \n
		Snippet: driver.inputPy.impedance.set(impedance = 1) \n
		This command selects the nominal input impedance of the RF input. In some applications, only 50 Ω are supported.
		For input from the analog baseband interface, use the method RsFsw.InputPy.Iq.Impedance.set command. \n
			:param impedance: 50 | 75 numeric value User-defined impedance from 50 Ohm to 100000000 Ohm (=100 MOhm) User-defined values are only available for the Spectrum application, the I/Q Analyzer, and some optional applications. (In MSRA mode, primary only) Unit: OHM
		"""
		param = Conversions.decimal_value_to_str(impedance)
		self._core.io.write(f'INPut:IMPedance {param}')

	def get(self) -> int:
		"""SCPI: INPut:IMPedance \n
		Snippet: value: int = driver.inputPy.impedance.get() \n
		This command selects the nominal input impedance of the RF input. In some applications, only 50 Ω are supported.
		For input from the analog baseband interface, use the method RsFsw.InputPy.Iq.Impedance.set command. \n
			:return: impedance: 50 | 75 numeric value User-defined impedance from 50 Ohm to 100000000 Ohm (=100 MOhm) User-defined values are only available for the Spectrum application, the I/Q Analyzer, and some optional applications. (In MSRA mode, primary only) Unit: OHM"""
		response = self._core.io.query_str(f'INPut:IMPedance?')
		return Conversions.str_to_int(response)

	def clone(self) -> 'Impedance':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Impedance(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
