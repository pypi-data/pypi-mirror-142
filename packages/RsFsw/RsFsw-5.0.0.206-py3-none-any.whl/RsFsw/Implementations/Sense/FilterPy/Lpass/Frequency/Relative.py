from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Relative:
	"""Relative commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("relative", core, parent)

	def set(self, frequency: float, filterPy=repcap.FilterPy.Default) -> None:
		"""SCPI: [SENSe]:FILTer<n>:LPASs:FREQuency:RELative \n
		Snippet: driver.sense.filterPy.lpass.frequency.relative.set(frequency = 1.0, filterPy = repcap.FilterPy.Default) \n
		This command selects the relative low pass filter type for the specified evaluation For details on the low pass filter
		refer to 'Low Pass'. \n
			:param frequency: 5PCT | 10PCT | 25PCT Unit: PCT
			:param filterPy: optional repeated capability selector. Default value: Nr1 (settable in the interface 'FilterPy')
		"""
		param = Conversions.decimal_value_to_str(frequency)
		filterPy_cmd_val = self._cmd_group.get_repcap_cmd_value(filterPy, repcap.FilterPy)
		self._core.io.write(f'SENSe:FILTer{filterPy_cmd_val}:LPASs:FREQuency:RELative {param}')

	def get(self, filterPy=repcap.FilterPy.Default) -> float:
		"""SCPI: [SENSe]:FILTer<n>:LPASs:FREQuency:RELative \n
		Snippet: value: float = driver.sense.filterPy.lpass.frequency.relative.get(filterPy = repcap.FilterPy.Default) \n
		This command selects the relative low pass filter type for the specified evaluation For details on the low pass filter
		refer to 'Low Pass'. \n
			:param filterPy: optional repeated capability selector. Default value: Nr1 (settable in the interface 'FilterPy')
			:return: frequency: 5PCT | 10PCT | 25PCT Unit: PCT"""
		filterPy_cmd_val = self._cmd_group.get_repcap_cmd_value(filterPy, repcap.FilterPy)
		response = self._core.io.query_str(f'SENSe:FILTer{filterPy_cmd_val}:LPASs:FREQuency:RELative?')
		return Conversions.str_to_float(response)
