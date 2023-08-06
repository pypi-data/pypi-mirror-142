from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Start:
	"""Start commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("start", core, parent)

	def get(self, trace=repcap.Trace.Default) -> List[float]:
		"""SCPI: FETCh:PNOise<t>:SWEep:STARt \n
		Snippet: value: List[float] = driver.applications.k40PhaseNoise.fetch.pnoise.sweep.start.get(trace = repcap.Trace.Default) \n
		This command queries the start frequency offset of each half decade. \n
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Pnoise')
			:return: start_freq_offsets: No help available"""
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		response = self._core.io.query_bin_or_ascii_float_list(f'FETCh:PNOise{trace_cmd_val}:SWEep:STARt?')
		return response
