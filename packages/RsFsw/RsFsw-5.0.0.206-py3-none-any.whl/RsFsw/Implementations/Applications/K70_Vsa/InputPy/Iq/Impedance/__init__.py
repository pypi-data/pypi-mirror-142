from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


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

	def set(self, impedance: float, inputIx=repcap.InputIx.Default) -> None:
		"""SCPI: INPut<ip>:IQ:IMPedance \n
		Snippet: driver.applications.k70Vsa.inputPy.iq.impedance.set(impedance = 1.0, inputIx = repcap.InputIx.Default) \n
		This command selects the nominal input impedance of the analog baseband input. The command is not available for
		measurements with the optional Digital Baseband Interface. For input from the RF input, use the method RsFsw.Applications.
		K10x_Lte.InputPy.Impedance.set command. \n
			:param impedance: 50 | 75 numeric value User-defined impedance from 50 Ohm to 100000000 Ohm (=100 MOhm) User-defined values are only available for the Spectrum application, the I/Q Analyzer (and thus MSRA mode, primary application only) and the optional Docsis 3.1 application. Unit: OHM
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
		"""
		param = Conversions.decimal_value_to_str(impedance)
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		self._core.io.write(f'INPut{inputIx_cmd_val}:IQ:IMPedance {param}')

	def get(self, inputIx=repcap.InputIx.Default) -> float:
		"""SCPI: INPut<ip>:IQ:IMPedance \n
		Snippet: value: float = driver.applications.k70Vsa.inputPy.iq.impedance.get(inputIx = repcap.InputIx.Default) \n
		This command selects the nominal input impedance of the analog baseband input. The command is not available for
		measurements with the optional Digital Baseband Interface. For input from the RF input, use the method RsFsw.Applications.
		K10x_Lte.InputPy.Impedance.set command. \n
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
			:return: impedance: 50 | 75 numeric value User-defined impedance from 50 Ohm to 100000000 Ohm (=100 MOhm) User-defined values are only available for the Spectrum application, the I/Q Analyzer (and thus MSRA mode, primary application only) and the optional Docsis 3.1 application. Unit: OHM"""
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		response = self._core.io.query_str(f'INPut{inputIx_cmd_val}:IQ:IMPedance?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Impedance':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Impedance(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
