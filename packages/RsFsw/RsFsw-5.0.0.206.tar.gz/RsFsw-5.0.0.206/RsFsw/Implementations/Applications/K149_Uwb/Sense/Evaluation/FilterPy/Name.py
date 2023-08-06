from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Utilities import trim_str_response
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Name:
	"""Name commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("name", core, parent)

	def set(self, filter_name: str, filterPy=repcap.FilterPy.Default) -> None:
		"""SCPI: [SENSe]:EVALuation:FILTer<n>:NAME \n
		Snippet: driver.applications.k149Uwb.sense.evaluation.filterPy.name.set(filter_name = '1', filterPy = repcap.FilterPy.Default) \n
		Creates a new packet filter or changes the name of an existing filter. \n
			:param filter_name: 1..n
			:param filterPy: optional repeated capability selector. Default value: Nr1 (settable in the interface 'FilterPy')
		"""
		param = Conversions.value_to_quoted_str(filter_name)
		filterPy_cmd_val = self._cmd_group.get_repcap_cmd_value(filterPy, repcap.FilterPy)
		self._core.io.write(f'SENSe:EVALuation:FILTer{filterPy_cmd_val}:NAME {param}')

	def get(self, filterPy=repcap.FilterPy.Default) -> str:
		"""SCPI: [SENSe]:EVALuation:FILTer<n>:NAME \n
		Snippet: value: str = driver.applications.k149Uwb.sense.evaluation.filterPy.name.get(filterPy = repcap.FilterPy.Default) \n
		Creates a new packet filter or changes the name of an existing filter. \n
			:param filterPy: optional repeated capability selector. Default value: Nr1 (settable in the interface 'FilterPy')
			:return: filter_name: No help available"""
		filterPy_cmd_val = self._cmd_group.get_repcap_cmd_value(filterPy, repcap.FilterPy)
		response = self._core.io.query_str(f'SENSe:EVALuation:FILTer{filterPy_cmd_val}:NAME?')
		return trim_str_response(response)
