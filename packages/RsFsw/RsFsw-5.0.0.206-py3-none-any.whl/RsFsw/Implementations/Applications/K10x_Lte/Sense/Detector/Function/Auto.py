from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Auto:
	"""Auto commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("auto", core, parent)

	def set(self, state: bool, trace=repcap.Trace.Default) -> None:
		"""SCPI: [SENSe]:DETector<det>[:FUNCtion]:AUTO \n
		Snippet: driver.applications.k10Xlte.sense.detector.function.auto.set(state = False, trace = repcap.Trace.Default) \n
		No command help available \n
			:param state: No help available
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Detector')
		"""
		param = Conversions.bool_to_str(state)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		self._core.io.write(f'SENSe:DETector{trace_cmd_val}:FUNCtion:AUTO {param}')

	def get(self, trace=repcap.Trace.Default) -> bool:
		"""SCPI: [SENSe]:DETector<det>[:FUNCtion]:AUTO \n
		Snippet: value: bool = driver.applications.k10Xlte.sense.detector.function.auto.get(trace = repcap.Trace.Default) \n
		No command help available \n
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Detector')
			:return: state: No help available"""
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		response = self._core.io.query_str(f'SENSe:DETector{trace_cmd_val}:FUNCtion:AUTO?')
		return Conversions.str_to_bool(response)
