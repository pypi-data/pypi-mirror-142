from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rpm:
	"""Rpm commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rpm", core, parent)

	def get(self, trace=repcap.Trace.Default) -> float:
		"""SCPI: FETCh:PNOise<t>:RPM \n
		Snippet: value: float = driver.applications.k40PhaseNoise.fetch.pnoise.rpm.get(trace = repcap.Trace.Default) \n
		This command queries the residual PM for a particular user range. The trace that is queried depends on method RsFsw.
		Applications.K40_PhaseNoise.Calculate.Evaluation.User.Trace.set. \n
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Pnoise')
			:return: value: No help available"""
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		response = self._core.io.query_str(f'FETCh:PNOise{trace_cmd_val}:RPM?')
		return Conversions.str_to_float(response)
