from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Utilities import trim_str_response
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Catalog:
	"""Catalog commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("catalog", core, parent)

	def get(self, window=repcap.Window.Default) -> str:
		"""SCPI: TRACe<n>:CATalog \n
		Snippet: value: str = driver.applications.k14Xnr5G.trace.catalog.get(window = repcap.Window.Default) \n
		This command queries the tpyes of traces in a diagram.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Query results in a window that contains one or more line traces. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trace')
			:return: trace_type: CLRW | SSBx | BWPx | AVG | MIN | MAX CLRW For result displays with a single trace (for example the capture buffer) . SSBx | BWPx For unfiltered result displays that show all signal parts (for example unfiltered EVM vs Carrier) . (SSB = synchronization signal block, BWP = bandwidth part) AVG | MIN | MAX For result displays that are filtered by a specific bandwidth part or subframe and show the average, minimum or maximum results of the slots (for example filtered EVM vs Carrier) ."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'TRACe{window_cmd_val}:CATalog?')
		return trim_str_response(response)
