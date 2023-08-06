from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Point:
	"""Point commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("point", core, parent)

	def set(self, points: float, trace=repcap.Trace.Default) -> None:
		"""SCPI: [SENSe]:DETector<t>:TRACe[:POINt] \n
		Snippet: driver.applications.k18AmplifierEt.sense.detector.trace.point.set(points = 1.0, trace = repcap.Trace.Default) \n
		Sets the maximum number of trace points to be used by detectors. \n
			:param points: numeric value
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Detector')
		"""
		param = Conversions.decimal_value_to_str(points)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		self._core.io.write(f'SENSe:DETector{trace_cmd_val}:TRACe:POINt {param}')

	def get(self, trace=repcap.Trace.Default) -> float:
		"""SCPI: [SENSe]:DETector<t>:TRACe[:POINt] \n
		Snippet: value: float = driver.applications.k18AmplifierEt.sense.detector.trace.point.get(trace = repcap.Trace.Default) \n
		Sets the maximum number of trace points to be used by detectors. \n
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Detector')
			:return: points: numeric value"""
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		response = self._core.io.query_str(f'SENSe:DETector{trace_cmd_val}:TRACe:POINt?')
		return Conversions.str_to_float(response)
