from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Avg:
	"""Avg commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("avg", core, parent)

	def get(self, trace=repcap.Trace.Default) -> List[int]:
		"""SCPI: FETCh:PNOise<t>:SWEep:AVG \n
		Snippet: value: List[int] = driver.applications.k40PhaseNoise.fetch.pnoise.sweep.avg.get(trace = repcap.Trace.Default) \n
		This command queries the number of measurements that have been performed in each half decade. \n
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Pnoise')
			:return: measurements: Number of measurements as displayed in the Sweep Result List. The command returns one value for each half decade as a comma separated list."""
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		response = self._core.io.query_bin_or_ascii_int_list(f'FETCh:PNOise{trace_cmd_val}:SWEep:AVG?')
		return response
