from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Impedance:
	"""Impedance commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("impedance", core, parent)

	def set(self, impedance: enums.LowHigh, inputIx=repcap.InputIx.Default) -> None:
		"""SCPI: INPut<Undef>:IQ:IMPedance \n
		Snippet: driver.applications.k91Wlan.inputPy.iq.impedance.set(impedance = enums.LowHigh.HIGH, inputIx = repcap.InputIx.Default) \n
		No command help available \n
			:param impedance: No help available
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
		"""
		param = Conversions.enum_scalar_to_str(impedance, enums.LowHigh)
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		self._core.io.write(f'INPut{inputIx_cmd_val}:IQ:IMPedance {param}')

	# noinspection PyTypeChecker
	def get(self, inputIx=repcap.InputIx.Default) -> enums.LowHigh:
		"""SCPI: INPut<Undef>:IQ:IMPedance \n
		Snippet: value: enums.LowHigh = driver.applications.k91Wlan.inputPy.iq.impedance.get(inputIx = repcap.InputIx.Default) \n
		No command help available \n
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
			:return: impedance: No help available"""
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		response = self._core.io.query_str(f'INPut{inputIx_cmd_val}:IQ:IMPedance?')
		return Conversions.str_to_scalar_enum(response, enums.LowHigh)
