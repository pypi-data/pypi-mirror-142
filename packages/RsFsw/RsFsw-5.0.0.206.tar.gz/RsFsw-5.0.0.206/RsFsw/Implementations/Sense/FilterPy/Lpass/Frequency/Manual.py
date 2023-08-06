from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Manual:
	"""Manual commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("manual", core, parent)

	def set(self, frequency: float, filterPy=repcap.FilterPy.Default) -> None:
		"""SCPI: [SENSe]:FILTer<n>:LPASs:FREQuency:MANual \n
		Snippet: driver.sense.filterPy.lpass.frequency.manual.set(frequency = 1.0, filterPy = repcap.FilterPy.Default) \n
		This command selects the cutoff frequency of the low pass filter for the specified evaluation. For details on the low
		pass filter refer to 'Low Pass'. \n
			:param frequency: numeric value Range: 0 to 3 MHz, Unit: HZ
			:param filterPy: optional repeated capability selector. Default value: Nr1 (settable in the interface 'FilterPy')
		"""
		param = Conversions.decimal_value_to_str(frequency)
		filterPy_cmd_val = self._cmd_group.get_repcap_cmd_value(filterPy, repcap.FilterPy)
		self._core.io.write(f'SENSe:FILTer{filterPy_cmd_val}:LPASs:FREQuency:MANual {param}')

	def get(self, filterPy=repcap.FilterPy.Default) -> float:
		"""SCPI: [SENSe]:FILTer<n>:LPASs:FREQuency:MANual \n
		Snippet: value: float = driver.sense.filterPy.lpass.frequency.manual.get(filterPy = repcap.FilterPy.Default) \n
		This command selects the cutoff frequency of the low pass filter for the specified evaluation. For details on the low
		pass filter refer to 'Low Pass'. \n
			:param filterPy: optional repeated capability selector. Default value: Nr1 (settable in the interface 'FilterPy')
			:return: frequency: numeric value Range: 0 to 3 MHz, Unit: HZ"""
		filterPy_cmd_val = self._cmd_group.get_repcap_cmd_value(filterPy, repcap.FilterPy)
		response = self._core.io.query_str(f'SENSe:FILTer{filterPy_cmd_val}:LPASs:FREQuency:MANual?')
		return Conversions.str_to_float(response)
