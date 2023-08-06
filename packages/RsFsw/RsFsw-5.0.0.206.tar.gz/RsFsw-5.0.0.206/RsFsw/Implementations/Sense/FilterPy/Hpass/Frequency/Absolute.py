from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Absolute:
	"""Absolute commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("absolute", core, parent)

	def set(self, frequency: float, filterPy=repcap.FilterPy.Default) -> None:
		"""SCPI: [SENSe]:FILTer<n>:HPASs:FREQuency[:ABSolute] \n
		Snippet: driver.sense.filterPy.hpass.frequency.absolute.set(frequency = 1.0, filterPy = repcap.FilterPy.Default) \n
		This command selects the high pass filter type for the specified evaluation. For details on the high pass filters refer
		to 'High Pass'. \n
			:param frequency: 20 Hz | 50 Hz | 300 Hz Unit: Hz
			:param filterPy: optional repeated capability selector. Default value: Nr1 (settable in the interface 'FilterPy')
		"""
		param = Conversions.decimal_value_to_str(frequency)
		filterPy_cmd_val = self._cmd_group.get_repcap_cmd_value(filterPy, repcap.FilterPy)
		self._core.io.write(f'SENSe:FILTer{filterPy_cmd_val}:HPASs:FREQuency:ABSolute {param}')

	def get(self, filterPy=repcap.FilterPy.Default) -> float:
		"""SCPI: [SENSe]:FILTer<n>:HPASs:FREQuency[:ABSolute] \n
		Snippet: value: float = driver.sense.filterPy.hpass.frequency.absolute.get(filterPy = repcap.FilterPy.Default) \n
		This command selects the high pass filter type for the specified evaluation. For details on the high pass filters refer
		to 'High Pass'. \n
			:param filterPy: optional repeated capability selector. Default value: Nr1 (settable in the interface 'FilterPy')
			:return: frequency: 20 Hz | 50 Hz | 300 Hz Unit: Hz"""
		filterPy_cmd_val = self._cmd_group.get_repcap_cmd_value(filterPy, repcap.FilterPy)
		response = self._core.io.query_str(f'SENSe:FILTer{filterPy_cmd_val}:HPASs:FREQuency:ABSolute?')
		return Conversions.str_to_float(response)
