from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tconstant:
	"""Tconstant commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tconstant", core, parent)

	def set(self, value: float, filterPy=repcap.FilterPy.Default) -> None:
		"""SCPI: [SENSe]:FILTer<n>:DEMPhasis:TCONstant \n
		Snippet: driver.sense.filterPy.demphasis.tconstant.set(value = 1.0, filterPy = repcap.FilterPy.Default) \n
		This command selects the deemphasis for the specified evaluation. For details on deemphasis refer to 'Deemphasis'. \n
			:param value: 25 us | 50 us | 75 us | 750 us Unit: S
			:param filterPy: optional repeated capability selector. Default value: Nr1 (settable in the interface 'FilterPy')
		"""
		param = Conversions.decimal_value_to_str(value)
		filterPy_cmd_val = self._cmd_group.get_repcap_cmd_value(filterPy, repcap.FilterPy)
		self._core.io.write(f'SENSe:FILTer{filterPy_cmd_val}:DEMPhasis:TCONstant {param}')

	def get(self, filterPy=repcap.FilterPy.Default) -> float:
		"""SCPI: [SENSe]:FILTer<n>:DEMPhasis:TCONstant \n
		Snippet: value: float = driver.sense.filterPy.demphasis.tconstant.get(filterPy = repcap.FilterPy.Default) \n
		This command selects the deemphasis for the specified evaluation. For details on deemphasis refer to 'Deemphasis'. \n
			:param filterPy: optional repeated capability selector. Default value: Nr1 (settable in the interface 'FilterPy')
			:return: value: 25 us | 50 us | 75 us | 750 us Unit: S"""
		filterPy_cmd_val = self._cmd_group.get_repcap_cmd_value(filterPy, repcap.FilterPy)
		response = self._core.io.query_str(f'SENSe:FILTer{filterPy_cmd_val}:DEMPhasis:TCONstant?')
		return Conversions.str_to_float(response)
