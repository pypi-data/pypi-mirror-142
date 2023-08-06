from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SymbolRate:
	"""SymbolRate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("symbolRate", core, parent)

	def get(self, trace=repcap.Trace.Default) -> List[float]:
		"""SCPI: FETCh:PNOise<t>:SWEep:SRATe \n
		Snippet: value: List[float] = driver.applications.k40PhaseNoise.fetch.pnoise.sweep.symbolRate.get(trace = repcap.Trace.Default) \n
		This command queries the sampling rate used in each half decade. \n
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Pnoise')
			:return: sampling_rates: No help available"""
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		response = self._core.io.query_bin_or_ascii_float_list(f'FETCh:PNOise{trace_cmd_val}:SWEep:SRATe?')
		return response
