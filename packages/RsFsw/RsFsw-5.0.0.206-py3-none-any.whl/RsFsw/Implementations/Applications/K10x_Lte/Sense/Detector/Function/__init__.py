from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Function:
	"""Function commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("function", core, parent)

	@property
	def auto(self):
		"""auto commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_auto'):
			from .Auto import Auto
			self._auto = Auto(self._core, self._cmd_group)
		return self._auto

	def set(self, detector: enums.Detector, trace=repcap.Trace.Default) -> None:
		"""SCPI: [SENSe]:DETector<det>[:FUNCtion] \n
		Snippet: driver.applications.k10Xlte.sense.detector.function.set(detector = enums.Detector.APEak, trace = repcap.Trace.Default) \n
		No command help available \n
			:param detector: No help available
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Detector')
		"""
		param = Conversions.enum_scalar_to_str(detector, enums.Detector)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		self._core.io.write(f'SENSe:DETector{trace_cmd_val}:FUNCtion {param}')

	# noinspection PyTypeChecker
	def get(self, trace=repcap.Trace.Default) -> enums.Detector:
		"""SCPI: [SENSe]:DETector<det>[:FUNCtion] \n
		Snippet: value: enums.Detector = driver.applications.k10Xlte.sense.detector.function.get(trace = repcap.Trace.Default) \n
		No command help available \n
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Detector')
			:return: detector: No help available"""
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		response = self._core.io.query_str(f'SENSe:DETector{trace_cmd_val}:FUNCtion?')
		return Conversions.str_to_scalar_enum(response, enums.Detector)

	def clone(self) -> 'Function':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Function(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
